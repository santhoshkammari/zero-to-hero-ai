# Curse of Dimensionality

## Key Insights
- As dimensions grow, ALL points become equidistant — distance metrics lose meaning
- The ratio of (max distance - min distance) / min distance approaches 0 in high dimensions
- k-NN breaks because "nearest" neighbor is barely closer than the "farthest"
- Most volume of a high-dimensional hypercube lives in thin shell near the surface and in the corners
- Need exponentially more data to maintain same density as dimensions increase
- A unit hypercube in 100D: a random point has ~0% chance of being within 0.1 of any axis

## Practical Implications
- Feature selection becomes critical, not optional
- PCA/UMAP/t-SNE aren't luxuries — they're necessities for distance-based methods
- Tree-based methods (RF, XGBoost) handle high dimensions better than distance-based ones
- This is WHY feature engineering matters more than model choice in many cases

## Interview Angle
- "Why does k-NN fail in high dimensions?" → distance concentration
- "When would you NOT use Euclidean distance?" → high-dimensional sparse data
