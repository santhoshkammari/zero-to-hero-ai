# Stacking & Kaggle Insights

## Stacking
- Level-1: diverse base models with OOF predictions
- Level-2: meta-model (usually simple: logistic regression, ridge)
- CRITICAL: must use out-of-fold predictions or meta-model overfits
- Typically adds 0.5-1% on top of best single model
- Worth it in competitions, rarely in production (3x complexity for marginal gains)

## Kaggle Best Practices 2024
- Diversity is key: multiple GBDT libs + different hyperparams + different seeds
- Feature engineering often matters more than model choice
- Clean CV procedures prevent leaderboard shakeups
- Optuna for hyperparameter search
- SHAP for interpretation
- Blending (simple weighted average) sometimes beats full stacking
