# Geometric Prediction Error: Free Energy on Lie Groups

**Author:** Walter Henrique Alves da Silva  
**Date:** March 2026  
**Institution:** Open Research Institute (Pontifícia Universidade Católica do Paraná)  
**DOI:** [10.5281/zenodo.19052561](https://doi.org/10.5281/zenodo.19052561)

## Files

- PDF: [Geometric Prediction Error.pdf](./Geometric%20Prediction%20Error.pdf)
- Markdown (agent-readable extraction): [Geometric Prediction Error.md](./Geometric%20Prediction%20Error.md)

## Summary

Friston's Free Energy Principle defines prediction error through KL divergence, variational free energy, and surprisal — all scalars derived from probability distributions over a generative model. This paper reformulates prediction error as geodesic distance on a compact Lie group, which produces two properties the information-theoretic version cannot guarantee.

The first is exact perturbation propagation: a perturbation of magnitude ε at any position in a composition chain shifts the running product by exactly ε regardless of chain length or position, because bi-invariance of the S³ metric makes group multiplication an isometry. The second is uniform input sensitivity: ‖∂C/∂g_k‖ = 1 for every position k, so no element of the sequence is privileged or blind. Both are theorems, not design goals, following from the geometry alone.

The geometric formulation also eliminates the generative model. Rather than maintaining a probabilistic model of causes and running variational inference against it, the system multiplies one group element per timestep and reads the result as σ = d(C_t, 𝟙) — one operation, O(1) cost, exact. When σ > 0 the Hopf decomposition reads off which axis diverged and by how much, providing the directional information that the scalar FEP discards.

The paper distinguishes this formulation from Kuramoto synchronization, which lives on S¹ and loses sensitivity to ordering because S¹ is commutative. S³ preserves the distinction between a→b and b→a, making it the correct substrate for temporal binding where the sequence of events matters.

## Testable Predictions

Binding failures should exhibit the algebraic signature of S³ non-commutativity: order-sensitive integration errors irreducible to scalar magnitude. Neural oscillatory binding should show neurally dissociable luminance-type and chrominance-type divergences corresponding to the W and RGB channels of the Hopf decomposition. The attosecond regime should show sub-cycle structure where the geometric and information-theoretic predictions diverge.

## Role in the Series

The Zeroth Law proves the three theorems algebraically; this paper presents them to the neuroscience and active inference community in the language of prediction error and free energy, and proposes the experiments that would distinguish the geometric from the information-theoretic formulation.

## Citation

```bibtex
@misc{alvesdasilva_geometric_prediction_error_2026,
  title  = {Geometric Prediction Error: Free Energy on {Lie} Groups},
  author = {Alves da Silva, Walter Henrique},
  year   = {2026},
  month  = {March},
  doi    = {10.5281/zenodo.19052561}
}
```
