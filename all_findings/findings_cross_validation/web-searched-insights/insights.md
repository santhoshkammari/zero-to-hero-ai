# Web Search Insights for Cross-Validation

## Key Insights Gathered

1. **K-fold bias-variance tradeoff is about the ESTIMATOR, not the model** — k controls the bias-variance of your performance estimate, not the model itself

2. **LOOCV paradox** — despite maximum training data, has high variance because training sets are nearly identical, making scores correlated

3. **Purged cross-validation** (López de Prado) — for financial time series, removes training samples whose label windows overlap test period + embargo period

4. **Preprocessing leakage is the #1 real-world CV mistake** — fit_transform before splitting = information from test fold leaks into training

5. **Nested CV is the gold standard** for unbiased performance when also tuning — outer loop never touched during tuning

6. **Kohavi (1995)** — empirical evidence that 10-fold is sweet spot for most problems

7. **Statistical comparison** — Nadeau-Bengio corrected test for repeated k-fold (standard paired t-test assumes independence which folds don't have)

8. **Group leakage** — medical imaging (same patient in train+test), NLP (same author), recommender systems (same user)

9. **Monte Carlo / ShuffleSplit** — random subsampling alternative to k-fold, more flexible split sizes

10. **Interview depth** — senior interviewers look for: preprocessing inside folds, temporal awareness, group awareness, nested CV knowledge, understanding of what high fold variance means
