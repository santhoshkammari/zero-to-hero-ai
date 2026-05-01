# Web Search Insights Summary

## Data Leakage Types (Critical Interview Topic)
- **Target leakage**: feature derived from target (e.g., account_closed_flag for churn prediction)
- **Temporal leakage**: future data leaking into past predictions (random split on time series)
- **Group leakage**: same entity in train+test (patient data, user data)
- **Normalization leakage**: computing mean/std on full dataset including test
- Prevention: chronological splits, GroupKFold, fit transforms only on train

## Data Contracts & Validation
- Formal agreements between data producers and consumers on schema, freshness, quality
- Great Expectations: define "expectations" as tests on data
- Pandera: type-safe schema validation for Pandas DataFrames
- In data mesh: domains publish data products with contract-enforced APIs
- ML teams benefit: contracts prevent silent pipeline breakage from upstream schema changes

## Imbalanced Datasets (Production Reality)
- Class weights preferred over SMOTE in production (simpler, less overfitting risk)
- SMOTE only on training data — never validation/test
- Use precision/recall/F1/AUC-ROC, never accuracy alone
- Extreme class weights can destabilize training

## Synthetic Data
- SDV (CTGAN, GaussianCopula, TVAE) for tabular
- Fundamental limitation: can't generate edge cases you haven't seen
- Faker for realistic dummy data (names, addresses)

## Tabular Augmentation
- Harder than image augmentation because feature semantics matter
- Mixup: interpolate features+labels between pairs (don't mix categoricals arithmetically)
- Feature noise/jittering: small Gaussian noise on continuous features
- Row dropout: simulate missing data
