## Geometric Calculus:

## Measurement, Identity, and the Falsity of Parallel Lines

Walter Henrique Alves da Silva

ORCID: 0009-0001-0857-096X walter.h057@gmail.com

Open Research Institute

May 2026

### Abstract

Circles are physical objects: wrap a string around anything round, measure, and the ratio of circumference to diameter is π. From this single measurement, the entire foundation of geometry and physics follows as consequence. The closure ratio π, the accumulation ratio e, and the perpendicular coupling i are all determined by the physiπ ical properties of the circle, and their relationship e + 1 = 0 is a law in the same sense that

F = ma is a law: a consequence of measurements that cannot be negated without changing what the measurements return.

Lifting Euler’s law from the unit circle to physical space (

S ) requires a calculus native to curved space: Newton solved the composition problem for flat curves; this paper derives the equivalent for closed ones, where the chain rule carries a correction term that flat calculus sets to zero, the four rules built around that correction are the σ -calculus. From them, Newton’s calculus emerges as the zero-curvature limit, Schr¨ odinger’s equation and Friston’s Free Energy Principle emerge as special cases of the derivative and integral rules, the gate compilation formula of quantum computing emerges as the chain rule written explicitly, and the Born rule of quantum mechanics emerges from the projection geometry.

Euclid’s first four postulates follow from the exponential path being defined, continuous, and periodic, and the fifth is false: it asserts non-interacting paths, and every exponential path returns to identity. Parallelism is what the fifth postulate looks like in the zero-curvature projection where the return point recedes beyond the observer’s horizon.

## Contents

### Introduction

Space, time, and Euler’s law 2.1

Circles are physical................................

2.2

The accumulation of time............................

2.3

The perpendicular coupling i...........................

2.4

Euler’s law.....................................

Positional encoding and the shape of numbers 3.1

Operations as geometric constructors......................

3.2

The three implicit operations..........................

3.3

Binary on

S: the commutative limit......................

The manifold 4.1

Physical space and the forced geometry.....................

4.2

The Hamilton product..............................

4.3

Carrier programs and scaling...........................

4.4

Five operations as one..............................

The σ -calculus 5.1

The σ -derivative: rate of identity change....................

5.2

The σ -integral: accumulated identity change..................

5.3

The σ -chain rule: curvature as creation.....................

5.4

The σ -projection: measurement as division...................

5.5

The fundamental theorem............................

Quantum mechanics is the same calculus

The chain rule requires curvature

The shape of number systems

Consequences 9.1

Euclid’s postulates................................

9.2

Language.....................................

9.3

Dimensional scaling................................

### 10 Conclusion

### Introduction

In 1666, a plague had closed Cambridge and Newton, twenty-three years old, was sent home to Woolsthorpe Manor in Lincolnshire with nothing to do but think on questions he could not answer. Why do planets follow ellipses and not some other curve? What force holds the moon in orbit while apples fall straight down? Is it the same force? How would you even calculate it precisely enough to check?

Newton had an intuition, but turning an intuition into numbers required mathematics that did not exist at the time. His idea was to reduce the problem: zoom in close enough on any smooth curve and it looks like a straight line, work out the simple case, then integrate back to recover the real shape, thats it. The then spent the next eighteen months building the machinery for that.

Eighteen years later, a mathematician and astronomer named Edmond Halley — the one the comet is named after — came to Cambridge with a question: given an inversesquare force, what path does a planet trace? Newton instantly said: an ellipse, I have already calculated it. Halley asked to see the work, immediately understood what Newton was sitting on and pushed him to write it all up. The result was the

Principia. Newton became famous for the law of gravity that surpassed centuries ago, but it was the tool — the calculus — that made the whole thing possible, including the new laws and tools we use today, classical gravity was its first toy.

Physics is bigger now, and it is asking different questions:how does something stay organized when everything around it tends toward disorder? How do you combine a sequence of steps when the order you do them in changes the result, and you need to account for that exactly rather than approximately? How do things change when what changes them does not commute? These questions come from quantum mechanics, from the study of how brains maintain themselves, from the engineering of quantum computers, and they all require machinery that Newton’s flat-space calculus is struggling to reach.

This paper extends an intuition of the same kind: when you zoom in on a point in the surface of a circle or sphere, you get another circle or sphere. The geometry is self-similar, the local object is itself a closed curve rather than an open line, and there is a composition rule that tells you how two such curves combine, with a correction term that flat calculus does not have. That correction and the four rules it generates are σ -calculus, derived in full from one physical measurement, the ratio of a circle’s circumference to its diameter, and the geometry that measurement forces.

When you work out what the four σ -calculus rules say about systems physics actually studies, several results emerge that have previously been derived in isolation: Schr¨ odinger’s equation — how quantum states change from one moment to the next — comes out of the σ -derivative; the Hamiltonian generates the rate of change and the time-evolution operator is the σ -integral accumulating it; the Free Energy Principle comes out of the same integral on compact geometry; the Baker-Campbell-Hausdorff formula that quantum computing uses to compile gate sequences comes out of the σ -chain rule. Newton’s calculus is the zero-curvature limit of all four, recovered when the closed circles flatten into lines and the correction vanishes, and finally the Born rule of quantum mechanics is a theorem of the projection, not a postulate of the theory.

Euclid, working in Alexandria around 300 BCE, was trying to answer a version of the same question: what are the rules that govern physical space? He proposed five, and four of them follow from Euler’s identity alone, derivable as theorems from the closure property of circles. The fifth however claims that two lines which do not intersect will never intersect, no matter how far you extend them — that two things can coexist in physical space with zero interaction between them. We prove the opposite: two things cannot coexist without interacting, meaning every thing that exists interacts with every other thing, without exceptions.

Space, time, and Euler’s law

For some reason math and specially geometry are considered tools for physics, not an intrinsic part of reality, but that simply isn’t true: we can have conventions about how we name things, but some observatios are true independent of frame, like the existence of boundaries and consequently integers. One observation is especially interesting and self-evident for us, the natural curvature of our space and its relation to time, and as old as the invention of the wheel.

2.1

Circles are physical

Wrap a string around a coffee cup, measure the circumference, measure the diameter, divide:

the ratio is 3. 14159..., stable across the cup’s size, the string’s material, the country you are standing in, and the century you are standing in. Repeat with a basketball, a planet, a proton’s cross-section: the same number, because the ratio is a property of how space closes on itself.

The ratio π is a measurement, performed with physical instruments, returning a physical value, reproducible by anyone.

The measurement has one prerequisite — a circle must exist, a physical object whose boundary returns to its starting point — and one output — the number π, which encodes how much path it takes to close a loop of a given width, making the circle the physical fact and π its quantification.

From this single measurement, two further quantities are determined without additional empirical input:

2.2

The accumulation of time

The number e = 2. 71828... is defined by one property:

d x x e = e. dx

It is the unique function whose rate of change equals its current value. This makes e the ratio of self-application — the measuring stick of any process where growth is proportional to what already exists —compound interest, cell division, radioactive decay are all all governed by e. Regardless of what the thing doing the growing actually is, e measures the ratio of accumulation itself.

