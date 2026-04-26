# EDA Workflow Insights

## Key Research Findings

### 1. Anscombe's Quartet / Datasaurus Dozen
- Four datasets with IDENTICAL summary stats (mean, variance, correlation, regression line) look completely different when plotted
- Datasaurus Dozen extends this: 13 datasets, same stats, wildly different shapes (dinosaur, star, circle)
- Core lesson: summary statistics are necessary but NEVER sufficient — always visualize

### 2. Missing Data Mechanisms (MCAR/MAR/MNAR)
- MCAR: missingness unrelated to any data (random deletion) — simple imputation OK
- MAR: missingness depends on OBSERVED variables (younger people skip income) — need model-based imputation
- MNAR: missingness depends on the MISSING VALUE ITSELF (high earners don't report income) — hardest, needs domain knowledge
- Detection: Little's MCAR test, logistic regression on missingness indicator, domain reasoning
- Impact: MNAR silently biases models; most practitioners wrongly assume MCAR

### 3. Correlation Pitfalls
- Simpson's Paradox: trend reverses when groups are combined (classic: UC Berkeley gender bias)
- Spurious correlations: ice cream sales vs drowning (both caused by summer heat)
- Zero Pearson ≠ independence (non-linear relationships can show zero correlation)
- Spearman for monotonic, Pearson for linear only
- Cramér's V for categorical-categorical associations

### 4. Data Leakage Detection
- Suspiciously high AUC (>0.95) is a red flag
- Feature importance: if one feature dominates, check if it's a proxy for the target
- Features that only exist AFTER the event you're predicting = temporal leakage
- Target encoding on full dataset before split = leakage
- Random shuffle experiment: shuffle target, retrain — if performance stays high, leakage confirmed

### 5. Production EDA
- Schema validation (Pandera, Great Expectations) — enforce column types, ranges, constraints
- Data contracts with upstream teams
- Distribution drift monitoring (EvidentlyAI, whylogs)
- EDA as CI/CD step, not ad-hoc notebook exercise
- Push filtering to source (SQL WHERE, not Python filter)

### 6. Senior Interview Expectations
- Not just "run describe()" — explain WHY each analysis matters
- Tailor EDA to domain (fraud detection EDA ≠ NLP EDA)
- Discuss automation and reproducibility
- Know statistical tests and their assumptions
- Communicate findings to non-technical stakeholders
