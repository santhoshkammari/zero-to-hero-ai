# Rewrite Plan for ch06/s03 — Anomaly Detection

## Brandon Rohrer Style Requirements
- Personal confession opening
- Running example throughout (factory sensor monitoring)
- Build from absolute zero: what is "normal"?
- Toy examples with walkthrough
- Rest stop after core methods
- Vulnerability moments (4-5)
- Recurring analogies (neighborhood density, random forest chopping)
- No listicle explanations — narrative prose
- Every term defined inline on first use

## Concept Ladder (dependency order)
1. The core flip: learn normal, flag different
2. Statistical baseline: z-score (simplest possible)
3. Limitation: correlated features → Mahalanobis distance
4. Limitation: outliers corrupt covariance → MCD
5. Isolation Forest: random partitioning intuition
6. IF internals: path length, scoring formula, contamination
7. Extended IF: axis-aligned bias fix
8. REST STOP
9. LOF: local density comparison
10. LOF internals: reachability distance, LRD, LOF score
11. One-Class SVM: kernel boundary
12. Autoencoders: reconstruction error
13. LSTM/VAE autoencoders for time series
14. Evaluation: PR-AUC, Precision@k
15. Production: drift, retraining, threshold tuning
16. Method selection guide

## Running Example
- Small factory with 3 temperature sensors monitoring a machine
- Start with 5 readings, grow as complexity demands
- Normal readings cluster, anomalies are unusual combinations

## Analogies
1. "Neighborhood watch" — density-based detection (LOF)
2. "Random chopping" — isolation forest splitting
3. "Copying machine" — autoencoder reconstruction

## Vulnerability Moments
1. Opening confession about avoiding anomaly detection
2. Admit Mahalanobis formula is intimidating
3. Still developing intuition for why IF normalization works
4. Threshold setting is more art than science
5. No one fully agrees on best evaluation metric
