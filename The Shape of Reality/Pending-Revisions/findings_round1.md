# May 22 Discovery Pass — Round 1

This note records the first active verification/discovery pass after re-reading `session_may22_results.md`. The goal is to turn surprising claims into proofs, reproducible computations, or sharply defined missing steps.

## 1. Trefoil uniqueness is stronger than the session note stated

For a torus knot \(T(p,q)\), the May 22 formula is
\[
\frac{1}{\mathrm{cs}(T(p,q))}
=
\frac{24pq}{(p^2-1)(q^2-1)}.
\]

A search over coprime \(2\leq p<q\leq 5000\) found only one integer value:
\[
T(2,3):\qquad \frac{1}{\mathrm{cs}}=6.
\]

The finite list with inverse-CS at least \(1\) is:
\[
\begin{aligned}
&(2,3),(2,5),(2,7),(2,9),(2,11),(2,13),(2,15),\\
&(3,4),(3,5),(3,7),(3,8),(4,5).
\end{aligned}
\]
Only \((2,3)\) is integral.

The proof can be made short. For fixed \(p\), the expression decreases with \(q\), so only small \(p\) can have value \(\geq 1\). For \(p=2\),
\[
\frac{1}{\mathrm{cs}}=\frac{16q}{q^2-1}.
\]
Since \(\gcd(q,q^2-1)=1\), integrality forces \(q^2-1\mid16\), hence \(q=3\) among admissible \(q>2\). The remaining finite cases \(p=3,4\) are checked directly, and \(p\geq5\) is below \(1\) already at \(q=p+1\). This should become a theorem.

## 2. The alpha residual has a real second structure

The May 22 alpha formula is
\[
\alpha_{\mathrm{phys}}^{-1}
=
\frac{9\pi^5}{e^3}
-
\frac{1}{3\pi}\log\frac94.
\]

Using CODATA inverse alpha \(137.035999084\), this gives
\[
137.036364346577\ldots,
\]
with residual \(2.665\) ppm.

The exact one-loop scale ratio that would hit CODATA is
\[
r_{\mathrm{exact}}=2.2577590146612003994\ldots,
\]
while
\[
\frac94=2.25.
\]
The missing log-scale correction is
\[
L=\log\frac{r_{\mathrm{exact}}}{9/4}
=0.0034425186877091865\ldots.
\]

Measured in powers of \(\alpha\):
\[
\frac{L}{\alpha^2}=64.6465938512\ldots.
\]
So the dominant missing term is very close to \(64\alpha^2\), with
\[
L-64\alpha^2
=3.4431998401\times 10^{-5}.
\]

Using
\[
r=\frac94\exp(64\alpha^2)
\]
self-consistently gives inverse alpha
\[
137.036002737367\ldots,
\]
leaving only \(0.02666\) ppm. This is not yet a derivation, but it is a strong target because \(64=8^2\), and \(8\) already appears in the trefoil self-interaction channel.

The next coefficient after \(64\alpha^2\) would be approximately
\[
88.6066344020\,\alpha^3,
\]
which was not immediately reducible to a clean small expression.

## 3. The proton correction is two-sided

The topological correction gives
\[
\frac{m_p}{m_e}
=
6\pi^5+\frac{\zeta(5)}{30}
=1836.15267297019\ldots,
\]
with residual
\[
-4.60\times10^{-7}
\]
against \(1836.15267343\).

The electromagnetic/self-interaction correction gives
\[
6\pi^5\exp\left(\frac{\alpha^2}{\sqrt8}\right)
=1836.15267799435\ldots,
\]
with residual
\[
4.56\times10^{-6}.
\]

A scan over neighboring square-root channels:
\[
\sqrt7,\sqrt8,\sqrt9
\]
shows \(\sqrt8\) is sharply selected. The neighbors are hundreds of times worse. This supports treating \(8=p(p-1)+q(q-1)\) for the trefoil as a genuine structural channel count.

## 4. The \(S^4\) zeta partial fractions have Catalan structure

For
\[
\zeta_{\mathrm{conf}}(s)
=
\frac16
\sum_{m=1}^{\infty}
\frac{2m+1}{[m(m+1)]^{s-1}},
\]
the \(s=3\) case telescopes exactly:
\[
\frac{2m+1}{m^2(m+1)^2}
=
\frac1{m^2}-\frac1{(m+1)^2},
\]
so \(\zeta_{\mathrm{conf}}(3)=1/6\).

