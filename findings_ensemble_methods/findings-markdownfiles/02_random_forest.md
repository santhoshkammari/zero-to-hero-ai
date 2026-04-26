# Random Forest Deep Dive

## Feature Subsampling = Decorrelation
- Without it, if one feature is dominant, all bagged trees split on it first → correlated trees → averaging doesn't help
- With random feature subsets per split: trees see different "views" → structurally different → less correlated predictions
- Classification: sqrt(p), Regression: p/3

## Weather Forecaster Analogy
- If all forecasters use same radar, all wrong together
- Different data sources → independent errors → averaging works

## OOB Score
- Each sample left out of ~1/3 of trees
- Predict using only those trees → essentially leave-one-out CV for free

## Feature Importance Trap
- MDI biased toward high-cardinality features
- Permutation importance is model-agnostic, no cardinality bias
