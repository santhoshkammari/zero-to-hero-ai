# Scikit-learn Research Findings

## Core Design Philosophy (Buitinck et al. 2013)
- Consistent API: fit/predict/transform pattern across ALL estimators
- Parameters in __init__, learned attributes end with underscore (_)
- get_params/set_params enable clone() and GridSearchCV internals
- Duck typing - no strict inheritance needed, just implement the right methods
- No side effects on input data

## The Contract
- Estimators: fit(X, y) learns from data
- Predictors: predict(X) generates predictions
- Transformers: transform(X) applies learned transformation
- fit_transform(X) convenience method
- Meta-estimators: Pipeline, ColumnTransformer, GridSearchCV

## Why Underscore Convention Matters
- coef_, intercept_, mean_, scale_ = learned from data
- C, max_iter, n_estimators = hyperparameters set by user
- This separation is what makes clone() work - it copies hyperparams, drops learned state

## Pipeline Deep Patterns
- Prevents data leakage in cross-validation automatically
- ColumnTransformer routes different column types to different transformers
- make_column_selector for dynamic dtype-based column selection
- FunctionTransformer wraps arbitrary functions into pipeline-compatible transformers
- set_output(transform='pandas') for DataFrame output (v1.2+)
- Global: sklearn.set_config(transform_output="pandas")

## Custom Transformers
- Inherit BaseEstimator + TransformerMixin
- Store params in __init__, learned state in fit() with underscore suffix
- fit() must return self
- transform() must be stateless (only use fitted attributes)
- check_estimator() validates API compliance

## Data Leakage Patterns
- Fitting transformers before train/test split = leakage
- Feature selection on full dataset before CV = leakage
- Pipeline solves this by re-fitting on each fold's training data
- TimeSeriesSplit for temporal data (KFold shuffles break time order)
- TransformedTargetRegressor for target transformations

## Production Considerations
- joblib.dump saves entire pipeline
- handle_unknown='ignore' in OneHotEncoder for unseen categories
- Schema validation with pandera/pydantic
- Scikit-learn excels at tabular data, in-memory datasets
- Limitations: no GPU, no deep learning, limited streaming (partial_fit)
- partial_fit for incremental learning (SGDClassifier, MiniBatchKMeans)

## Modern Features (v1.2-1.5)
- set_output API for pandas DataFrame outputs
- Metadata routing through pipelines
- feature_names_in_ attribute across estimators
- HDBSCAN added, HistGradientBoosting improvements
