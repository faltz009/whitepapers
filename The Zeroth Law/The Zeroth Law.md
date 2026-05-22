## The Zeroth Law: Identity and Coherence

Walter Henrique Alves da Silva walter.h057@gmail.com ORCID: 0009-0001-0857-096X

Open Research Institute

March 2026

### Abstract

How does information gain meaning? Shannon answered how much information a channel can carry, founding the theory of information capacity. This paper asks the prior question: how does a sequence of symbols become something that can be checked, composed, and veried as coherent how does raw data become trustworthy?

I derive the answer from two axioms. Existence requires interaction: nothing is dened in isolation. Coherence requires directionality: a before and after is what allows accumulation. These two constraints force a specic algebra (the quaternions), a specic geometry (the 3-sphere, proven unique by Hurwitz's theorem), and a S specic decomposition of every possible failure into exactly two types: something is missing, or something is out of place. I call this last result the Zeroth Law, because it precedes and grounds every measurement the geometry provides.

The construction produces a computational primitive a data structure where any ordered sequence composes into a xed-size geometric state that is lossless, self-verifying, and decomposable into channels at every step. A working implementation (the Closure SDK, 22 operations, 207 tests) is released alongside this paper, benchmarked against SHA-256 checksums, Merkle trees, and hash chains. An experimental validation (Brahman, 1,031 parameters, 9 minutes of training on a laptop) demonstrates that gradient descent on discovers algebraic structure from S data alone the system learns that opening and closing brackets are compositional inverses, with no instruction beyond the geometry and a closure loss.

Everything in the derivation is deterministic. The axioms force the algebra, the algebra forces, forces three theorems, the theorems force the channel decomS

S position, and the decomposition matches experiment. There are no free parameters from axiom to result.

### 1 The Question

Consider a page of symbols. By itself, the page means nothing ink on paper, voltage in memory, ones and zeros in a register. The symbols become meaningful only when something checks them against something else: another copy, an expectation, a rule, a memory. Meaning enters through verication two ledgers agree and the transaction is

real, two witnesses corroborate and the testimony holds, a prediction matches an observation and the theory survives. In every case, the same operation is at work: comparison of one thing with another, and a judgment of whether they cohere.

This operation is older than mathematics. It is the question every existing thing must answer continuously, at every scale, in every substrate:

A am I still what I was? proton answers it through the electromagnetic force that binds its quarks, a cell answers it through the metabolic cycle that maintains its membrane, a mind answers it through the thread of memory that connects this moment to the last, and a distributed ledger answers it through the consensus protocol that reconciles its nodes. The question is always the same and the failure to answer it is dissolution: the proton decays, the cell? A =

A dies, the mind fragments, the ledger forks.

The question this paper asks is: what is the minimal mathematical structure that can pose and answer for any ordered sequence of data?? A =

A Shannon [ ] answered a dierent question how much information a channel can carry and founded the theory of information capacity. His atom is the bit: a binary distinction, measured by entropy, and everything digital is built on it. The bit is also shapeless, orientationless, unaware of its neighbors, and two bits side by side compose into nothing richer than what they were apart. Shannon's theory measures the size of the pipe, and the structure of what ows through it remains an open question.

The question of structure requires a dierent atom. An atom that has shape, that knows its orientation, that composes with its neighbors into something richer, and that can verify its own coherence. This paper derives that atom.

The derivation begins with an equation that has been taught as a beautiful curiosity for nearly three centuries: (1) iπ e + 1 = 0 Five symbols, three operations, every foundational constant. Euler wrote it down in

### 1748 [

] and called it remarkable. This paper reads it as an engineering specication. Each symbol names a property that ordered information must have, and the equation describes how those properties compose. By the end of the paper, every operation in the computational toolkit embedding, composition, inversion, verication, channel decomposition will be a direct translation of a component of this identity into an operation on data.

The claim is specic: ordered information has a natural geometry, that geometry is the 3-sphere (the space of unit quaternions), and this is forced by two axioms S and a classical theorem of Hurwitz. The paper derives it in full, implements it as a working computational tool, reports the rst experimental conrmation, and draws the consequences for how information gains meaning which is to say, for how consensus actually works.

### 2 Two Axioms

The derivation begins with two statements about what it takes for anything to exist and persist.

(Existence requires interaction)

Nothing is dened in isolation. Every entity Axiom 1. exists through its relationships to other entities a proton through the force between its quarks, a word through its use among other words, a node through its connections in

a network. Strip away all relationships and nothing remains to point at. Existence is relational.

(Coherence requires directionality)

For anything to persist across time, there Axiom 2. must be a before and an after an input that precedes an output, a cause that precedes an eect. Directionality is what allows accumulation: each state builds on the previous one, and the sequence carries forward. A universe with direction is a universe with memory.

These axioms are minimal in the sense that removing either one collapses the structure entirely: interaction (Axiom 1) is what distinguishes entities and produces information, directionality (Axiom 2) is what orders sequences and produces coherence, and together they produce the complete algebraic structure needed for the construction exactly the quaternions, nothing more and nothing less.

### 2.1 What the axioms produce

Axiom 1, taken algebraically, says that generators are dened entirely by how they interact with each other the mathematical structure called a Lie bracket, which measures the dierence between doing then versus then. When this dierence is zero, X

Y

Y

X the generators are independent; when it is nonzero, each one's identity depends on the other. This is Axiom 1 made algebraic: pure relational structure.

Axiom 2, taken algebraically, says there must be a one-way map from the space of generators to the space of states the exponential map, which takes an innitesimal tendency (a direction to rotate in) and produces a nite transformation (an actual rotation, a denite state). The map ows in one direction: from generator to transformation, from cause to eect. This is Axiom 2 made algebraic: the arrow that gives composition its direction.

Together, the two axioms produce a consistency condition (the Jacobi identity) that guarantees interactions can refer to each other recursively without generating contradictions the same problem Bertrand Russell found in set theory, where self-reference produces paradox, resolved here by the algebra's own structure. The formal construction appears in Appendix A; what matters here is the output.

The output is the quaternion algebra [ ], and it has two parts. H The comes from Axiom 1. Three imaginary axes, each dened vector part ( i, j, k ) entirely through interaction with the others:,,. Fully symmetric, i j = k j k = i k i = j fully relational, each axis existing only because the other two do. This is interaction made concrete: three dimensions that generate each other through composition.

The comes from Axiom 2. The product of all three interactions lands scalar part ( w ) on the real axis and stays there:. The real axis receives the result of interaction − ijk = unidirectionally,, and generate, and the ow is one-way. This is directionality i j k w made concrete: a channel that accumulates the product of all interactions.

