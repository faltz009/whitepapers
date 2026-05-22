#!/usr/bin/env python3
"""
Search small structural expressions for the alpha log residual.

The current one-loop scale is 9/4.  The exact scale needed to hit CODATA is
slightly larger.  This script searches whether the missing log correction has
a low-complexity expression in powers of alpha and common topology constants.
"""

import math
from fractions import Fraction

import sympy as sp


mp = sp.N
pi = sp.pi
E = sp.E
alpha_inv = sp.Float("137.035999084", 80)
alpha = 1 / alpha_inv

bare_inv = 9 * pi**5 / E**3
r_exact = sp.exp(3 * pi * (bare_inv - alpha_inv))
L = sp.log(r_exact / sp.Rational(9, 4))


def show_base():
    print("bare inverse alpha =", sp.N(bare_inv, 30))
    print("r_exact =", sp.N(r_exact, 40))
    print("L = log(r_exact/(9/4)) =", sp.N(L, 40))
    for k in range(2, 7):
        print(f"L/alpha^{k} =", sp.N(L / alpha**k, 30))


def rational_alpha_series(max_order=5, max_den=512):
    print("\nGreedy alpha-power series for L")
    residual = sp.N(L, 80)
    for k in range(2, max_order + 1):
        coeff = sp.N(residual / alpha**k, 60)
        rat = Fraction(float(coeff)).limit_denominator(max_den)
        term = sp.Rational(rat.numerator, rat.denominator) * alpha**k
        print(
            f"order alpha^{k}: coeff={sp.N(coeff, 25)}  "
            f"rat={rat}  residual_after={sp.N(residual - term, 25)}"
        )
        residual = sp.N(residual - term, 80)


def pslq_targets():
    print("\nPSLQ tests")
    consts = [
        ("1", sp.Integer(1)),
        ("pi", pi),
        ("1/pi", 1/pi),
        ("sqrt2", sp.sqrt(2)),
        ("sqrt8", sp.sqrt(8)),
        ("log2", sp.log(2)),
        ("log3", sp.log(3)),
        ("log(9/4)", sp.log(sp.Rational(9, 4))),
    ]
    targets = [
        ("L/alpha^2", L / alpha**2),
        ("(L-64a2)/alpha^3", (L - 64 * alpha**2) / alpha**3),
    ]
    for tname, target in targets:
        print(f"\nTarget {tname} = {sp.N(target, 30)}")
        for cname, c in consts:
            ratio = sp.N(target / c, 60)
            rat = Fraction(float(ratio)).limit_denominator(256)
            approx = sp.Rational(rat.numerator, rat.denominator) * c
            err = sp.N(target - approx, 20)
            if abs(float(err)) < 1e-4:
                print(f"  near {rat} * {cname}; err={err}")


if __name__ == "__main__":
    show_base()
    rational_alpha_series()
    pslq_targets()