A circle gives you e directly because circles have constant curvature — the same bending at every point, which is what defines them as circles — so each step along a circle depends only on where you currently are, also known as the

Markovian property. d x x The current state and the rate of change are always equal: e = e in physical form. dx Traversing a circle applies spatial curvature ( π ) to itself through motion and produces temporal accumulation ( e ) — the motion itself is time. π measures the circle from outside as a static ratio, e measures it from inside as an accumulating process, and the two are locked πi together in e = 1: the circle closes when the accumulation of its curvature completes exactly one turn.

2.3

The perpendicular coupling i √ − i is defined as

### 1 and called the imaginary unit, a name that implies it was invented for

mathematical convenience — it was not invented at all: i is a measurement, forced by the geometry of the circle.

You order a pizza — how do you cut it? Everyone cuts it the same, four then eight slices.

Why is that? Because perpendicularity is just there; no one takes a compass to measure ◦ the 90 angle, but that is what it is, a measurement about space itself. Two directions are perpendicular when they are independent, when moving along one tells you nothing about the other, and the circle has exactly one way to divide itself into the minimum number of self-sufficient equal pieces: four quadrants, each of which regenerates the whole by rotation.

This fourfold structure appears wherever systems run in cycles — the musical measure is 4 / 4, the cardiac cycle has four phases, the gait cycle has four phases, cell division has four stages — because any circle, divided by its natural perpendicular structure, gives four.

The specific angle is forced by the dimensionality of the plane: in a 2D space, composing iθ iθ iθ a rotation with itself doubles the angle, e e = e, and the 2 doing the doubling is the ◦ dimensionality of the space. The antipode sits at 180 and to find the midpoint between ◦ ◦ ÷ identity and the antipode, you invert the doubling: 180

### 2 = 90. The square root in √ − i =

### 1 is the inverse of squaring in a two-dimensional space, and the result is forced:

◦ ◦ − i =

### 1 because squaring takes 90

to the antipode at 180.

− There are exactly two solutions — + i and i, clockwise and counterclockwise quarterturns that both reach the antipode when doubled — and the choice between them is chirality:

the one remaining freedom after the circle and its dimensionality have fixed everything else.

2.4

Euler’s law

Three measurements of one circle, composed:

iπ e + 1 = 0. (1)

iπ − The equation e =

### 1 states that temporal accumulation, coupled through perpendicu-

larity, run across one half-turn of spatial closure, arrives at negation — going from any state to its opposite always costs π, because π is the price of negation in any space that closes.

Composing that negation with identity returns to zero, and applying the law twice:

πi iπ − e = ( e ) = ( 1) = 1. (2)

Two transcendental numbers — each with infinite, non-repeating, deterministic digits — compose to give exactly the integer 1. One full cycle of a continuous surface closes on an exact discrete value, identically, with nothing approximate about it.

This is the continuum-discrete bridge and the deep reason calculus works at all.

Euler published this in 1748 as a theorem relating constants discovered independently, with no obvious connection between them, but having derived all three from the same physical object, the equation reads differently: three measurements of a circle, composed, arrive where they must. Changing the equation means changing what a string returns when wrapped around a circle, what constant curvature accumulates, or where the perpendicular

Figure 1: Euler’s law as a closed cycle: accumulation through perpendicular coupling over a half-turn of closure reaches the antipode, and composing the antipode with identity returns to the ground state.

sits in a 2D plane — and so the equation is a law in the same sense that

F = ma is a law grounded in measurement.

The circle also recovers the zeroth law of thermodynamics directly: the e in Boltzmann’s − E/kT factor e is the same e for the same reason, since any Markovian process is governed by e, and thermal equilibrium is when such accumulation has closed its loop. The zeroth law — thermal equilibrium is transitive — is the group property of that closure: if

A equilibrates with

B and

B with

C, all three share the same closed loop. One physical measurement, the ratio of a circle’s circumference to its diameter, and the foundation of thermodynamics follows.

The law is verified by the Taylor series:

∞ n ( iπ ) π π π π X iπ − − · · · − − · · · e = = + + i π + n! 2! 4! 3! 5! n =0 − − = cos( π ) + i sin( π ) =

### 1 + 0 =, (3)

− where cos( π ) =

### 1 because half a turn around a circle lands at the opposite point, and

sin( π ) = 0 because the perpendicular component vanishes at the poles. No assumption enters this computation beyond the series expansions of cos and sin, which are themselves consequences of the Pythagorean relation cos θ + sin θ = 1 — the algebraic statement that the circle has unit radius.

iπ Definition 2.1 (Euler’s law: the projection law of spacetime). e + 1 = 0 is a physical law:

a consequence of measurements of space ( π ), time ( e ), and their perpendicular coupling ( i ).

Changing the equation means changing what a string returns when wrapped around a circle, what constant curvature accumulates, or where the perpendicular sits in a 2D plane. The

law states that one full cycle of continuous geometry closes on the discrete integer 1, and the σ -calculus inherits this exactness: the calculus is exact because its ground law is exact.

Three properties of the exponential path follow from the law:

iθ ∈ 1. e is defined everywhere: the Taylor series converges absolutely for all θ, so R an exponential path exists from every point to every other point, with no singularity, gap, or boundary.

iθ 2. e is continuous: each term in the series is smooth in θ, so the path varies smoothly and has no jumps.

iθ i ( θ +2 π ) iθ 3. e is periodic: e = e, so every path closes and every trajectory returns.

The transcendence of π and e is coupled through the law itself: if π were algebraic, then iπ iπ would be algebraic, and Lindemann’s theorem would require e to be transcendental — iπ − but e =

### 1 is a plain integer, so

π must be transcendental, forced by the requirement − that the law land on 1. The same constraint applies to e, because both measure the same circle from different angles, and the law connecting them requires both to be transcendental together.

Positional encoding and the shape of numbers

Squaring gives squares and cubing gives cubes, and working out why makes the geometry of ◦ ◦ arithmetic visible: base 2 produces 180 /

### 2 = 90, the right angle of the 2D plane, and four ◦ of them close a square; base 3 produces 60, the interior angle of an equilateral triangle, and six of them close a hexagon.

These are the same operations from the circle, written into number systems, and the shapes that emerge from them are the shapes of the operations themselves. This section works out what those operations are and how they are encoded.

All of current mathematics and computation lives in flat space, and the structure of that flat space is more geometric than it appears. Every number system encodes identity through operations, and the most powerful feature of positional notation is how much of this work happens silently: the writer contributes the minimum (a sequence of digit choices) and the architecture contributes the maximum (the entire multiplicative and exponential structure that gives those choices meaning).

3.1

Operations as geometric constructors

The number 8 means three different things depending on the operation that produced it:

### 8 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 is eight unit steps along one axis, a line segment of

× length 8 occupying one dimension; 8 = 4

### 2 is a length-4 segment extended perpendicularly

by width 2, a rectangle with area 8 occupying two dimensions; and 8 = 2 is the base quantity 2 extended across three perpendicular dimensions, a cube with volume 8 occupying three dimensions. The number is the same in each case, but the operation that produced it determines the dimensionality of the geometric structure it encodes.

