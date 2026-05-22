# The Zeroth Law: Identity and Coherence

**Author:** Walter Henrique Alves da Silva  
**Date:** March 2026  
**Institution:** Open Research Institute (Pontifícia Universidade Católica do Paraná)  
**DOI:** [10.5281/zenodo.19140055](https://doi.org/10.5281/zenodo.19140055)

## Files

- PDF: [The Zeroth Law.pdf](./The%20Zeroth%20Law.pdf)
- Markdown (agent-readable extraction): [The Zeroth Law.md](./The%20Zeroth%20Law.md)

## Summary

The paper asks what minimum mathematical structure can pose and answer A?=A for any ordered sequence of data, and derives the answer from two foundational observations without free parameters.

**First law (Existence requires interaction):** Nothing is defined in isolation — every entity exists through its relationships, and stripping away all relationships leaves nothing to point at. This is an observation about what existence means, not a starting assumption: a particle with no forces, no measurable effects, and no interactions is operationally identical to nothing.

**Second law (Coherence requires directionality):** For anything to persist across time there must be a before and an after, and directionality is what allows accumulation so that each state builds on the previous one. Coherence without direction is indistinguishable from static noise.

Hurwitz's theorem closes the argument: the only normed division algebras over the reals are ℝ, ℂ, ℍ, and 𝕆, and ℝ and ℂ are commutative (which loses directionality), while 𝕆 are non-associative (which makes running products ambiguous). Quaternions satisfy both laws simultaneously, and the unit quaternions form S³, so the geometry is forced along with the algebra.

## The Three Theorems

S³ produces three theorems that together form a complete diagnostic for coherence failure in any ordered data:

**Theorem 0 — The Zeroth Law (Axis Completeness):** Coherence between two ordered sequences can break in exactly two ways, orthogonal and exhaustive, corresponding to the two eigenspaces of the conjugation operator on ℍ. The *existence axis* (scalar W, symmetric under conjugation) signals that something is present in one sequence and absent from the other. The *position axis* (vector RGB, antisymmetric under conjugation) signals that something is present in both sequences at different positions. These two types are algebraic inverses of each other: inversion flips the vector part while preserving the scalar part, exhausting the possible axes by algebraic necessity.

**Theorem 1 — Exact Propagation:** A perturbation of magnitude ε at any position in a composition chain shifts the running product by exactly ε, regardless of chain length or perturbation position, because bi-invariance of the S³ metric makes group multiplication an isometry.

**Theorem 2 — Uniform Sensitivity:** The sensitivity ‖∂C/∂g_k‖ = 1 for all k, so every element of the sequence contributes equally to the running product's detectability.

Theorem 0 identifies the type of failure, Theorem 1 preserves its magnitude without distortion through the composition chain, and Theorem 2 guarantees it is detectable wherever it occurred.

## The Prism

The Hopf fibration S³ → S²×S¹ acts as a prism that makes the diagnostic readable in separated channels. W (scalar, S¹ fiber) tracks the existence axis — whether something is present or absent, aligned with the second law. R, G, B (vector, S² base) track the position axis — direction and magnitude of positional displacement, aligned with the first law. The human eye evolved the same luminance/chrominance decomposition through selection pressure, parsing the identical split the algebra provides algebraically from these two founding observations.

## Six Operations

The SDK implements six operations, each a direct translation of a component of Euler's identity:

- **Embed:** bytes → unit quaternion on S³
- **Compose:** Hamilton product, the running product, O(1) per record
- **Invert:** quaternion conjugate q̄ = (w,−x,−y,−z)
- **Sigma:** σ = arccos(|w|), geodesic distance from identity
- **Diff:** a⁻¹·b, the algebraic gap between two compositions
- **Compare:** measures sigma and returns a verdict: equal, inverse, or disordered

## Gilgamesh and Enkidu

**Gilgamesh** resolves ambiguity in space: given two completed sequences, binary search on S³ locates the first divergence in O(log n) steps, classifying each record as coherent (advance both pointers), missing (W axis, existence break), or reordered (RGB axis, position break).

**Enkidu** resolves ambiguity in time: when records arrive on two live streams, an unmatched record opens a grace period as potentially missing. When the grace period expires without a match it promotes to missing on the W axis, and when a late match arrives the Hopf fiber reclassifies it to the RGB axis. The reclassification is forced by the geometry.

## Experimental Validation

The Brahman experiment uses 1,031 parameters trained for 9 minutes on a laptop. Gradient descent on S³ learns that opening and closing brackets are compositional inverses with no instruction beyond the geometry and a closure loss — the system discovers algebraic structure from data alone, because the geometric zero provides the target that any balanced sequence must return to.

## Role in the Series

Every operation in the SDK and every theorem in the geometric computer traces back to the structure derived here. The two foundational observations force the algebra, the algebra forces S³, S³ forces the three theorems, and the theorems force the six operations — no free parameters anywhere in the chain.

## Citation

```bibtex
@misc{alvesdasilva_zeroth_law_2026,
  title  = {The Zeroth Law: Identity and Coherence},
  author = {Alves da Silva, Walter Henrique},
  year   = {2026},
  month  = {March},
  doi    = {10.5281/zenodo.19140055}
}
```
