# AIM — 200 Open Applied Problems

A sourced collection of **200 precise mathematical research problems** in spectral theory, operator theory, applied mathematics, and related fields. Each problem has a self-contained statement, an applied motivation, brief references, and a dated literature-status review. The problem pages do not attempt solutions.

**Expanded collection:** Problems **101–200** add 100 questions drawn from books, surveys, and specific research papers. They broaden the existing subjects into wave propagation, quantum systems, control, continuum mechanics, spatial ecology, stochastic transport, and statistical mechanics. The additional 100 contain no numerical linear algebra (NLA) problems. The original 001–100 are retained.

**Status checked: 8 September 2026.** The entries are open in the cited literature, and targeted searches did not locate later resolutions of their exact statements. This is a documented literature check, not a guarantee that no proof exists. Restrictions and relevant partial results are explained on each page.

Read the [research methodology](research/METHODOLOGY.md) and [contribution guide](CONTRIBUTING.md). The [source maps and exclusion records](research/README.md) identify the books and paper sections used, and explain why some older open problems are absent. Machine-readable index metadata lives in [data/](data/).

The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may have mathematical implications for one another; the count does not assert logical independence.

| Subject group | Problems |
| --- | ---: |
| [Spectral theory and spectral geometry](#spectral-theory-and-spectral-geometry) | 001–025 |
| [Operators, matrices and computation](#operators-matrices-and-computation) | 026–050 |
| [Inverse problems, control and dynamics](#inverse-problems-control-and-dynamics) | 051–075 |
| [PDEs, materials, probability and optimization](#pdes-materials-probability-and-optimization) | 076–100 |
| [Waves, quantum systems and spectral geometry](#waves-quantum-systems-and-spectral-geometry) | 101–125 |
| [Imaging, control, geometry and dynamics](#imaging-control-geometry-and-dynamics) | 126–150 |
| [Fluids, kinetic theory and continuum mechanics](#fluids-kinetic-theory-and-continuum-mechanics) | 151–175 |
| [Stochastic growth, populations and statistical mechanics](#stochastic-growth-populations-and-statistical-mechanics) | 176–200 |

## Spectral theory and spectral geometry

| ID | Problem | Area |
| --- | --- | --- |
| 001 | [Pólya's eigenvalue inequalities](problems/001-polya-eigenvalue-bound.md) | Spectral geometry |
| 002 | [Ivrii's measure-zero conjecture for billiards](problems/002-ivrii-periodic-billiards.md) | Spectral asymptotics and ray dynamics |
| 003 | [Hot spots on convex planar domains](problems/003-planar-convex-hot-spots.md) | Heat flow and Neumann eigenfunctions |
| 004 | [Pólya–Szegő polygonal Faber–Krahn conjecture](problems/004-polygonal-faber-krahn.md) | Spectral shape optimization |
| 005 | [Does the disk minimize the third Dirichlet eigenvalue?](problems/005-third-dirichlet-disk.md) | Spectral shape optimization |
| 006 | [Rayleigh's clamped-plate conjecture in higher dimensions](problems/006-rayleigh-clamped-plate.md) | Elasticity and fourth-order spectra |
| 007 | [Pólya–Szegő conjecture for the first buckling load](problems/007-buckling-load-ball.md) | Elastic stability |
| 008 | [The sharp ratio of the first two buckling eigenvalues](problems/008-buckling-eigenvalue-ratio.md) | Elastic stability and eigenvalue inequalities |
| 009 | [The spectral honeycomb conjecture](problems/009-spectral-honeycomb.md) | Spectral partitions |
| 010 | [The Mercedes-star partition of a disk](problems/010-mercedes-disk-partition.md) | Spectral partitions |
| 011 | [Yau's sharp upper bound for nodal volume](problems/011-yau-nodal-upper-bound.md) | Eigenfunction geometry |
| 012 | [The sharp planar Pleijel constant](problems/012-sharp-pleijel-constant.md) | Nodal domains and spectral complexity |
| 013 | [Quantum unique ergodicity in negative curvature](problems/013-quantum-unique-ergodicity.md) | Quantum chaos |
| 014 | [Berry's random-wave conjecture as a local limit](problems/014-berry-random-waves.md) | Quantum chaos and random waves |
| 015 | [Extended states in the three-dimensional Anderson model](problems/015-anderson-extended-states.md) | Disordered quantum transport |
| 016 | [Localization at every disorder strength in two dimensions](problems/016-anderson-planar-localization.md) | Disordered quantum transport |
| 017 | [A fractal Weyl lower bound for obstacle resonances](problems/017-fractal-weyl-resonances.md) | Scattering and open wave systems |
| 018 | [The three-dimensional Lieb–Thirring constant](problems/018-lieb-thirring-three-dimensional.md) | Quantum mechanics and spectral inequalities |
| 019 | [The Benguria–Loss ovals conjecture](problems/019-ovals-conjecture.md) | Geometric Schrödinger operators |
| 020 | [The polygonal Payne–Pólya–Weinberger ratio conjecture](problems/020-polygonal-ppw.md) | Spectral shape optimization |
| 021 | [Bareket's conjecture for simply connected planar domains](problems/021-bareket-simply-connected.md) | Robin spectra and surface interactions |
| 022 | [The Robin fundamental gap conjecture](problems/022-robin-fundamental-gap.md) | Diffusion and elastically supported membranes |
| 023 | [The Robin eigenvalue ratio at fixed volume](problems/023-robin-ppw.md) | Robin spectra and resonator design |
| 024 | [The regular-polygon Steklov conjecture](problems/024-steklov-polygon-optimizer.md) | Boundary spectral optimization |
| 025 | [Exponential interior decay for smooth Steklov domains](problems/025-steklov-smooth-interior-decay.md) | Boundary waves and harmonic extension |

## Operators, matrices and computation

| ID | Problem | Area |
| --- | --- | --- |
| 026 | [The complete Crouzeix conjecture](problems/026-complete-crouzeix.md) | Operator theory and numerical linear algebra |
| 027 | [Lieb’s permanental dominance conjecture](problems/027-lieb-permanental-dominance.md) | Matrix analysis and quantum information |
| 028 | [Chollet’s Hadamard-product permanent inequality](problems/028-chollet-permanent.md) | Matrix analysis and bosonic computation |
| 029 | [Hadamard matrices in every admissible order](problems/029-hadamard-all-orders.md) | Matrix design, coding and experimental design |
| 030 | [The exact real Grothendieck constant](problems/030-real-grothendieck-constant.md) | Operator norms and semidefinite optimization |
| 031 | [Komlós’s vector-balancing conjecture](problems/031-komlos.md) | Discrepancy and matrix rounding |
| 032 | [The Beck–Fiala discrepancy conjecture](problems/032-beck-fiala.md) | Sparse constraint rounding |
| 033 | [Is the matrix-multiplication exponent two?](problems/033-matrix-multiplication-exponent.md) | Numerical linear algebra and algebraic complexity |
| 034 | [Explicit matrices with Valiant-scale rigidity](problems/034-explicit-rigid-matrices.md) | Matrix computation and complexity lower bounds |
| 035 | [SIC measurements in every finite dimension](problems/035-sic-povms.md) | Quantum measurement and frame theory |
| 036 | [The maximum number of mutually unbiased bases in dimension six](problems/036-mub-dimension-six.md) | Quantum information and matrix design |
| 037 | [Existence of NPT bound entanglement](problems/037-npt-bound-entanglement.md) | Quantum information and positive operators |
| 038 | [Exact quantum capacity of the qubit depolarizing channel](problems/038-depolarizing-quantum-capacity.md) | Quantum communication and operator optimization |
| 039 | [Uniform spatial stability of von Neumann algebras](problems/039-kadison-kastler.md) | Operator perturbation theory |
| 040 | [Are the standard quantum entropy inequalities complete?](problems/040-quantum-entropy-cone.md) | Quantum information and convex optimization |
| 041 | [Arveson–Douglas essential normality for homogeneous ideals](problems/041-arveson-douglas.md) | Multivariable operator theory |
| 042 | [Kadison’s similarity problem](problems/042-kadison-similarity.md) | Operator representations and stability |
| 043 | [Dixmier’s unitarizability problem for countable groups](problems/043-dixmier-unitarizability.md) | Group representations and operator theory |
| 044 | [Deterministic sensing matrices with optimal RIP measurement count](problems/044-deterministic-rip.md) | Compressed sensing and matrix construction |
| 045 | [Uniformly effective algebraic multigrid for diagonally dominant systems](problems/045-universal-algebraic-multigrid.md) | Numerical PDE solvers and preconditioning |
| 046 | [Deterministic pseudospectral shattering in nearly cubic time](problems/046-deterministic-pseudospectral-shattering.md) | Eigenvalue computation and nonnormal operators |
| 047 | [Accurate selected bidiagonal singular vectors in O(kn) work](problems/047-accurate-bidiagonal-svd.md) | Numerical linear algebra and low-rank approximation |
| 048 | [A nearly cubic Schur algorithm using only linear precision](problems/048-linear-precision-schur.md) | Stable algorithms for general eigenproblems |
| 049 | [Quadratic-scale bit complexity for well-conditioned sparse systems](problems/049-sparse-linear-solve-bit-complexity.md) | Sparse numerical linear algebra |
| 050 | [Improve the worst-case tensor-train approximation factor](problems/050-tensor-train-approximation.md) | Tensor computation and high-dimensional models |

## Inverse problems, control and dynamics

| ID | Problem | Area |
| --- | --- | --- |
| 051 | [Calderón uniqueness for bounded measurable conductivities](problems/051-rough-conductivity-calderon.md) | Inverse problems / electrical impedance tomography |
| 052 | [Smooth anisotropic Calderón uniqueness](problems/052-smooth-anisotropic-calderon.md) | Inverse problems / anisotropic imaging |
| 053 | [Calderón uniqueness from an arbitrary local boundary patch](problems/053-arbitrary-local-calderon-data.md) | Inverse problems / partial boundary data |
| 054 | [Global conductivity uniqueness for the p-Laplacian in higher dimensions](problems/054-nonlinear-p-calderon.md) | Nonlinear inverse problems / electrical materials |
| 055 | [Recover both Lamé moduli from static boundary measurements](problems/055-static-lame-uniqueness.md) | Inverse elasticity / nondestructive testing |
| 056 | [Recover a potential on a general known Riemannian manifold](problems/056-potential-on-general-manifold.md) | Inverse boundary problems / anisotropic wave media |
| 057 | [Global uniqueness from inverse backscattering data](problems/057-inverse-backscattering.md) | Inverse scattering / monostatic imaging |
| 058 | [Recover an arbitrary sound speed from one incident direction](problems/058-fixed-angle-sound-speed.md) | Inverse scattering / acoustic tomography |
| 059 | [Determine a smooth sound-soft obstacle from one far-field pattern](problems/059-single-wave-obstacle.md) | Inverse obstacle scattering / acoustic detection |
| 060 | [Boundary rigidity of simple manifolds in dimensions at least three](problems/060-simple-boundary-rigidity.md) | Travel-time tomography / geometric inverse problems |
| 061 | [Solenoidal injectivity of the geodesic ray transform on 2-tensors](problems/061-tensor-ray-injectivity.md) | Tensor tomography / linearized travel-time imaging |
| 062 | [Marked length rigidity in negative curvature](problems/062-marked-length-rigidity.md) | Geometric inverse problems / periodic ray dynamics |
| 063 | [Classify noninjectivity sets of spherical mean tomography](problems/063-spherical-mean-noninjectivity-sets.md) | Integral geometry / thermoacoustic imaging |
| 064 | [Simultaneously recover sound speed and initial pressure](problems/064-photoacoustic-joint-recovery.md) | Photoacoustic tomography / inverse wave problems |
| 065 | [Broken-ray tomography with two smooth convex obstacles](problems/065-two-obstacle-broken-rays.md) | Reflection tomography / integral geometry |
| 066 | [Invertibility of the Pestov–Uhlmann reconstruction operator](problems/066-pestov-uhlmann-fredholm-invertibility.md) | Integral geometry and computational tomography |
| 067 | [Injectivity with attenuation of finite angular degree](problems/067-finite-angular-attenuation.md) | Attenuated tomography |
| 068 | [Characterizing realizable geodesic scattering data](problems/068-range-of-geodesic-scattering.md) | Geometric inverse problems and data consistency |
| 069 | [Global Birkhoff billiard integrability conjecture](problems/069-birkhoff-billiard-integrability.md) | Hamiltonian dynamics and ray optics |
| 070 | [Positive metric entropy for a standard map](problems/070-standard-map-metric-entropy.md) | Hamiltonian chaos and transport |
| 071 | [Small-time global control of a slightly superlinear heat equation](problems/071-small-time-superlinear-heat-control.md) | Nonlinear PDE control |
| 072 | [Exact uniform control time near a viscous Burgers shock](problems/072-burgers-shock-uniform-control-time.md) | Singular limits and control |
| 073 | [Unique continuation for the higher-dimensional p-Laplace equation](problems/073-p-harmonic-unique-continuation.md) | Nonlinear potential theory and inverse problems |
| 074 | [A strictly convex function on every simple manifold](problems/074-convex-function-on-simple-manifold.md) | Geometric tomography |
| 075 | [Non-Abelian ray transform for simple Gaussian thermostats](problems/075-thermostatic-nonabelian-tomography.md) | Matrix-valued transport tomography |

## PDEs, materials, probability and optimization

| ID | Problem | Area |
| --- | --- | --- |
| 076 | [Global regularity of the three-dimensional Navier–Stokes equations](problems/076-navier-stokes-global-regularity.md) | Fluid dynamics |
| 077 | [Finite-time singularity for smooth three-dimensional Euler flow without a boundary](problems/077-euler-smooth-free-space.md) | Fluid dynamics |
| 078 | [Global regularity for supercritical dissipative surface quasi-geostrophic flow](problems/078-supercritical-sqg.md) | Geophysical fluid dynamics |
| 079 | [Large-data global classical solutions of relativistic Vlasov–Maxwell](problems/079-vlasov-maxwell-global-classical.md) | Kinetic theory and plasma physics |
| 080 | [Large-data global smoothness for the spatially inhomogeneous Boltzmann equation](problems/080-inhomogeneous-boltzmann-regularity.md) | Kinetic theory |
| 081 | [The no-slip inviscid limit in two dimensions](problems/081-no-slip-inviscid-limit.md) | Fluid dynamics and boundary layers |
| 082 | [Bressan's logarithmic lower bound on the cost of mixing](problems/082-bressan-mixing-cost.md) | Transport and mixing |
| 083 | [Global smoothness for the real scalar defocusing septic wave equation](problems/083-scalar-supercritical-wave.md) | Nonlinear waves |
| 084 | [Soliton resolution for bounded nonradial energy-critical waves](problems/084-nonradial-soliton-resolution.md) | Nonlinear waves |
| 085 | [Global regularity of two-dimensional ideal incompressible MHD](problems/085-ideal-mhd-two-dimensions.md) | Magnetohydrodynamics |
| 086 | [Large-data global regularity for creeping-flow Oldroyd–B without stress diffusion](problems/086-non-diffusive-oldroyd-b.md) | Viscoelasticity |
| 087 | [Preservation of strict positivity for the cubic thin-film equation](problems/087-thin-film-positivity.md) | Thin films and lubrication |
| 088 | [Smooth unforced inviscid Boussinesq evolution on the whole plane](problems/088-inviscid-boussinesq-plane.md) | Geophysical fluid dynamics |
| 089 | [The bulk ground-state energy of the planar Lennard–Jones system](problems/089-lennard-jones-planar-crystallization.md) | Atomistic materials |
| 090 | [The three-dimensional lattice-periodic Kelvin problem](problems/090-kelvin-lattice-foam.md) | Foams and geometric optimization |
| 091 | [The optimal three-dimensional quadratic quantization constant](problems/091-bcc-quantization.md) | Quantization and mesh generation |
| 092 | [The symmetric Mahler inequality in four dimensions](problems/092-mahler-symmetric-four-dimensions.md) | Convex geometry and optimization |
| 093 | [Gaussian-energy optimality of the triangular lattice among periodic configurations](problems/093-triangular-universal-optimality.md) | Crystallization and energy minimization |
| 094 | [Absence of an infinite cluster at criticality in three-dimensional percolation](problems/094-critical-percolation-three-dimensions.md) | Random media |
| 095 | [The planar Mumford–Shah regularity conjecture](problems/095-mumford-shah-planar-cracks.md) | Image segmentation and fracture |
| 096 | [One-dimensionality of monotone Allen–Cahn fronts in dimension five](problems/096-de-giorgi-dimension-five.md) | Phase transitions |
| 097 | [Cardy's crossing formula for square-lattice bond percolation](problems/097-square-bond-cardy-formula.md) | Random media and conformal invariance |
| 098 | [The planar self-avoiding-walk displacement exponent](problems/098-planar-self-avoiding-walk-exponent.md) | Polymer models |
| 099 | [The dimension-free Kannan–Lovász–Simonovits inequality](problems/099-kls-poincare.md) | High-dimensional probability and sampling |
| 100 | [A strongly polynomial pivot rule for the simplex method](problems/100-strongly-polynomial-simplex.md) | Numerical optimization |

## Waves, quantum systems and spectral geometry

| ID | Problem | Area |
| --- | --- | --- |
| 101 | [Absolute continuity for smooth periodic scalar elliptic operators](problems/101-periodic-elliptic-absolute-continuity.md) | Periodic media and spectral theory |
| 102 | [Irreducibility of complex Fermi varieties](problems/102-complex-fermi-irreducibility.md) | Periodic quantum Hamiltonians |
| 103 | [Sunada’s no-gap conjecture for abelian covers](problems/103-sunada-no-gap-cover.md) | Wave spectra on periodic curved spaces |
| 104 | [Simon’s multidimensional weighted square-integrability conjecture](problems/104-simon-weighted-l2.md) | Quantum scattering and transport |
| 105 | [A universal bound on excess molecular charge](problems/105-maximal-molecular-ionization.md) | Many-electron quantum mechanics |
| 106 | [Uniform boundedness of the first atomic ionization energy](problems/106-uniform-first-ionization.md) | Atomic spectroscopy |
| 107 | [Convexity of atomic ground-state energy in electron number](problems/107-atomic-energy-convexity.md) | Quantum chemistry and density functional theory |
| 108 | [Concentration of nuclear charge minimizes the Dirac gap level](problems/108-dirac-charge-concentration.md) | Relativistic quantum chemistry |
| 109 | [Faber–Krahn inequality for graphene quantum dots](problems/109-quantum-dot-dirac-faber-krahn.md) | Dirac spectral geometry |
| 110 | [The disk maximizes the first magnetic Neumann eigenvalue](problems/110-magnetic-neumann-disk.md) | Magnetic spectral optimization |
| 111 | [Strict angle monotonicity of magnetic wedge ground energy](problems/111-magnetic-wedge-angle-monotonicity.md) | Corner superconductivity |
| 112 | [Baur’s high-field disk conjecture for all higher eigenvalues](problems/112-baur-high-field-disk.md) | Magnetic confinement and shape design |
| 113 | [Is the optimal magnetic rectangle always a square?](problems/113-optimal-magnetic-rectangle.md) | Magnetic quantum wells |
| 114 | [A sharp universal inequality for clamped-plate eigenvalues](problems/114-clamped-plate-universal-bound.md) | Elastic vibration |
| 115 | [Uniqueness of the critical catenoid](problems/115-critical-catenoid-uniqueness.md) | Capillary surfaces and spectral geometry |
| 116 | [The first Steklov eigenvalue of a free-boundary minimal hypersurface](problems/116-free-boundary-first-steklov.md) | Capillary geometry and boundary vibrations |
| 117 | [Linear growth of interior Steklov nodal volume](problems/117-steklov-bulk-nodal-volume.md) | Boundary-driven wave patterns |
| 118 | [Unbounded first Steklov multiplicity with fixed boundary count](problems/118-steklov-fixed-boundary-multiplicity.md) | Boundary-mode degeneracy |
| 119 | [Arbitrarily large Steklov frequency with a prescribed embedded boundary](problems/119-fixed-embedded-boundary-steklov.md) | Geometric design of boundary-loaded media |
| 120 | [Anderson localization for the cosine skew-shift model at every coupling](problems/120-skew-shift-localization.md) | Deterministic quantum disorder |
| 121 | [A universal central limit law for quantum-graph nodal surplus](problems/121-quantum-graph-nodal-clt.md) | Wave networks and quantum chaos |
| 122 | [Jakobson–Naud’s essential spectral-gap conjecture](problems/122-jakobson-naud-essential-gap.md) | Open chaotic scattering |
| 123 | [Full-order resonance growth for every nonzero real compact potential](problems/123-full-order-potential-resonances.md) | Wave scattering by a localized medium |
| 124 | [Boundary contact of the second nodal set in convex domains](problems/124-convex-higher-dimensional-payne.md) | Vibration interfaces and geometry |
| 125 | [Subpolynomial compact-set peaks of Hecke–Maass waves](problems/125-sarnak-compact-supnorm.md) | Arithmetic quantum chaos |

## Imaging, control, geometry and dynamics

| ID | Problem | Area |
| --- | --- | --- |
| 126 | [Local scalar geodesic tomography on smooth surfaces](problems/126-local-ray-injectivity-surfaces.md) | Geometric inverse problems / local tomography |
| 127 | [Lens rigidity for nontrapping surfaces with conjugate points](problems/127-nontrapping-surface-lens-rigidity.md) | Geometric inverse problems / travel-time imaging |
| 128 | [Minimal filling volume of a simple manifold](problems/128-simple-manifold-minimal-filling.md) | Geometric analysis / travel-time bounds |
| 129 | [Exact minimum length of an opaque barrier for a square](problems/129-shortest-opaque-square-barrier.md) | Geometric optimization / sensing |
| 130 | [Sard conjecture for smooth bracket-generating distributions](problems/130-sard-conjecture-endpoint-map.md) | Nonholonomic control / sub-Riemannian geometry |
| 131 | [Continuous velocity of every sub-Riemannian length minimizer](problems/131-c1-subriemannian-minimizers.md) | Nonholonomic optimal control / regularity |
| 132 | [Nonbranching of analytic equiregular sub-Riemannian geodesics](problems/132-equiregular-analytic-nonbranching.md) | Nonholonomic geometry / optimal transport |
| 133 | [Pansu's isoperimetric conjecture in the Heisenberg group](problems/133-pansu-heisenberg-isoperimetry.md) | Sub-Riemannian geometric optimization |
| 134 | [Euclidean isoperimetry in higher-dimensional Cartan–Hadamard manifolds](problems/134-cartan-hadamard-isoperimetry.md) | Geometric analysis / volume and boundary optimization |
| 135 | [An SRB measure for the classical Hénon parameters](problems/135-classical-henon-srb-measure.md) | Dissipative dynamics / chaotic statistics |
| 136 | [Saari's constant-inertia conjecture for planar gravitation](problems/136-saari-constant-inertia.md) | Celestial mechanics / rigid gravitational motions |
| 137 | [Finiteness of planar central configurations for fixed masses](problems/137-finite-planar-central-configurations.md) | Celestial mechanics / relative equilibria |
| 138 | [Almost-everywhere global existence for Newtonian gravitation](problems/138-almost-sure-global-newtonian-motion.md) | Celestial mechanics / singular dynamics |
| 139 | [Exactly n or infinitely many periodic orbits on a convex energy surface](problems/139-convex-hamiltonian-n-or-infinity.md) | Hamiltonian mechanics / periodic motions |
| 140 | [Irrational ellipticity when a convex energy surface has finitely many orbits](problems/140-finite-convex-orbits-irrational-ellipticity.md) | Hamiltonian mechanics / orbital stability |
| 141 | [Exact optimal control in the scalar Witsenhausen benchmark](problems/141-witsenhausen-exact-optimum.md) | Decentralized stochastic control |
| 142 | [Symmetric capacity of the binary multiplying two-way channel](problems/142-binary-multiplying-two-way-capacity.md) | Interactive communication / information theory |
| 143 | [Capacity of the Gaussian relay channel with independent receiver noises](problems/143-gaussian-relay-capacity.md) | Network information theory / cooperative communication |
| 144 | [Exact capacity of the binary deletion channel](problems/144-binary-deletion-channel-capacity.md) | Information theory / synchronization errors |
| 145 | [Uniqueness of nonnegative heat controls at the minimum time](problems/145-unique-minimum-time-positive-heat-control.md) | Constrained PDE control / thermal processes |
| 146 | [Sharp characterization of exactly trackable boundary heat fluxes](problems/146-sharp-heat-tracking-range.md) | PDE control / thermal flux tracking |
| 147 | [Global null control of a heat equation with cubic growth](problems/147-global-cubic-heat-null-control.md) | Nonlinear PDE control / reaction-diffusion |
| 148 | [Finite-jet determination of small-time local controllability](problems/148-finite-jet-small-time-control.md) | Nonlinear control / local system identification |
| 149 | [An irrational polygon with nonergodic billiard flow](problems/149-irrational-nonergodic-polygon.md) | Billiard dynamics / transport and ergodicity |
| 150 | [Positive metric entropy for billiards arbitrarily close to an ellipse](problems/150-positive-entropy-billiards-near-ellipse.md) | Hamiltonian billiards / chaotic ray transport |

## Fluids, kinetic theory and continuum mechanics

| ID | Problem | Area |
| --- | --- | --- |
| 151 | [Energy conservation at the exact Onsager Hölder exponent](problems/151-onsager-endpoint.md) | Fluid mechanics and turbulence |
| 152 | [Surjectivity of the two-dimensional Euler endpoint map](problems/152-euler-endpoint-map.md) | Geometric hydrodynamics |
| 153 | [A closed Lagrangian Euler trajectory on a surface of higher genus](problems/153-closed-euler-geodesic.md) | Geometric hydrodynamics |
| 154 | [An inertial manifold for the two-dimensional Navier–Stokes flow](problems/154-navier-stokes-inertial-manifold.md) | Fluid mechanics and reduced models |
| 155 | [The unregularized Coulomb mean-field limit](problems/155-uncut-coulomb-mean-field.md) | Kinetic theory and plasma physics |
| 156 | [Tagged-particle thermalization with an interacting background](problems/156-lenard-balescu-thermalization.md) | Kinetic theory and plasma relaxation |
| 157 | [The nonlinear Landau limit of weakly interacting particles](problems/157-newton-landau-weak-coupling.md) | Kinetic theory and collisional relaxation |
| 158 | [The finite-Dirichlet Liouville problem for steady three-dimensional flow](problems/158-steady-navier-stokes-liouville.md) | Viscous fluid mechanics |
| 159 | [Steady planar flow around an obstacle at arbitrary Reynolds number](problems/159-exterior-steady-flow.md) | Viscous flow around bodies |
| 160 | [Smooth approximation of three-dimensional Sobolev homeomorphisms](problems/160-ball-evans-three-dimensions.md) | Nonlinear elasticity and approximation |
| 161 | [Approximation preserving a compressible elastic energy](problems/161-elastic-energy-approximation.md) | Nonlinear elasticity and variational approximation |
| 162 | [The full set of zero-energy cubic-to-tetragonal strains](problems/162-tetragonal-quasiconvex-hull.md) | Materials science and nonlinear elasticity |
| 163 | [Concentration of eikonal entropy production on jump curves](problems/163-eikonal-entropy-concentration.md) | Variational interfaces and nonlinear PDE |
| 164 | [The first dimension with a singular one-phase minimizing cone](problems/164-one-phase-critical-dimension.md) | Free boundaries and fluid interfaces |
| 165 | [Multiplicity one at planar network singularities](problems/165-network-multiplicity-one.md) | Grain-boundary evolution |
| 166 | [Uniqueness of the limiting shape at a network singularity](problems/166-network-tangent-uniqueness.md) | Grain-boundary evolution |
| 167 | [Sharp enstrophy-limited heat transport in two dimensions](problems/167-two-dimensional-wall-transport.md) | Heat transfer and flow optimization |
| 168 | [The maximal heat-transfer exponent at finite Prandtl number](problems/168-finite-prandtl-heat-scaling.md) | Buoyant convection and heat transfer |
| 169 | [An extreme solitary wave for the bidirectional Whitham system](problems/169-extreme-bidirectional-solitary-wave.md) | Nonlinear water-wave models |
| 170 | [Uniqueness of the Brownian coagulation similarity profile](problems/170-brownian-coagulation-profile.md) | Aerosol kinetics and aggregation |
| 171 | [A uniform limit-cycle bound for quadratic planar dynamics](problems/171-quadratic-hilbert-sixteen.md) | Nonlinear oscillations and dynamical systems |
| 172 | [A stationary isotropic gas of freely moving non-colliding disks](problems/172-stationary-noncolliding-billiards.md) | Kinetic geometry and hard-particle systems |
| 173 | [Anomalous viscous dissipation with fixed large-scale forcing](problems/173-large-scale-forced-dissipation.md) | Turbulence and energy transfer |
| 174 | [The Euler vortex-filament limit for a general moving curve](problems/174-vortex-filament-binormal.md) | Vortex dynamics and fluid mechanics |
| 175 | [Sustained double-exponential gradient growth on the Euler torus](problems/175-euler-sustained-double-exponential-growth.md) | Fluid mixing and creation of small scales |

## Stochastic growth, populations and statistical mechanics

| ID | Problem | Area |
| --- | --- | --- |
| 176 | [Strict convexity of the planar exponential first-passage shape](problems/176-strict-convexity-fpp.md) | Stochastic growth and random media |
| 177 | [The two-thirds passage-time variance exponent](problems/177-fpp-kpz-variance.md) | Random interfaces and growth fluctuations |
| 178 | [Absence of doubly infinite minimizing paths in planar first-passage percolation](problems/178-absence-fpp-bigeodesics.md) | Optimal transport through random media |
| 179 | [Exclusion of coexistence for unequal Richardson growth rates](problems/179-unequal-richardson-competition.md) | Competing infections and stochastic growth |
| 180 | [Monotonicity of transport speed on Galton–Watson trees](problems/180-galton-watson-speed-monotonicity.md) | Transport on random branching networks |
| 181 | [Connectivity of the three-dimensional minimal spanning forest](problems/181-three-dimensional-minimal-spanning-forest.md) | Disordered network optimization |
| 182 | [Does supercritical percolation preserve transience?](problems/182-percolation-preserves-transience.md) | Diffusion in diluted networks |
| 183 | [A nonuniqueness phase on every nonamenable transitive graph](problems/183-nonamenable-nonuniqueness-phase.md) | Percolation and network resilience |
| 184 | [A deterministic nontrivial growth exponent for planar DLA](problems/184-dla-growth-exponent.md) | Aggregation and fractal growth |
| 185 | [Does directional transience imply ballistic transport in an iid medium?](problems/185-rwre-transience-ballisticity.md) | Diffusion and transport in random environments |
| 186 | [The directional zero–one law in three-dimensional random media](problems/186-rwre-directional-zero-one.md) | Random transport and ergodicity |
| 187 | [The density conjecture for activated random walk on the square lattice](problems/187-activated-random-walk-density.md) | Self-organized criticality |
| 188 | [Coexistence for every positive cyclic invasion rate](problems/188-cyclic-spatial-coexistence.md) | Spatial ecology and evolutionary dynamics |
| 189 | [Coexistence in a three-strain colicin model](problems/189-three-strain-colicin-coexistence.md) | Spatial microbiology |
| 190 | [Competitive exclusion with unequal death rates](problems/190-competing-contact-unequal-deaths.md) | Spatial epidemics and population competition |
| 191 | [Liouville invariance under changing local moves on a Cayley network](problems/191-liouville-generating-set-invariance.md) | Random walks and network potential theory |
| 192 | [Selection of the carbon-monoxide poisoning phase](problems/192-catalytic-carbon-monoxide-poisoning.md) | Catalytic surface reactions |
| 193 | [Two stationary phases in a positive-rate nonlinear voter perturbation](problems/193-positive-rate-nonlinear-voter.md) | Spatial population dynamics and phase coexistence |
| 194 | [A phase transition for continuum hard disks](problems/194-hard-disk-phase-transition.md) | Equilibrium fluids and phase transitions |
| 195 | [A roughening transition in the three-dimensional Ising model](problems/195-ising-three-dimensional-roughening.md) | Interfaces and equilibrium statistical mechanics |
| 196 | [Uniqueness of the planar spin-glass ground-state pair](problems/196-planar-spin-glass-ground-states.md) | Disordered magnetic materials |
| 197 | [Pathwise uniqueness at the three-quarter Hölder threshold](problems/197-stochastic-heat-critical-uniqueness.md) | Stochastic reaction–diffusion equations |
| 198 | [Strong disorder versus a shifted pinning threshold](problems/198-pinning-strong-disorder-critical-shift.md) | Disordered polymers and adsorption |
| 199 | [Polynomial mixing of planar Ising dynamics with plus boundary](problems/199-ising-plus-boundary-polynomial-mixing.md) | Statistical mechanics and stochastic relaxation |
| 200 | [A continuous strictly decreasing moment spectrum for Gaussian polymers](problems/200-directed-polymer-moment-spectrum.md) | Polymers in random media |

## Maintaining the collection

Run `python3 scripts/catalogue.py --write` after metadata changes, then `python3 scripts/catalogue.py --check`. These commands use only the Python standard library and check count, unique IDs, required content, metadata consistency, and local links. They do not verify mathematical or open-status claims.