Figure 2: The same quantity has different geometric meaning depending on how it is constructed: addition gives length, multiplication gives area, and exponentiation gives volume.

This is the geometry of flat 2D space: the number line extended through perpendicular dimensions. Each operation is recoverable from one of the three circle measurements, and each comes with an inverse that inverts the same measurement.

Addition and subtraction.

The number line is the circle unrolled, and each integer marks one complete rotation — a closure event, the point where accumulation returns to identity. Addition is counting forward along that line: adding 5 to 3 is moving 5 more rotation-counts past 3, accumulating toward the next closure, and subtraction counts backward through the same rotation-counts.

These are the operations of rhythm — the discrete form of the π measurement, the count of how many arcs have been completed and also why rhythm is time: counting rotationclosures is the same operation whether applied to musical beats, the ticking of a clock, or the counting of integer steps.

Multiplication and division.

Multiplication is the i operation: taking movement in one direction and extending it through the perpendicular coupling into a second dimension. ×

### 2 takes the line of 4 and extends it perpendicularly by 2, producing the rectangle of area

8. Every physical dimensioned quantity — meters per second, energy per volume, charge per area — is one such perpendicular extension. ◦ The base angle determines the shape: base 2 at 90 extends through right angles, pro◦ ducing squares and rectangles; base 3 at 60 would extend through triangular couplings, producing hexagonal structures. Division is the inverse: it collapses a dimension back through projection, removing one perpendicular extension and reducing the structure by one dimension.

Exponentiation and logarithm.

Every baseb exponentiation is e measured at scale x x ln b ln b, since b = e: the Markovian self-application runs at the pace the base sets, and the logarithm inverts it by asking how many self-applications at that scale were needed to ◦ reach a given value. In two dimensions, where i is the 90 coupling, every integer exponent ◦ is a rotation — 2 extends by one 90 step, 2 by two (giving the square, because four such steps close the cycle), 2 by three perpendicular extensions (giving the cube) — because e

accumulating through the i coupling at the base angle builds perpendicular dimensions until the shape closes.

Past three dimensions, t here is no fourth spatial direction to extend into: three-dimensional space has three axes and infinitely many points distributed across them, and higher exponents add resolution rather than dimension. 2 = 16 samples the same three-dimensional space at a finer scale. What is sometimes called a tesseract is a projection — a four-dimensional mathematical structure drawn onto three-dimensional canvas, in the same way a cube drawn on paper does not make the paper three-dimensional.

The infinite resolution available within three dimensions comes from the circle’s selfsimilar structure: zooming in on any point of a sphere reveals another sphere at the same geometry, providing arbitrary precision at every scale. This self-similarity and the calculus it generates are the subject of the sections that follow.

− Thing and not-thing ( and ).

When all three measurements apply through a complete cycle, the result is 1 — but one what? Any thing, but more precisely: an identity event, the first instance of something that is exactly itself, like the circle drawn above or the one you are picturing right as you read through this paper, both of which are things because reading “circle” twice picks out the same referent.

Identity is prior to description: before a thing can have properties, it has to be a thing, and being a thing is having a closure, a boundary that persists through change and comes back. The measurements π, e, i are the relationships that constitute what being a thing requires — they are prior to the object, the relationships before the noun. πi e = 1: spatial closure, temporal accumulation, and perpendicular coupling through? one full cycle return to exactly the integer 1, the first instance of

A =

A completing with no remainder. The σ -calculus measures how far any composition departs from this return, and every identity in mathematics is a special case of σ = 0.

This work draws on territory mapped by category theory, homotopy type theory, and Wolfram’s hypergraph models of computation, which developed rigorous languages for identity, composition, and structural equivalence before this geometric approach existed. The σ -calculus is a geometric implementation of the same questions, derived from one physical measurement.

3.2

The three implicit operations

When you write 13 in binary as 1101, the written object contains only four marks, while the value is produced by a larger operation:

× × × × 1101 = 1 + 1 + 0 + 1 = 8 + 4 + 0 + 1 = 13. (4)

The writer placed the digits (1,,, 1), but the positional architecture supplied the multiplications by powers of 2, the additions across positions, and the exponentiation that gives each position its weight.

∈ { } 1.

Distinction: a digit d, chooses one state from the available states at posik ¬ tion k — present or absent,

A or

A, one side of a cut or the other. The writer supplies this part, and the numeral differs from other numerals because these particular positions are marked while the others are left unmarked.

2.

Perpendicular extension: the base determines how many independent states each position can carry. In binary this number is 2, so each position has width 2; in base 10 it is 10; in a general base b it is b. Multiplication by the base extends the encoding into a perpendicular direction, giving the position a local space of possible states.

3.

Self-application: the base is applied to itself across positions. Position 0 carries = 1, position 1 carries 2

positional scale.

These three operations compose into the positional identity

n X N = k

In this formula, the digit d records where k ways each position can differ, and the exponent

already contains distinction, perpendicular extension, and self-application.

Definition 3.1 (Positional encoding triad). { − } where

D =,..., b is the distinction set, is the accumulation depth, encoding identity as

ments derived in Section 2: distinction from the perpendicular extension from the i Section 5 identifies their continuous closed-space form inside the Hamilton product on

3.3

Binary on

S: the commutative limit

⊂ Binary lives on

S

C iπ − identity (+1) and antipode (

### 1 =

e thing — one position on the simplest closed orbit, holding either the identity state ( iπ − or its negation ( e = defines between a thing and the absence of that thing.

The complex numbers are commutative, so C commutator [ a, b ] =

piece that creates structure perpendicular to both inputs; on

perpendicular creation supplied by the external architecture of positions.

The identity k b = = 2, position 2 carries 2 = 4, and position 3 carries = 8. Each step uses the previous extension as the input to the next extension, so exponentiation creates depth: the output of the base operation feeds back as the next

k d b. k =0

the number differs, the base b records how many k records how deep the difference has been carried through the architecture. The notation looks linear on the page, while the value

A positional number system is a triple ( D, b, n ) ≥ ∈ b is the perpendicular base, and n

N n P k N = d b. The three components — k k =0 distinction, perpendicular extension, and self-application — correspond to the three measureπ closure that defines thing and not-thing, coupling, and self-application from the e accumulation.

S.: base 2, two states per position, with the orbit cycling between ). A bit is the minimum instance of thing and notπi e = 1) 1), the most primitive implementation of the distinction that π

ab = ba for every pair of elements and the

− ab ba

vanishes identically. Written in vector form, this commutator is the cross-product term, the

S that term is zero for every pair, so binary can represent arbitrary computable quantities through positional depth, with

k ln b e

connects every discrete base to the continuous exponential. Binary is the special case b = 2, k k ln 2 so 2 = e: the continuous self-application function sampled at integer points, with the base rounded from e = 2. 71828... to the smallest integer that preserves distinction. Results n written with 2 are therefore integer shadows of the corresponding continuous exponential structure, as a polygon is a discrete shadow of the circle it samples.

