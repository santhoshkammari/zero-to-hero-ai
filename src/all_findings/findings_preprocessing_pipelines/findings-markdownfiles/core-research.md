# Preprocessing Pipelines - Core Research Findings

## Pipeline Internals
- Pipeline iterates steps sequentially: for each intermediate step, calls `fit_transform()` if available (optimization), else `fit()` then `transform()`
- Last step: if transformer, gets `fit_transform()`; if estimator (classifier/regressor), only `fit()` is called
- The output of each step becomes the input to the next — a chain of transformations
- Key insight: `fit_transform` can be more efficient than separate `fit` + `transform` (e.g., PCA computes SVD once)

## ColumnTransformer Deep Dive
- Handles heterogeneous data: different columns get different transformations
- `remainder='passthrough'` keeps unspecified columns unchanged (appended at end)
- `remainder='drop'` (default) silently drops unmentioned columns — a common gotcha
- `sparse_threshold` controls sparse vs dense output (default 0.3)
- `get_feature_names_out()` recovers column names after transformation (sklearn 1.0+)
- Column order in output: transformer outputs first (in order), then remainder columns

## Custom Transformers
- Stateless: `fit()` returns self, no learning (e.g., log transform, column dropping)
- Stateful: `fit()` learns parameters stored as `attribute_` (trailing underscore convention)
- `FunctionTransformer`: quick wrapper for stateless functions — use for prototyping
- Custom class (BaseEstimator + TransformerMixin): for stateful, complex logic
- Constructor `__init__` must only assign params, no computation — enables `get_params`/`set_params`
- Never mutate X in-place; always return new array

## Data Leakage Prevention
- THE killer use case for pipelines: prevents train/serve skew
- Without pipeline: scaler fit on all data before train/test split = leakage
- With pipeline inside cross_val_score: fit happens only on training fold each time
- Common mistake: preprocessing outside CV loop
- Time series: must use TimeSeriesSplit, not random KFold

## Production Considerations
- Pipeline as single serializable artifact (joblib.dump)
- Feature stores (Feast, Tecton) solve what pipelines can't: real-time serving, versioning, point-in-time joins
- sklearn pipelines = prototyping/batch; feature stores = production at scale
- Train-serve skew: monitor feature distributions in production vs training stats

## Modern sklearn Features
- `set_output(transform="pandas")` — preserves DataFrame output with column names
- `make_pipeline()` vs `Pipeline()` — auto-generates step names vs explicit names
- Double-underscore notation for nested param access in GridSearchCV

## Interview-Depth Insights
- Why `fit_transform` exists as optimization (not just convenience)
- The `remainder` parameter gotcha in ColumnTransformer
- Pipeline + GridSearchCV: the double-underscore param access pattern
- Data leakage via preprocessing before splitting: the #1 beginner mistake
- When to use FunctionTransformer vs custom class
