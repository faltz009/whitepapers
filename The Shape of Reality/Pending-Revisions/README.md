# Agent Self-Discovery — Physics Results Workspace

This folder contains the results of a supervised agent discovery pass on the geometric physics framework. The agent worked from the theoretical structure in the Shape of Reality paper and ran independent numerical verification, proof searches, and cross-checks against CODATA values.

**Start here:** [PENDING_UPDATES.md](./PENDING_UPDATES.md) — organized inventory of what's tight, what's strong but needs derivation, and what remains open. Written to be readable without prior knowledge of the workspace.

---

## Quick Summary

The particle mass spectrum and two fundamental constants come out of the geometry with no free parameters. The strongest results:

- **Proton:** m_p/m_e = 6π⁵ + ζ(5)/30 = 1836.152673, measured value 1836.152673 — agreement to seven significant figures
- **Alpha:** α⁻¹ = 137.0364 from geometry, CODATA 137.0360 — gap of about 3 parts per million, with a projection derivation for the one-loop scale ratio
- **Particle topology:** four exact knot/link identifications (proton = trefoil, J/ψ = figure-eight, Σ⁰ = L6a1, D± = L9n6), with the Z boson sharing the proton's topology plus four electroweak dimensions
- **Heavy sector:** multiplicative corrections bring the worst-case heavy particle error from 0.19% to 0.0048%
- **Gravitational constant:** the dimensionless G formula lands at 51.5246, measured target 51.5278 — now accurate to about 0.006%
- **Cosmological constant:** right order of magnitude, prefactor 3π/5 hits the target to within a fraction of a percent, derivation still open

The main open problems are the S³/S⁴ bridge (why the same invariant 1/6 appears independently from two geometric directions), the group-action proof for the particle DOF counting, and the structural origin of the cosmological prefactor.

---

## Files

| File | Contents |
|---|---|
| [PENDING_UPDATES.md](./PENDING_UPDATES.md) | Full organized status document — start here |
| [findings_round1.md](./findings_round1.md) | Raw discovery ledger, 26 sections, all numerical details |
| [s4_zeta_proof_notes.md](./s4_zeta_proof_notes.md) | Proof notes for the S⁴ spectral zeta, Catalan coefficient formula |
| [dof_constraint_workup.md](./dof_constraint_workup.md) | DOF quotient formulation, baryon/meson constraint rules |
| [candidate_revision_sections.tex](./candidate_revision_sections.tex) | Paper-ready section drafts for integration into the main paper |
| [verify_may22.py](./verify_may22.py) | Reproduces all core numerical results |
| [s4_zeta_coefficients.py](./s4_zeta_coefficients.py) | Derives the Catalan-triangle partial fraction formula |
| [structural_checks.py](./structural_checks.py) | Dimension theorem, trefoil phase sector, heavy-sector kappa |
| [alpha_residual_search.py](./alpha_residual_search.py) | Searches for structural expressions behind the remaining alpha gap |
| [lambda_prefactor_search.py](./lambda_prefactor_search.py) | Cosmological constant prefactor comparison |
