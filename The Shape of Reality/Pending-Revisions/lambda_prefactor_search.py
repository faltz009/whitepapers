#!/usr/bin/env python3
"""
Explore simple topological prefactors for the sigma-relaxation Lambda scale.

The raw hierarchy is (t_Pl/t0)^2.  Existing notes mention an observed
dimensionless scale near 2.89e-122.  This script records the factor needed
and compares nearby closure/topology constants.
"""

import math
from fractions import Fraction


raw = 1.5332084e-122
target = 2.89e-122
needed = target / raw

# Common cosmology value for Lambda used in many references, in m^-2.
# This is included only to check sensitivity of the rounded 2.89e-122 target.
planck_length = 1.616255e-35
lambda_m2_reference = 1.1056e-52
target_from_lambda = lambda_m2_reference * planck_length**2
needed_from_lambda = target_from_lambda / raw

candidates = {
    "6/pi": 6 / math.pi,
    "3*pi/5": 3 * math.pi / 5,
    "sqrt(pi)": math.sqrt(math.pi),
    "sqrt(8)/1.5": math.sqrt(8) / 1.5,
    "e/log(4)": math.e / math.log(4),
    "pi/e * 5/3": math.pi / math.e * 5 / 3,
    "2 - 1/(6*pi)": 2 - 1 / (6 * math.pi),
    "2 - alpha^-1 not used": 2.0,
    "12/(2*pi)": 12 / (2 * math.pi),
    "6/(pi+1/24)": 6 / (math.pi + 1 / 24),
}

print("raw =", raw)
print("target =", target)
print("needed factor =", needed)
print("target from Lambda=1.1056e-52 m^-2 =", target_from_lambda)
print("needed factor from that Lambda =", needed_from_lambda)
print("near rationals:")
for d in [12, 24, 48, 96, 256]:
    f = Fraction(needed).limit_denominator(d)
    print(f"  maxden {d}: {f} = {float(f)} err={float(f)-needed:+.6e}")

print("\ncandidate prefactors")
for name, val in sorted(candidates.items(), key=lambda kv: abs(kv[1] - needed)):
    pred = raw * val
    rel = (pred - target) / target
    print(f"{name:<18} {val:.9f}  rel_err={rel:+.5%}  pred={pred:.5e}")
