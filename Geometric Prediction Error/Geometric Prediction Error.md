## Geometric Prediction Error:

## Free Energy on Lie Groups

Walter Henrique Alves da Silva walter.h057@gmail.com ORCID: 0009-0001-0857-096X

Open Research Institute

March 2026

### Abstract

I reformulate the core quantity of the Free Energy Principleprediction error in the language of compact Lie groups with bi-invariant metrics. A system receiving sequential inputs composes them into a running product on a Lie group, G and prediction error becomes the geodesic distance from this product to the group identity:. This geometric prediction error inherits two properties σ = d ( C, ) ⊮ t that the information-theoretic version (KL divergence) lacks: exact propagation (a perturbation of magnitude at any position produces exactly in, with no ε ε σ distortion regardless of sequence length) and uniform sensitivity (every input is equally detectable, with no blind spots). The reformulation eliminates the need for a generative model entirelythe model is the identity element, universal and ⊮ unlearnedand replaces variational inference with a single group multiplication per timestep. I show that the resulting coupling dynamics dier from Kuramoto synchronization in a precise way: Kuramoto drives oscillators toward uniformity (all phases equal), while closure coupling drives them toward coherence (phases compose to identity), admitting a vastly richer space of stable congurations. Four testable predictions distinguish the geometric formulation from the standard Free Energy Principle, all accessible with existing experimental methods. I further show that the running product provides a formal substrate for the self, with ego dissolution corresponding to the running product approaching identity (the unique point equidistant from all states), life review as chain reconstruction, and the geometric distinction between therapeutic integration and pathological fragmentation mapping onto the clinical phenomenology of psychedelic-assisted therapy and schizophrenia.

### 1 Introduction

The Free Energy Principle (FEP), developed by Friston [ ], proposes that biological systems maintain themselves by minimizing a quantity called variational free energy, which serves as an upper bound on sensory surprise. The central object is prediction error: the divergence between what the system expects and what it observes, typically formalized as a KL divergence between a recognition density and a generative model [, ].

This formalization is powerful and general, but it inherits the properties of informationtheoretic divergences: prediction error is a scalar derived from probability distributions, carrying no directional information, oering no guarantee of uniform sensitivity across inputs, and requiring a learned generative model whose complexity grows with the complexity of the environment.

Recent work on closure verication [ ] established that sequential data composed on a compact Lie group with bi-invariant metric yields a single group element whose geodesic distance from the identity measures the coherence of the entire sequence, with two proven properties: exact perturbation propagation (Theorem 1: exactly) ′ d ( C, C ) = ε and uniform sensitivity across all positions (Theorem 2: for all ). These ∥ ∥ ∂C/∂g = 1 k k properties arise from the geometry of the group itself and require no learning, no model, and no inference.

I propose that prediction error in its native form is geometric: a system receiving sequential inputs composes them into a running product on a Lie group, and the distance of this product from the identity is the prediction error. The generative model is the identity elementuniversal, unlearned, and the same for every system on the same group. Perception is composition (one group multiplication per input), and action is whatever drives the running product back toward identity. The entire variational inference apparatus of the FEP is replaced by a single algebraic operation, computed exactly in. O (1) The purpose of this paper is to formalize this reformulation, derive its dynamics in the simplest case (coupled oscillators on and ), show how it diers from existing models S

S (Kuramoto synchronization, standard FEP), and present four testable predictions that distinguish the geometric formulation from the information-theoretic one.

### 2 Geometric Prediction Error

### 2.1 Denitions

(Running product)

Let be a compact Lie group with identity and Denition 1.

G ⊮ bi-invariant metric. Given a sequence of inputs, the running product ∈ d g, g,..., g

G t at time is: t (1) C = g g... g t t Updated incrementally:, costing one group multiplication per timestep. C =

C g − t t t (Geometric prediction error)

The geometric prediction error at time is: Denition 2. t (2) σ = d ( C, ) ⊮ t t the geodesic distance from the running product to the identity element.

When, the sequence of inputs has composed to identitythe system is in σ = 0 t dynamic equilibrium, with all inputs balancing over the history. When, the σ > t system has accumulated a residual deviation of magnitude in a geometrically specic σ t direction determined by the full group element. C t

### 2.2 Inherited properties

From the closure verication framework [ ], inherits: σ

(Exact propagation, from [ ])