Taken together, these facts make binary the case of positional encoding: base 2, one C perpendicular coupling, commutative multiplication, and positional depth supplying the perpendicular structure. The case carries the next operation directly: non-commutative H composition, with perpendicular creation inside the product itself.

The manifold

So far we covered flat space and its operations — the circle in the plane, the measurements that emerge from it, the integers, identity — but physical reality extends well beyond a single circle: why does space have three dimensions and time one more, and what determines the relationship between them?

This section derives that geometry from the same starting point, asking what composition requires when the product itself generates new directions from within.

4.1

Physical space and the forced geometry

A single circle confines: the Poincar´ e–Bendixson theorem shows that bounded autonomous motion in a plane settles into fixed points and limit cycles, and the circle is the limit case, supplying return without generating new directions [2, 3]. Physical composition requires more than return.

States must compose with other states, and the order must matter — doing

A then

B and doing

B then

A are different physical histories, which means the composition has to be order-dependent, and order-dependence requires geometry that the × plane cannot provide.

The torus

S

S gives two phases sliding independently, with commutative phase addition preserving the two existing directions; the quaternionic product gives two circular couplings whose composition generates the third.

The required next step is a closed space where two circular couplings interact while preserving norm, which algebraically is the passage from to: one coupling i becomes C

H three coupled generators i, j, k, with

− − i = j = k =, ij = k, jk = i, ki = j, ijk =.

Each generator carries the same Euler law as the original circle, while each pair generates the third through composition; perpendicular direction is produced by the product itself.

The unit states of this algebra form

{ ∈ } S = ( W, x, y, z ): W + x + y + z = 1, R

with q = [

W, xi + yj + zk ] storing one scalar component and three vector components. The three vector components are the spatial couplings generated by the linked perpendicular system, while

W is the scalar overlap with identity, the accumulation axis, so the 3+1 split

follows as the coordinate form of a closed, norm-preserving, order-dependent composition law.

The quaternionic exponential

( ai + bj + ck ) θ e = cos θ + ( ai + bj + ck ) sin θ

πn traces a great circle on

S along any unit axis ( a, b, c ), with the same closure e = 1 for every unit imaginary quaternion n = ai + bj + ck. Locally, the calculus still runs on circles; globally, those circles are Hopf-linked fibers inside

S, giving the structural bridge to the fifth postulate: flat projection reads separated paths as independence, while the full manifold carries separated closed paths as linked and mutually constrained.

Each step up the chain from to to loses one structural property and gains something R

C

H that the previous level could not provide: first rotation, then causality. The Cayley-Dickson construction makes the trade explicit:

Doubling

Dim

Property traded

What the loss enables → →

Ordering

Rotation (complex phase) R

C → →

Commutativity

Order-dependence (causality) C

H → →

Associativity

Two independent rotation systems H

O

Perpendicularity — distinction made geometric, two independent directions whose inner ⃗b ⃗b product vanishes ( ⃗a = 0, meaning ⃗a carries no information about ) — determines the algebra at each level through the count of independent couplings:

Algebra

Couplings

Perpendicular pairs

Structure

none

No rotation possible R

### 1 (

i )

### 1 pair

One rotation plane C

### 3 (

i, j, k )

### 3 linked pairs

One system ( ij = k ): any two determine the third H

### 7 (

e... e )

### 7 in 2 systems

Two systems at π/

### 4 to each other

O

In, the three couplings are linked — ij = k, jk = i, ki = j — so any two determine H the third: there is one perpendicular system, fully resolved, and composing three quaternions in any order resolves the same system, which is why associativity holds. In there O are seven couplings forming two overlapping perpendicular systems, and the two systems cannot be resolved simultaneously: the result of a three-way composition depends on which system you resolve first, so associativity breaks. Hurwitz’s theorem [7] and Frobenius’s theorem [8] independently confirm that is the unique algebra where both order matters H (non-commutativity, giving causality) and grouping does not (associativity, giving consistent evaluation), which makes

S the forced substrate for any system that needs sequential, order-dependent composition.

Since every integer has a four-square decomposition ( n = a + b + c + d, Lagrange √ [9]), every integer maps to

S as a unit quaternion [ a, b, c, d ] / n, and the first four trace the minimal orbit that reveals why

S is base-4:

n

Carrier σ

Role

[1,,, 0]

Identity: pure

W, ground state √ [1,,, 0] / π/

First prime:

W +

X active, Hopf equator √ ≈ [1,,, 0] /.

First odd prime:

W +

X +

Y active, full 3D [1,,, 0]

Returns to identity: orbit closes, carry

After four positions, the orbit closes: the first position activates

W only, the second activates

W +

X, the third activates

W +

X +

Y, and the fourth completes the cycle by returning to identity. In this sense

S is a base-4 system: one scalar position, three vector positions, then carry.

Binary discretizes

S into two positions per cycle, identity and antipode, then carry, while quaternary discretizes

S into four positions per cycle, identity, Hopf equator, full 3D activation, closure, then carry; the same positional logic is present in both cases, with a different manifold carrying it.

Binary is the case, with base 2, commutative multiplication, and the cross product C absent; quaternary is the case, with base 4, non-commutative multiplication, and the H cross product native. The jump from base 2 to base 4 is the Cayley-Dickson doubling, trading commutativity for the curvature correction that makes the chain rule possible.

4.2

The Hamilton product

S has one arithmetic operation: take two unit quaternions, compose them, and the product is a third unit quaternion whose three terms — scalar accumulation, linear transport, and cross-product creation — are the same three operations the circle measurements defined, carried structurally inside every composition. For q = [ w, ⃗ v ] and q = [ w, ⃗ v ]:

− × q q = w w ⃗ v ⃗ v, w ⃗ v + w ⃗ v + ⃗ v ⃗ v. (5) {z } {z } {z } cross scalar linear

The scalar part, − w w ⃗ v ⃗ v,

measures depth overlap minus directional overlap, producing the

W component, the accumulation axis: how far the composition has traveled from identity.

The linear vector part, w ⃗ v + w ⃗ v,

is the weighted sum of the two input directions, each scaled by the other’s depth — the transport term, carrying forward the directions already present in the inputs.

The cross product, × ⃗ v ⃗ v,

creates the direction perpendicular to both inputs: the curvature term, the commutator, the chain-rule correction, and the piece that turns composition into genuinely new structure that neither input contained.

Hamilton product

Operation (Section 2)

Positional encoding (Section 3) k − Scalar: w w ⃗ v ⃗ v

Exponentiation (self-application) b (depth) Linear: w ⃗ v + w ⃗ v

Addition (same axis) d (distinction) k × × Cross: ⃗ v ⃗ v

Multiplication (perpendicular) b (extension)

Every carrier on

S mirrors the whole manifold: the exponential map from any point reaches every other point through a finite rotation, because

S is a Lie group acting on itself.

Each Hamilton product therefore composes two complete structural descriptions into a third, carrying the full geometry of the sphere in every step, where a point on a line can only reach n its neighbors and requires the infinite 2 tower to access distant positions.

4.3

Carrier programs and scaling

