# Curse of Dimensionality, Manifold Learning, Other Methods

## Curse of Dimensionality
- Volume of space increases exponentially with dimensions
- For random points in [0,1]^d: E[distance²] = d/6, std/mean ~ 1/√d
- As d grows, all pairwise distances concentrate around the mean
- Nearest and farthest neighbors become nearly indistinguishable
- Distance-based algorithms (k-NN, clustering) fail

## Manifold Hypothesis
- High-dimensional data lies on lower-dimensional manifold
- Swiss roll: 2D surface curled in 3D — Euclidean distance misleading, geodesic distance meaningful
- Goal of manifold learning: unfold the manifold

## Isomap
- Global approach: geodesic distances via shortest paths on k-NN graph
- Then classical MDS on geodesic distance matrix
- Good for globally smooth manifolds (Swiss roll)
- Fails with holes, noise, disconnected graphs

## LLE (Locally Linear Embedding)
- Local approach: reconstruct each point as weighted sum of neighbors
- Find low-D embedding preserving those weights
- Good for locally linear manifolds
- Sensitive to neighborhood size, struggles with non-uniform density

## Kernel PCA
- Apply kernel trick to PCA
- Project data into high-D feature space via kernel, then do PCA there
- RBF kernel captures nonlinear structure
- Can transform new points (out-of-sample extension)

## NMF (Non-negative Matrix Factorization)
- V ≈ WH, all non-negative
- Parts-based: components can only add, not subtract
- Faces: learns eyes, nose, mouth (localized parts)
- PCA: learns eigenfaces (holistic, positive+negative)
- Great for topic modeling, image decomposition
- Interpretable by construction

## Random Projection (Johnson-Lindenstrauss)
- JL lemma: can project to O(log n / ε²) dimensions preserving distances within (1±ε)
- No data dependence — random matrix multiplication
- Fastest possible dimensionality reduction
- Use when speed matters more than optimality
- Privacy-preserving (obscures original features)

## LDA (Linear Discriminant Analysis)
- Supervised: maximizes between-class / within-class scatter ratio
- At most C-1 components (C = number of classes)
- Assumes Gaussian classes with equal covariance
- Often outperforms PCA for classification with fewer dimensions