For higher \(s\), the partial-fraction coefficients form the Catalan triangle. Examples:
\[
s=6:
\quad
5,5,3,1
\]
and
\[
s=8:
\quad
42,42,28,14,5,1.
\]
These are reversed Catalan-triangle rows. This is likely important: Catalan numbers count binary composition trees, so the same combinatorics that governs self-application appears inside the \(S^4\) spectral correction series.

At \(s=6\),
\[
\zeta_{\mathrm{conf}}(6)
=
\frac{5\zeta(3)+\zeta(5)-7}{3},
\]
so the coefficient of \(\zeta(5)\) is \(1/3\). The proton correction needs \(\zeta(5)/30\), meaning the missing normalization from the spectral value to the proton correction is \(1/10\). A natural target is \(1/(2\,\mathrm{DOF})=1/10\) for the proton's five degrees of freedom, but this still needs derivation.

## 5. DOF constraints have a cleaner candidate rule

The May 22 table:
\[
\begin{array}{c|c|c|c}
\text{particle} & \text{raw} & \text{constraints} & \text{DOF}\\
\hline
p(uud)&12&7&5\\
\Sigma^0(uds)&12&8&4\\
J/\psi(c\bar c)&8&1&7\\
D^\pm(c\bar d)&8&3&5
\end{array}
\]

The attempted \(S_3/H\) explanation in the session note does not work. A cleaner candidate rule is:

- each constituent carries a full \(S^3\) carrier, so raw DOF is \(4N\);
- baryons remove one 4D center-of-mass carrier;
- baryon color/flavor closure removes \(d+1\), where \(d\) is the number of distinct flavors;
- symmetric mesons remove one phase-locking constraint;
- asymmetric mesons remove three spatial alignment constraints.

This gives:
\[
\begin{aligned}
p(uud):&\quad 12-4-(2+1)=5,\\
\Sigma^0(uds):&\quad 12-4-(3+1)=4,\\
J/\psi(c\bar c):&\quad 8-1=7,\\
D^\pm(c\bar d):&\quad 8-3=5.
\end{aligned}
\]

This is still a derivation target, but it is cleaner than the broken subgroup-index formula because it uses visible geometric operations: center carrier, flavor distinction count, singlet closure, phase lock, and spatial alignment.

## Next Targets

1. Write the torus-knot uniqueness proof fully.
2. Test whether the \(64\alpha^2\) alpha correction also appears in \(G\), proton EM correction, or the \(8\)-channel trefoil count.
3. Derive the Catalan-triangle partial fraction formula for \(\zeta_{\mathrm{conf}}(s)\).
4. Derive the \(1/10\) normalization from \(S^4\) spectral \(\zeta(5)\) to proton \(\zeta(5)/30\).
5. Turn the DOF candidate rule into a group/action proof or falsify it with additional particles.

---

# Round 2 Additions

## 6. Torus-knot uniqueness proof

The trefoil uniqueness result can be stated cleanly:

\[
\text{Among coprime torus knots }T(p,q),\quad
\frac{24pq}{(p^2-1)(q^2-1)}
\in \mathbb{Z}
\]
only for \((p,q)=(2,3)\).

Assume \(2\leq p<q\). The expression decreases with \(q\) for fixed \(p\). Its maximum at fixed \(p\) occurs at \(q=p+1\):
\[
\frac{24p(p+1)}{(p^2-1)((p+1)^2-1)}
=
\frac{24}{(p-1)(p+2)}.
\]
For \(p\geq5\), this is at most
\[
\frac{24}{4\cdot7}=\frac67<1,
\]
so no integer value \(\geq1\) can occur.

Only \(p=2,3,4\) remain.

For \(p=2\):
\[
\frac{24(2)q}{(4-1)(q^2-1)}
=
\frac{16q}{q^2-1}.
\]
Since \(\gcd(q,q^2-1)=1\), integrality requires \(q^2-1\mid 16\). With \(q>2\), this forces \(q=3\), giving \(6\).

For \(p=3\), the condition that the value be at least \(1\) leaves only
\[
q=4,5,7,8,
\]
with values
\[
\frac{12}{5},\quad \frac{15}{8},\quad \frac{21}{16},\quad \frac87.
\]
None is an integer.

For \(p=4\), only \(q=5\) remains, giving
\[
\frac43.
\]

Therefore \(T(2,3)\) is the unique torus knot with integer inverse Chern-Simons invariant under this formula.

## 7. Closed form for the \(S^4\) zeta coefficients

