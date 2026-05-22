#!/usr/bin/env python3
"""
Structural checks for the May 22 additions.

This script keeps theorem-level claims separate from numerical fits:
1. Dimension uniqueness from scalar curvature and torus-knot CS.
2. Trefoil group abelianization / finite phase quotient.
3. Heavy-sector kappa comparison for rational candidates.
"""

from fractions import Fraction
from math import pi


def cs_torus(p, q):
    return Fraction((p * p - 1) * (q * q - 1), 24 * p * q)


def inv_cs_torus(p, q):
    return Fraction(1, 1) / cs_torus(p, q)


def dimension_table(nmax=12):
    print("Dimension curvature/topology calibration")
    print("n  R=n(n-1)  cs(T(n-1,n))  inv_cs  R==inv_cs")
    for n in range(3, nmax + 1):
        R = n * (n - 1)
        cs = cs_torus(n - 1, n)
        inv_cs = Fraction(1, 1) / cs
        print(f"{n:<2} {R:<9} {str(cs):<15} {str(inv_cs):<10} {R == inv_cs}")


def trefoil_phase_quotient():
    print("\nTrefoil group check")
    print("Group presentation: <a,b | a^2=b^3>")
    print("Abelianization relation: 2a = 3b")
    print("Since gcd(2,3)=1, abelianization is Z, not Z2 x Z3.")
    print("Therefore unrestricted U(1) characters form a circle.")
    print("The six phases arise only if the central closure is quotiented by")
    print("a^2=b^3=1, giving a finite phase set a in Z2, b in Z3.")
    finite = []
    for a in [1, -1]:
        for b_pow in range(3):
            finite.append((a, f"omega^{b_pow}"))
    print("Finite closure characters:", finite)


def heavy_kappa_candidates():
    print("\nHeavy-sector kappa rational check")
    alpha_inv = 137.035999084
    alpha = 1 / alpha_inv
    sin2 = 0.223044624
    particles = [
        ("top", 0.652012858, Fraction(2, 3)),
        ("W", 1.295012119, Fraction(4, 3)),
        ("H", 1.624995931, Fraction(13, 8)),
        ("H_alt", 1.624995931, Fraction(5, 3)),
    ]
    for name, observed, candidate in particles:
        err = float(candidate) - observed
        print(f"{name:<6} k*={observed:.9f}  candidate={candidate}={float(candidate):.9f}  delta={err:+.9f}")
    for lam in [Fraction(7, 12), Fraction(3, 5), Fraction(1, 2), Fraction(2, 3)]:
        kz = Fraction(4, 3) - float(lam) * sin2
        print(f"Z lambda={lam:<5} kappa={kz:.9f} delta={kz - 1.203927825:+.9f}")
    print(f"alpha/(2pi)={alpha/(2*pi):.12f}")


if __name__ == "__main__":
    dimension_table()
    trefoil_phase_quotient()
    heavy_kappa_candidates()