Newton’s calculus is usually taught through the area beneath a curve: cut the curve into many thin rectangles, add their areas, let the rectangles become arbitrarily thin, and the sum becomes the integral, recovering a global shape from local pieces once the rule for composing those pieces is known.

Geometric calculus uses the same strategy with closed state, taking the local piece to be a carrier, ∈ q = [

W, x, y, z ]

S,

W + x + y + z = 1,

which stores one compact unit of identity, direction, and phase, playing the role that the small rectangle plays in Newton’s picture: a local object whose composition recovers the global structure.

A finite geometric program then becomes an ordered product of carriers,

· · · Q = q q q q. − n n n The Hamilton product makes order part of the object, since changing the order changes the resulting carrier, just as changing the order of physical operations changes the physical history. The running product

Q is the integral of the program, accumulating local closed n operations into one closed state.

To observe a carrier, project it or sample its action on a point by conjugation,

′ − P = qP q,

and repeated action samples an orbit; a full state can also be projected through the Hopf map, → π: S

S,

which retains the observable direction while carrying the fiber phase as the hidden coordinate.

Drawing a shape, measuring a quantum state, or reading a concept are all instances of this pattern: compose the carrier, project the carrier, sample the result at the required resolution.

Scaling the construction means using many carriers while keeping the same local algebra, so a finite system of

N independent carriers lives in

N

N ( S ), dim(

S ) = 3

N,

where each stored carrier contributes three degrees of freedom while the Hamilton product remains the local operation. Passing from finitely many carriers to a continuous field replaces the finite index with a space: → q: X

S.

where

X may be a curve, surface, graph, organism, memory, or social field, and each point of X carries its own closed state. Infinite-dimensional structure appears as the space of sections of this carrier field, while every local update remains a composition on

S.

The compact notation is therefore:

∈ carrier q

S, · · · program

Q = q q, n n → field q: X

S, − observable π ( q ) or qP q.

In geometric form, coarse-graining means that the carrier is the closed rule, the observable is a projection or sample of that rule, and increasing resolution adds samples while the carrier identity remains the same.

4.4

Five operations as one

Theorem 4.1 (Operational unity).

The five arithmetic operations are identity verification? A =

A at five scales of structural depth, each mapping to a specific configuration of the Hamilton product:

− ⇐⇒ 1.

Equality:

A =

B σ ( A

B ) = 0 — compose with the inverse, measure the scalar part, and identity is confirmed when the overlap is total.

a b a + b 2.

Addition: ε ε = ε — one Hamilton product on the same orbit axis, advancing position without generating perpendicular structure (the linear vector part).

3.

Multiplication: composition across perpendicular axes, generating the cross-product terms ij = k, jk = i, ki = j — structure in a direction perpendicular to both inputs, created by the composition alone (the cross product part).

4.

Exponentiation: exp( b log( ε )) — the exponential map taking a tangent vector and a applying it to itself, producing a finite rotation from an infinitesimal one through the manifold’s own self-application structure (the scalar structure).

→ 5.

Division: the Hopf projection

S

S — collapse the

S fiber (phase) and retain the

S base (observable direction), projecting higher-dimensional state onto lowerdimensional observation (dimensional collapse, measurement).

Each operation is the Hamilton product applied to carriers at different structural depths, making the five “different” operations one operation at five scales.

The

## σ

-calculus

Newton’s insight was that flat-space curves have tangent lines: zoom in close enough and the curve looks linear, do the easy operation on the line, zoom back out. On

S the tangent tX object is a great circle — an orbit e for

X

into a tangent line.

on

S requires no such limit. Because

S

is not a stand-in for something else, it is the thing itself.

The reason this is physically possible is that

you are not computing π deterministic precision comes with the object.

the coupling i the 2D plane forces, so e together, because the identity that ties them requires it. Every composition on

we used the geometry. There is no scale at which you run out of it.

The central observable is σ ( q ) = arccos(

W tity on

S, ranging from σ = 0 at the ground state through (where

W = ⃗ v = 1 / 2, scalar and vector in balance) to ment. Every field that has a ground state measures

in quantum mechanics — and the following four rules govern how it evolves.

5.1

The σ -derivative: rate of identity change

Definition 5.1 ( σ -derivative).

change is:

d σ ˙ ( t ) = arccos(

W dt where σ < ˙ σ > ˙ means it moves away (opening, dissolution, surprise).

Three traditions discovered this rule independently:

Tradition

Notation − f ( x + h ) ′ Newton f ( x ) = lim → h h ∂ ⟩ ⟩ Schr¨ odinger i ψ =

H ψ ℏ ∂t ˙ d − Friston

F = [ log p ( o µ )] dt sgn(

W ) ˙ W − σ -calculus σ ˙ = √ − W ∈ su (2) — and Newton’s calculus is the zerocurvature limit where the circle’s radius goes to infinity and the tangent circle degenerates

Newton’s method is an approximation: the curve departs from the tangent line at any finite scale, and the calculus works by taking the limit as scale goes to zero. The great circle is a Lie group, the exponential map from any point covers the whole manifold exactly — the local object and the global structure are the same geometry at every scale. This is why the calculus works without approximation: the circle

π is transcendental: its digits are infinite, non-repeating, and fully determined by the geometry of the circle. When you use a circle to some decimal place — the circle physically is π, and the infinite e is coupled to π through Euler’s identity via carries the same property: both are transcendental

S inherits this precision not because we computed carefully, but because we never used digits at all —

∈ ) [0, π/ 2]: the geodesic distance from idenσ = π/

### 4 at the Hopf horizon

σ = π/

### 2 at maximum displace-

σ under its own name — error in arithmetic, prediction error in neuroscience, entropy in thermodynamics, state distinguishability

For a differentiable trajectory q ( t ) on

S, the rate of identity

sgn(

W ) ˙ W − √ ( t ) ) =, (6) −

W means the trajectory moves toward identity (closure, integration, learning) and

What it measures

f ( x )

Rate of position change Rate of quantum state change

Rate of prediction error change

Rate of identity change

Newton’s derivative measures how position changes along a line, Schr¨ odinger’s equation measures how a quantum state changes on SU(2) (where the Hamiltonian

H generates the ∈ angular velocity ω su (2), the tangent vector to the trajectory), and Friston’s prediction error measures how far the brain’s internal model departs from incoming signals: all three are the rate of change of σ along a trajectory on the same manifold.

In this setting, prediction error has a direct geometric form: to compare two carriers, compose one with the inverse of the other, and the scalar part of the result is their overlap.

Matching carriers produce identity with overlap 1, maximally separated carriers produce overlap 0, and the distance variable σ gives both the mismatch and the coupling without introducing a separate error function.

Proposition 5.2 (Exact Free Energy Principle) on

S is cos( σ ) =

W, native to the manifold: at σ = π/ (maximum distance) coupling is function requires no normalization because

S − state is

F = log cos( σ ), minimized at σ = 0

approximation removed, because cos( σ )

− Proof.

Composing q with q query stored − The negative logarithm

