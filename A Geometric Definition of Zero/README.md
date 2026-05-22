# A Geometric Definition of Zero: Closure Events on S³ and the Riemann Hypothesis

**Author:** Walter Henrique Alves da Silva  
**Date:** April 2026  
**DOI:** [10.5281/zenodo.19427453](https://doi.org/10.5281/zenodo.19427453)  
**Lean 4 proof + experiments:** [github.com/faltz009/geometric-zero-rh](https://github.com/faltz009/geometric-zero-rh)

## Files

- PDF: [A Geometric Definition of Zero.pdf](./A%20Geometric%20Definition%20of%20Zero.pdf)
- Markdown (agent-readable extraction): [A Geometric Definition of Zero.md](./A%20Geometric%20Definition%20of%20Zero.md)

## Core Argument

When a mathematician says ζ(s) has a zero at s, they mean the function evaluates to zero in ℂ. That framing is a geometric choice, and Lagrange's four-square theorem (1770) shows it is the wrong one: every prime p = a²+b²+c²+d² has a canonical position on S³, the unit quaternion q̂_p = [a,b,c,d]/√p, forced by the prime's own arithmetic rather than by any embedding we choose. The Euler product is built from primes, so it is a composition of elements of S³, and the correct ambient space for that composition is S³ rather than ℂ. The classical ζ(s) in ℂ is the two-dimensional shadow of a quaternionic running product, obtained by projecting away the two dimensions that carry the four-square structure.

In S³ a zero of ζ is a **Hopf closure event**: the running quaternionic Euler product Q(s) reaches the equatorial locus where the scalar channel W and the vector channel RGB are exactly equal, satisfying W² = 1/2. From the pure geometry of S³, with no additional assumptions, this Hopf balance condition forces Re(s) = 1/2. The critical line is not a conjecture in this geometry; it is the only locus where a closure event can occur.

## Why S³ Settles Four Open Questions

Four structural properties of the Euler product are unaccounted for in ℂ and derived immediately from S³:

| Property | Status in ℂ | Status in S³ |
|---|---|---|
| Functional equation ξ(s) = ξ(1−s) | Requires Poisson summation, Mellin transform, gamma factors | The star involution Q(1−s) = Q(s)*, the algebra's own symmetry |
| Zero distribution on Re(s) = 1/2 | Unproved for 160 years | Forced by Hopf balance from the unit sphere constraint |
| GUE spacing statistics | No causal account in ℂ | Follows from Haar measure on SU(2) ≅ S³, the natural measure on the space |
| Lagrange's theorem | Plays no role | The reason S³ is the correct space in the first place |

One assignment leaves four properties as unexplained coincidences. The other derives all four from the geometry.

## Lean 4 Formal Proof

Verified against Mathlib 4.29 with zero sorry. The file is in three parts. Part I covers pure S³ geometry from Mathlib's quaternion library: the 1+3 eigenspace decomposition, chiral closure q·q* = 1, Hopf balance forcing Re(q)² = 1/2, S³ having no zero element, and Hopf-balanced quaternions always forming free orbits. Part II proves the Geometric Riemann Hypothesis from three geometric axioms, all of which are Mathlib coverage gaps rather than mathematical gaps. Part III proves the Phase Lift theorem and derives the classical RH in one line from Definition B.

Axiom count: 7. Six are Mathlib coverage gaps that disappear once Q and ζ are contributed to Mathlib. One is Definition B, the geometric foundation.

## Experimental Validation

Three independent tests on the first 1000 Riemann zeros using the closure-verification Rust implementation:

1. Hopf balance error is consistently lower at zero ordinates than at midpoints between zeros, across every prime checkpoint from 1k to 50k primes.
2. GUE spacing statistics: KS distance 0.111 (GUE) vs 0.322 (Poisson), a 2.9× ratio, derived from Haar measure on SU(2) rather than cited as an empirical observation.
3. A two-detector intersection test shows zeros satisfy both the phase-closure signal and the spatial-balance signal simultaneously, while non-zero ordinates satisfy at most one.

## Notable Additional Results

ζ(−1) = −1/12 as Hopf reflection: since vol(S³) = 2π² and ζ(2) = π²/6 = vol(S³)/12, the Casimir value is the S³-volume constant reflected through the critical line, making the analytic continuation regularization a projection artifact with a geometric source.

## Role in the Series

The same Hopf equatorial locus (σ = π/4) that The Geometric Computer identifies as the Riemann zero detector is given a complete proof and experimental validation here. The result also feeds back into the particle physics papers: the critical line is the equatorial balance locus, and Riemann zeros are the spectral eigenstates of the prime composition on S³, connecting number theory to the particle mass spectrum through the same geometric object.

## Citation

```bibtex
@misc{alvesdasilva_geometric_zero_2026,
  title  = {A Geometric Definition of Zero: Closure Events on {S³} and the {Riemann} Hypothesis},
  author = {Alves da Silva, Walter Henrique},
  year   = {2026},
  month  = {April},
  doi    = {10.5281/zenodo.19427453}
}
```