Let
\[
F_n(m)=\frac{2m+1}{m^n(m+1)^n},
\qquad n=s-1.
\]
The partial fraction around \(m=0\) has terms
\[
F_n(m)=\sum_{j=2}^{n}\frac{A_{n,j}}{m^j}+\cdots
\]
with
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
\begin{array}{c|l}
n & |A_{n,j}|\\
\hline
2 & 1\\
3 & 1,1\\
4 & 2,2,1\\
5 & 5,5,3,1\\
6 & 14,14,9,4,1\\
7 & 42,42,28,14,5,1\\
8 & 132,132,90,48,20,6,1
\end{array}
\]

This is a real structural bridge: the \(S^4\) spectral correction is not merely producing odd zeta values; it is producing them through the combinatorics of binary composition trees. Catalan structure is exactly what should appear when a closed operation recursively composes with itself.

The first sums are:
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

The \(s=6\) value is important because it is the first one containing \(\zeta(5)\), the proton correction term.

## 8. \(S^4\rightarrow\zeta(5)/30\): sharper missing normalization

At \(s=6\),
\[
\zeta_{\mathrm{conf}}(6)
=
\frac{5\zeta(3)+\zeta(5)-7}{3}.
\]
The coefficient of \(\zeta(5)\) is \(1/3\).

The proton correction is
\[
\frac{\zeta(5)}{30},
\]
so the normalization needed after projecting out the highest odd-zeta channel is exactly
\[
\frac{1/30}{1/3}=\frac{1}{10}.
\]

This suggests a concrete target:
\[
\frac{1}{10}=\frac{1}{2\cdot5}
\]
where \(5\) is the proton's DOF and \(2\) is the orientation/spin doublet. This is not yet a proof, but it sharply identifies what the missing derivation must produce.

## 9. The \(64\alpha^2\) correction also nearly closes \(G\)

Using the May 22 dimensionless \(G\) expression
\[
G_*=
\frac{27\pi^5}{8e^3}+\frac{\zeta(5)}{10}
=51.52459529358\ldots
\]
and the session's measured target \(51.52784\), the residual is
\[
0.0032447064\ldots.
\]

The earlier comparison to
\[
64\alpha^2=0.0034080867\ldots.
\]
gave the ratio
\[
\frac{G_{\mathrm{meas}}-G_*}{64\alpha^2}=0.95206\ldots.
\]

Adding \(64\alpha^2\) overshoots by only
\[
1.63\times 10^{-4}.
\]
Adding \(64\alpha^2\sqrt8/\pi\) undershoots by
\[
1.76\times 10^{-4}.
\]

This did not close \(G\), but it showed the same \(8^2\) correction scale appearing in the gravitational residual. A later check with current constants sharpened the target: the residual is
\[
G_{\mathrm{meas}}-G_*
=0.0032445433385\ldots
=60.9288414861\ldots\,\alpha^2.
\]
Thus
\[
61\alpha^2
\]
is a much better candidate than \(64\alpha^2\). Adding \(61\alpha^2\) leaves only
\[
-3.79\times10^{-6}
\]
in the logarithmic Planck/electron mass ratio, corresponding to roughly \(7.6\) ppm in \(G\). The integer \(61\) is not yet explained, but the residual has been narrowed from a loose \(8^2\) clue to a sharply quantified \(61\alpha^2\) target.

## 10. Lambda prefactor target

The raw sigma-relaxation estimate is
\[
\left(\frac{t_{\mathrm{Pl}}}{t_0}\right)^2
=1.5332084\times10^{-122}.
\]
Using the session's observed ratio \(2.89\times10^{-122}\), the missing factor is
\[
1.88494\ldots.
\]

The nearby topological prefactor
\[
\frac6\pi=1.90986\ldots
\]
would give
\[
\frac6\pi
\left(\frac{t_{\mathrm{Pl}}}{t_0}\right)^2
=2.92821\times10^{-122}.
\]
This is high by about \(1.3\%\) relative to the session value. A later prefactor search found a better structural target:
\[
\frac{3\pi}{5}=1.884955592\ldots,
\]
which gives
\[
\frac{3\pi}{5}
\left(\frac{t_{\mathrm{Pl}}}{t_0}\right)^2
=
2.89003\times10^{-122}.
\]
Using the rounded session target \(2.89\times10^{-122}\), this is high by only about \(0.001\%\).

Using the common reference value \(\Lambda\approx1.1056\times10^{-52}\,\mathrm{m}^{-2}\) and \(l_P=1.616255\times10^{-35}\,\mathrm m\), the target becomes \(2.88814\times10^{-122}\), and \(3\pi/5\) is high by about \(0.0655\%\). This candidate still has a cleaner dimensional reading than \(6/\pi\): three spatial dimensions times the closure unit \(\pi\), normalized by the proton/topological degree count \(5\). Because cosmological inputs and conventions matter here, this should be treated as a strong prefactor target rather than a closed derivation.

