# \(S^4\) Spectral Zeta Proof Notes

This note extracts the reusable proof structure from `s4_zeta_coefficients.py`.

## 1. Definition

For the conformal scalar on \(S^4\),
\[
\zeta_{\mathrm{conf}}(s)
=
\frac16\sum_{m=1}^{\infty}
\frac{2m+1}{[m(m+1)]^{s-1}}.
\]
Write \(n=s-1\):
\[
F_n(m)=\frac{2m+1}{m^n(m+1)^n}.
\]

This note should be read as the harmonic counterpart to the \(S^3\) carrier calculus.  The \(S^3\) side uses carriers, Hamilton products, knots, and projections.  The \(S^4\) side uses modes, degeneracies, spectral traces, and zeta regularization.  The shared value
\[
\zeta_{\mathrm{conf},S^4}(3)=\mathrm{cs}_{S^3}(T(2,3))=\frac16
\]
is therefore a wave/topology bridge rather than a second way of writing the same calculation.

The factors in the summand already carry harmonic meaning.  The denominator
\[
m(m+1)
\]
is angular-momentum/Casimir structure, while the numerator
\[
2m+1
\]
is the size of the \(m\)-th harmonic multiplet and also the adjacent shell difference
\[
(m+1)^2-m^2=2m+1.
\]
At \(s=3\), the spectral trace becomes an adjacent-shell cancellation.

## 2. Partial fractions and Catalan triangle

Around \(m=0\), the partial fraction coefficients are
\[
F_n(m)=\sum_{j=2}^{n}\frac{A_{n,j}}{m^j}
+ \sum_{j=2}^{n}\frac{B_{n,j}}{(m+1)^j},
\]
where symmetry gives
\[
B_{n,j}=-A_{n,j}.
\]
The explicit coefficient is
\[
A_{n,j}
=
(-1)^{n-j}
\frac{j-1}{2n-j-1}
\binom{2n-j-1}{n-j},
\qquad j=2,\ldots,n.
\]
The absolute values form Catalan-triangle rows:
\[
1;\quad
1,1;\quad
2,2,1;\quad
5,5,3,1;\quad
14,14,9,4,1;\quad\ldots
\]

This matters because Catalan numbers count binary composition trees. The spectral correction series produces zeta constants through the same recursive-composition combinatorics that the calculus uses for self-application.

## 3. Why even zeta values cancel

Summing the partial fractions gives terms of the form
\[
\sum_{m=1}^{\infty}\frac{1}{m^j}
-\sum_{m=1}^{\infty}\frac{1}{(m+1)^j}.
\]
The second sum is
\[
\sum_{m=1}^{\infty}\frac{1}{(m+1)^j}
=
\zeta(j)-1.
\]
Therefore each matched pair contributes a rational constant plus a surviving zeta term only when the coefficients do not cancel across the full decomposition. In the conformal \(S^4\) case the even zeta coefficients cancel identically, and the closed forms contain only rational numbers plus odd zeta values.

The first values are
\[
\zeta_{\mathrm{conf}}(3)=\frac16,
\]
\[
\zeta_{\mathrm{conf}}(4)=\frac{\zeta(3)-1}{3},
\]
\[
\zeta_{\mathrm{conf}}(5)=\frac{5-4\zeta(3)}{6},
\]
\[
\zeta_{\mathrm{conf}}(6)=\frac{5\zeta(3)+\zeta(5)-7}{3}.
\]

## 4. Why \(s=3\) is the rational closure point

At \(s=3\), \(n=2\), and
\[
\frac{2m+1}{m^2(m+1)^2}
=
\frac{1}{m^2}-\frac{1}{(m+1)^2}.
\]
The entire infinite sum telescopes to \(1\), so
\[
\zeta_{\mathrm{conf}}(3)=\frac16.
\]

The telescoping should be interpreted as spectral closure.  Neighboring harmonic shells cancel by their boundary difference, and the whole infinite mode tower leaves one rational residue.  That residue is the same value as the trefoil Chern-Simons invariant on the \(S^3\) carrier side, making the proton result the point where a bulk harmonic closure and a boundary topological closure return the same invariant.

For every computed \(s>3\), at least one odd zeta coefficient survives. The coefficient formula above gives a path to an analytic proof: show that the highest available odd zeta coefficient is nonzero for every \(n>2\). This is the remaining formal step if the paper wants to state uniqueness of rationality as a theorem rather than as a verified pattern.

## 5. Proton correction target

At \(s=6\),
\[
\zeta_{\mathrm{conf}}(6)
=
\frac{5\zeta(3)+\zeta(5)-7}{3}.
\]
The \(\zeta(5)\) coefficient is \(1/3\), while the proton one-loop correction is
\[
\frac{\zeta(5)}{30}.
\]
The missing projection/normalization is therefore exactly
\[
\frac{1/30}{1/3}=\frac{1}{10}.
\]
The likely geometric target is
\[
\frac{1}{10}=\frac{1}{2\cdot5},
\]
with \(5\) the proton's degrees of freedom and \(2\) the orientation/spin doublet. This is now a sharply defined missing derivation rather than a vague gap.

## 6. The sixfold mode

The \(1/6\) result also points to the base-3/hexagonal slicing of the circle.  The geometric calculus paper already distinguishes the right-angle mode
\[
180^\circ/2=90^\circ
\]
from the triangular mode
\[
180^\circ/3=60^\circ.
\]
The \(90^\circ\) mode supports binary distinction, square geometry, and perpendicular computation.  The \(60^\circ\) mode supports sixfold closure:
\[
6\cdot60^\circ=360^\circ.
\]
This is the stable packing mode seen in triangular lattices and hexagonal structures.

The same six appears in three May 22 structures:
\[
R_{S^3}=3(3-1)=6,
\]
\[
\frac{1}{\mathrm{cs}(T(2,3))}=6,
\]
\[
\zeta_{\mathrm{conf},S^4}(3)=\frac16.
\]
The current working interpretation is that \(3\cdot2\) counts the six oriented curvature channels of \(S^3\): three spatial directions, each with two transverse oriented couplings, or equivalently three coordinate planes with two orientations each.  This sixfold curvature count matches the inverse trefoil cost and the reciprocal \(S^4\) spectral residue.

This remains a derivation target.  The closed claim requires showing that the curvature-channel count, the \(60^\circ\) circle slicing, and the trefoil CS denominator are the same object under the relevant projection.
