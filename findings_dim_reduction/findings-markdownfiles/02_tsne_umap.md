# t-SNE and UMAP — Research Findings

## t-SNE Core
- Builds probability distribution over pairs in high-D (Gaussian kernel)
- Builds probability distribution in low-D (Student's t with 1 DOF = Cauchy)
- Minimizes KL divergence between the two via gradient descent

## The Crowding Problem
- In 100D, a point can have dozens of equidistant neighbors (hypersphere surface area huge)
- In 2D, can only pack ~6 equidistant neighbors
- Gaussian in low-D creates traffic jam — everything smushes to center
- t-distribution's heavy tails push moderately distant points much further apart
- Creates breathing room for clusters to separate

## Perplexity
- Defined as 2^{H(P_i)} where H is Shannon entropy
- Roughly "how many effective neighbors each point considers"
- Controls balance between local (low perp 5-10) and global (high perp 30-50)
- t-SNE adapts local Gaussian width so each point matches target perplexity

## t-SNE Gotchas
- Cluster sizes meaningless
- Inter-cluster distances meaningless
- Only cluster existence and membership reliable
- Never use as features for models
- Non-deterministic across runs
- O(n²) naive, O(n log n) with Barnes-Hut

## UMAP Core
- Build weighted k-NN graph in high-D (fuzzy simplicial sets)
- Build similar graph in low-D
- Minimize cross-entropy between high-D and low-D edge weights
- Cross-entropy vs KL divergence: CE also penalizes "things that should be far apart but aren't"
- This is why UMAP preserves global structure better

## UMAP Advantages
- Faster: O(n) practical, handles millions
- Better global structure preservation
- Can use output as features (higher-D embeddings)
- Supervised mode (pass labels)
- More deterministic

## Key Parameters
- n_neighbors (default 15): local vs global trade-off
- min_dist (default 0.1): how tightly points pack
