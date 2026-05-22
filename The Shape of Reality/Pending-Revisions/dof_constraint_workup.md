# DOF Constraint Workup

The current particle topology story has two layers:

1. the prefactor \(c\) in \(c\pi^w\), interpreted as \(1/\mathrm{cs}\);
2. the exponent \(w\), interpreted as the number of independent integration dimensions or degrees of freedom.

The prefactor layer is much stronger than the DOF layer.  The proton prefactor is derived from the trefoil, and several single-term particles have exact knot/link matches.  The exponent layer still needs a rule that is explicit enough to test.

## 1. Current data

\[
\begin{array}{c|c|c|c|c}
\text{particle} & \text{constituents} & \text{formula} & \mathrm{cs} & \mathrm{DOF}\\
\hline
p & uud & 6\pi^5 & 1/6 & 5\\
\Sigma^0 & uds & 24\pi^4 & 1/24 & 4\\
D^\pm & c\bar d & 12\pi^5 & 1/12 & 5\\
J/\psi & c\bar c & 2\pi^7 & 1/2 & 7\\
Z & - & 6\pi^9 & 1/6 & 9\\
\text{top} & t & 112\pi^7 & 1/112\text{ target} & 7
\end{array}
\]

The DOF values are \(5,4,5,7,9,7\).  Any derivation must explain why these exponents differ when some prefactors repeat, especially \(p\) and \(Z\), which share \(c=6\) but differ by four powers of \(\pi\).

## 2. Carrier-counting candidate

The cleanest rule found so far treats each physical constituent as an \(S^3\) carrier with four coordinates.  Constraints remove whole geometric freedoms rather than arbitrary numbers:

- a baryon starts with three carriers, so \(4N=12\);
- translation invariance removes one center carrier, giving \(-4\);
- flavor/color closure removes \(d+1\), where \(d\) is the number of distinct flavors;
- a symmetric meson removes one phase-locking constraint;
- an asymmetric meson removes three spatial alignment constraints.

This gives:
\[
p(uud):\quad 12-4-(2+1)=5,
\]
\[
\Sigma^0(uds):\quad 12-4-(3+1)=4,
\]
\[
J/\psi(c\bar c):\quad 8-1=7,
\]
\[
D^\pm(c\bar d):\quad 8-3=5.
\]

This rule has the right shape because every subtraction names a geometric operation: center removal, flavor distinction, phase lock, or spatial alignment.  It should not yet be presented as proved, because the \(d+1\), \(1\), and \(3\) constraints still need to be derived from the relevant symmetry action.

## 3. What a proof would need

For baryons, the proof target is:
\[
\mathrm{DOF}_{\mathrm{baryon}}
=
4N-4-(d+1)
=
8-d,
\]
for \(N=3\).  That gives \(6\) for \(d=2\) if the final color-neutrality condition is counted separately, or \(5\) if it is included in \(d+1\).  The current proton formula requires the latter.

A real proof should identify the quotient:
\[
(S^3)^3 / G_{\mathrm{baryon}},
\]
where \(G_{\mathrm{baryon}}\) includes center translation plus the color/flavor closure group.  The dimension of the quotient should be the exponent \(w\).

For mesons, the proof target is:
\[
(S^3)^2 / G_{\mathrm{meson}},
\]
with
\[
\dim G_{\mathrm{meson}}=1
\]
for self-conjugate \(c\bar c\), and
\[
\dim G_{\mathrm{meson}}=3
\]
for asymmetric \(c\bar d\).  The natural interpretation is that self-conjugacy locks only phase, while asymmetric particle-antiparticle linking locks a full spatial frame.

## 4. Z as trefoil plus electroweak depth

The \(Z\) shares the trefoil prefactor:
\[
Z:\quad 6\pi^9.
\]
Relative to the proton,
\[
9-5=4.
\]
That difference has a clean candidate interpretation:
\[
\dim SU(2)+\dim U(1)=3+1=4.
\]
So the \(Z\) can be described as the trefoil topology lifted by the electroweak gauge depth.  This is one of the strongest DOF clues because it explains why the prefactor stays \(6\) while the exponent changes.

## 5. Immediate testable questions

1. Can the baryon quotient \((S^3)^3/G_{\mathrm{baryon}}\) be written explicitly so that repeated-flavor baryons have \(w=5\) and all-distinct baryons have \(w=4\)?
2. Can amphichirality of the figure-eight knot supply the one phase-lock constraint for \(J/\psi\)?
3. Can a two-component non-self-conjugate link naturally fix a three-dimensional relative frame, giving \(D^\pm\) the \(-3\) constraint?
4. Can the \(Z\) be treated as the same trefoil carrier with four extra electroweak integration coordinates?

If these four questions close, the exponent \(w\) becomes derived rather than fitted for the most important single-term particles.
