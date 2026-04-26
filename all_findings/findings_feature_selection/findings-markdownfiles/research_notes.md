# Feature Selection & Data Splitting - Research Notes

## Key Insights from Research

### Feature Selection
- **Three families**: Filter (stats-based, fast), Wrapper (model feedback, slow), Embedded (built into training)
- Filter methods miss feature interactions entirely - Pearson correlation only catches linear; MI captures nonlinear
- Curse of dimensionality: in high dimensions all points become equidistant (Hughes phenomenon)
- L1/Lasso drives coefficients to exactly zero due to diamond-shaped constraint region geometry (corners on axes)
- L2/Ridge shrinks but never zeros - circle has no corners
- RFE is unstable with correlated features; stability selection (subsample + refit) is more robust
- Variance threshold → correlation filter → MI ranking is a practical pipeline
- Feature selection preserves interpretability; dimensionality reduction (PCA) doesn't

### Data Splitting
- Train/val/test serve three distinct purposes: learn, tune, evaluate
- Test set must be touched ONCE - otherwise it becomes a second validation set
- Stratification essential for imbalanced classes; for regression, bin target first (quantile binning preferred)
- Time series: NEVER shuffle; chronological split only; purging/embargo for overlapping features
- Group splits prevent same-entity leakage (patient, user, etc.)
- Cross-validation: K-fold for small data; 5-fold standard, 10-fold more stable but 2x cost

### Data Leakage
- Fitting preprocessors on full data before splitting = leakage
- Target encoding without CV folds = leakage
- Using future features in time series = leakage
- Feature computed from target (e.g., "approved_amount" predicting "loan_approved") = leakage
- Telltale sign: suspiciously high val accuracy that craters in production
- Real-world examples: hospital mortality with "total blood transfused", loan default with "last payment date"

### Interview Depth
- Senior ML engineers expected to explain WHY each method works, not just HOW to use it
- Must articulate curse of dimensionality intuitively
- Must identify leakage sources from feature descriptions alone
- Must choose splitting strategy based on data characteristics