---

# Round 3 Additions

## 11. Dimension three calibration is theorem-level

The revision section "Why Only Three Dimensions" survives direct checking. For the minimal adjacent torus knot \(T(n-1,n)\),
\[
\mathrm{cs}(T(n-1,n))
=
\frac{((n-1)^2-1)(n^2-1)}{24n(n-1)}
=
\frac{(n-2)(n+1)}{24}.
\]
The unit \(n\)-sphere has scalar curvature
\[
R_{S^n}=n(n-1).
\]
The calibration condition
\[
\frac{1}{\mathrm{cs}(T(n-1,n))}=R_{S^n}
\]
therefore gives
\[
\frac{24}{(n-2)(n+1)}=n(n-1),
\]
or
\[
n(n-1)(n-2)(n+1)=24.
\]
For \(n>2\), the left side is strictly increasing, and
\[
3\cdot2\cdot1\cdot4=24,
\qquad
4\cdot3\cdot2\cdot5=120.
\]
Thus \(n=3\) is the unique integer dimension where the simplest adjacent torus-knot topological cost is calibrated to intrinsic sphere curvature.

This should be promoted from "interesting addition" to a central theorem. It is independent from the verification-branching argument and uses only two standard formulas: scalar curvature of \(S^n\) and the Chern-Simons invariant of torus-knot complements.

## 12. Trefoil representation claim needs a finite-closure qualifier

The revision section "Gauge Structure from Knot Topology" currently says the trefoil complement group
\[
\langle a,b\mid a^2=b^3\rangle
\]
has exactly six one-dimensional irreducible representations. As stated, this is not correct.

After abelianization, the relation is
\[
2a=3b.
\]
Since \(\gcd(2,3)=1\), the abelianization is \(\mathbb Z\), so unrestricted one-dimensional \(U(1)\) characters form a circle, not six isolated characters.

The six-character statement becomes correct after imposing the finite closure quotient
\[
a^2=b^3=1.
\]
Then \(a\) has two allowed phases and \(b\) has three allowed phases, producing
\[
\mathbb Z_2\times\mathbb Z_3
\]
and six finite phase characters:
\[
a\in\{\pm1\},\qquad b\in\{1,\omega,\omega^2\}.
\]

This does not destroy the intended \(2\times3=6\) structure, but it changes the claim. The paper should say that the raw trefoil complement group has a continuous one-dimensional character family, while the closed finite phase sector selected by \(a^2=b^3=1\) has six characters. That is sharper and avoids an avoidable algebra error.

## 13. Heavy-sector \(\kappa\): Higgs prefers \(13/8\), Z mixing target is precise

The heavy-sector regime switch is more serious than the original audit gave it credit for. The additive zeta model has a coherent \(\pi^7\)-sector residual, and the multiplicative correction
\[
\frac{\delta m}{m_{\mathrm{bare}}}
=
\kappa\frac{\alpha}{2\pi}
\]
reduces the worst residual from roughly \(0.188\%\) to roughly \(0.00483\%\).

The extracted coefficients are:
\[
\kappa^\star_t=0.652012858,
\quad
\kappa^\star_W=1.295012119,
\quad
\kappa^\star_Z=1.203927825,
\quad
\kappa^\star_H=1.624995931.
\]

The Higgs coefficient is not merely "near \(5/3\)"; it is essentially
\[
\frac{13}{8}=1.625,
\]
with error
\[
4.07\times10^{-6}.
\]
The alternative \(5/3\) is much farther away:
\[
5/3-\kappa^\star_H\approx0.04167.
\]

For the Z coefficient, if
\[
\kappa_Z=\frac43-\lambda\sin^2\theta_W
\]
with \(\sin^2\theta_W=0.223044624\), the extracted target is
\[
\lambda=0.58017766\ldots.
\]
The simple fraction \(7/12=0.58333\ldots\) is a plausible small-denominator candidate, but it is not the closest rational once denominators above 12 are allowed. For example,
\[
11/19=0.57895\ldots,\qquad 18/31=0.58065\ldots
\]
are closer. The paper should present \(7/12\) only as a low-complexity candidate unless a structural reason for denominator 12 is supplied.

