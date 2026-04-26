# Web Search Insights for Clustering Section

## Key insights gathered from web research:

1. **K-Means convergence** - SSE bounded below by 0, finite partitions, monotonically decreasing → guaranteed termination at local minimum
2. **K-Means++ guarantee** - O(log k) competitive with optimal, from Arthur & Vassilvitskii 2007
3. **DBSCAN density reachability** - chain concept: directly density-reachable → density-reachable → density-connected
4. **HDBSCAN mutual reachability** - max(core_dist(a), core_dist(b), dist(a,b)) prevents single-linkage chaining
5. **Spectral clustering** - Laplacian eigenvectors encode connectivity not geometry; normalized cut balances partition sizes
6. **GMM-KMeans relationship** - K-Means = GMM with spherical equal covariances and hard assignments
7. **Metric bias** - Silhouette favors compact spherical clusters; ARI needs ground truth; NMI can overrate many small clusters
8. **Curse of dimensionality** - Always reduce to <20 dims before clustering; cosine distance preferred in high-d