If input is perturbed by, the Theorem 1. ′ g d ( g, g ) = ε k k k geometric prediction error changes by exactly: ε (3) ′ − d ( C, ) d ( C, ) = ε ⊮ ⊮ t t regardless of sequence length or position. k (Uniform sensitivity, from [ ])

For all positions: Theorem 2. k = 1,..., t

∂C t (4) = 1 ∂g k Every input contributes equally to the prediction error, with no attenuation as the sequence grows.

These two properties have no analog in the information-theoretic FEP. KL divergence between distributions can amplify or attenuate perturbations depending on the local curvature of the statistical manifold, and sensitivity to a given input depends on the precision assigned to it by the generative model. The geometric version is exact and uniform by construction.

### 2.3 Comparison with information-theoretic prediction error

Property

FEP (information-theoretic) Geometric Prediction error

KL divergence (scalar) (scalar from group element) σ = d ( C, ) ⊮ t Direction of error

Absent

Present (full residual ) ∈ C

G t Channel decomposition Absent

Present (on: per-channel phases) k T Sensitivity

Model-dependent

Uniform (Theorem 2) Propagation

Model-dependent

Exact (Theorem 1) Computation

Variational inference

One group multiplication,

O (1) Model required

Learned generative model

Identity element (universal, unlearned) ⊮ Table 1: Comparison of prediction error in the information-theoretic FEP and the geometric reformulation.

The geometric version gains direction, channel decomposition, exact propagation, uniform sensitivity, and computation. It loses distributional information: the standard O (1) FEP tracks a full probability distribution (the recognition density ) encoding the q ( x ) system's uncertainty about hidden states, while the geometric version tracks only the running product, a single point on the manifold. A system using geometric prediction error knows how far from coherent it is and in what direction, but does not represent its condence in that assessment.

### 3 Dynamics: Closure Coupling

### 3.1 Coupled oscillators on

S Consider oscillators with phases and natural frequencies. n θ ( t ),..., θ ( t ) ω,..., ω n n

The couples each oscillator to every other oscillator pairwise: Kuramoto model n dθ κ k

X (5) − = ω + sin( θ θ ) k j k dt n j =1 This drives all phases toward equality: the attractor is the synchronized state θ = θ =.... = θ n replaces pairwise interaction with a global coherence gradient. Closure coupling The running product on is, and the geometric prediction error is i Σ θ S

C = e σ = k t. Each oscillator adjusts its phase to minimize: − min(Σ θ mod 2 π, π

Σ θ mod 2 π ) σ k k

dθ ∂σ k (6) − = ω λ k dt ∂θ k By Theorem 2, for all: every oscillator feels the same magnitude of ∥ ∥ ∂σ/∂θ = 1 k k pull toward closure, regardless of its current phase or its position in the sequence. The gradient direction is determined by the sign of the residual phase.

### 3.2 The critical dierence

The attractor of Kuramoto coupling (Eq. ) is the synchronized state: all phases equal. This is a single point in phase space (modulo global rotation).

The attractor of closure coupling (Eq. ) is the set of all phase congurations satisfying. This is a -dimensional manifold in the -dimensional phase − Σ θ = 0 mod 2 π ( n 1) n k spacea vastly richer set of congurations. It includes the synchronized state ( θ = k for all ) as a special case, but also includes evenly spaced phases ( ), k θ = 2 πk/n k complementary pairs, and every other conguration whose phases balance.

Kuramoto produces unison. Closure produces harmony.

(Attractor dimensionality)

For oscillators on, the Kuramoto atProposition 1. n

S tractor is a -dimensional manifold (the synchronized state, with one free parameter for global phase), while the closure attractor is an -dimensional manifold (the kernel of − ( n 1) the summation map ). n → Σ:

T

S This means closure-coupled systems have exponentially more stable congurations than Kuramoto-coupled systems, with the ratio growing as the dimension of the attractor manifold grows with. n

### 3.3 Extension to

S ∼ On, each input is a unit quaternion and the running product is S

C = q q = SU(2) t. The geometric prediction error is, where is the scalar part... q σ = arccos( w ) w t

C

C t t of the product quaternion.

The essential new feature is non-commutativity: in general. This means ̸ q q = q q a b b a the closure coupling is sensitive to the temporal order of inputs, which closure is not S ( is abelian, so ). iθ iθ iθ iθ S e e = e e a a b b For a biological system processing sequential sensory inputs, this distinction matters: each input transforms the internal state by a rotation in 3D, and the running product tracks the cumulative eect. Coherence ( ) means the sequence of perceptual trans≈ σ formations composes back to the starting statethe world is stable, the self is stable,