### 2.2 The cross-parametrization

Euler's identity encodes how the two parts relate, and the relationship is the heart of this paper.

The constant parametrizes cycles periodicity, return, the property that after a π full rotation you arrive back where you started. It lives naturally on the vector axes (RGB), because cycles require multiple dimensions through which to rotate.

The constant parametrizes invertibility the function that equals its own derivative, e self-generating by denition. It lives naturally on the scalar axis (W), because invertibility is a directional property: every step forward has a unique step backward, and the direction matters.

When the algebra moves from complex numbers to quaternions (from to ), it C

H trades commutativity the property that, that order does not matter. This ab = ba is 's property being sacriced. And this sacrice is precisely what creates 's property: π e when order starts mattering, directionality emerges. Losing commutativity IS gaining directionality. The sacrice of one constant produces the emergence of the other.

At the same time, the algebra keeps associativity the property that, ( ab ) c = a ( bc ) that grouping does not matter. This is 's property being preserved. And this preservae tion is precisely what allows 's property to persist: associativity guarantees that every π element has an exact inverse (you can always undo a step by regrouping), and exact invertibility is what makes the cycle close. Preserving one constant allows the return of the other.

The cross is complete: 's sacrice produces 's emergence, and 's preservation π e e produces 's return. Each constant depends on the other through the structure of the π algebra.

There is a subtlety here that matters. The commutative property of survives inside π the quaternion the vector space remains internally symmetric as a three-body ( i, j, k ) system, each axis interchangeable with the others through cyclic permutation. What changes is that this commutative space is now coupled to a directed scalar axis ( ) w through the associativity of the full quaternion. The coupling is Euler's identity operating on the planes: the three vector dimensions compose through the scalar dimension, and the sign of is the interaction that binds them. The structure − ijk =

### 3 + 1

three symmetric spatial dimensions plus one directional scalar dimension is the unique output of coupling a commutative interaction space (Axiom 1) with a directional accumulation axis (Axiom 2) through an associative algebra. It is forced by the axioms, and there is no other conguration that satises both.

### 3 Why

and Only

## S

## S

The algebra determines the geometry, and the geometry is unique.

In 1898, Hurwitz proved that there are exactly four normed division algebras over the reals: the real numbers, the complex numbers, the quaternions, and the octonions R

C

H [ ]. Each one is obtained by doubling the previous, and each doubling trades away a O structural property:

Going from to trades ordering you cannot say whether is greater or less than i R

C. Going from to trades commutativity, so the order of multiplication ̸ ij = ji C

H matters. Going from to trades associativity, so even the grouping ̸ ( ab ) c = a ( bc ) H

O of multiplication matters.

Now consider what sequential composition requires. A running product

C =

C g t t − t is built by multiplying one element at a time onto an accumulating total. This requires associativity: if grouping mattered, the running total would depend on how you parenthesize the history, and there is no canonical parenthesization for a stream of arriving data. Octonions break running products because and can give dierent answers, ( ab ) c a ( bc ) making the total so far ambiguous.

Quaternions are therefore the richest algebra where sequential composition is welldened. The unit quaternions form the 3-sphere the set of all quaternions with S [ ]. This is the composition space, and Hurwitz guarantees there w + x + y + z = 1 is no richer one.

A useful way to think about this: choosing your composition space is like choosing a number system for keeping books. Real numbers can track a single unsigned balance. Complex numbers add a sign (credit and debit), gaining a dimension. Quaternions add ordering (which transaction came rst), gaining two more dimensions and for a ledger, ordering is essential because the sequence of transactions determines the state. Octonions would add one more doubling, but the books would no longer balance deterministically because the associativity that guarantees well-dened running totals would be gone. Quaternions are the sweet spot: the richest system where the books always close.

What about simpler spaces? The circle (unit complex numbers) and the -torus k S k

T ( independent circles) are both Lie groups where composition is dened. They are also k projections of through the Hopf bration (Section 5), seeing less of the same structure. S composes phases but loses sensitivity to ordering adding then gives the same S a b result as adding then, because is commutative. The torus gives independent k b a

S

T k phase channels, each individually blind to ordering. These lower-dimensional spaces are useful for specic applications (ledger balancing on, phase tracking on ), and the k T

S Closure SDK supports them in its engine layer, but they are subordinate views: always embed on, always compose on, and project down through the Hopf bration when S

S you need separated channels.

### 4 The Zeroth Law and Its Consequences

The algebra derived from two axioms on the unique geometry of produces three theoS rems that characterize every possible coherence failure completely. The rst Theorem 0, the Zeroth Law is the central result of this paper.

### 4.1 Theorem 0: Axis completeness

(The Zeroth Law Axis Completeness)

Coherence between two ordered Theorem 1. sequences can break in exactly two ways, which are orthogonal and exhaustive.

A quaternion has two parts that behave dierently under conq = w + xi + yj + zk jugation: the scalar part is symmetric (preserved under 7→ − − − q q ¯ = w xi yj zk w conjugation), and the vector part is antisymmetric (sign-ipped under conjuga( x, y, z ) tion). Any divergence between two compositions lands on one axis or the other:

The (scalar,, symmetric): something is present in one sequence existence axis

W and absent from the other. The question is binary has or has not.

The (vector,, antisymmetric): something is present in both seposition axis

RGB quences at dierent positions. The question is directional where and how far.

These two types are algebraic inverses of each other: the inversion operation 7→ q q ¯ ips the vector part while preserving the scalar part, which is why applying inversion to a missing-type divergence produces a position-type divergence and vice versa. There is no third type because the quaternion has no third part under conjugation the scalar-vector decomposition is the complete eigendecomposition of the conjugation operator on. H

The Zeroth Law precedes the other two theorems because it denes what they are measuring. Theorems 1 and 2 characterize how precisely and uniformly the algebra detects divergence. Theorem 0 says what divergence: a displacement along one of two is orthogonal axes, classied by the conjugation symmetry of the quaternion itself. The two incident types are the geometry's own categories, forced by the algebra, exhaustive by construction.

### 4.2 Theorem 1: Exact propagation

(Exact Propagation)

Let with running product Theorem 2. ∈ g,..., g

S

C = g n. If any single element is perturbed to with geodesic distance, ′ ′ · · · g g g g d ( g, g ) = ε n k k k k the running product shifts by exactly: ε (2) ′ d ( C, C ) = ε regardless of the sequence length or the position. n k Write and where and. Proof. ′ ′ · · · · · · C =