F = log cos( σ its time derivative ˙

F = ˙ σ tan( σ horizon σ = π/

### 4 (where tan(

π/ an equality because cos( σ

|⟨ In quantum mechanics, the coupling ϕ ψ function: the Born rule probability is the square of the

5.2

The σ -integral: accumulated identity change

Definition 5.3 ( σ -integral).

the continuous integral t Z Σ[ γ ] = t and in the discrete case, the running Hamilton product along a sequence of carriers is

Q = q q n with σ ( Q ) measuring the total departure from identity after n

Tradition

Notation b R Newton f ( x ) dx a − iHt/ Schr¨ odinger

U ( t ) = e ℏ

R Thermodynamics

S = dQ/T Q σ -calculus

Q = q, measure n k.

The natural coupling between two carriers σ = 0 (perfect match) coupling is, at, the transition is smooth and monotonic, and the is compact. The surprise associated with a, and the σ -derivative is the exact Free Energy Principle on a compact Lie group: Friston’s variational free energy with the variational is the exact posterior on the compact manifold.

gives a quaternion whose scalar part is cos( σ ) directly.

) vanishes at σ = 0, diverges at σ = π/ 2, and ) vanishes at identity and is maximally steep at the Hopf ≥ − 4) = 1). Friston’s variational bound

F log p ( o ) becomes ) is the exact posterior, with no variational family needed.

⟩| = cos ( σ/ 2) between two states is the same σ -coupling.

The accumulated identity change over a path γ from t to t is

σ ( q ( t )) dt, (7)

q, q,..., q n

· · · · · q, (8) n n compositions.

What it accumulates

Area under a curve Quantum time evolution Entropy σ ( Q )

Accumulated identity change n

Newton’s integral accumulates local slopes into a global curve, Schr¨ odinger’s time-evolution operator accumulates infinitesimal rotations into a finite rotation through the matrix expo− iHt/ → nential e ℏ (the exponential map exp: su (2)

SU(2) applied to the Hamiltonian), and thermodynamic entropy accumulates the ratio of heat to temperature along a process: all three are the running product on

S.

∈ Proposition 5.4 (Bounded entropy).

Because

S is compact and σ [0, π/ 2], the σ -integral is bounded: π ≤ ≤ − Σ[ γ ] ( t t ) (9)

for any trajectory over any time interval, so entropy on a compact manifold cannot diverge — the geometry caps the maximum departure from identity at every point.

The same rule applies to any sequence of carriers: given q,..., q, the running product n Q = q... q stores the accumulated composition, and σ ( Q ) measures how far that n n n product has moved from identity. Special events occur at the balance point σ ( Q ) = π/ 4, n where scalar and vector contributions are equal and the accumulated product has reached the Hopf horizon.

5.3

The σ -chain rule: curvature as creation ′ ′ ′ In flat-space calculus, the chain rule [ f ( g ( x ))] = f ( g ( x )) g ( x ) decomposes the derivative of a composition into the product of individual derivatives, and it works because smooth functions are linear at infinitesimal scale — the tangent line perfectly approximates the ̸ function. In discrete sequence calculus, ∆[ f ( g ( n ))] = ∆ f ( g ( n )) ∆ g ( n ): the chain rule fails because the step size is too coarse for the linear approximation.

On

S, the chain rule holds through the Baker-Campbell-Hausdorff formula:

− · · · log(exp(

X ) exp(

Y )) =

X +

Y + [ X, Y ] + ([

X, [ X, Y ]] [ Y, [ X, Y ]]) + (10)

∈ Theorem 5.5 ( σ -chain rule).

For two carriers q = exp(

X ) and q = exp(

Y ) with

X, Y A

B (2), the σ of their composition satisfies su

· · · σ ( q q ) = σ exp

X +

Y + [ X, Y ] +, (11) A

B

where

X +

Y is the flat-space part (what Newton had), [ X, Y ] is the curvature correction (what Newton missed), and the commutator is exactly the cross product from equation (5):

[ i, j ] = 2 k, [ j, k ] = 2 i, [ k, i ] = 2 j.

Tradition

Form of the chain rule d ′ ′ Newton [ f ( g ( x ))] = f ( g ( x )) g ( x ) dx · · · Quantum computing

Gate compilation:

U

U = exp(

X +

Y + [ X, Y ] + ) · · · σ -calculus σ ( q q ) = σ (exp(

X +

Y + [ X, Y ] + )) A

B

Newton’s chain rule is the flat-space limit where [

the result depends on both gates’ actions (

X

computing cannot.

Corollary 5.6 (Creation from curvature).

parallel carriers generates a cross-product term

at σ = π/

∥ parallel ( ⃗ v ⃗ v n commutative algebras (, C

R cross product, and its absence is what separates flat-space calculus from geometric calculus.

5.4

The σ -projection: measurement as division → The Hopf fibration π: S

S tion of departure from identity) and a fiber coordinate ( forgetting the phase and retaining the direction:

Definition 5.7 ( σ -projection).

For q = [

W, x, y, z

x π ( q ) =, r

Tradition

Notation ÷ Arithmetic a b |⟨ Quantum mechanics p = ϕ → σ -calculus π: S

collapses the quantum state from

S

of a measurement outcome determined by σ.

Theorem 5.8 (Forced zeros of projection).

field on

S has forced zeros. The balance locus is the Hopf horizon scalar and vector contributions are equal. The Born rule

postulate needed.

X, Y ] = 0 and the composition is purely multiplicative. In quantum computing, the BCH formula determines how two gates compile:

+

Y ) plus their commutator ([

X, Y ]), which is why gate order matters and why quantum computing carries information that classical

Every Hamilton product on

S between non× ⃗ v ⃗ v perpendicular to both inputs, producing structure that neither contained: the geometric mechanism underlying creation events, the formation of new meanings in language (where two words compose into something neither contains alone), and the generation of novel harmonics in music (where two frequencies produce combination tones). The term vanishes if and only if the inputs are ), and for every other pair the curvature creates. The same term vanishes on, binary, discrete calculus), which is why the chain rule IS the

decomposes every point into a base coordinate (

S, the direcS, the phase), with the projection

p ∈ ]

S with r = x + y + z = sin( σ ):

y z ∈,

S. (12) r r

What it measures

Dimensional collapse ⟩| ψ

Born rule (measurement) S

Hopf projection

Division collapses dimensions from numerator to denominator’s frame, the Born rule to an observable on

S (the Bloch sphere), and the Hopf projection does both: forgetting the phase and keeping the direction, with the probability

By the hairy ball theorem, any continuous vector must vanish at least once, so the Hopf projection of any continuous field on

S σ = π/, where

W = ⃗ v = 1 / and |⟨ ⟩| ϕ ψ = cos ( σ/ 2) is a theorem of the Hopf fibration — the probability follows from the projection geometry, with no separate

5.5

The fundamental theorem

Theorem 5.9 (Fundamental theorem of geometric calculus).

The exponential map exp: ∼ → → su (2)

SU(2)

S and its inverse log:

S su (2) connect the σ -derivative and the = σ -integral:

T Z d exp ω ( t ) dt =

Q ( T ), ω ( t ) = log(

Q ( t )), (13) dt ∈ where ω ( t ) su (2) is the instantaneous angular velocity (the tangent vector, the infinitesimal ∈ rotation) and