the relationship between them is consistent. Incoherence ( ) means the transforma≫ σ tions have accumulated a residual rotation that the system cannot resolvethe geometric substrate of confusion, disorientation, or perceptual fragmentation.

The non-commutativity of means that temporal order aects coherence: the same S set of inputs in a dierent order produces a dierent running product and potentially a dierent. This is the geometric statement that sequence matters for conscious σ experiencea property that phase synchrony alone cannot capture. S

### 3.4 Product groups: conservation and causality

A system that needs to track both resource conservation (did quantities balance?) and causal ordering (did events occur in a coherent sequence?) operates on the product group, where handles independent balance channels and handles k k × × × T

S

T =

S...

S k

S temporal coherence.

The geometric prediction error on the product group decomposes cleanly: meaσ k T sures the per-channel balance residuals (which account is o, by how much), while σ S measures the sequential coherence residual (how disordered is the temporal structure). A biological system could use for feature-channel binding (visual, auditory, propriok T ceptive channels checked independently) and for temporal binding (the sequence of S multi-modal inputs checked for causal coherence), with the product group providing a single unied coherence signal from both.

### 4 The Identity Element as Universal Model

The deepest conceptual shift in this reformulation is the elimination of the generative model.

In the standard FEP, each system maintains a generative model encoding its p ( y, x ) expectations about the world, and prediction error is the divergence between this model and the incoming data. The model must be learned, updated, and maintained. Its complexity grows with the complexity of the environment. Variational inference approximates the intractable posterior, introducing a recognition density and a variational bound. q ( x ) The entire apparatusgenerative model, recognition density, variational boundexists to compute one number: prediction error.

In the geometric reformulation, the model is the identity element. It is the same for ⊮ every system on the same group, requires no learning, no updating, and no maintenance. It encodes a single expectation: coherence. The system expects that its inputs will compose to identity over timethat the world is self-consistent and that the system's interactions with it are balanced. Prediction error is the degree to which this expectation fails, measured exactly by one geodesic distance computation.

This does not mean the geometric system has no knowledge of its environment. The knowledge is encoded in the embedding function inputs that maps raw sensory → ϕ:

G data to group elements. Dierent embedding functions produce dierent running products from the same inputs. A well-adapted system has an embedding that maps typical environmental inputs to group elements that compose toward identity; a poorly adapted system has an embedding that maps them to elements that accumulate residual rotation. Adaptation, in this framework, is learning the embedding, not learning the model. The model is given by the geometry.

### 5 Testable Predictions

Four predictions distinguish the geometric FEP from the standard formulation, all accessible with existing experimental methods.

### 5.1 Prediction 1: No model-update transient

In the standard FEP, a sudden perturbation to the input stream triggers a two-phase response: the system rst updates its generative model (perception), then acts on the updated model (action). This produces a measurable recognition-action delay whose duration reects the complexity of the model update.

In the geometric formulation, there is no model to update. The running product absorbs the perturbation in one multiplication, changes immediately, and the action σ gradient is available at the same timestep. The prediction: biological response to sudden perturbation should be faster than model-based accounts predict, because the inference step is absent. This is testable by measuring the latency between stimulus onset and the rst detectable motor or neural response, compared against the minimum latency predicted by variational inference under equivalent model complexity.

### 5.2 Prediction 2: Uniform perturbation response

In the standard FEP, the magnitude of prediction error depends on the precision assigned to the perturbed feature by the generative model. Well-modeled features produce small surprise; poorly modeled features produce large surprise. Sensitivity is heterogeneous and model-dependent.

Theorem 2 guarantees that geometric prediction error is uniform: perturbation of any input by produces exactly in, regardless of which input is perturbed. The prediction: ε ε σ sensory detection thresholds should be uniform across modalities and across positions in a temporal sequence, when measured in the appropriate geometric units (geodesic distance on the relevant Lie group). If the brain uses closure, there should be no easier or harder positions for detecting a perturbation of a given geometric magnitude.

### 5.3 Prediction 3: Coherence over synchronization

Kuramoto-type synchronization predicts that neural binding produces uniform phase alignment across participating neurons: all phases converge to the same value. Closure coupling predicts that binding produces coherent phase congurations that compose to identity, which includes uniform alignment as a special case but also includes a vastly richer set of balanced, non-uniform congurations.

