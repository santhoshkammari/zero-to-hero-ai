# Key Insights from Web Research

1. The 2013 API design paper (Buitinck et al.) established the estimator specification that made sklearn dominant
2. get_params/set_params are not just convenience - they're the engine behind GridSearchCV and clone()
3. The underscore convention (coef_ vs C) is a deliberate design choice separating hyperparams from learned state
4. Pipeline prevents data leakage because it re-fits transformers on each CV fold's training data
5. ColumnTransformer + make_column_selector enables dynamic, schema-resilient preprocessing
6. FunctionTransformer wraps arbitrary functions into pipeline-compatible transformers
7. set_output(transform='pandas') is a game-changer for debugging pipelines (v1.2+)
8. check_estimator() validates custom estimators against the full API contract
9. TransformedTargetRegressor handles target transformations without leakage
10. partial_fit enables incremental learning but not all estimators support it
11. Scikit-learn's sweet spot: tabular data, in-memory, CPU - not for images/text/GPU
