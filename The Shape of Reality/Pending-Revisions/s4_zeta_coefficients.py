#!/usr/bin/env python3
"""Derive and print the Catalan-triangle coefficients in the S4 conformal zeta."""

import math
import sympy as sp


def coeff(n, j):
    """Coefficient of 1/m^j in (2m+1)/(m^n (m+1)^n), where n=s-1."""
    r = n - j
    if r == 0:
        return 1
    return (-1) ** r * (math.comb(n + r - 1, r) - 2 * math.comb(n + r - 2, r - 1))


def coeff_closed(n, j):
    """Equivalent compact form."""
    r = n - j
    return (-1) ** r * math.comb(n + r - 1, r) * (n - r - 1) // (n + r - 1)


def row(n):
    return [coeff(n, j) for j in range(2, n + 1)]


def zeta_expression(s):
    """Closed form of zeta_conf(s) in terms of Riemann zeta values."""
    n = s - 1
    zeta = sp.zeta
    total = 0
    # Sum A_j/m^j + B_j/(m+1)^j.  The B side follows from partial fractions.
    m = sp.symbols("m")
    expr = sp.apart((2 * m + 1) / (m * (m + 1)) ** n, m)
    for term in sp.Add.make_args(expr):
        coeff_term = term
        # Sum term from m=1 to infinity with known shift rule.
        # Simpler and robust: parse powers from apart expression.
    summed = sp.summation(expr, (m, 1, sp.oo)) / 6
    return sp.simplify(summed)


if __name__ == "__main__":
    print("Rows are coefficients of 1/m^j, j=2..n, for n=s-1.")
    for n in range(2, 13):
        print(f"n={n:2d} s={n+1:2d}:", row(n), "abs:", [abs(x) for x in row(n)])
        assert row(n) == [coeff_closed(n, j) for j in range(2, n + 1)]

    print("\nClosed form:")
    print("A_{n,j} = (-1)^(n-j) * (j-1)/(2n-j-1) * binom(2n-j-1, n-j)")
    print("with n=s-1 and j=2,...,n.")

    print("\nSums:")
    for s in range(3, 10):
        print(f"s={s}:", zeta_expression(s))
