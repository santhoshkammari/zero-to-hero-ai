# Rewrite Plan: Linear Algebra Section (ch02/s02.html)

## Running Example
A tiny movie recommender system. Start with 3 users and 3 movies.
- Introduces vectors (user preferences), matrices (ratings table)
- Naturally extends to dot products (similarity), projections, SVD (recommendations)
- Threads through entire post

## Recurring Analogies
1. **Telescope analogy**: Eigenvectors are like finding the right angle to look at data through a telescope — rotate until you see the clearest picture. Recurs in PCA, SVD, spectral clustering.
2. **Shadow analogy**: Projection = casting a shadow of a 3D object onto a wall. Linear regression = the shadow of reality onto the subspace of predictions. Recurs in least squares, PCA.
3. **Stretchy fabric analogy**: A matrix transformation is like stretching fabric — eigenvectors are the directions along the threads that don't twist, only stretch. Singular values measure how much.

## Concept Ladder (dependency order)
1. Scalars → Vectors → Matrices → Tensors (data hierarchy)
2. Dot product (similarity measure) → cosine similarity → word embeddings
3. Matrix multiplication (THE operation) → neural net layers
4. Linear combinations, span, independence → why features matter
5. Norms (L1, L2) → regularization geometry
6. Matrix as transformation → geometric intuition
7. Systems of equations → least squares → regression as projection
8. Determinants → volume scaling → invertibility
9. Eigenvalues/eigenvectors → PCA → variance directions
10. SVD → low-rank approximation → recommender systems
11. Condition number → numerical stability → why models produce NaN
12. Decompositions (Cholesky, QR, LU) → when to use which
13. Graph Laplacian → spectral clustering → PageRank
14. NMF → topic modeling → parts-based representations

## Rest Stop Placement
After eigenvalues/PCA section — reader has enough to understand dimensionality reduction and the core "matrices as transformations" insight.

## Vulnerability Moments
1. Opening: "I avoided linear algebra courses for years"
2. After matrix multiplication: "If this is your first time seeing this, it might feel needlessly complex. I remember staring at the indices wondering why anyone would define multiplication this way."
3. After eigenvalues: "I'm still developing my intuition for why diagonalization makes things easier"
4. After SVD: "I'll be honest — I didn't fully grasp SVD until I saw it predict movie ratings"
5. Condition number: "I spent two days debugging NaN values before someone told me to check the condition number"

## Structure
- Brandon-style opening (confession, orientation, heads-up, journey invitation)
- Table of contents
- Build-up sections with running example
- Rest stop after PCA
- Advanced topics (decompositions, graph Laplacian, NMF)
- Wrap-up with gratitude, recap, future hope
- Resources with personality
