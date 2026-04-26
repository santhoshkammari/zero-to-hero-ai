# SciPy Section Rewrite Plan

## Running Example
Building a movie recommendation engine from scratch - starts with a tiny 4-user, 5-movie rating matrix.
This naturally touches: sparse matrices, SVD, optimization, statistics, spatial distance.

## Concept Ladder (dependency order)
1. Why SciPy exists (FORTRAN wrappers, the "standing on shoulders" idea)
2. Sparse matrices (the recommendation matrix is mostly empty)
3. Truncated SVD on sparse data (extracting latent factors)
4. Optimization (fitting/calibrating the model)
5. Statistical testing (is model A better than model B?)
6. Spatial distances (finding similar users/movies)
7. Signal processing & interpolation (briefly, for completeness)
8. The boundaries - where SciPy stops

## Recurring Analogies
1. SciPy as a "translator" sitting between you and battle-hardened FORTRAN veterans
2. Sparse matrix as a warehouse ledger (only record where things ARE, not every empty shelf)
3. Optimization as navigating a landscape blindfolded

## Vulnerability Moments
1. Confession about avoiding scipy.optimize for years
2. Admitting CSR/CSC confusion
3. Still developing intuition for when KDTree breaks
4. Oversimplification correction on sparse memory savings

## Rest Stop
After sparse matrices + truncated SVD - reader has enough to build a basic recommender

## Brandon Style Elements
- Personal confession opening
- Build from scratch with toy example
- Each section motivated by limitation of previous
- Organic transitions
- No bullet-point explanations
- Terms defined inline on first use
