# KNN Deep Dive Findings

## Core Mechanics
- Lazy learner: no training, entire dataset IS the model
- Prediction: compute distance to every training point, pick k closest, vote
- For classification: majority vote. For regression: average of neighbors
- O(n·d) per prediction brute force

## Distance Metrics
- Euclidean (L2): default, straight-line
- Manhattan (L1): robust to outliers in individual features
- Minkowski (Lp): generalization
- Cosine similarity: for high-dimensional text/embedding spaces
- Feature scaling is MANDATORY - without it, high-range features dominate

## Decision Boundaries
- k=1: Voronoi diagram - each point owns a region, jagged boundaries
- Higher k: boundaries smooth out, averaging effect
- k=1 overfits (zero training error, high variance)
- k=n: everything gets same prediction (majority class), max bias
- Voronoi tessellation is the geometric insight for k=1

## Weighted KNN
- Uniform: all k neighbors vote equally
- Distance-weighted: closer neighbors get higher weight (1/distance)
- Distance weighting helps when local density varies
- sklearn: weights='uniform' vs weights='distance'

## Acceleration Structures
- KD-tree: axis-aligned splits, O(d·log n) avg, degrades past ~20 dims
- Ball tree: hypersphere-based, better for moderate dimensions, non-Euclidean
- Approximate NN: FAISS, Annoy, HNSW, LSH for production scale
- FAISS handles billions of vectors with GPU
- HNSW: graph-based, state-of-art quality-speed tradeoff

## Curse of Dimensionality
- In high dimensions, all points equidistant
- Volume of hypersphere shrinks relative to hypercube
- Need exponentially more data as dimensions grow
- Practical limit: ~20 features for KNN
- Mitigation: PCA, feature selection, approximate methods

## When KNN Wins
- Small datasets (<10k)
- Low dimensions
- Quick baselines/prototyping
- Locally interpretable decisions
- Non-parametric: makes no distributional assumptions