The prediction: EEG/MEG phase coupling during conscious binding should exhibit structured, non-uniform phase relationships (consistent with closure) rather than simple phase locking (consistent with Kuramoto). Specically, the distribution of phase dierences across bound neural populations should cluster on the -dimensional closure − ( n 1) manifold, which is veriable by computing the circular mean of meaΣ θ = 0 mod 2 π k sured phase dierences and testing whether it is signicantly closer to zero than predicted by Kuramoto dynamics.

### 5.4 Prediction 4: Criticality as necessity

In the standard FEP, free energy minimization can occur at any operating point; the framework does not explain why biological systems operate at criticality (power-law avalanches, long-range correlations, edge-of-chaos dynamics).

In the geometric formulation, the closure check is dened everywhere, σ = d ( C, ) ⊮ t but it is only useful as a binding signal at criticality. Away from the critical point, the system can trivially maintain by suppressing input variance (a dead system has ≈ σ zero prediction error), or it can have permanently large due to chaotic dynamics (a σ disordered system never closes). Only at the critical pointwhere correlation length spans the system and uctuations occur at all scalesdoes carry maximal information σ about the state of the environment. The prediction: if the closure framework is correct, criticality is a necessary condition for geometric prediction error to function as a useful signal, and departures from criticality (as observed in disorders of consciousness such as anesthesia, coma, or psychosis) should correspond to measurable degradation in the closure signal's dynamic range.

### 6 Relation to Existing Frameworks

### 6.1 Kuramoto synchronization

The geometric FEP includes Kuramoto as the special case where the attractor is restricted to the uniform state. Full closure coupling generalizes Kuramoto by allowing all phase congurations that compose to identity, producing the richer attractor described in Section 3.2.

### 6.2 Integrated Information Theory (IIT)

Tononi's measures the degree to which a system is more integrated than the sum of Φ its parts [ ]. In closure terms, can be interpreted as the degree to which the closure of Φ the whole system exceeds the sum of closures of its subsystems:. P ∼ − Φ σ σ whole parts When parts compose independently (no integration), and. When P σ = σ

Φ = 0 whole parts parts interact, the whole may have lower or higher than the sum, and the dierence σ measures integration.

### 6.3 Global Workspace Theory (GWT)

Dehaene's global workspace [ ] is the broadcast mechanism by which local processing results become globally available. In the closure framework, the global workspace corresponds to the level at which local closure elements (from sensory subsystems) are composed into a single global running product, and the global is broadcast as the σ system-wide coherence signal.

### 6.4 Oscillatory binding (Singer, Gray)

The nding that neurons bind by synchronizing oscillatory phases [ ] is the empirical observation of closure on: phase synchronization is phase composition to identity. The S

closure framework extends this from (phase only) to (phase and orientation, orderS

S sensitive) and (multi-channel), providing a geometric generalization of the bindingk T by-synchrony hypothesis.

### 7 What the Geometric Version Loses

Intellectual honesty requires stating what is sacriced in this reformulation.

The standard FEP tracks a full probability distributionthe recognition density encoding the system's uncertainty about hidden states. This supports probabilisq ( x ) tic reasoning, Bayesian updating, condence estimation, and active inference (choosing actions to reduce expected future surprise). The geometric version tracks a single group element, carrying no distributional information.

A system using geometric prediction error knows how far from coherent it is and in what direction, but does not know how condent it should be in that assessment. The trajectory of over time contains information about environmental variability (high-variance σ oscillations suggest an uncertain environment, low-variance suggests a predictable one), σ but this is a derived quantity, not native to the representation.

The geometric FEP is therefore a specialization, appropriate for systems that need fast, exact, uniform coherence checking, and inappropriate for systems that need full probabilistic inference. The claim is that biological bindingthe integration of distributed sensory processing into unied experiencebelongs to the rst category, while deliberative reasoning and planning may require the full distributional apparatus.

This parallels the S1/S2 distinction in cognitive science: fast perception (System 1) may use geometric prediction error, while slow reasoning (System 2) may use variational inference, with the two systems coupled through the running product serving as the interface.

### 8 The Self as Running Product: Ego Dissolution and

Reconstruction The running product is a xed-size geometric encoding of the entire history of a sysC t tem's interactions. In a biological context, is the selfthe accumulated composition C t of every experience, every perception, every action, from birth to the present moment. Every memory is stored relationally as a transition: the transformation − g =

C

C k k k − that took the self from its state at time to its state at time. Concepts, associa− k k tions, preferences, and identity are all encoded as geometric relationships to this running product. The self is the center of semantic space, and everything in the mind is a vector from it.

