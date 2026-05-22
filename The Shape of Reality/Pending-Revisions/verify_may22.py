#!/usr/bin/env python3
"""Reproducible checks for the May 22 Shape of Reality additions."""

from fractions import Fraction
import math

import mpmath as mp
import sympy as sp

mp.mp.dps = 80


def alpha_checks():
    alpha_inv_meas = mp.mpf("137.035999084")
    alpha = 1 / alpha_inv_meas
    bare = 9 * mp.pi**5 / mp.e**3
    correction = mp.log(mp.mpf(9) / 4) / (3 * mp.pi)
    physical = bare - correction
    needed_ratio = mp.e ** (3 * mp.pi * (bare - alpha_inv_meas))
    base_ratio = mp.mpf(9) / 4
    log_residual = mp.log(needed_ratio / base_ratio)

    candidates = [
        ("9/4", base_ratio),
        ("(9/4)*(1+64*a^2)", base_ratio * (1 + 64 * alpha**2)),
        ("(9/4)*exp(64*a^2)", base_ratio * mp.e ** (64 * alpha**2)),
        ("(9/4)*(1+a/2)", base_ratio * (1 + alpha / 2)),
    ]

    print("\n== alpha ==")
    print("bare inverse:", mp.nstr(bare, 40))
    print("one-loop correction:", mp.nstr(correction, 40))
    print("physical inverse:", mp.nstr(physical, 40))
    print("residual inverse:", mp.nstr(physical - alpha_inv_meas, 40))
    print("needed scale ratio:", mp.nstr(needed_ratio, 40))
    print("log residual:", mp.nstr(log_residual, 40))
    print("log residual / alpha^2:", mp.nstr(log_residual / alpha**2, 40))
    print("log residual - 64 alpha^2:", mp.nstr(log_residual - 64 * alpha**2, 40))
    for label, ratio in candidates:
        pred = bare - mp.log(ratio) / (3 * mp.pi)
        ppm = (pred - alpha_inv_meas) / alpha_inv_meas * 1e6
        print(label, "residual", mp.nstr(pred - alpha_inv_meas, 25), "ppm", mp.nstr(ppm, 18))


def proton_checks():
    alpha_inv_meas = mp.mpf("137.035999084")
    alpha = 1 / alpha_inv_meas
    measured = mp.mpf("1836.15267343")
    base = 6 * mp.pi**5
    topological = base + mp.zeta(5) / 30
    electromagnetic = base * mp.e ** (alpha**2 / mp.sqrt(8))

    print("\n== proton ==")
    print("6*pi^5:", mp.nstr(base, 40))
    print("zeta(5)/30:", mp.nstr(mp.zeta(5) / 30, 40))
    print("topological residual:", mp.nstr(topological - measured, 40))
    print("EM sqrt8 residual:", mp.nstr(electromagnetic - measured, 40))
    print("correction ratio:", mp.nstr((electromagnetic - base) / (mp.zeta(5) / 30), 40))
    print("sqrt channel scan:")
    for n in range(3, 17):
        pred = base * mp.e ** (alpha**2 / mp.sqrt(n))
        print(n, mp.nstr(pred - measured, 18))


def zeta_checks():
    m = sp.symbols("m")
    print("\n== S4 zeta partial fractions ==")
    for s in range(3, 12):
        n = s - 1
        expr = (2 * m + 1) / (m * (m + 1)) ** n
        print("s =", s, ":", sp.apart(expr, m))

    print("\nclosed-form numeric checks:")
    forms = {
        3: mp.mpf(1) / 6,
        4: (mp.zeta(3) - 1) / 3,
        5: (5 - 4 * mp.zeta(3)) / 6,
        6: (5 * mp.zeta(3) + mp.zeta(5) - 7) / 3,
        7: (21 - 14 * mp.zeta(3) - 4 * mp.zeta(5)) / 3,
    }
    for s, formula in forms.items():
        total = mp.nsum(lambda k: (2 * k + 1) / (k * (k + 1)) ** (s - 1), [1, mp.inf]) / 6
        print(s, "diff", mp.nstr(total - formula, 20))


def trefoil_uniqueness(limit=5000):
    pairs = []
    integer_pairs = []
    for p in range(2, limit + 1):
        for q in range(p + 1, limit + 1):
            if math.gcd(p, q) != 1:
                continue
            inv_cs = Fraction(24 * p * q, (p * p - 1) * (q * q - 1))
            if inv_cs >= 1:
                pairs.append((p, q, inv_cs))
                if inv_cs.denominator == 1:
                    integer_pairs.append((p, q, inv_cs))

    print("\n== torus knot inverse-CS ==")
    print("pairs with inverse CS >= 1 up to", limit, ":")
    print(pairs)
    print("integer pairs:")
    print(integer_pairs)


if __name__ == "__main__":
    alpha_checks()
    proton_checks()
    zeta_checks()
    trefoil_uniqueness()