L g

R

C =

L g

R

L = g g

R = g g − k k k +1 n k By right-invariance of the bi-invariant metric on:. ′ ′ S d ( L g

R, L g

R ) = d ( L g, L g ) k k k k By left-invariance:. ′ ′ d ( L g, L g ) = d ( g, g ) = ε k k k k In most computational systems, errors compound. A small mistake early in a long pipeline can grow, shrink, or vanish unpredictably by the time it reaches the output, depending on the operations it passes through. On with the bi-invariant metric, this S cannot happen: an error of magnitude at position 1 in a chain of a billion compositions ε arrives at the running product as an error of magnitude exactly, because every group ε multiplication is an isometry that preserves distances perfectly. The geometry is faithful in the strongest possible sense.

### 4.3 Theorem 2: Uniform sensitivity

(Uniform Sensitivity)

For with the bi-invariant metric, the sensitivity Theorem 3.

S of the running product to perturbation at any position satises: C k ∂C (3) = 1 ∂g k for all. k = 1,..., n Write. The dierential, where and Proof. ◦ ◦ C =

L g

R dC/dg = dL id dR dL dR k k

L

R

L

R are the dierentials of left and right multiplication. By bi-invariance, both are isometries. Therefore. ∥ ∥ ∥ ∥ dC/dg = id = 1 k Every position in the sequence is equally detectable. The rst element and the billionth contribute with identical sensitivity to the running product, and a perturbation anywhere is visible from the endpoint with the same delity.

### 4.4 The complete diagnostic

Together, the three theorems form a complete diagnostic for any coherence failure in ordered data. Theorem 0 tells you broke existence or position, classied by the what algebra itself. Theorem 1 tells you the exact magnitude, preserved without how much distortion through the entire composition chain. Theorem 2 tells you it is detectable it occurred uniformly across all positions. wherever

### 5 The Prism

The three theorems characterize the algebra's diagnostic power. The Hopf bration provides the lens through which that diagnostic becomes readable.

In 1931, Heinz Hopf discovered that can be decomposed into a family of circles S ( ) threaded through a sphere ( ) the Hopf bration [ ]. Every point → × S

S

S

S

S on decomposes uniquely into a direction on (where it points) and a phase on S

S

S (where it sits on its circle). This is a topological fact about the 3-sphere, independent of any application.

For the closure construction, the Hopf bration acts as a prism. A composition on

S is a single quaternion four numbers, encoding everything at once. The bration splits this into separated channels: (the scalar part, the ber) measures existence is the light on or o? This is W