The revised heavy-sector target should be:
\[
\kappa_t\sim\frac23,\qquad
\kappa_W\sim\frac43,\qquad
\kappa_H\sim\frac{13}{8},\qquad
\kappa_Z=\frac43-\lambda\sin^2\theta_W,\quad \lambda\approx0.58017766.
\]

This keeps the regime-switch discovery visible while separating exact-looking structure from fitted structure.

## 14. Alpha residual search: no clean second coefficient yet

The exact scale ratio required to match CODATA is
\[
r_{\mathrm{exact}}=2.2577590146612003994\ldots,
\]
and the missing logarithmic correction beyond \(9/4\) is
\[
L=\log\frac{r_{\mathrm{exact}}}{9/4}
=0.0034425186877091865\ldots.
\]
The leading structural observation remains
\[
\frac{L}{\alpha^2}=64.6465938512\ldots,
\]
so \(64\alpha^2\) accounts for almost all of the missing log scale. The remaining coefficient is
\[
\frac{L-64\alpha^2}{\alpha^3}=88.6066344020\ldots.
\]

A small search against common constants \(\{1,\pi,1/\pi,\sqrt2,\sqrt8,\log2,\log3,\log(9/4)\}\) found rational approximants but no expression with an obvious structural denominator or coefficient. This should remain an active target, not a paper claim.

The disciplined statement is: the \(9/4\) one-loop scale gets alpha to \(2.67\) ppm; adding a self-consistent \(64\alpha^2\) log-scale correction gets it to about \(0.027\) ppm; the coefficient \(64=8^2\) is structurally suggestive because the trefoil has the same eight-channel count, but the next term is not yet derived.

## 15. DOF counting has a quotient-space target

The exponent \(w\) in \(c\pi^w\) should be treated as the dimension of a quotient configuration space. The current candidate rule is:
\[
\mathrm{raw}=4N
\]
for \(N\) constituent \(S^3\) carriers, followed by geometric constraints.

For baryons:
\[
(S^3)^3/G_{\mathrm{baryon}},
\]
with one center carrier removed and color/flavor closure removing \(d+1\), where \(d\) is the number of distinct flavors. This reproduces
\[
p(uud):12-4-(2+1)=5,
\]
\[
\Sigma^0(uds):12-4-(3+1)=4.
\]

For mesons:
\[
(S^3)^2/G_{\mathrm{meson}},
\]
with a self-conjugate meson such as \(J/\psi(c\bar c)\) losing one phase-lock constraint:
\[
8-1=7,
\]
and an asymmetric meson such as \(D^\pm(c\bar d)\) losing three spatial alignment constraints:
\[
8-3=5.
\]

The strong clue is the \(Z\):
\[
Z=6\pi^9,
\]
which shares the proton's trefoil prefactor \(6\) but has four extra powers of \(\pi\):
\[
9-5=4=\dim SU(2)+\dim U(1).
\]
This supports reading the exponent as integration depth: same topology, extra electroweak gauge coordinates.

The missing proof is now precise: define the groups \(G_{\mathrm{baryon}}\) and \(G_{\mathrm{meson}}\), then show that their quotient dimensions are the observed exponents.

---

# Round 4 Additions

## 16. Jones-polynomial transparency check survives

The revision note says the trefoil Jones polynomial
\[
V(t)=-t^{-4}+t^{-3}+t^{-1}
\]
has determinant \(3\) at \(t=-1\), and becomes transparent at the third root of unity. Direct evaluation confirms both statements:
\[
V(-1)=-3,\qquad |V(-1)|=3,
\]
and for
\[
\omega=e^{2\pi i/3},
\]
\[
V(\omega)=1
\]
up to numerical roundoff. The common mirror-convention variants
\[
t^{-1}+t^{-3}-t^{-4},
\qquad
t+t^3-t^4
\]
give the same two evaluations.

This means the "topological transparency" paragraph is safe in content: at the third root of unity, the trefoil evaluates to the identity. The paper should still be careful with the Chern-Simons level convention, but the polynomial statement itself checks.

## 17. \(S^4\) rationality uniqueness can be proved

The notes had said \(s=3\) is the unique purely rational evaluation of
\[
\zeta_{\mathrm{conf}}(s)
=
\frac16
\sum_{m=1}^{\infty}
\frac{2m+1}{[m(m+1)]^{s-1}}.
\]
The coefficient formula makes the proof accessible.

Let \(n=s-1\). The partial fractions have Catalan-triangle coefficients
\[
A_{n,j}
=
(-1)^{n-j}
\frac{j-1}{2n-j-1}
\binom{2n-j-1}{n-j},
\qquad j=2,\ldots,n.
\]
Even zeta values cancel. For \(n>2\), an odd zeta coefficient always survives:

- if \(n\) is odd, the highest term \(\zeta(n)\) survives with nonzero coefficient, because the \(1/m^n\) and \(1/(m+1)^n\) coefficients add rather than cancel;
- if \(n\) is even, the highest odd term is \(\zeta(n-1)\), and its coefficient is proportional to \(n-2\), so it is nonzero for every \(n>2\).

Therefore \(s=3\) (\(n=2\)) is the only integer evaluation where the zeta terms all disappear and the result is purely rational. This upgrades the rationality claim from a computed pattern to a proof outline. The remaining formal work is just to write the coefficient signs cleanly in the paper.

## 18. Heavy-sector correction becomes much cleaner with \(H=13/8\)

Using the corrected heavy-sector structure
\[
\kappa_t=\frac23,\qquad
\kappa_W=\frac43,\qquad
\kappa_H=\frac{13}{8},
\]
and writing
\[
\kappa_Z=\frac43-\lambda\sin^2\theta_W
\]
with the extracted \(\lambda=0.58017766\ldots\), the full spectrum benchmark becomes:
\[
\text{geometric mean absolute error}=0.000013850\%,
\]
\[
\text{max absolute error}=0.004443979\%.
\]
The max residual is then the W, not the Higgs or Z.

This is a large improvement over the earlier class-law note that used \(H=5/3\):
\[
0.000086\%\quad\longrightarrow\quad0.00001385\%
\]
in geometric mean error. The Higgs coefficient is effectively locked by
\[
\kappa^\star_H=1.624995931\approx\frac{13}{8}.
\]

If \(\lambda\) is restricted to simple rationals, the results remain strong:
\[
\lambda=7/12:\quad \text{geo}=0.00004114\%,\quad \text{max}=0.00444398\%,
\]
\[
\lambda=11/19:\quad \text{geo}=0.00003864\%,\quad \text{max}=0.00444398\%,
\]
\[
\lambda=18/31:\quad \text{geo}=0.00003623\%,\quad \text{max}=0.00444398\%.
\]
The max error remains W because the Z error is already below the W residual for all three choices.

The clean statement is: the \(\pi^7\) heavy sector wants multiplicative one-loop correction, Higgs wants \(13/8\), and Z wants electroweak mixing. The exact structural origin of the Z mixing coefficient remains open.

## 19. The alpha scale ratio \(9/4\) has a simple projection derivation

The May 22 source file contains the missing bridge for the running scale ratio:
\[
\cos\sigma_{\mathrm{bare}}=\frac23.
\]
The value \(2/3\) is the up-quark charge coordinate. If the energy scale associated with a projected \(S^3\) component is the inverse projection length, then
\[
\frac{Q}{\mu}=\sec\sigma_{\mathrm{bare}}
=
\frac{1}{\cos\sigma_{\mathrm{bare}}}
=
\frac32.
\]
The QED one-loop running uses the squared scale ratio:
\[
\frac{Q^2}{\mu^2}
=
\sec^2\sigma_{\mathrm{bare}}
=
\left(\frac32\right)^2
=
\frac94.
\]
So the correction
\[
\alpha_{\mathrm{phys}}^{-1}
=
\frac{9\pi^5}{e^3}
-
\frac{1}{3\pi}\log\frac94
\]
can be read as bare geometric coupling at the \(W=2/3\) projection scale, run down one QED loop to the electron scale.

This is stronger than merely identifying \(9/4\) with \((n/2)^2\). The dimension expression and the charge/projection expression coincide:
\[
\left(\frac{n}{2}\right)^2
=
\left(\frac{3}{2}\right)^2
=
\sec^2(\arccos(2/3)).
\]
The remaining precision problem is not the origin of \(9/4\); it is the \(2.67\) ppm residual after that one-loop correction.

## 20. The trefoil \(8\)-channel count is safe; one alternate formula is trefoil-specific

The electromagnetic proton correction uses
\[
\exp\!\left(\frac{\alpha^2}{\sqrt8}\right),
\]
and the May 22 source identifies
\[
8=p(p-1)+q(q-1)
\]
for the trefoil \(T(2,3)\):
\[
2(1)+3(2)=8.
\]
This is a good winding-pair count: it is twice the number of unordered self-pairs in each winding family,
\[
2\binom{p}{2}+2\binom{q}{2}
=p(p-1)+q(q-1).
\]

