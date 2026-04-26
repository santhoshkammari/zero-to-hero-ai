# Unsupervised Learning Interview Gotchas

1. **t-SNE/UMAP clusters ≠ real clusters** — visualization artifacts, not ground truth
2. **PCA before clustering can destroy signal** — PCA maximizes variance, not cluster separation
3. **K-Means implicit assumptions** — spherical, equal-sized, equal-density clusters. Violations are silent
4. **Wrong distance metric** — cosine vs Euclidean dramatically changes results for text/embeddings
5. **Evaluating without labels** — silhouette score fails on non-convex clusters, elbow method is subjective
6. **Categorical data** — most algorithms assume continuous. Need k-modes, Gower distance, or encoding strategies
7. **Curse of dimensionality** — distances converge in high dimensions, making clustering meaningless without reduction
8. **Anomalies forming their own cluster** — not detected as anomalies, just become a small cluster
