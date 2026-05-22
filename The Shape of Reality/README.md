# The Shape of Reality: Computing Physics from π and e

**Author:** Walter Henrique Alves da Silva  
**DOI:** [10.5281/zenodo.18906682](https://doi.org/10.5281/zenodo.18906682)  
**Status:** Active revision — integrating May 22 results and Geometric Calculus spine

## Files

- `The Shape of Reality.tex` — current working draft
- [images/](./images/) — all figures referenced by the tex
- [`Pending-Revisions/`](Pending-Revisions/) — results ledger, verification scripts, revision work queue

## What This Paper Argues

If the local geometry of physical space is S³ and elementary interactions are Hamilton products, then the masses and coupling constants of particles are topological invariants of closed paths on that geometry — and those invariants can be computed from the same Chern-Simons theory and knot invariants that mathematicians study independently. The paper derives the fine structure constant, the proton-to-electron mass ratio, and the particle mass spectrum from this claim, with results accurate to sub-ppm for the best-constrained quantities.

## Main Results in the Current Draft

The fine structure constant has a two-term geometric derivation:

α⁻¹ = 9π⁵/e³ − (1/3π)·ln(9/4)

The first term is the bare geometric coupling; the second is the one-loop QED running correction. The scale ratio 9/4 = sec²(arccos(2/3)) follows from the up-quark charge coordinate W = 2/3 under Hopf projection, connecting the running to the same geometric object that produces the proton topology.

The proton mass ratio has two independent routes to the same correction:

m_p/m_e = 6π⁵ + ζ(5)/30

The 6 is the inverse Chern-Simons invariant of the trefoil T(2,3), which is the unique torus knot with an integer inverse CS value — a fact that is now a proved theorem rather than a search result. The π⁵ exponent comes from DOF = 5. The ζ(5)/30 correction comes from the S⁴ spectral zeta at s = 6 through a Catalan-triangle coefficient derivation. The residual against CODATA is −4.6×10⁻⁷.

Single-term particle identifications:

| Particle | Formula | 1/CS | Topology |
|---|---|---|---|
| Proton | 6π⁵ | 6 | trefoil T(2,3) |
| J/ψ | 2π⁷ | 2 | figure-eight 4₁ |
| Σ⁰ | 24π⁴ | 24 | L6a1 |
| D± | 12π⁵ | 12 | L9n6 |
| Z | 6π⁹ | 6 | trefoil + SU(2)⊕U(1) depth |

The Z boson case is the most revealing: it shares the proton's trefoil prefactor 6 but carries four more powers of π, because 9 − 5 = 4 = dim SU(2) + dim U(1). The same topology, lifted by the electroweak gauge depth.

## Theorem-Level Results Being Integrated from May 22

- **Trefoil uniqueness:** T(2,3) is the unique torus knot with integer inverse CS invariant. Proof closed: for p = 2, integrality forces q²−1 | 16, leaving only q = 3 among coprime q > 2; cases p = 3, 4 are checked directly; p ≥ 5 falls below 1.
- **Dimension-three calibration:** n(n-1)(n-2)(n+1) = 24 has n = 3 as its unique integer solution above 2, selecting 3+1 spacetime from the calibration condition 1/cs(T(n-1,n)) = R_{Sⁿ}.
- **S⁴ spectral rationality:** s = 3 is the only integer evaluation of ζ_conf(s) that is purely rational (two-line telescoping proof). For all s > 3, odd zeta residues survive through the Catalan-triangle coefficient structure.
- **S⁴ rationality uniqueness:** proved from the partial-fraction formula, not just observed from finite computation.

## Open Derivation Targets

- DOF quotient groups for baryons and mesons: the constraint rule is geometrically motivated but the group-action proof is not yet written
- Full derivation of the 9/4 alpha running scale from the W = 2/3 projection (the identification exists; the formal "energy scales as inverse projected length" step remains)
- S³/S⁴ bridge: why the conformal S⁴ shell trace and the S³ trefoil carrier produce the same invariant 1/6
- Gravity residual: 61α² is the current correction target, sharpened from 64α²
- Cosmological constant prefactor: 3π/5 matches the target to 0.066% but derivation from sigma relaxation is open
- Heavy sector kappa values: κ_H = 13/8 identified to 4×10⁻⁶ error but origin unproved
- Top quark topology: open

## Citation

```bibtex
@misc{alvesdasilva_shape_of_reality_2025,
  title  = {The Shape of Reality: Computing Physics from $\pi$ and $e$},
  author = {Alves da Silva, Walter Henrique},
  year   = {2025},
  doi    = {10.5281/zenodo.18906682}
}
```
