# Clustering Research Findings

## K-Means Internals
- Lloyd's algorithm: assign → update → repeat
- Convergence proof: SSE monotonically decreases (assignment minimizes for fixed centroids, update minimizes for fixed assignments), finite number of partitions → must terminate
- Converges to LOCAL minimum, not global
- K-Means++ (Arthur & Vassilvitskii, 2007): D² weighting picks centers proportional to squared distance from nearest existing center → O(log k) competitive guarantee
- Voronoi cells: K-Means carves feature space into convex polygons → can't handle non-convex shapes
- Mini-Batch K-Means: random batch per step, 10x faster, ~1-2% quality loss

## DBSCAN
- Core/Border/Noise classification based on eps and min_samples
- Density reachability: directly density-reachable → density-reachable (chain) → density-connected
- Finds arbitrary shapes via recursive expansion of core point neighborhoods
- Single eps problem: can't handle varying density clusters
- k-distance plot for eps tuning, 2×n_features rule for min_samples

## HDBSCAN
- Mutual reachability distance: max(core_dist(a), core_dist(b), dist(a,b)) — prevents chaining
- Builds hierarchy across ALL density levels, uses cluster stability to extract persistent clusters
- No eps parameter needed, automatic cluster count, soft assignments via probabilities
- Strictly better than DBSCAN for most use cases

## Spectral Clustering
- Build similarity graph → compute graph Laplacian (L = D - W) → take k smallest eigenvectors → run K-Means in embedded space
- Eigenvectors encode "smoothest" signals on graph — points in same cluster get similar values
- Normalized cut balances partition size with connectivity
- O(n²) space, O(n³) time — small-to-medium data only
- Works for non-convex shapes because it captures connectivity, not geometric distance

## Gaussian Mixture Models
- K-Means is degenerate special case: spherical covariance + hard assignments
- EM: E-step (compute responsibilities via Bayes) → M-step (update params with soft counts)
- Covariance types: full (arbitrary ellipsoid), diagonal (axis-aligned), spherical, tied
- BIC/AIC for model selection instead of elbow
- BayesianGMM with Dirichlet process prior auto-selects k

## Evaluation Metrics
- Internal (no labels): Silhouette (biased toward convex), Davies-Bouldin, Calinski-Harabasz
- External (with labels): ARI (chance-adjusted, pairwise), NMI (mutual information)
- Silhouette favors K-Means-like clusters — metric bias trap
- Stability analysis: bootstrap/subsample and check if clusters persist

## High-Dimensional Clustering
- Curse of dimensionality: distances converge, neighborhoods break down
- Always reduce dims (PCA, UMAP) before clustering when d > 10-20
- Cosine distance often better than Euclidean in high-d
