# Key Insights from Research: Linear Algebra for ML

## Core Geometric Intuition
- Matrices ARE transformations: stretching, rotating, projecting, reflecting
- Every ML model is really a sequence of matrix transformations on data
- Eigenvectors = directions that survive transformation unchanged (only scaled)
- Eigenvalues = how much stretching happens along those directions
- Covariance matrix ellipse: eigenvectors are axes, eigenvalue sqrt = length

## PCA Deep Dive
- PCA finds the coordinate system where your data's covariance matrix becomes diagonal
- Eigenvectors of covariance = directions of max variance
- Eigenvalues = amount of variance along each direction
- Scree plot elbow = signal vs noise boundary
- PCA under the hood uses SVD (not eigendecomposition) for numerical stability
- Outliers disproportionately affect PCA (they distort covariance)

## SVD & Recommender Systems (Netflix Prize Story)
- Simon Funk's 2006 blog post revolutionized the Netflix Prize
- SVD factorizes user-item matrix into latent factors
- Latent factors = hidden "taste dimensions" (not labeled, emerge mathematically)
- Prediction: dot product of user profile and movie profile
- Truncated SVD = keeping top-k singular values = denoising
- Eckart-Young theorem: this is provably the BEST rank-k approximation

## Condition Number & Numerical Stability
- κ(A) = σ_max / σ_min — ratio tells you digits of accuracy you lose
- Feature scaling improves condition number → prevents NaN
- Normal equation squares condition number (κ² problem)
- QR preserves condition number; SVD handles rank-deficiency

## Graph Connections
- PageRank = dominant eigenvector of web transition matrix (power iteration)
- Spectral clustering = embed graph nodes using Laplacian eigenvectors, then k-means
- Fiedler vector (2nd smallest eigenvector) = optimal graph bisection

## Deep Learning Connections
- Neural net layer = matrix multiplication + nonlinearity
- Backpropagation = chain of Jacobian matrix multiplications
- Singular values of weight matrices control gradient flow
- Near-zero singular values → vanishing gradients
- Huge singular values → exploding gradients
- Orthogonal weight initialization helps preserve gradient flow

## Interview-Depth Points
- Why you never invert matrices in production (use solve/decomposition)
- eig vs eigh: symmetric matrices → always real eigenvalues, orthogonal eigenvectors
- L1 vs L2 geometry: L1 ball has corners → sparsity
- Cosine similarity = normalized dot product → measures directional agreement
- Word2Vec arithmetic works because similar relationships create consistent vector offsets
