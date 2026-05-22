#!/usr/bin/env python3
"""Discovery-oriented mass correction experiments.

This script compares two correction layers on top of the current bare formulas:
1) Baseline: additive zeta corrections from revision_sections.tex.
2) Hybrid candidate: keep additive zeta for low/mid sector, but use
   multiplicative one-loop correction for the heavy pi^7 sector.

It is intentionally small and transparent so you can tweak assumptions quickly.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from math import prod


# Small zeta set used in the current correction table.
ZETA = {
    2: math.pi**2 / 6,
    3: 1.202056903159594,  # Apery's constant
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
    # Baseline additive correction from current revision table.
    add_sign: str | None = None
    add_k: int | None = None
    add_denom: int | None = None
    # Optional multiplicative class for hybrid heavy-sector correction.
    mult_class: str | None = None


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
    Particle("Top", 338529.0, "112*pi**7", "+", 2, 1, "fermion"),
    Particle("Z", 178449.0, "59*pi**7+log(4*pi)", "+", 2, 1, "vector_z"),
    Particle("W", 157294.0, "52*pi**7+log(4*pi)", "+", 2, 1, "vector_w"),
    Particle("Higgs", 245108.0, "81*pi**7+log(4*pi)", "+", 2, 1, "scalar"),
]


def bare_mass(expr: str) -> float:
    return float(eval(expr, {}, NS))


def baseline_prediction(p: Particle) -> float:
    base = bare_mass(p.bare_expr)
    if p.add_k is None or p.add_denom is None or p.add_sign is None:
        return base
    corr = ZETA[p.add_k] / p.add_denom
    return base + corr if p.add_sign == "+" else base - corr


def hybrid_prediction(p: Particle, alpha: float) -> float:
    base = bare_mass(p.bare_expr)

    # Heavy pi^7 sector: multiplicative one-loop style renormalization.
    if p.mult_class:
        # Discovery candidate: simple rational kappas by sector.
        # Top-like fermion ~2/3, W-like vector ~4/3,
        # Z-like vector suppressed by mixing ~6/5, Higgs scalar ~5/3.
        kappa = {
            "fermion": 2.0 / 3.0,
            "vector_w": 4.0 / 3.0,
            "vector_z": 6.0 / 5.0,
            "scalar": 5.0 / 3.0,
        }[p.mult_class]
        return base * (1.0 + kappa * alpha / (2.0 * math.pi))

    # Else keep current additive zeta layer.
    return baseline_prediction(p)


def summary(label: str, preds: list[tuple[Particle, float]]) -> None:
    rel_errs = [abs(pred - p.measured) / p.measured for p, pred in preds]
    geo = prod(rel_errs) ** (1.0 / len(rel_errs))
    max_err = max(rel_errs)

    print(f"\n=== {label} ===")
    print(f"{'Particle':8s} {'Pred':>12s} {'Measured':>12s} {'Err %':>10s}")
    for p, pred in preds:
        err_pct = 100.0 * (pred - p.measured) / p.measured
        print(f"{p.name:8s} {pred:12.6f} {p.measured:12.6f} {err_pct:10.5f}")
    print(f"\nGeometric mean abs error: {100.0 * geo:.9f} %")
    print(f"Max abs error:            {100.0 * max_err:.9f} %")


def print_heavy_kappas(alpha: float) -> None:
    print("\n=== Heavy-Sector Implied Kappas ===")
    print("kappa* = ((m_meas / m_bare) - 1) / (alpha / 2pi)")
    for p in DATA:
        if not p.mult_class:
            continue
        base = bare_mass(p.bare_expr)
        kappa = ((p.measured / base) - 1.0) / (alpha / (2.0 * math.pi))
        print(f"{p.name:8s} kappa* = {kappa:.9f}")


def main() -> None:
    alpha = 1.0 / 137.035999084

    baseline = [(p, baseline_prediction(p)) for p in DATA]
    hybrid = [(p, hybrid_prediction(p, alpha)) for p in DATA]

    summary("Baseline: additive zeta corrections", baseline)
    summary("Hybrid: zeta + multiplicative heavy-sector loop", hybrid)
    print_heavy_kappas(alpha)


if __name__ == "__main__":
    main()
