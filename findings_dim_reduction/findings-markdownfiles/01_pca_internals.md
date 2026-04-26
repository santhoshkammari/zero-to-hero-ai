# PCA Internals — Research Findings

## Core Insight
PCA is a rotation of coordinate axes to align with directions of maximum variance. Not a compression — a change of basis. Same data, better coordinates.

## Step-by-step
1. Center data (subtract mean from each feature)
2. Compute covariance matrix C = (1/(n-1)) X^T X — shape p×p
3. Eigendecompose: C = VΛV^T — eigenvectors are PC directions, eigenvalues are variance amounts
4. Sort by eigenvalue descending, keep top k

## SVD vs Eigendecomposition
- Nobody actually forms X^T X — for p=10000, that's 10K×10K matrix
- SVD directly on X: X = UΣV^T
- V columns = PC directions (same as eigenvectors of covariance)
- λ_i = σ_i² / (n-1) — eigenvalues from singular values
- Better numerics, never form covariance matrix

## Randomized SVD (Halko et al.)
- Project data onto random low-dim subspace first
- Then do exact SVD on the small matrix
- Orders of magnitude faster when k << min(n,d)
- sklearn auto-selects when n_components is small relative to features

## Reconstruction Error
- X_rec = X_proj @ W_k^T
- Error = ||X - X_rec||_F² = sum of discarded eigenvalues
- Directly tells you how much variance you threw away

## Key Production Considerations
- MUST standardize before PCA (otherwise scale dominates)
- PCA inside pipeline (not before cross-validation split)
- Incremental PCA for streaming/mini-batch scenarios
- PCA ≈ linear autoencoder (with linear activations + MSE loss)