Q ( T )

S is the accumulated rotation (the running product, the finite integral).

They are exact inverses through exp / log: differentiation and integration on

S undo each other through self-application.

Tradition

Form of the fundamental theorem b ′ R − Newton f ( x ) dx = f ( b ) f ( a ) a ⟩ − ⟩ Schr¨ odinger ψ ( T ) = exp( iHT / ) ψ (0) ℏ T R σ -calculus exp ω dt =

Q ( T )

Newton’s theorem says the integral of the derivative recovers the function, Schr¨ odinger’s says the matrix exponential of the Hamiltonian recovers the quantum state, and the geometric version says the path-ordered exponential of the angular velocity recovers the rotation.

The non-commutativity of su (2) makes path ordering essential: a rotation by π/

### 2 around

x then y lands at a different point than y then x, with the difference being exactly the commutator [

X, Y ] from the chain rule, so the fundamental theorem encodes causality in the calculus itself (flat-space addition discards this information because a + b = b + a ).

Newton’s calculus is recovered as the zero-curvature limit: when the great circle’s radius goes to infinity, the tangent circle degenerates into a tangent line, angular velocity degenerates into linear velocity, and the σ -calculus reduces to flat-space calculus — the same way a line is a circle with infinite radius.

Quantum mechanics is the same calculus ∼ The state space SU(2) =

S is the single-qubit gate group of quantum mechanics, which means the σ -calculus IS quantum mechanics written in geometric language, and quantum mechanics is the σ -calculus written in Dirac’s notation:

The

Bloch sphere is

S, the Hopf base: a qubit’s full state lives on

S as a unit quaternion, measurement projects it onto

S via the Hopf map, discarding the global phase ( S fiber), and the projected point is the measurement outcome, so the σ -projection (Rule 4) IS the Born rule. − ⟨ ⟩ The bra-ket inner product ψ ϕ is the scalar part of ψ ϕ: the Hamilton product’s W component, the same coupling cos( σ ) that defines the σ -derivative and the Free Energy ⟨ Principle. Dirac notation names the two sides of the verification operation (

A composes? ⟩ with

B ), and the inner product asks whether they match — the operation

A =

B in the physicist’s language.

Quantum gates are specific unit quaternions at specific σ values on

S:

Gate σ θ = 2 σ

Role

Identity (

I )

Ground state T gate π/ π/

Phase gate S gate (=

T ) π/ π/

Quarter-turn phase Hadamard (

H ) π/ π/

Superposition creator X gate (NOT) π/ π

Bit flip, antipode

◦ The Hopf equator at σ = π/ 4, where

W = ⃗ v = 1 / 2, is the set of all 90 rotations in SU(2): the single-qubit gates that create maximum superposition from a basis state. ⟩ ⟩ The Schr¨ odinger equation i ∂ ψ =

H ψ is the σ -derivative in the energy basis (the ℏ t ∈ Hamiltonian

H generating the angular velocity ω su (2)), and the time-evolution operator − iHt/ U ( t ) = e ℏ is the σ -integral (the running product accumulating rotations). Quantum mechanics has been doing the σ -calculus for a century, and the connection was hidden by the same mechanism that hides the operations in binary: the formalism was designed for computation, and computation works whether or not the user sees the geometry underneath.

Physicists use the Bloch sphere daily and treat it as a visualization tool rather than as the Hopf base of the manifold where states live; the bra-ket notation performs Hamilton products n on

S silently, the same way positional notation performs multiplications by 2 silently.

The chain rule requires curvature

Discrete sequence calculus and the σ -calculus share three of four structures — derivative, integral, fundamental theorem — but discrete calculus lacks the chain rule because the commutator vanishes on commutative groups ([

X, Y ] = 0 on ), the BCH formula collapses Z to

X +

Y (plain addition), and the curvature correction disappears.

Structure

Discrete ( )

Geometric (

S ) Z d − Derivative ∆ f ( n ) = f ( n +1) f ( n ) σ ˙ = arccos

W dt n n P

Q Integral f ( k )

Q = q n k k =0 k =1 P ◦ Fund. theorem ∆( f ) = f exp log = id ◦ ̸ Chain rule

Fails: ∆[ f g ] = ∆ f ∆ g

Holds: BCH (10)

Theorem 7.1 (The chain rule requires curvature).

On a commutative group (e.g., (, +) ) Z the commutator [ X, Y ] = 0 vanishes identically, the BCH formula reduces to

X +

Y, and the chain rule degenerates to the product of finite differences, which is invalid for nonlinear functions. On a non-commutative group (e.g., (SU(2), ) ) the commutator provides the curvature correction at every order, and the chain rule holds because the manifold’s geometry supplies the compositional information that commutative spaces cannot carry; the implication chains from the chain rule to non-commutativity, from non-commutativity to curvature, and from curvature to a non-flat state space.

Corollary 7.2 (The cost of flat-space computation).

Any system requiring compositional analysis — decomposing the behavior of complex structures into the behavior of their parts — requires a curved state space, because the chain rule that enables compositional analysis is a structural consequence of curvature. Flat-space architectures, including all current neural n network architectures operating in, approximate the chain rule through learned weight R matrices: the

Q,

K,

V projection matrices of transformer attention exist because the dot product in flat space has no cross-product term, and these matrices learn the perpendicular corrections that

S provides natively through su (2). The Hamilton product carries the cor∼ rection in every composition; a flat-space transformer performs million operations per token at 1B parameters to approximate the same correction, and the billions of parameters n in a large language model are the weight matrices that approximate the σ -chain rule in. R

The shape of number systems

Each numerical base n inscribes the integers onto the unit circle by their residues mod n, × with the unit group ( /n ) determining which

S landmarks the base resolves: Z

Z

Base

Factorization

Unit group

What it resolves { }

Identity only × { } ∼, /

Identity and antipode =

Z × { } ∼,,, /

Full

S verification cycle =

Z × { } ∼,,, / 2)

