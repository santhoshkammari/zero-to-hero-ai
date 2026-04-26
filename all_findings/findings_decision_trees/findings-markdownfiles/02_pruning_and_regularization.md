# Pruning & Regularization

## Pre-pruning (Early Stopping)
- max_depth: single most important hyperparameter
- min_samples_split, min_samples_leaf, max_features
- Risk: may stop too early and miss important splits
- Depth-5 tree = max 32 leaves, depth-20 = over 1 million

## Post-pruning (Cost-Complexity)
- Grow full tree, then prune back
- R_α(T) = R(T) + α * |T| — misclassification + complexity penalty
- ccp_alpha in sklearn: larger α = more aggressive pruning
- Often produces better trees than pre-pruning alone
- Cross-validate to find optimal alpha

## Key Insight
- Post-pruning can evaluate the full structure before cutting
- Like regularization strength for trees
- The cost_complexity_pruning_path gives a menu of tree sizes
