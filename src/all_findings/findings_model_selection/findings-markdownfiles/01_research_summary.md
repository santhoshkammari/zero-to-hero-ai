# Model Selection Research Summary

## Key Topics Researched

### 1. No Free Lunch Theorem (Wolpert & Macready, 1997)
- No single algorithm dominates all problems averaged across all datasets
- Practical implication: domain knowledge + empirical evaluation are essential
- Ensembling often helps because different models capture different structure

### 2. Hyperparameter Tuning Methods
- **Grid Search**: Brute force, wastes budget on unimportant axes, exponential cost
- **Random Search** (Bergstra & Bengio 2012): Surprisingly effective because most hyperparams have 1-2 important values. 60 random trials ≥ grid search with 10 intervals per param
- **Bayesian Optimization / TPE**: Models P(x|y) instead of P(y|x). Splits trials into good/bad, fits KDEs, maximizes l(x)/g(x). Used in Optuna/Hyperopt
- **Optuna pruning**: MedianPruner compares current trial intermediate values to median of completed trials, kills underperformers early

### 3. Information Criteria (AIC/BIC)
- AIC = 2k - 2ln(L): lighter penalty, good for prediction
- BIC = ln(n)k - 2ln(L): heavier penalty scaling with sample size, good for inference/true model
- ΔAIC or ΔBIC < 2 weak evidence, 4-7 considerable, >10 strong
- Neither proves a model is true; both for relative comparison

### 4. AutoML
- Auto-sklearn: Bayesian optimization + ensemble, slower, higher ceiling
- FLAML: Fast, lightweight, resource efficient, good-enough-fast
- Key insight: AutoML doesn't replace understanding; it automates the tedious parts

### 5. Model Complexity & Occam's Razor
- Bias-variance tradeoff: increasing complexity ↓bias ↑variance
- Match model capacity to data size
- Learning curves: both low = underfit, gap = overfit

### 6. SHAP Values
- Based on Shapley values from cooperative game theory
- Fair attribution: average marginal contribution across all permutations
- Additive: sum of SHAP values + baseline = prediction
- TreeSHAP for tree models, KernelSHAP for model-agnostic

### 7. Nested Cross-Validation
- Inner loop: hyperparameter tuning on training folds
- Outer loop: unbiased performance estimation on held-out test folds
- Prevents data leakage from test set influencing model selection

### 8. Interview-Depth Topics
- Parametric vs non-parametric model selection
- Statistical comparison of models (paired t-test, Wilcoxon)
- Deployment constraints: latency, memory, interpretability
- When simpler models win (tabular data, small data, speed needs)