The source also says equivalently
\[
8=2(\text{minimal crossings})+2(\text{genus})
\]
for the trefoil. This is true for \(T(2,3)\), since the crossing number is \(3\) and genus is \(1\). It should not be stated as generally equivalent for all \(T(p,q)\). For \(p<q\),
\[
2c+2g
=
2q(p-1)+(p-1)(q-1)
=
(p-1)(3q-1),
\]
while
\[
p(p-1)+q(q-1)
\]
is a different expression in general.

The safe general prediction is therefore the winding-pair formula
\[
\exp\!\left(
\frac{\alpha^2}{\sqrt{p(p-1)+q(q-1)}}
\right),
\]
while the crossings-plus-genus wording should be restricted to the trefoil or removed.

## 21. Status labels from the May 22 source need revision

The original `session_may22_results.md` is valuable, but several status labels should be changed before integration.

\[
\begin{array}{l|l|l}
\text{claim} & \text{source status} & \text{revised status}\\
\hline
\alpha\text{ running} & \text{derived/verified} & \text{strong; }9/4\text{ now has projection derivation}\\
\mathrm{DOF}\text{ for non-proton particles} & \text{derived/closed} & \text{identified; quotient proof still needed}\\
\Delta(\mathrm{DOF})\text{ in multi-term particles} & \text{pattern identified} & \text{same}\\
\Lambda\sim(t_P/t_0)^2 & \text{order explained} & \text{same; }3\pi/5\text{ prefactor target found}\\
\zeta(5)/30\text{ proton correction} & \text{verified} & \text{strongest proton formula}\\
\exp(\alpha^2/\sqrt8)\text{ proton correction} & \text{verified} & \text{appendix/bridge; less precise than zeta}\\
8\text{ channel count} & \text{derived} & \text{safe via winding pairs; alternate crossing/genus expression is trefoil-specific}\\
\text{trefoil uniqueness} & \text{exhaustive search/proven} & \text{theorem-level proof available}\\
\sigma\text{ particle thresholds} & \text{computed} & \text{diagnostic/visualization}\\
\text{prefactor decomposition} & \text{4/5 decomposed} & \text{useful table; trefoil rep claim needs finite-closure qualifier}\\
\kappa\text{ heavy sector} & \text{identified} & \text{stronger with }H=13/8\text{; still derivation target}
\end{array}
\]

The most important changes are:

1. DOF should not be called closed until the quotient groups are written.
2. Trefoil uniqueness and dimension-three calibration should be upgraded to theorem-level.
3. The finite \(2\times3\) trefoil phase sector should replace the incorrect "all one-dimensional irreps" wording.
4. The alpha \(9/4\) scale is no longer merely an identified ratio; it follows from the \(W=2/3\) projection if energy scales by inverse projected length.
5. The heavy-sector \(\kappa\) section should use \(13/8\) for Higgs, not \(5/3\).

## 22. \(S^3\) carrier geometry and \(S^4\) harmonic geometry should be separated

The geometric calculus machinery lives on \(S^3\): a physical state is a carrier
\[
q=[W,\vec v]\in S^3,
\]
composition is the Hamilton product, and the local observable is the distance from identity
\[
\sigma(q)=\arccos |W|.
\]
This is the particle-side language of the framework: localized carriers, stable topological defects, Hopf-linked fibers, knots, and projections.

The \(S^4\) result uses a different vocabulary.  The conformal scalar zeta function
\[
\zeta_{\mathrm{conf}}(s)
=
\frac16
\sum_{m=1}^{\infty}
\frac{2m+1}{[m(m+1)]^{s-1}}
\]
is a harmonic trace: \(m(m+1)\) is Casimir/angular-momentum language, and \(2m+1\) is the degeneracy of the \(m\)-th harmonic shell.  The May 22 result therefore looks like a bulk wave-spectrum statement, while the trefoil result looks like a boundary/topological carrier statement.

The proton is currently the cleanest place where the two languages meet:
\[
\zeta_{\mathrm{conf},S^4}(3)=\frac16,
\qquad
\mathrm{cs}_{S^3}(T(2,3))=\frac16.
\]
The same invariant appears from a harmonic \(S^4\) trace and from an \(S^3\) trefoil carrier.  This suggests the working split:
\[
S^3:\ \text{carrier / particle / topological projection},
\]
\[
S^4:\ \text{harmonic bulk / wave spectrum / mode completion}.
\]
The core calculus is already well-defined on \(S^3\), because derivative, integral, chain rule, and projection are native to the carrier manifold.  The particle-physics extension needs the \(S^4\) harmonic layer once it explains why the proton trefoil value appears spectrally as well as topologically.