S the channel, tracking whether something is present or absent, aligned with luminance Axiom 2 (coherence, directionality, the -axis of Euler's identity). e (the vector part, the base) measure displacement where is the light R, G, B

S pointing, and how far has it moved? These are the channels, tracking chrominance the direction and magnitude of any positional shift, aligned with Axiom 1 (interaction, relationship, the -axes of Euler's identity). π The analogy to light is structural, and this matters. White light enters a glass prism and separates into a spectrum because dierent wavelengths refract at dierent angles, and a quaternion enters the Hopf prism and separates into channels because the scalar and vector parts transform dierently under conjugation in both cases, a single signal carries information that was always there and becomes readable only after decomposition. The prism reveals what the signal already contains.

The choice of color as the communication layer is deliberate and grounded in Theorem 0. Color is the minimum perceptual representation that carries both axes of the Zeroth Law in a single object: a color exists (it is either present or absent, luminance) and a color is invertible (every hue has a complement, chrominance). The electromagnetic spectrum exists continuously in nature, with no inherent divisions between wavelengths, and organisms actively transform it into meaningful distinctions through the interaction of sensory organs and neural systems separate neural pathways for luminance and chrominance, millions of years of evolved channel separation parsing the same decomposition the Hopf bration provides algebraically. A divergence that dims the signal is an existence break, a divergence that shifts the hue is a position break, and the biology already reads both.

The channels are available at every step of the composition, in real time, as data ows through the system. They are the endpoint of the theoretical arc: the axioms produced the algebra, the algebra produced, produced the theorems, and the Hopf bration S

S translates the theorems into a readable signal that decomposes every possible divergence into two channels that a human eye (or an automated system) can parse immediately.

### 6 How Consensus Works

The previous sections built a vocabulary: two axioms produced an algebra, the algebra produced a unique geometry, the geometry produced three theorems, and the Hopf - bration translated those theorems into readable channels. This section writes the rst sentence in that vocabulary the mechanism by which information gains meaning. The

question from Section 1 was: how does consensus work? The answer is: through composition on, veried by closure to identity. S

### 6.1 The data structure

Every record in an ordered sequence a transaction, a measurement, a message, a gene can be embedded as a unit quaternion on. The running product at time is: S t (4) C = g g... g t t updated by a single quaternion multiplication per record:. C =

C g − t t t This running product is four numbers regardless of how many records ( w, x, y, z ) have been composed the millionth record and the tenth produce a state of the same size. And because every quaternion has an exact inverse, every individual record is recoverable from consecutive running products:. The path of running − g =

C

C t t t − products is a lossless encoding of the full history: any element recoverable ( C, C,..., C ) n in one multiplication, any subsequence's coherence checkable from two endpoints in one multiplication, and the global coherence of the entire sequence readable from one number, the geodesic distance from the running product to the identity σ = arccos( w ) C n quaternion. (1,,, 0) The running product encodes what the data the transformation it applied to did the system state. A 10-megabyte database transaction and a 16-byte quaternion describe dierent things: the transaction is the content, the quaternion is the state change. The raw data can be archived, sharded, compressed, or even discarded. The geometric path stays small and navigable forever, carrying coherence information at every point along the way.

### 6.2 The operations

The Closure SDK implements six operations on, each derived from the algebra. S Raw bytes enter the system. They are hashed with SHA-256 (a one-way Embed. function the hash uniquely identies the content while the content itself stays behind), and the hash is mapped to a unit quaternion on. The mapping is deterministic: same S bytes, same point, every time. After embedding, the system works only with geometry.

Two points on the sphere multiply through the Hamilton product Compose.

### 16 multiplications and 12 additions, yielding a new point on the sphere. This is the

running product, and it is the core operation: non-commutative (order matters), associative (grouping does not), and producing a result of the same type as its inputs (a unit quaternion). One multiplication per record,. O (1) Every point has an exact opposite the quaternion conjugate Invert. − − − q ¯ = ( w, x, y, z ) such that composing an element with its inverse returns to identity:. q q ¯ = (1,,, 0) This is the undo operation, and it generates the duality between the two incident types of Theorem 0: inverting ips the vector part (position axis) while preserving the scalar part (existence axis).

The geodesic distance from the running product to identity:. Sigma. σ = arccos( w ) When, the composition has returned to identity everything balances, the seσ = 0 quence is coherent. When, something diverged by exactly that much. This is the σ > single number that veries the entire history, the answer to, computed in? A =

A

O (1) from the four components of the running product.

The algebraic gap between two compositions: yields the quaternion that, Di. − a b when composed with, gives. The gap itself is a point on, decomposable through a b

S the Hopf bration into channels, carrying the full geometric information about what kind of divergence occurred and in which direction.

Computes the di, measures sigma, returns the verdict: how far apart Compare. are these two compositions, and does the distance exceed a coherence threshold? This is the consensus check two systems that independently composed the same data will land at the same point on, and comparing their elements (without ever sharing the S data itself) determines whether they agree.

### 6.3 The naming of zero

There is one more element in the construction that deserves its own discussion, because it plays the same role here that the invention of zero played in the history of arithmetic.

The identity quaternion is the representation of emptiness. It is the state (1,,, 0) before any data has been composed the blank page, the empty ledger, the fresh start. Composing identity with anything changes nothing:. It is the element q = q = q ⊮ ⊮ that says nothing has happened yet.

In the computational implementation, this is literal: every composition starts at identity, every Seer (the streaming monitor) initializes there, and every coherence check measures distance from there. The closure primitive needs zero to function and zero on

S is the identity element, the unique point equidistant from all states, the geometric representation of no accumulated history. From this zero, the running product accumulates, and the running product IS the information the bit here is the cycle of composition itself, a sustained act of self-verication that stores nothing as a static state and does everything as an ongoing operation.

This is also what gives the system its minimum semantic embedding. The embedding maps content to points from identity, and emptiness identity. The distance away is from identity to any content is, which is prediction error, which is surprise, which σ is information. Shannon's entropy measures how much surprise a channel carries. The geometric measures where the surprise is, on which axis, with what direction, and σ whether the system is still coherent after absorbing it.

In the Brahman experiment (Section 9), the system learns that opening and closing brackets are algebraic inverses from data alone and it can do this precisely because identity exists as the target that a balanced sequence must return to. The geometric zero provides the notion of balanced, the target for the closure loss, and the path by which gradient descent discovers the algebraic structure. The naming of zero is what makes the learning possible.

### 6.4 Resolving ambiguity in space: Gilgamesh

When two complete sequences have already been written and the question is where do, the answer is Gilgamesh. Both sequences are composed on, producing two they dier

S paths of running products. Binary search on the paths locates the rst divergence in. Then two pointers walk the sequences in lockstep, and at each step the Hopf O (log n ) ber classies the record. Three outcomes, exhaustive by Theorem 0: the records cohere (same payload, advance both pointers), a record is missing (present on one side, absent on the other, axis broke, existence), or a record is reordered (present on both sides at W

dierent positions, axis broke, position). The same binary question at every step, RGB the same two answers, the same classication, total. O ( n )

### 6.5 Resolving ambiguity in time: Enkidu

When records arrive one at a time on two streams and the question is is this record, the future is unwritten and no amount of computation can resolve missing or just late it. Enkidu turns this uncertainty into a bounded binary decision. An unmatched record starts as. A grace period holds the slot open one cycle, explicit, potentially missing the empty position where the match should be. When the grace period expires without a match, the record is promoted to missing ( axis). When a late match does arrive, the W classication revises to reorder ( axis). The reclassication is forced by the geometry RGB the Hopf ber ips from one axis to the other and the tool chains with its own output: after any misalignment, the next step is the same case, the same question, the same instrument.

### 6.6 Consensus as closure

The answer to Section 1's question is now concrete. Meaning enters when composition closes. Two systems compose the same ordered data, arrive at the same point on, and S verify agreement by comparing elements without ever sharing the data itself. The bind operation checks both products ( and ) and returns one of three verdicts: equal − A

B

A

B (consensus same data, same order), (complementary one is the algebraic inverse undo of the other), or (disagreement with the Hopf channels diagnosing disordered which axis broke and by how much).

This is the same operation at every scale. A hydrogen atom closes its binding cycle through the electromagnetic eld in femtoseconds the electron's orbital IS the running product of the verication, and the atom persists because the cycle returns to identity. A bacterium closes its chemotactic cycle in a tenth of a second the phosphorylation cascade is the running product, and the agellar motor responds because the composition shifted away from identity. A conscious mind closes its narrative cycle across hundreds of milliseconds the integrated percept is the running product, and attention shifts because crossed a threshold. A distributed ledger closes its consensus cycle across seconds or σ minutes the running product on is the state of all accounts, and the coherence k T check is one comparison against identity. Same closure, same two axes (existence and position), same check, four timescales spanning fteen orders of magnitude. O (1) Consensus is checkable in constant time, classiable into exactly two types, localizable in logarithmic steps, and veriable without revealing the underlying data. The hierarchy extends this across scales: chunks compose to blocks, blocks to epochs, each level a running product of the same type, each carrying the same coherence check. O (1) For adversarial settings, the geometric layer pairs with a cryptographic layer: the SHA-256 hash at the embedding step means every group element is derived from a cryptographically irreversible digest, and when those digests come from signed blockchain entries, an adversary cannot craft a compensating element without forging a valid block. The chain constrains the geometry, the geometry veries the chain, and security and eciency each come from the layer designed for it.

### 7 Learning

The construction so far describes a system that composes, veries, and decomposes ordered data. This section shows that the same construction, applied to a system that receives sequential inputs, is a theory of learning.

The running product is the system's accumulated state the geometric sumC t mary of everything it has received. The geodesic distance is the system's σ = d ( C, ) ⊮ t t prediction error: how far from equilibrium, how much unresolved, how surprised.

The identity element is the generative model. In the standard Free Energy Principle ⊮ [ ], the model is a learned probability distribution complex, expensive to maintain, and specic to a particular environment. Here, the model is universal, unlearned, and the same for every system on: the point that represents everything is coherent. Perception is S one group multiplication per input. Action is whatever drives back toward zero. The σ entire apparatus of variational inference the recognition density, the generative model, the precision-weighted update is replaced by a single algebraic operation computed in. O (1)

The dynamics of closure coupling dier from Kuramoto synchronization [ ] in a precise and testable way. Kuramoto coupling drives oscillators toward uniform phase everyone playing the same note, converging to a single point. Closure coupling drives oscillators toward congurations that compose to identity, which includes uniform phase as a special case (everyone at zero) and also includes every other conguration where the phases balance a chord, a counterpoint, a fugue. The Kuramoto attractor is 1-dimensional (everyone in phase). The closure attractor is -dimensional (every − ( n 1) balanced conguration). Coherence is richer than synchronization.

Four testable predictions distinguish geometric prediction error from the standard Free Energy Principle, all accessible with existing experimental methods: the absence of a model-update transient in biological response to sudden perturbation (because there is no model to update), uniform perturbation sensitivity across modalities and sequence positions (Theorem 2 in neural tissue), structured non-uniform phase relationships composing to identity in EEG/MEG binding data, and measurable degradation of the closure signal's dynamic range during departures from criticality (anesthesia, coma, psychosis). The full development appears in a companion paper [ ]; what matters here is that Enkidu conrms the rst prediction operationally each record is a perception (one multiplication), the grace period is the prediction horizon, reclassication from missing to reorder is learning forced by the geometry when new evidence arrives, and Enkidu's model IS the identity element, so reclassication is instantaneous. The geometry does the learning.

### 8 The Self

If the running product is a system's accumulated state and is its prediction error, then σ for a system complex enough to model itself, the running product is the formal substrate of the self.

The self, in this framework, is a single point on a unied state carrying the full S history of composed experiences, decomposable through the Hopf bration into channels at any moment, measurable in its distance from identity at any step. The clinical and phenomenological implications follow from the algebra.

is approaching. The identity element is the unique point Ego dissolution

C ⊮ t on that is equidistant from all other points the state of maximal openness, every S direction equally accessible. The phenomenology reported under psychedelic compounds (boundary dissolution, equal connection to everything, emptying of self) maps directly onto the geometry of approaching this point: the self moves toward pure equidistance, which is experienced as boundarylessness. is chain reconstruction. The running product is the composition Life review g, and as approaches identity, the individual elements can be recovered by · · · g g

C t t successive inversions:, working backward through the chain. This sequential − g =

C

C t t t − re-experiencing of composed history, in order, corresponds to the life review phenomenon reported in near-death experiences and deep psychedelic states. emerge at criticality. When the system is at the boundary of Fractal hallucinations ego dissolution, correlation length spans the entire composition and uctuations occur at all scales simultaneously. The visual hallucination patterns reported under psychedelics spirals, lattices, tunnels, nested self-similar structures are the eigenmodes of the Laplacian on, the base manifold of the Hopf bration. These patterns (spherical S harmonics) were documented by Klüver [ ] and formalized by Bresslo et al. [ ] as arising from the symmetry structure of primary visual cortex. The closure framework derives them as the natural visual projection of dynamics approaching identity through S the Hopf bration's base. S is the distinction between successful and unIntegration versus fragmentation successful recomposition. Controlled dissolution followed by successful recomposition produces a new that encodes the same history in a dierent geometric conguration C t lower, fewer internal contradictions, a more coherent self. This is therapeutic inteσ gration, the clinical goal of psychedelic-assisted therapy. Uncontrolled dissolution without successful recomposition produces a forked chain multiple incompatible running products, each claiming to be the self. This is the geometric description of dissociative and psychotic fragmentation, and the clinical distinction between the two outcomes is precisely whether the reconstruction completes.

Vision, audition, and proprioception are running The binding problem dissolves. products on independent channels. Conscious binding is the moment when these products compose into a single global running product the level at which local closures become a global closure. Tononi's integrated information [ ] can be read as the dierence between Φ the global closure and the sum of the parts' closures:. Dehaene's P ∼ − Φ σ σ whole parts global workspace [ ] is the level at which this composition happens. Both become natural quantities in the closure framework, unied under a single algebraic structure.

### 9 Proof

Three bodies of evidence conrm the construction: a minimal learning experiment, a full computational toolkit, and the Zeroth Law operating across all tests.

### 9.1 Brahman

The bracket experiment is the minimal test of the theory. Brackets are the simplest instance of the Zeroth Law in data: an opening bracket creates an existence that a closing bracket must resolve, and the composition of a balanced sequence must return to

identity. The question is whether a system operating on can discover this structure S from data alone.

Brahman is an recurrent neural network with 1,031 parameters an embedding S layer that maps each of three tokens (open bracket, close bracket, end-of-sequence) to a unit quaternion, a running product that composes one token at a time through the Hamilton product, and an output head that predicts the next token. The hidden state is the running product: four numbers, updated by one quaternion multiplication per token.

The training loss combines next-token prediction with a closure term: the geodesic distance of the nal running product from identity. The closure loss says: produce σ sequences that close. The prediction loss says: predict the next token correctly. The system must satisfy both.

After 30 epochs of training on 50,000 random valid bracket sequences (9 minutes on a laptop CPU), the embedding layer had mapped open and close brackets to conjugate quaternions on algebraic inverses of each other, such that composing an open S bracket with a close bracket steps back toward identity. This was discovered by gradient descent from random initialization, with no architectural hint, no hardcoded structure, and no guidance beyond the constraint and the closure loss. The geometry forced S the learning: on, the only embedding conguration that minimizes for balanced S σ sequences is the one where paired tokens are inverses.

The numbers conrm the separation. The mean for valid sequences is 0.030 (near σ nal identity), while for corrupted sequences (two brackets swapped at random) it is 0.730 (far from identity), giving a separation of 0.699 and a -statistic of 72.02. In autoregressive t generation, 988 out of 1,000 generated sequences are valid (98.8%), with an average of σ

### 0.009 for the valid ones.

A learned embedding on captures structural coherence from data alone, the closure S signal is a reliable diagnostic, and the Hopf decomposition (applied to the generated sequences' running products) correctly classies failures into existence and position types. The result also carries a deeper implication: gradient descent on discovers algebraic S structure that gradient descent in at space does not discover at comparable scale, providing the rst computational evidence for the Platonic Representation Hypothesis [ ] that neural representations converge toward a shared geometric structure, and that structure may be. Prior work on quaternion neural networks [ ] and geometric deep S learning [ ] explored non-Euclidean representations, and the closure construction explains why those approaches gain expressiveness: they are working closer to the geometry the algebra demands.

### 9.2 The Closure SDK

The Closure SDK implements the full construction as a computational tool: 22 exported operations, 207 passing tests, released alongside this paper under AGPL-3.0. The SDK provides three observation instruments (Seer for streaming monitoring, Oracle for O (1) full-history recording with localization, Witness for reference-template vericaO (log n ) tion), two reconciliation engines (Gilgamesh for static two-sequence comparison, Enkidu for real-time stream classication with oracle-problem resolution), and the full Hopf channel decomposition (expose, expose_incident, bind) at every step of the composition.

Benchmarked on identical datasets against SHA-256 checksums, Merkle tree verication, and hash-chain comparison, the Closure SDK is the only method providing

O (1) verication, order sensitivity, localization, and geometric error characterization O (log n )

simultaneously (full benchmark data in Appendix D). The outperformance is structural: the group carries richer information than any at summary function because it remembers order, preserves magnitude exactly (Theorem 1), detects uniformly across positions (Theorem 2), and decomposes every failure into the two channels of the Zeroth Law.

### 9.3 The Zeroth Law in operation

Across all benchmarks, all tests, and all classications the SDK has performed, every divergence has landed on one of the two axes (existence or position) and no incident has required a third category. The exhaustiveness is exact forced by the conjugation symmetry of the quaternion algebra, and conrmed empirically across 207 tests. The two axes are the geometry's own categories, and they are complete.

### 10 Implications

Everything in this paper is deterministic. The two axioms force the quaternion algebra. The algebra and Hurwitz's theorem force as the unique composition space. The biS invariant metric on forces the three theorems. The Hopf bration on forces the S

S channel decomposition. The channel decomposition matches experiment. There are no free parameters, no tuning, no choices between alternatives at any point in the chain from axiom to result.

The primitive is universal in the sense that it applies to any ordered data that can be serialized to bytes nancial ledgers, genomic sequences, network packets, sensor telemetry, database transactions, event streams. The SDK demonstrates this for sequential records. Brahman demonstrates it for learned compositional structure. The geometric prediction error connection (Section 7) demonstrates it for cognition. The author's prior work [, ] demonstrates it for physical matter itself, where the proton's mass formula ( ) emerges from the topology of the minimal stable conguration on. π

S Shannon's bit measures capacity how much information a channel can carry. The quaternion on measures structure what the information, on which axis it changed, is S whether it is still coherent. Shannon founded the theory of information capacity. This paper presents what I believe to be the rst step toward a theory of information structure: the minimal unit that composes, self-veries, and decomposes into diagnostic channels, derived from two axioms and conrmed by experiment.

This paper is a working draft, released alongside a working tool. The repository is public. The reader is encouraged to test the Closure SDK against their own data, in their own domain, and to see whether the geometry holds.

Verication is one number, computed in constant time, decomposable into two channels, localizable in logarithmic steps. Meaning enters when composition closes, when two independent systems arrive at the same point on the sphere and verify agreement without ever sharing the data itself. Consensus is geometry, and the geometry is free.

The question, now, is what we build together.

A Lie Algebra Construction This appendix contains the formal mathematics summarized in prose in Section 2.

A.1 From Axiom 1 to the Lie bracket Axiom 1 (existence requires interaction) asserts that generators are dened through their mutual relationships. The algebraic encoding is the Lie bracket:

(5) − [ X, Y ] =

XY

Y X which measures the failure of commutativity between two generators and. When X

Y, the generators are independent. When, each generator's eect ̸ [ X, Y ] = 0 [ X, Y ] = 0 depends on the other, and the bracket itself is a new generator produced by their interaction.

For the simplest case with three generators, the brackets are determined by e, e, e the structure constants (the Levi-Civita symbol): ε ijk (6) [ e, e ] = 2 ε e i j ijk k This is the Lie algebra: three generators, each produced by the interaction of the su (2) other two, fully symmetric under cyclic permutation.

A.2 From Axiom 2 to the exponential map Axiom 2 (coherence requires directionality) asserts the existence of a one-way map from generators to transformations. The algebraic encoding is the exponential map:

∼ (7) → exp: su (2)

SU(2)

S = Given a generator where is a unit vector in and is a rotation angle: X = θ (ˆ n ⃗ e ) ˆ n θ R

θ θ (8) exp θ n ˆ ⃗ e = cos + sin (ˆ n ⃗ e ) ⊮ which is a unit quaternion with and. q = ( w, x, y, z ) w = cos( θ/ 2) ( x, y, z ) = sin( θ/ 2) ˆ n The map is surjective (every unit quaternion is reached) and ows in one direction: from the algebra to the group. ∼ su (2)

SU(2)

S = A.3 The Jacobi identity The consistency condition that prevents self-referential contradiction:

(9) [ X, [ Y, Z ]] + [

Y, [ Z, X ]] + [

Z, [ X, Y ]] = 0 In components, substituting the structure constants: su (2) (10) ε ε + ε ε + ε ε = 0 ijm mkl jkm mil kim mjl which is the contraction identity for the Levi-Civita symbol, satised automatically. The Jacobi identity guarantees that nested interactions remain bounded the algebra is self-consistent at all depths of recursion.

A.4 The quaternion algebra The generators correspond to the imaginary quaternion units via e, e, e i, j, k e = m where are the Pauli matrices. The multiplication table: − iσ / σ m m (11) i j = k, j k = i, k i = j (12) − − − j i = k, k j = i, i k = j (13) − i = j = k = ijk = The last line encodes both axioms simultaneously: says each inter− i = j = k = action squared lands on the scalar axis (Axiom 2, directionality), and says − ijk = the triple product of all interactions produces the same landing (Axiom 1, three-body closure).

The quaternion algebra is isomorphic to the Cliord algebra the algebra Cl(0, 2) H generated by two anti-commuting square roots of over the reals. This conrms that − two generators (and their product) produce the full quaternion structure, consistent with two axioms producing the complete algebra.

B Hurwitz's Theorem B.1 Statement (Hurwitz, 1898)

The normed division algebras over are exactly (diTheorem 4.

R

R mension 1), (dimension 2), (dimension 4), and (dimension 8). C

H

O A normed division algebra is an algebra over equipped with a norm satisfying ∥·∥ A

R for all, and where every nonzero element has a multiplicative ∥ ∥ ∥ ∥ · ∥ ∥ ∈ ab = a b a, b

A inverse. The norm condition guarantees that composition preserves magnitude a property essential for Theorem 1 (exact propagation).

B.2 The Cayley-Dickson construction Each algebra is obtained from the previous by doubling. Given an algebra with conjugaA tion, the doubled algebra consists of pairs with and multiplication: ∗ 7→ ∈ a a ( a, b ) a, b

A (14) ∗ ∗ − ( a, b )( c, d ) = ( ac d b, da + bc ) Applying this construction:: trades total ordering. The reals are totally ordered ( or for → a < b b < a R

C all ). The complex numbers admit no total ordering compatible with the eld ̸ a = b operations.: trades commutativity. Complex multiplication satises. Quaternion → ab = ba C

H multiplication satises and, so. − ̸ ij = k ji = k ij = ji: trades associativity. Quaternion multiplication satises. Oc→ ( ab ) c = a ( bc ) H

O tonion multiplication satises only the weaker alternativity condition, and a ( ab ) = a b generic triples fail full associativity.

B.3 Why the construction terminates Applying Cayley-Dickson once more to produces the sedenions (, dimension 16), which O

S contain zero divisors ( with ). The norm-product identity ̸ ∥ ∥ ∥ ∥∥ ∥ ab = 0 a, b = 0 ab = a b fails, and with it, exact propagation (Theorem 1). All higher doublings inherit zero divisors and are unsuitable as composition spaces.

B.4 Relevance to sequential composition A running product requires three properties simultaneously: C =

C g − t t t, so that Associativity ( C g ) g = t − t − t well-dened regardless of parenthesization. This excludes, so that Norm preservation ∥ ∥ C = t unit elements, keeping the composition on the sphere. This excludes doublings., so that Non-commutativity

C g − t t depends on order. This excludes and R

C both remain useful as projections through the Hopf bration).

The unique algebra satisfying all three is

C Extended Theorem Discussion C.1 Theorem 0: Why exactly two types The conjugation operator on acts as q H involution ( ) and therefore has exactly two eigenspaces: ¯ q ¯ = q The eigenspace (xed under conjugation): +1 real axis. This is the existence axis ( ). W The eigenspace (sign-ipped under conjugation): − ∈ } zk: x, y, z

R composition ⊕ =

Im( ) H

R

H

decomposition.

C.2 Theorem 1: The role of bi-invariance The proof of exact propagation relies on the bi-invariant metric on group is bi-invariant if G d ( gx, gy ) = d ( x, y metric is the geodesic distance:

d ( q, q ) = arccos which corresponds to the angle of the rotation tances exactly. The perturbation at position and right context

R through undistorted. and the running product is C ( g g ) t − t − t. O and unit elements compose to ∥ ∥ · ∥ ∥ C g − t t and all higher S generically and the composition ̸ = g

C − t t from full order-sensitive composition (though, and its unit elements form. S H. This is a linear 7→ − − − q ¯ = w xi yj zk, the { ∈ } { ∈ } q: ¯ q = q = w: w H ⊮

R

{ ∈ − } { q: ¯ q = q = xi + yj + H, the pure imaginary quaternions. This is the position axis ( ). RGB Since conjugation is a linear involution on a 4-dimensional space, the eigenspace deis complete every quaternion has a unique decomposition into scalar and vector parts, and every divergence projects onto one axis or the other. The exhaustiveness of the two incident types is the algebraic completeness of this eigen-. A metric on a S d for all. On, this ∈ ) = d ( xg, yg ) g, x, y

G

S

(15) q q ¯. q q ¯ Bi-invariance means left and right multiplication are isometries they preserve disis sandwiched between left context k

L, and both act as isometries, so the perturbation's magnitude passes

Bi-invariance holds on because is compact and simple, guaranteeing the S

SU(2) existence of a unique (up to scaling) bi-invariant metric. On non-compact groups (such as ) or groups with non-simple structure, bi-invariant metrics may fail to exist, SL(2, ) R and Theorem 1 would require modication.

C.3 The choice of closure scalar The geodesic distance is the geometrically natural closure scalar, inherσ = arccos( w ) C iting uniform sensitivity from Theorem 2.

An alternative scalar (used in some early implementations) is a monotone − ˜ σ = 1 w

C function of but introduces non-uniform nite-perturbation sensitivity. The relationship σ is, which has derivative vanishing at (near identity) and − σ ˜ = 1 cos σ sin σ σ = 0 (antipodal). Perturbations near identity or near the antipodal point produce σ = π smaller changes in than perturbations at intermediate distances, creating a ∼ × σ ˜ sensitivity imbalance across positions in nite-dierence tests.

The geodesic distance avoids this: its derivative with respect to the σ = arccos( w ) C composition is uniformly 1 (Theorem 2), and this uniformity holds at nite perturbation scale as well as innitesimally.

D Benchmarks D.1 Comparison of verication methods

Method

Comp.

Verif.

Order

Localize

Characterize SHA-256 checksum

No

No

No O ( n )

O (1) Merkle tree

No

No O ( n )

O (log n )

O (log n ) Hash chain

Yes

Link-level

No O ( n )

O ( n ) Error-correcting code

No

Yes

Limited O ( n )

O ( n ) Closure on

S

O ( n )

O (1)

Yes

O (log n )

Geometric Table 1: Comparison of sequential verication methods. Comp. = composition cost, Verif. = verication cost, Order = sensitive to element ordering, Localize = cost to nd rst divergence, Characterize = qualitative information about divergence type.

Closure on is the only method in this table providing all ve properties: veriS

O (1) cation, order sensitivity, localization, and geometric characterization (the Hopf O (log n ) decomposition classies every divergence into existence or position type with directional information). The group structure carries this information because it remembers order (non-commutativity), preserves magnitude exactly (Theorem 1, from norm preservation), detects uniformly (Theorem 2, from bi-invariance), and decomposes completely (Theorem 0, from conjugation symmetry).

D.2 Brahman experimental results The training curve shows prediction loss decreasing from 1.06 to 0.53 over 30 epochs, and closure loss decreasing from 0.81 to 0.03. The closure loss drops sharply at epochs 34 (from 0.46 to 0.08), which corresponds to the moment the embedding discovers the inverse

Parameter

Value Model

S

RNN Total parameters 1,031 Vocabulary

### 3 tokens:,, EOS ( ) Training set 50,000 valid bracket sequences Validation set 2,000 sequences Epochs Batch size Learning rate

### 0.001 (cosine decay)

Closure weight ( ) 0.3 λ Hidden dimension Training time

### 542 seconds (laptop CPU)

Table 2: Brahman training conguration.

Metric

Valid

Corrupted (mean) 0.030 0.730 σ nal Separation 0.699 -statistic 72.02 t -value p <. Pair accuracy 88.3% (1766/2000) Table 3: Separation between valid and corrupted sequences. Corrupted sequences were generated by swapping two brackets at random positions.

pairing the gradient on nds the conjugate conguration and locks onto it. After S epoch 5, the closure loss plateaus near 0.03 while prediction loss continues to decrease, indicating that the geometric structure is learned early and the remaining training renes the prediction head.

D.3 SDK test suite summary The Closure SDK passes 207 tests covering all exported operations, edge cases, and integration scenarios.

Algebraic properties: compose associativity (veried to tolerance over ran− dom triples), inverse correctness ( to ), norm preservation through − q q ¯ = ⊮ sequential compositions (drift ). − < Theorem verication: exact propagation (perturbation of at random positions in ε chains of length 10 to 10,000, measured matches to ), uniform sensitivity ′ − d ( C, C ) ε (nite-dierence Jacobian measured at across all positions using ∥ ∥ ± ∂C/∂g.. k geodesic distance ). σ = arccos( w ) Zeroth Law exhaustiveness: across all Gilgamesh and Enkidu test cases (missing records, reordered records, mixed incidents, edge cases with duplicates and empty sequences), every classied incident falls on the existence axis ( -dominant) or position W axis ( -dominant), with zero incidents requiring a third category. RGB

Metric

Value Sequences generated 1,000 Valid

### 988 (98.8%)

Average length

### 7.0 tokens

(valid, mean) 0.009 σ nal (invalid, mean) 0.432 σ nal Table 4: Autoregressive generation results.

Methodology This paper was written under unusual conditions and the reader deserves transparency about the process.

The theoretical content the axioms, the cross-parametrization, the Zeroth Law, the identication of the running product as cognitive substrate, the color-channel design, and the Closure SDK architecture is the author's work, developed across six prior publications [,,,,, ] and the initial closure verication paper [ ], and implemented as working software with 207 passing tests and public benchmarks.

The manuscript itself was drafted in collaboration with Claude Opus 4.6 (Anthropic), operating as a writing and verication tool under the author's direction. The author provided the theoretical content, the structural decisions, the stylistic corrections, and the nal editorial judgment at every stage. Claude provided drafting, proof formalization, literature search, LaTeX preparation, and computational verication of claims. The collaboration was extensive this paper went through multiple complete rewrites in a single working session, with the author directing the frame, the logic, and the voice while Claude executed the prose.

This is an honest accounting: the ideas are human, the verication is joint, and the prose is a collaboration that has not yet received full human polishing. The author intends to revise the manuscript for style and precision before formal journal submission. This version is released as a working draft alongside the Closure SDK repository to establish priority and provide theoretical context for the computational tool.

The author believes this transparency serves the reader better than the alternative of presenting AI-assisted work as if it were produced by traditional means. The content stands on its theorems, its implementation, and its experimental results, regardless of how the sentences were constructed.

Acknowledgments Computational verication, literature search, proof formalization, and manuscript preparation were performed in collaboration with Claude (Anthropic), operating as a verication and drafting tool under the author's direction.

The axioms, the cross-parametrization of and through the quaternion algebra, e π the Zeroth Law (Theorem 0), the identication of the running product as the formal substrate of the self, the color-channel communication design via the Hopf bration, the naming of the identity element as the geometric zero (the minimal semantic embedding), and the Closure SDK architecture are the author's contributions.

The proofs of exact perturbation propagation (Theorem 1) and uniform sensitivity

(Theorem 2) were formalized jointly. The prior art search conrming novelty of the construction was performed by Claude.

References [1] Shannon, C.E. (1948). A Mathematical Theory of Communication.

Bell System Tech, 27(3), 379423. nical Journal [2] Euler, L. (1748).. Introductio in analysin innitorum [3] Hamilton, W.R. (1843). On quaternions, or on a new system of imaginaries in algebra.. Philosophical Magazine [4] Hurwitz, A. (1898). Über die Composition der quadratischen Formen von beliebig vielen Variablen., Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen 309316.

[5] Hopf, H. (1931). Über die Abbildungen der dreidimensionalen Sphäre auf die

Kugeläche., 104, 637665. Mathematische Annalen [6] Friston, K. (2010). The free-energy principle: a unied brain theory?

Nature Reviews, 11(2), 127138. Neuroscience [7] Tononi, G. (2004). An information integration theory of consciousness.

BMC Neu, 5, 42. roscience [8] Dehaene, S. (2011).. Viking Press. Consciousness and the Brain [9] Kuramoto, Y. (1984).. Springer. Chemical Oscillations, Waves, and Turbulence [10] Klüver, H. (1928).. Kegan Mescal: The Divine Plant and Its Psychological Eects Paul.

[11] Bresslo, P.C., Cowan, J.D., Golubitsky, M., Thomas, P.J., & Wiener, M.C. (2001).

Geometric visual hallucinations, Euclidean symmetry and the functional architecture of striate cortex., 356(1407), 299 Philosophical Transactions of the Royal Society B 330.

[12] Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The Platonic Representation

Hypothesis.. ICML [13] Nakahara, M. (2003)., Second Edition. Institute of Geometry, Topology and Physics Physics Publishing.

[14] Bronstein, M. et al. (2021). Geometric Deep Learning: Grids, Groups, Graphs,

Geodesics, and Gauges. arXiv:2104.13478.

[15] Parcollet, T. et al. (2019). Quaternion Recurrent Neural Networks.. ICLR [16] da Silva, W.H.A. (2025). The Holy Trinity of Information. Zenodo.

[17] da Silva, W.H.A. (2025). The Geometrical Theory of Communication. Zenodo.

[18] da Silva, W.H.A. (2025). At the Border of Chaos: The Geometry of Information.

Zenodo.

[19] da Silva, W.H.A. (2025). Information Evolution Dynamics. Zenodo.

[20] da Silva, W.H.A. (2025). Computational Chemistry: Hydrogen as Physical

InS stantiation of the Ruliad. Zenodo.

[21] da Silva, W.H.A. (2026). The Shape of Reality. Zenodo.

[22] da Silva, W.H.A. (2026). Closure: A Geometric Method for Sequential Data Verication. Zenodo. CC BY-NC-SA 4.0.

[23] da Silva, W.H.A. (2026). Geometric Prediction Error: Free Energy on Lie Groups.

Zenodo.

This paper is released under CC BY-NC-SA 4.0 (Creative Commons AttributionLicense. NonCommercial-ShareAlike 4.0 International). The Closure SDK is released under the GNU Aero General Public License v3.0 (AGPL-3.0): anyone may use, modify, and distribute the software freely, and any network service built on it must release its source code under the same terms. Commercial licensing for the SDK is available from the author.

### 2026 Walter Henrique Alves da Silva.

©