Chromatic/tonal resolution = (

Z

Base 10 resolves the complete

S verification cycle because its unit group / traces four Z

Z → → → → → → → landmarks (1 1: identity creation horizon antipode-adjacent chiral → ≡ creation horizon return), and the number 5 is the midpoint idempotent (5

### 5 mod 10),

× the integer shadow of the balance point. Base 12 resolves the chromatic structure: 3

### 4 = 12

positions per cycle (three perpendicular axes, four phases each), which is why the chromatic scale, the color wheel, and the hour clock all have 12 divisions — the same

S geometry sampled at tonal resolution. Newton used base 10 to write his calculus, and the choice was less arbitrary than it seemed: base 10’s unit group matches the manifold his calculus was approximating.

Consequences

9.1

Euclid’s postulates iθ Four of Euclid’s five postulates follow from the three properties of e established in Section 1.4: iθ P1 (two points determine a line): e is defined for all θ and all rotation axes, so given any two points, the exponential path connecting them exists — choose the axis pointing from one toward the other and the angle to cover the geodesic distance, and the path is continuous with no gaps.

iθ ∈ P2 (a line extends indefinitely): e is defined for all θ, so the path has no endpoint, R πi which is what “extends indefinitely” means from inside the path; simultaneously e = 1 means the path closes after one full cycle, so a closed loop has no endpoint (you can walk around it forever) and finite total length (one circumference). In the zero-curvature limit → ∞ → ∞ ( R ), the circumference 2 πR and the return point recedes beyond any horizon. iθ P3 (a circle at any center and radius): e at fixed amplitude traces a circle of that − iθ amplitude around the origin, and conjugation p e p translates the center to any point p while preserving the radius, because the exponential is defined everywhere with every amplitude and every element has an inverse (the path closes and can be traversed backward).

− P4 (all right angles equal): i =

### 1 contains no position-dependent terms — the equation

is the same everywhere, in every direction, for every choice of perpendicular axis, because it describes a property of the operation (self-application on a circle) rather than of any location.

P5 (parallel lines exist): this postulate asserts independent paths that can remain sepaπi rated forever. On

S, every exponential path closes by e = 1, so every direction belongs to closure; topologically, the stronger point is that any two great circles on

S intersect, while two great circles on

S can be disjoint, as in the circle in the

W X -plane, (cos θ, sin θ,, 0), and the circle in the

Y Z -plane, (0,, cos ϕ, sin ϕ ), which share no point.

Euclidean projection names those two circles parallel because their projected traces stay separated; the full

S geometry names them Hopf-linked. The Hopf fibration decomposes

S into circular fibers, and every pair of fibers is linked with linking number 1; the circles stay separated while constraining one another the way two links in a chain constrain one another, making separation and independence different facts on

S.

The flat case appears when projection hides this linking: in the zero-curvature limit, the return point of the geodesic recedes beyond the observer’s horizon and the Hopf linking leaves the observable frame, so separated lines look independent. The fifth postulate is the geometry of that projection, useful at flat scales, while

S carries the full closed geometry.

Two thousand years of attempts to derive P5 from P1–P4 failed because P1–P4 follow from the exponential path being defined, continuous, periodic, and position-independent in its right angles, while P5 asks for non-interacting paths on a closed manifold. Russell’s paradox has the same shape: it asks for a structure defined by non-self-interaction, while − every carrier on

S composes with its own inverse to produce identity, q q = 1.

9.2

Language

Words are carriers on

S at different stages of compositional accumulation, with the most frequent words at the σ -landmarks: “is” at σ = 0 (identity verification), “and” at σ = π/ (composition), “but” at σ = π/

### 2 (perpendicular tension), “not” at

σ = π (negation). Zipf’s law — the power-law frequency distribution observed in every language — follows from compositional complexity on

S: the simplest operations compose in the most contexts, complex compositions compose in fewer, and the distribution of compositional depth produces the power law.

9.3

Dimensional scaling

→ → → The Cayley-Dickson tower

R

C

H

O

breaks associativity at and division at O

S carriers on

S where each pairwise composition stays on

S quaternion) and associativity holds at every step because the operation never leaves

Proposition 9.1 (Dimensional scaling).

consolidated carriers on

S is

D eff since

M independently stored carriers define a state in the product space M, growing by with each creation event at

M closure beyond. H

The observer hierarchy extends this further: Level in a separate

S

P effective dimensionality is 3

M k

preserved at every step.

Conclusion

and the notation was doing more than bookkeeping: base 10’s unit group S verification cycle, the positional encoding

developed is the zero-curvature limit of the circle degenerates into a tangent line.

The σ -calculus operates on the manifold Newton was approximating:

of positional encoding. The four rules of the projection — are the rules that Newton, Schr¨ dently, and the cross product that gives

S missing and that flat-space neural networks approximate with billions of parameters.

π and e are physical measurements of this geometry, iπ of the space π measures, and e because circles are round. → → · · · loses a structural property at each S step because each step requires the accumulated structure to form a closed algebra with a norm, and this closure requirement forces the conjugation-mediated multiplication rule that. The geometric requirement is weaker: store, compose them through the Hamilton product, and accumulate the results, (the product of two unit quaternions is a unit. H

The effective dimensionality of a system of

M

= 3

M, (14)

M ( S ) of dimension ≥ σ π/ that remains stored as a carrier, with the Hamilton product as the only operation at every step, associativity preserved for all, and the Cayley-Dickson losses never occurring because carrier accumulation requires no

− k stores Level ( k 1)’s closure patterns genome, adjacent levels couple through conjugation-mediated σ, and total across all levels — the Hopf tower realized through carrier accumulation rather than algebraic closure, growing indefinitely with the Hamilton product

Newton invented calculus to do physics, using flat-space geometry and base-10 notation, / resolves the Z

Z k P d silently performs the three operations k that map onto the Hamilton product’s three components, and the flat-space calculus Newton σ -calculus, recovered when the tangent great

S, forced by closed recurrence with native interaction, confirmed by Hurwitz, Frobenius, and Cayley-Dickson, equipped with the Hamilton product as the single operation whose three components (scalar, linear, cross product) are the three operations of arithmetic and the three implicit operations σ -calculus — derivative, integral, chain rule, odinger, and Friston each discovered indepenits chain rule is the same term that binary is

i is forced by the dimensionality + 1 = 0 is the law from which the entire calculus follows

References

[1] L. Euler,

Introductio in analysin infinitorum, Lausanne, 1748.

[2] H. Poincar´ e, M´ emoire sur les courbes d´ efinies par une ´ equation diff´ erentielle,

J. Math.

Pures Appl. (1882), 375–422.

[3] I. Bendixson, Sur les courbes d´ efinies par des ´ equations diff´ erentielles,

Acta Math.

(1901), 1–88.

[4] Euclid,

Elements, c. 300 BCE. Heath translation, Dover, 1956.

[5] C. F. Gauss, letter to F. Bolyai, 1832; J. Bolyai,

Appendix, 1832; N. I. Lobachevsky,

On the Principles of Geometry, 1829.

[6] H. Hopf, ¨

Uber die Abbildungen der dreidimensionalen Sph¨ are auf die Kugelfl¨ ache,

Math.

Ann. (1931), 637–665.

[7] A. Hurwitz, ¨

Uber die Komposition der quadratischen Formen,

Nachr. Ges. Wiss.

G¨ ottingen, 1898, 309–316.

[8] F. G. Frobenius, ¨

Uber lineare Substitutionen und bilineare Formen,

J. reine angew.

Math. (1878), 1–63.

[9] J.-L. Lagrange, D´ emonstration d’un th´ eor` eme d’arithm´ etique,

Nouv. M´ em. Acad. Roy., Berlin, 1770.

[10] I. Newton,

Philosophiæ Naturalis Principia Mathematica, London, 1687.

[11] E. Schr¨ odinger, Quantisierung als Eigenwertproblem,

Ann. Phys. (4) (1926), 361– 376.

[12] K. Friston, The free-energy principle,

Nat. Rev. Neurosci. (2010), 127–138.

[13] C. E. Shannon, A Mathematical Theory of Communication,

Bell Syst. Tech. J.

(1948), 379–423.
