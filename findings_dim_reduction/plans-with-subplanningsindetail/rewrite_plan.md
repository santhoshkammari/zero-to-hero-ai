# Rewrite Plan: Dimensionality Reduction (ch06/s02)

## Concept Ladder (dependency order)
1. The curse of dimensionality — why we need this at all
2. The manifold hypothesis — the intuition that makes reduction work
3. PCA from absolute zero — variance, covariance, eigenvectors, rotation
4. SVD under the hood — why nobody uses eigendecomposition
5. Choosing components — scree plot, explained variance
6. PCA in production — standardization, pipelines, gotchas
7. PCA ≈ linear autoencoder — the connection
8. REST STOP — you now have a solid mental model of linear reduction
9. Kernel PCA — when linearity fails
10. t-SNE — the visualization microscope
11. UMAP — the modern default
12. LDA — supervised reduction
13. ICA — cocktail party
14. NMF — parts-based decomposition
15. Random Projections — the brute force shortcut
16. Choosing a method — decision framework
17. Full pipeline example

## Running Example
A product recommendation dataset: users × products (500 features of behavior signals).
Starts small (4 users, 3 features → show PCA rotation), scales up.

## Recurring Analogies
1. "Map projection" — reducing 3D Earth to 2D map (distortion is inevitable, different projections preserve different things)
2. "Photography" — high-D is a hologram, PCA is choosing which angle to photograph from (loses depth but captures the most important view)

## Vulnerability Moments
1. Opening: confession about avoiding eigenvectors
2. PCA math: "first time I saw eigendecomposition I didn't believe rotation was all it was doing"
3. t-SNE: "I still get tripped up interpreting t-SNE plots"
4. UMAP theory: "I'm still developing my intuition for why fuzzy simplicial sets work"
5. Choosing: "there's no formula — I usually try 2-3 methods and compare"

## Rest Stop Placement
After PCA + scree plot + pipeline section — reader has 80% of practical knowledge
