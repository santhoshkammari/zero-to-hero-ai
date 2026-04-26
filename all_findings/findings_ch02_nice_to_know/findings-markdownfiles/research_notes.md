# Ch02 Nice to Know - Research Notes

## Key Topics Researched

### 1. Measure Theory for ML
- Sigma algebras define "legal" events for probability
- Lebesgue integration generalizes expectations to complex distributions
- Foundation for rigorous probability theory used in ML

### 2. Topology in Neural Networks
- Topological Data Analysis (TDA) uses persistent homology for feature extraction
- Loss landscape topology: connectivity of minima, sharpness/flatness
- giotto-tda and GUDHI libraries

### 3. Category Theory & ML
- Functors as structure-preserving maps between categories
- Compositionality: neural networks as morphism composition
- "Backprop as Functor" paper by Fong, Spivak, Tuyéras (2019)

### 4. RKHS & Functional Analysis
- Reproducing Kernel Hilbert Spaces underpin kernel methods
- Kernel trick operates in infinite-dimensional feature space
- Representer theorem reduces infinite-dim optimization to finite

### 5. Group Theory & Equivariant Networks
- Symmetry groups formalize data invariances
- Lie groups for continuous symmetries (rotations, translations)
- E(3)-equivariant GNNs for molecular modeling
- Geometric Deep Learning umbrella framework

### 6. Information Geometry
- Fisher information metric as Riemannian metric on probability manifolds
- Natural gradient: steepest descent respecting manifold geometry
- Amari's natural gradient descent

### 7. Random Matrix Theory
- Marchenko-Pastur law for eigenvalue distribution of random matrices
- At initialization, weight matrices follow MP law
- Trained networks show spiked eigenvalues (learned structure)

### 8. Optimal Transport
- Wasserstein distance embeds geometric info for distribution comparison
- WGANs use Earth Mover's distance
- Sinkhorn algorithm for efficient approximation
- Applications in fairness, domain adaptation, shape analysis

### 9. Interview Gotchas
- Eigenvalue gotchas: nilpotent matrices, singular values vs eigenvalues
- Bayes theorem base rate fallacy (medical test example)
- E[f(X)] ≠ f(E[X]) for nonlinear f (Jensen's inequality)
- Zero covariance ≠ independence
- PCA fails when variance is uniform across dimensions