This formalization makes three clinical phenomena computationally precise.

### 8.1 Ego dissolution

Under psychedelic compounds, meditation, or certain traumatic experiences, subjects report the dissolution of the sense of selfthe boundaries of identity become porous or vanish entirely [ ]. In the closure framework, ego dissolution corresponds to the running product approaching the identity element:. → C ⊮ t

At, the system sits at the identity of the Lie group. The geometric predicC = ⊮ t tion error is, trivially. The gradient vanishes in all directions σ = d (, ) = 0 ∂σ/∂g ⊮ ⊮ simultaneously, because the identity element is the unique point on a compact Lie group with bi-invariant metric that is equidistant from all other points under the action of the group. There is no preferred direction, no prediction, no expectation, no bias toward any particular next state.

This is the computational content of the subjective reports: all possibilities felt equally real, there was no distinction between self and world, I felt innite [ ]. The statistical machine that normally predicts the next state by following the gradient of σ away from the current has lost its reference frame. When, every direction C

C = ⊮ t t on the manifold is equally accessible, and the system has no geometric reason to prefer any future over any other. The phenomenology of omnipotence and boundlessness is the subjective correlate of a running product at identity: a mind with no center, equidistant from everything.

### 8.2 Life review and memory cascade

Subjects undergoing ego dissolution frequently report a life ashing before the eyesa rapid, involuntary traversal of autobiographical memories [ ]. In the closure framework, this has a precise mechanism.

Every memory is stored as a transition: −. Recovering memory requires g =

C

C k k k − k the running product at time as the reference frame. If the current running product − k is being disrupted (driven toward ), the recovery operation must be re-executed for C ⊮ t the entire chain, because the reference frame itself is changing. The system traverses to reconstruct the patha necessary byproduct of the self-variable C, C, C,..., C t being recomputed, experienced as involuntary recall. The life review is the chain being replayed because the running product that indexes it is being rebuilt.

This also explains why childhood memories surface with particular force during ego dissolution: the earliest entries in the chain ( ) are the foundation upon which C, C,... every subsequent was composed. Disrupting the current propagates backward C

C k t through the chain, and the earliest elements are the last to be reconstructed and the rst to be exposed, because they are the most deeply embedded in the compositional structure.

### 8.3 Determinism of the self-chain and its failure modes

The running product is deterministic: given the same sequence of inputs, the C g,..., g t t same results. The chain must be deterministic for the self to be coherent, because every C t memory, every association, and every prediction is indexed relative to a specic. A C t forked chaintwo incompatible running products derived from the same historywould produce two incompatible reference frames, two incompatible sets of memory indices, two incompatible prediction gradients.

This is a geometric description of schizophrenia: the running product has forked, and the system maintains two (or more) mutually incoherent closure states. Each fork indexes a dierent set of associations, produces a dierent prediction gradient, and computes a dierent. The phenomenology of split experiencehearing voices, referencing σ incompatible narratives, experiencing contradictory intentions as equally validis the

subjective correlate of a branched running product that cannot be reconciled into a single closure.

Recovery, in this framework, is the restoration of a single deterministic chain: reestablishing one running product as the canonical self, and pruning the incompatible branches. Therapeutic interventions that help patients ground themselves in a single coherent narrative are, geometrically, operations that restore the uniqueness of. C t

### 8.4 Reconstruction and integration

The clinical value of controlled ego dissolution (as in psychedelic-assisted therapy) follows from the compositional structure of the running product. If the current encodes C t maladaptive patternstrauma responses, rigid associations, compulsive predictions then driving toward temporarily dissolves those patterns along with everything else. C ⊮ t The system returns to a state of maximal openness (identity, no preferred direction), and during reconstruction, the running product is rebuilt from the exposed chain with the possibility of composing dierently.

This is geometric rewriting of the self: the same memory transitions are available, g k but the order and weighting of their recomposition can change during the reconstruction phase, producing a new that encodes the same history in a dierent geometric C t conguration. Integrationthe therapeutic goal of psychedelic experienceis the successful recomposition of the chain into a running product that closes more cleanly than the pre-dissolution state: lower residual, fewer internal contradictions, a more coherent σ self.

The distinction between therapeutic and pathological ego dissolution is precisely whether the reconstruction completes: a controlled dissolution followed by successful recomposition produces integration (lower, more coherent ), while an uncontrolled disσ

