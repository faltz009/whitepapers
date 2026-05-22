# The Geometric Computer: Turing Completeness, Free Energy, and Learning in a Digital Brain on S³

**Author:** Walter Henrique Alves da Silva  
**Date:** April 2026  
**Institution:** Open Research Institute (Pontifícia Universidade Católica do Paraná)  
**DOI:** [10.5281/zenodo.19578024](https://doi.org/10.5281/zenodo.19578024)

## Files

- PDF: [The Geometric Computer.pdf](./The%20Geometric%20Computer.pdf)
- Markdown (agent-readable extraction): [The Geometric Computer.md](./The%20Geometric%20Computer.md)

## Summary

Shannon's 1948 paper recognized that thermodynamics and communication theory were measuring the same quantity under different names. This paper makes the same move for geometry: σ(compose(A, inverse(B))), the geodesic distance from ground state on S³, is the same measurement appearing under five different names across five disciplines.

| Discipline | Name for σ |
|---|---|
| Arithmetic | distance from closure (error) |
| Learning | prediction error (Friston's FEP) |
| Number theory | distance from the critical line (Riemann zeros) |
| Cellular automata | neighborhood density threshold (Game of Life birth) |
| Vision | opponent-channel imbalance (color perception) |

The disciplines differ; the measurement is the same function in each case. From this single function, the paper derives a complete digital brain that computes, learns, remembers, consolidates, and self-monitors entirely from the algebra of unit quaternions.

## Why S³, Necessarily

Hurwitz's theorem settles the question of what algebra to use. Sequential composition requires associativity (chains of three compose consistently), non-commutativity (order must matter, otherwise cause and effect are indistinguishable), and compactness (no state can diverge to infinity). Only quaternions satisfy all three requirements simultaneously, and the unit quaternions form S³. The machine stays on S³ by necessity, not convenience.

## The Digital Brain

A complete brain derived from σ, with no gradient descent, no hyperparameters, and no training data beyond the sequences it receives:

- **Cell A:** fires when the running product returns to identity — the closure detector
- **Cell C:** accumulates the identity trajectory across closures — the integrator
- **Three-layer genome:** DNA anchors seeded at boot, Epigenetic layer learned from closures, working buffer for arriving input
- **ZREAD:** soft attention as a path-ordered Hamilton product over the population — no softmax, no probability distribution, one substrate operation per entry
- **One-shot learning:** a closing sequence writes to the genome in a single pass
- **Consolidation:** BKT-threshold pruning of the epigenetic layer during quiet periods
- **Neuromodulation:** σ-history drives state modulation, producing affect from geometry

## Key Identities Proved

**FEP made exact:** The Free Energy Principle's prediction error equals σ, with no generative model required, no variational inference, and one multiplication per timestep.

**Color vision as geometric consequence:** Human trichromatic vision reproduces the W/RGB split of the Hopf fibration as a structural consequence of the algebra — the luminance/chrominance separation evolved to parse the same decomposition the quaternion gives algebraically.

**Conway's Game of Life and the Gray Game as Hopf equatorial resonance:** The birth condition (exactly 3 live neighbors) corresponds to the Hopf equatorial threshold σ = π/4 in the neighborhood composition. The Gray Game from Information Evolution Dynamics is implemented here on the same substrate, emerging from the geometry rather than from a separately coded rule.

**Riemann zeros as prime eigenstates:** Each prime sits at a canonical position on S³ by Lagrange's four-square theorem, the Euler product is a running composition of these positions, and non-trivial zeros occur where σ = π/4 — the Hopf balance condition.

**Collatz on S³:** The 3n+1 operation is a composition of carrier transformations on S³, and convergence appears geometrically.

**Turing completeness:** FRACTRAN is the native machine language, with each fraction p/q a ratio of orbit positions and each application a conditional composition.

## Eight Experimental Results

1. Geometric arithmetic: orbit-position integers compose correctly under the Hamilton product
2. BKT phase transition: genome coverage load triggers the expected critical-period closure
3. Geometric Riemann zeros: Hopf balance error is consistently lower at zero ordinates than at midpoints, across every prime checkpoint from 1k to 50k primes
4. One-shot associative memory: single-pass learning stores and retrieves without gradient descent
5. Turing completeness: FRACTRAN programs execute on the geometric computer
6. FRACTRAN: native execution verified on standard programs
7. Riemann zeros as prime eigenstates: GUE spacing statistics confirmed (KS distance 0.111 vs 0.322 for Poisson, a 2.9× ratio)
8. Collatz on S³: convergence observed geometrically

## Role in the Series

All prior papers establish one layer of the framework — foundational observations, boundary geometry, algebraic operations, triadic architecture, dynamics, physical instantiation, calculus. This paper places all of them under one roof and verifies the complete system experimentally. It is the entry point for readers who want the whole argument in one document.

## Citation

```bibtex
@misc{alvesdasilva_geometric_computer_2026,
  title  = {The Geometric Computer: Turing Completeness, Free Energy, and Learning in a Digital Brain on {S³}},
  author = {Alves da Silva, Walter Henrique},
  year   = {2026},
  month  = {April},
  doi    = {10.5281/zenodo.19578024}
}
```
