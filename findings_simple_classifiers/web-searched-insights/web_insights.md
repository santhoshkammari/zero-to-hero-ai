# Web Search Insights

## Key insights gathered from web research:

1. **KD-tree vs Ball tree**: KD-tree uses axis-aligned splits (like a grid), Ball tree uses hyperspheres. KD-tree degrades to brute force past ~20 dims because axis-aligned splits can't efficiently partition high-dim space.

2. **Complement Naive Bayes** (Rennie et al., 2003): Instead of modeling P(features|class), models P(features|NOT class). This fixes the imbalanced class problem where majority class dominates parameter estimates. Often outperforms standard MultinomialNB.

3. **Voronoi tessellation for k=1**: The decision boundary of 1-NN is exactly the Voronoi diagram of training points. Increasing k smooths boundaries progressively — a beautiful geometric intuition.

4. **Weighted KNN**: Distance weighting (1/d) helps when local density varies. Closer points should matter more. sklearn supports weights='distance'.

5. **Approximate Nearest Neighbors at scale**: FAISS (Facebook), Annoy (Spotify), HNSW graphs — these are how KNN-like ideas work in production at billion-point scale. Not exact KNN but trade recall for speed.

6. **Log-space trick for NB**: Multiplying hundreds of small probabilities causes numerical underflow. Working in log space turns products into sums. Standard practice in all implementations.

7. **Why simple beats complex**: On small data (<1k samples), sparse high-dim data (text), or when features genuinely are near-independent, NB/KNN can outperform deep learning. Always establish baseline.

8. **Interview depth points**: 
   - Curse of dimensionality: distances converge in high dims
   - Feature scaling mandatory for distance-based methods
   - NB probability calibration is garbage — use for ranking only
   - Correlated features double-counted in NB
   - ComplementNB for imbalanced classes
