# Feature Importance & Bias

## Impurity-based Importance
- Sum of impurity decreases weighted by samples at each split
- Built-in, no extra computation
- BIASED toward high-cardinality features (more split points = more chances to reduce impurity)
- A random ID column can appear "important"

## Permutation Importance
- Shuffle feature values, measure accuracy drop
- Measures actual predictive power regardless of cardinality
- Less biased but can underestimate correlated features
- sklearn: permutation_importance()

## SHAP / TreeSHAP
- Game-theoretic approach to feature attribution
- TreeSHAP is polynomial-time for tree models
- Most theoretically grounded method
