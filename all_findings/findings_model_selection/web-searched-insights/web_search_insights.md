# Web Search Insights

## Search 1: Bayesian Optimization / TPE
- TPE models P(x|y) not P(y|x) — fundamentally different from GP-based BO
- Splits trials into "good" (top N%) and "bad", fits KDE on each
- Maximizes l(x)/g(x) ratio — equivalent to Expected Improvement
- Handles conditional/tree-structured spaces natively

## Search 2: Random Search vs Grid Search
- Bergstra & Bengio 2012 key finding: most hyperparams aren't equally important
- Grid search wastes budget on unimportant dimensions
- 60 random trials often matches grid search with 10 intervals per param
- Random gives better coverage of important dimensions by chance

## Search 3: AIC/BIC
- AIC favors prediction, BIC favors true model discovery
- BIC penalty grows with sample size — stronger preference for simpler models
- ΔAIC/ΔBIC thresholds: <2 weak, 4-7 considerable, >10 strong

## Search 4: AutoML (Auto-sklearn vs FLAML)
- Auto-sklearn: higher accuracy ceiling, slower, heavier
- FLAML: fast, lightweight, resource-efficient
- Both have their place — depends on compute budget and accuracy requirements

## Search 5: Occam's Razor / Bias-Variance
- Match model capacity to data: simple for small, complex for large
- Regularization as complexity control
- Learning curves as diagnostic tool

## Search 6: Interview Questions
- Senior engineers asked about parametric vs non-parametric choices
- Nested CV, statistical model comparison, deployment constraints
- "When does simple beat complex?" is a favorite question

## Search 7: Learning Curves
- Both curves low = underfit (need more complex model)
- Large gap = overfit (need simpler model or more data)
- Plateau = more data won't help

## Search 8: NFL Theorem
- Averaged over ALL possible problems, no algorithm dominates
- Practical: exploit domain structure, try multiple approaches, ensemble

## Search 9: SHAP
- Shapley values: fair distribution of "payout" among "players"
- Each feature's contribution = average marginal contribution across all permutations
- Additive property: baseline + sum(SHAP values) = prediction
- TreeSHAP is fast; KernelSHAP is model-agnostic but slower

## Search 10: Optuna Pruning
- MedianPruner: compares trial intermediate values to median of completed trials
- Kills trials performing below median
- n_startup_trials prevents premature pruning
- Saves massive compute on iterative training

## Search 11: Nested Cross-Validation
- Inner loop: tune hyperparameters on training folds only
- Outer loop: evaluate on truly held-out test folds
- Prevents data leakage from test influencing model selection
- Essential for unbiased performance estimates