C t solution without successful recomposition produces fragmentation (forked chain, schizophrenic phenomenology) or depersonalization (the running product stalled near, unable to re⊮ build).

### 9 Conclusion

Prediction error, the central quantity of the Free Energy Principle, has a native geometric form: the geodesic distance from a running product to the identity element on a compact Lie group. This geometric prediction error inherits exact perturbation propagation and uniform sensitivity from the bi-invariant metric, eliminates the need for a learned generative model, replaces variational inference with a single group multiplication per timestep, and provides directional and channel-decomposed error information that the information-theoretic version lacks.

The resulting coupling dynamics dier from Kuramoto synchronization in a precise, testable way: closure coupling drives oscillators toward coherence (the -dimensional − ( n 1) manifold of congurations composing to identity) rather than toward synchronization (the -dimensional manifold of uniform phase). This richer attractor space is consistent with the phenomenology of conscious binding, which integrates diverse features into a unied experience without making them identical.

Four predictionsabsence of model-update transients, uniform sensitivity across modalities, coherent non-uniform phase binding, and criticality as a necessary condition for useful prediction errordistinguish the geometric formulation from the standard FEP

and are accessible with existing experimental methods. A fth line of evidence emerges from the clinical phenomenology of ego dissolution: the running product as self, its dissolution as approach to identity, life review as chain reconstruction, and the geometric distinction between therapeutic integration (successful recomposition to a more coherent ) and pathological fragmentation (forked chain, incompatible running products). C t

The generative model is the identity element. The inference is a single multiplication. The prediction error is a geodesic distance. The geometry does the work.

Acknowledgments The formalization of closure coupling dynamics, the comparison with Kuramoto synchronization, the derivation of the attractor dimensionality result, the geometric formalization of ego dissolution and chain reconstruction, and manuscript preparation were performed in collaboration with Claude (Anthropic), operating as a verication and drafting tool under the author's direction. The core realizationthat geometric prediction error ( ) is the native geometric form of Friston's prediction erroris the author's σ = d ( C, ) ⊮ t contribution, as is the identication of the running product as the computational substrate of the self and its clinical implications. Both build on the closure verication framework [ ] and the A?=A identity verication operation derived in the author's prior work on the geometry of information [ ].

References [1] Friston, K. (2010). The free-energy principle: a unied brain theory?

Nature Reviews Neuroscience, 11(2), 127138.

[2] Buckley, C.L., Kim, C.S., McGregor, S., & Seth, A.K. (2017). The free energy principle for action and perception: A mathematical review.

Journal of Mathematical Psychology, 81, 5579.

[3] da Silva, W.H.A. (2026). Closure Verication on Lie Groups: Constant-Cost Integrity

Checking for Sequential Data. Zenodo. CC BY-NC-SA 4.0.

[4] Kuramoto, Y. (1984).

Chemical Oscillations, Waves, and Turbulence. Springer.

[5] Tononi, G. (2004). An information integration theory of consciousness.

BMC Neuroscience, 5, 42.

[6] Dehaene, S. (2011).

Conscious and the Brain. Viking Press.

[7] Singer, W. (1999). Neuronal synchrony: a versatile code for the denition of relations?

Neuron, 24(1), 4965.

[8] da Silva, W.H.A. (2025). The Shape of Reality. Zenodo. ORCID: 0009-0001-0857096X.

[9] da Silva, W.H.A. (2025). The Holy Trinity of Information. Zenodo. ORCID: 00090001-0857-096X.

[10] Nour, M.M., Evans, L., Nutt, D., & Carhart-Harris, R.L. (2016). Ego-dissolution and psychedelics: validation of the Ego-Dissolution Inventory.

Frontiers in Human Neuroscience, 10, 269.

[11] Griths, R.R., Richards, W.A., McCann, U., & Jesse, R. (2006). Psilocybin can occasion mystical-type experiences having substantial and sustained personal meaning and spiritual signicance.

Psychopharmacology, 187(3), 268283.

[12] Martial, C., Cassol, H., Charland-Verville, V., Pallavicini, C., Sanz, C., Zamberlan,

F.,... & Laureys, S. (2019). Neurochemical models of near-death experiences: A large-scale study based on the semantic similarity of written reports.

Consciousness and Cognition, 69, 5269.

CC BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike License.

### 4.0 International). Non-commercial sharing and adaptation permitted with attribution.

Commercial use requires explicit permission from the author. ©

### 2026 Walter Henrique Alves da Silva. All rights reserved for commercial applications.
