# CART Algorithm & Splitting Criteria

## Key Findings

### History
- CART (1984) by Breiman, Friedman, Olshen, Stone — the foundational binary tree algorithm
- ID3 (1986) by Quinlan — entropy/info gain, categorical only, no pruning
- C4.5 (1993) by Quinlan — gain ratio (fixes info gain bias), handles continuous + missing

### CART Algorithm Mechanics
- Always produces **binary splits** (left/right)
- For each feature, sorts values and tries every midpoint as candidate threshold
- Picks (feature, threshold) pair with highest impurity reduction
- Greedy: locally optimal at each step, globally NP-hard to find optimal tree
- Time complexity: O(n * m * log n) where n=samples, m=features

### Gini vs Entropy
- Gini = 1 - Σ(pᵢ²) — measures misclassification probability
- Entropy = -Σ(pᵢ log₂ pᵢ) — measures uncertainty/information
- In practice: disagree on <2% of splits
- Gini slightly faster (no log computation)
- Both are concave functions that peak at 50/50 distribution

### Information Gain Ratio (C4.5)
- Plain info gain is biased toward features with many values
- Gain ratio = info gain / split information (normalizes by the feature's own entropy)
- This is why C4.5 was an improvement over ID3

### Regression Trees
- Minimize MSE (variance reduction) instead of Gini/entropy
- Leaf prediction = mean of training samples in that leaf
- Cannot extrapolate beyond training range — fundamental limitation

### Surrogate Splits (CART)
- When main split feature is missing, uses other features that mimic the same split
- Ranks backup features during training
- XGBoost different: learns default direction (left/right) for missing values at each split
