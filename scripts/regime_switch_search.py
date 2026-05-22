#!/usr/bin/env python3
"""Search regime-switch laws and kappa mechanisms for heavy-sector corrections.

Goal:
- identify when additive zeta corrections stop being the right correction regime
- test multiplicative one-loop style alternatives in that regime
- provide concrete, reproducible numbers for discussion and iteration
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from math import prod


ZETA = {
    2: math.pi**2 / 6,
    3: 1.202056903159594,
    4: math.pi**4 / 90,
    5: 1.03692775514337,
    8: math.pi**8 / 9450,
    9: 1.002008392826082,
}


@dataclass
class Particle:
    name: str
    measured: float
    bare_expr: str
    sign: str
    zeta_k: int
    zeta_d: int
    # For heavy-sector mechanism candidates:
    spin: float | None = None
    charge_abs: float | None = None
    field_class: str | None = None  # fermion/vector/scalar
    is_z: bool = False


NS = {"pi": math.pi, "sqrt": math.sqrt, "log": math.log}


DATA = [
    Particle("Proton", 1836.15267, "6*pi**5", "+", 5, 30),
    Particle("Tau", 3477.2300, "3*pi**2*(12*pi**2-1)", "+", 8, 9),
    Particle("Neutron", 1838.68366, "6*pi**5+log(4*pi)", "+", 9, 29),
    Particle("Kaon0", 973.800, "33*pi**3-5*pi**2", "-", 8, 17),
    Particle("Pionpm", 273.130, "28*pi**2-pi", "-", 4, 14),
    Particle("Charm", 2485.330, "26*pi**4-15*pi", "-", 2, 9),
    Particle("Pion0", 264.140, "29*pi**2-7*pi", "-", 2, 19),
    Particle("Strange", 182.780, "6*pi**3-pi", "-", 5, 9),
    Particle("Muon", 206.768, "3*pi**4/sqrt(2)", "+", 3, 9),
    Particle("Bottom", 8180.060, "28*pi**5-4*pi**4", "+", 3, 1),
    Particle("Kaonpm", 966.100, "33*pi**3-18*pi", "-", 2, 3),
    Particle("Top", 338529.0, "112*pi**7", "+", 2, 1, 0.5, 2 / 3, "fermion"),
    Particle("Z", 178449.0, "59*pi**7+log(4*pi)", "+", 2, 1, 1.0, 0.0, "vector", True),
    Particle("W", 157294.0, "52*pi**7+log(4*pi)", "+", 2, 1, 1.0, 1.0, "vector", False),
    Particle("Higgs", 245108.0, "81*pi**7+log(4*pi)", "+", 2, 1, 0.0, 0.0, "scalar"),
]


def bare_mass(p: Particle) -> float:
    return float(eval(p.bare_expr, {}, NS))


def max_pi_power(expr: str) -> int:
    # simple parser for 'pi**N' patterns in our current formulas
    out = 0
    needle = "pi**"
    i = 0
    while True:
        j = expr.find(needle, i)
        if j < 0:
            break
        j += len(needle)
        k = j
        while k < len(expr) and expr[k].isdigit():
            k += 1
        if k > j:
            out = max(out, int(expr[j:k]))
        i = k
    # plain "pi" without exponent
    if out == 0 and "pi" in expr:
        out = 1
    return out


def baseline_pred(p: Particle) -> float:
    base = bare_mass(p)
    corr = ZETA[p.zeta_k] / p.zeta_d
    return base + corr if p.sign == "+" else base - corr


def err_rel(pred: float, measured: float) -> float:
    return abs(pred - measured) / measured


def geom_mean(values: list[float]) -> float:
    return prod(values) ** (1.0 / len(values))


def implied_kappa(p: Particle, alpha: float) -> float:
    base = bare_mass(p)
    return ((p.measured / base) - 1.0) / (alpha / (2.0 * math.pi))


def fit_kappa_constant(heavy: list[Particle], alpha: float) -> float:
    vals = [implied_kappa(p, alpha) for p in heavy]
    return sum(vals) / len(vals)


def fit_kappa_charge_linear(heavy: list[Particle], alpha: float) -> tuple[float, float]:
    # kappa = a + b*|Q| ; closed form LS for one feature
    xs = [p.charge_abs or 0.0 for p in heavy]
    ys = [implied_kappa(p, alpha) for p in heavy]
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * sxx - sx * sx
    if abs(den) < 1e-12:
        return (sy / n, 0.0)
    b = (n * sxy - sx * sy) / den
    a = (sy - b * sx) / n
    return (a, b)


def kappa_physics_rational(p: Particle, sin2w: float, z_lambda: float) -> float:
    # Discovery candidate:
    # fermion: 2/3
    # vector W: 4/3
    # vector Z: 4/3 - z_lambda * sin^2(theta_W)
    # scalar: 5/3
    if p.field_class == "fermion":
        return 2.0 / 3.0
    if p.field_class == "scalar":
        return 5.0 / 3.0
    if p.field_class == "vector":
        if p.is_z:
            return (4.0 / 3.0) - z_lambda * sin2w
        return 4.0 / 3.0
    return 1.0


def predict_with_model(
    model: str,
    threshold_pi: int,
    alpha: float,
    z_lambda: float = 0.5,
) -> tuple[list[tuple[Particle, float]], dict]:
    # heavy regime by pi-power threshold
    heavy = [p for p in DATA if max_pi_power(p.bare_expr) >= threshold_pi]
    heavy_names = {p.name for p in heavy}

    extra = {"heavy_names": sorted(heavy_names)}
    preds = []

    # pre-fit model params if needed
    if model == "const":
        k_const = fit_kappa_constant(heavy, alpha)
        extra["k_const"] = k_const
    elif model == "charge":
        a, b = fit_kappa_charge_linear(heavy, alpha)
        extra["a"] = a
        extra["b"] = b
    else:
        # use measured masses to estimate sin^2(theta_W), then test lambda choices
        mW = next(p.measured for p in DATA if p.name == "W")
        mZ = next(p.measured for p in DATA if p.name == "Z")
        sin2w = 1.0 - (mW / mZ) ** 2
        extra["sin2w"] = sin2w
        extra["z_lambda"] = z_lambda

    for p in DATA:
        base = bare_mass(p)
        if p.name in heavy_names and p.field_class is not None:
            if model == "const":
                k = extra["k_const"]
            elif model == "charge":
                k = extra["a"] + extra["b"] * (p.charge_abs or 0.0)
            else:
                k = kappa_physics_rational(p, extra["sin2w"], z_lambda)
            pred = base * (1.0 + k * alpha / (2.0 * math.pi))
        else:
            pred = baseline_pred(p)
        preds.append((p, pred))
    return preds, extra


def evaluate(preds: list[tuple[Particle, float]]) -> tuple[float, float]:
    errs = [err_rel(pred, p.measured) for p, pred in preds]
    return geom_mean(errs), max(errs)


def main() -> None:
    alpha = 1.0 / 137.035999084

    # baseline
    base_preds = [(p, baseline_pred(p)) for p in DATA]
    g0, m0 = evaluate(base_preds)
    print("Baseline")
    print(f"  geom mean abs err = {100*g0:.9f}%")
    print(f"  max abs err       = {100*m0:.9f}%")

    # search thresholds + models
    candidates = []
    for threshold in [6, 7, 8]:
        eligible_heavy = [
            p
            for p in DATA
            if max_pi_power(p.bare_expr) >= threshold and p.field_class is not None
        ]
        if not eligible_heavy:
            continue
        for model in ["const", "charge", "rational"]:
            if model == "rational":
                # few physically meaningful lambda candidates for Z mixing suppression
                for lam in [0.5, 0.6, 2.0 / 3.0, 1.0]:
                    preds, extra = predict_with_model(model, threshold, alpha, lam)
                    g, m = evaluate(preds)
                    candidates.append((g, m, threshold, model, extra, preds))
            else:
                preds, extra = predict_with_model(model, threshold, alpha)
                g, m = evaluate(preds)
                candidates.append((g, m, threshold, model, extra, preds))

    candidates.sort(key=lambda x: (x[1], x[0]))  # prioritize worst-case improvement
    best = candidates[0]
    g, m, threshold, model, extra, preds = best

    print("\nBest regime-switch candidate")
    print(f"  threshold (pi power) = {threshold}")
    print(f"  model                = {model}")
    print(f"  heavy                = {', '.join(extra['heavy_names'])}")
    if model == "const":
        print(f"  kappa const          = {extra['k_const']:.9f}")
    elif model == "charge":
        print(f"  kappa(Q)             = {extra['a']:.9f} + {extra['b']:.9f}*|Q|")
    else:
        print(f"  sin^2(theta_W)       = {extra['sin2w']:.9f}")
        print(f"  kappa_Z lambda       = {extra['z_lambda']}")
        print("  kappas               = fermion 2/3, W 4/3, Z 4/3-lambda*sin^2(theta_W), scalar 5/3")
    print(f"  geom mean abs err    = {100*g:.9f}%")
    print(f"  max abs err          = {100*m:.9f}%")

    print("\nPer-particle error (%):")
    for p, pred in preds:
        e = 100.0 * (pred - p.measured) / p.measured
        print(f"  {p.name:8s} {e: .6f}")

    print("\nImplied heavy kappas from data:")
    for p in DATA:
        if p.field_class is None:
            continue
        k = implied_kappa(p, alpha)
        frac = Fraction(k).limit_denominator(24)
        print(f"  {p.name:8s} k*={k:.9f}  ~  {frac.numerator}/{frac.denominator}")


if __name__ == "__main__":
    main()
