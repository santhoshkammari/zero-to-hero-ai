# Rewrite Plan for Clustering Section (ch06/s01.html)

## Approach: Brandon Rohrer Style
- Personal confession opening about avoiding clustering
- Running example: sorting a music library by "vibe" without genre labels
- Build from absolute zero: what does "similar" even mean?
- Each concept motivated by limitation of previous one
- Rest stop after K-Means + evaluation basics
- Vulnerability moments throughout
- Recurring analogies: sorting party guests into tables, maps/terrain

## Concept Ladder:
1. What is clustering? (The question: structure without labels)
2. Distance — what does "close" mean? (Euclidean, the bedrock)
3. K-Means from scratch (Lloyd's algorithm, toy example with 6 points)
4. K-Means++ (why starting position matters)
5. Choosing k (silhouette, elbow, gap)
6. Where K-Means breaks (non-convex, varying density)
7. REST STOP
8. DBSCAN (density as the new definition of cluster)
9. HDBSCAN (the modern fix)
10. Hierarchical clustering (the merge tree, dendrograms)
11. Spectral clustering (change the representation)
12. Gaussian Mixture Models (soft K-Means, EM)
13. Evaluation metrics (internal + external)
14. Decision framework
15. Wrap-up

## Vulnerability Moments:
- Confession: used K-Means for everything, got burned
- Still developing intuition for spectral clustering eigenvectors
- Admit silhouette score led me astray once
- Honest about "no one agrees what cluster means"
- Oversimplification correction when moving from K-Means to GMM
