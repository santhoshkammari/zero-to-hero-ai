# Feature Engineering Findings

## Why Feature Engineering Beats Deep Learning on Tabular Data
- DL struggles with heterogeneous, small datasets
- Signal hides in derived features that DL can't discover
- Well-engineered features + tree models (XGBoost/LightGBM) consistently outperform DL on tabular
- "Feature engineering is the key lever; the model is just there to process your signal" - Kaggle grandmasters

## High-Impact Feature Types
1. **Ratios/Interactions**: price_per_sqft, credit_utilization = balance/limit
2. **Aggregation features**: per-group statistics (mean, count, std by user_id)
3. **Lag features**: yesterday's value, last week's value
4. **Rolling statistics**: 7-day rolling mean, rolling std
5. **Time-since-event**: days since last purchase, since last failure
6. **Cyclical encoding**: sine/cosine for hour, day_of_week, month

## Cyclical Encoding - The Why
- Hour 23 and hour 0 are 1 hour apart, but numerically 23 apart
- Sine/cosine transform makes this distance correct
- Same for day_of_week (Sunday and Monday), month (December and January)

## Production Feature Stores
- Centralized repository for storing/sharing features
- Ensures same computation in training and inference
- Feast (open-source), Databricks Feature Store, Tecton
- Handle freshness/staleness, point-in-time correct retrieval

## Outlier Handling
- IQR method: not sensitive to multimodal data, struggles with skewed distributions
- Winsorization vs clipping: both cap extremes, Winsorization uses quantiles (more statistical)
- Tree-based models naturally robust to outliers—don't remove for them
- Outlier removal harmful when outliers are real signal (rare events, minority class)
