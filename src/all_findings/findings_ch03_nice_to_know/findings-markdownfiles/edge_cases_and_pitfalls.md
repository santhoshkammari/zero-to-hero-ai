# Data Wrangling Edge Cases & Production Pitfalls

## Key Edge Cases
- Unseen categories at inference time (new product codes, cities not in training)
- Unexpected nulls appearing in production that weren't in training data
- Date/time columns arriving in mixed formats
- Feature leakage through improper join operations (key explosion)
- Data drift where source "hasn't changed" but schemas evolved silently
- High-cardinality categoricals causing dimensionality explosion with naive one-hot
- 99% zero columns (sparse/skewed) — log transform? binarize? regularize?

## Production-Specific Gotchas
- Training/serving skew: different preprocessing logic in batch vs real-time
- Silent failures: preprocessing that drops rows without logging
- Pandas single-threaded limits on large data → need Dask/Spark
- Joins with non-unique keys creating row duplication
- Missing data mechanism matters: MCAR vs MAR vs MNAR affects imputation choice

## Interview-Level Insights
- Senior engineers expected to discuss business meaning of missingness, not just mean imputation
- Must know when pandas breaks and alternatives (Dask, Spark, chunking)
- Data leakage is the #1 gotcha: time-based splits, grouped aggregation boundaries
- Test-driven wrangling: "how do we know our cleaning worked?"