## 23. The \(1/6\) result exposes the \(60^\circ\) stability mode

The geometric calculus paper already distinguishes the base-2 and base-3 slicings of the unit circle:
\[
\text{base }2:\quad 180^\circ/2=90^\circ,
\]
\[
\text{base }3:\quad 180^\circ/3=60^\circ.
\]
The \(90^\circ\) mode is the orthogonal/computational mode: binary distinction, square geometry, right-angle axes, and the \(i^2=-1\) operation.  The \(60^\circ\) mode is the triangular/hexagonal mode: six sectors close a circle,
\[
6\cdot60^\circ=360^\circ,
\]
and equal-neighbor packing becomes stable through triangular lattices, honeycombs, and hexagonal closure.

The May 22 discoveries keep returning the same sixfold quantity:
\[
R_{S^3}=3(3-1)=3\cdot2=6,
\]
\[
\frac{1}{\mathrm{cs}(T(2,3))}=6,
\]
\[
\zeta_{\mathrm{conf},S^4}(3)=\frac16.
\]
The factor \(3\cdot2\) should be read geometrically.  A unit \(S^3\) has three spatial directions, and each direction has two transverse oriented couplings; equivalently, the three coordinate planes carry two orientations each.  This gives six oriented curvature channels, the same count as the six \(60^\circ\) sectors of the hexagonal circle and the same inverse cost as the trefoil.

This is probably the missing mode behind the \(1/6\): the calculus derives the right-angle \(90^\circ\) operation for computation, while the particle/topology results point to the \(60^\circ\) harmonic stability sector.  The square mode gives clean distinction; the hexagonal mode gives stable resonance.

## 24. Spectral telescoping is shell cancellation

At \(s=3\), the summand is
\[
\frac{2m+1}{m^2(m+1)^2}
=
\frac1{m^2}-\frac1{(m+1)^2}.
\]
The numerator has a simple shell meaning:
\[
(m+1)^2-m^2=2m+1.
\]
So the rational \(1/6\) value is adjacent harmonic shells canceling through their boundary difference, leaving one rational closure residue after the full tower collapses.  In this vocabulary, \(s=3\) is the spectral closure point: the wave tower reduces to the same invariant carried by the trefoil topology.

For \(s>3\), the Catalan-triangle coefficients and odd zeta residues show that higher corrections retain recursive-composition structure instead of collapsing completely.  The proton correction
\[
\frac{\zeta(5)}{30}
\]
should therefore be treated as the first non-rational harmonic correction to the trefoil closure, with the remaining open step being the projection factor
\[
\frac{1}{10}=\frac{1}{2\cdot5}.
\]

## 25. Two angular diagnostics must be kept distinct

There are now two different angular patterns to track:

1. The near-\(90^\circ\) particle/coupling observation, where stable particles may sit close to the high-coupling perpendicular regime.
2. The \(60^\circ\) hexagonal/harmonic stability mode indicated by the \(1/6\) spectral and trefoil results.

Keep these as separate diagnostics.  The \(90^\circ\) sector belongs to perpendicular coupling and maximal cross-product generation; the \(60^\circ\) sector belongs to stable closure, packing, and sixfold resonance.  A useful next computation is therefore a particle-angle table with at least three columns:
\[
\text{particle},\qquad \sigma\text{ or carrier angle},\qquad \text{nearest landmark }(60^\circ,90^\circ,120^\circ,\ldots).
\]
If the particle carriers cluster near \(90^\circ\), that supports the perpendicular-coupling story.  If their topology or spectrum returns sixfold invariants, that supports the hexagonal harmonic story.  Both can be true, but they are different facts.

## 26. Updated open derivations after the harmonic split

The new structure changes the next targets:

1. Write the \(S^3/S^4\) bridge precisely: \(S^3\) as carrier/topological projection, \(S^4\) as harmonic bulk/wave spectrum.
2. Derive why the conformal \(S^4\) shell trace lands on the \(S^3\) trefoil CS invariant at \(s=3\), rather than only recording the numerical equality.
3. Formalize the sixfold mode: show whether \(3\cdot2=6\), six oriented curvature channels, \(60^\circ\) hexagonal closure, and inverse trefoil CS are the same structure in four descriptions.
4. Compute the particle-angle diagnostics so the near-\(90^\circ\) claim becomes a table rather than an impression.
5. Derive the \(1/(2\cdot5)\) normalization from \(S^4\) harmonic correction to the proton \(\zeta(5)/30\) term.
