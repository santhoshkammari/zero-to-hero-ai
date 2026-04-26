# Anomaly Detection — Core Research Findings

## Key Insights from Research

### Isolation Forest Internals
- Path length is the anomaly score — short path = anomaly, long path = normal
- Anomaly score formula: s(x,n) = 2^(-l(x)/c(n)) where c(n) is the expected BST path length
- c(n) = 2*H(n-1) - 2(n-1)/n where H is harmonic number
- Score ~1 = anomaly, ~0.5 = uncertain, ~0 = normal
- Original IF has axis-aligned split bias — fails on diagonal anomalies
- Extended IF (Hariri et al., 2021) uses random hyperplane splits to fix this

### LOF Internals
- Reachability distance: reach_dist(A,B) = max(k-distance(B), dist(A,B)) — smooths density
- LRD = inverse of avg reachability distance to k-neighbors
- LOF = avg ratio of neighbor LRDs to point's own LRD
- LOF ≈ 1 = normal, LOF >> 1 = outlier
- Key insight: it's LOCAL — compares to neighbors, not global distribution

### Mahalanobis + MCD
- Standard Mahalanobis breaks when outliers contaminate covariance estimate
- MCD finds smallest-determinant covariance subset (≥50% of data) — robust to contamination
- sklearn EllipticEnvelope implements this
- Chicken-and-egg: need clean data to estimate covariance, but need covariance to find outliers

### Autoencoders for Anomaly Detection
- Train on normal only, flag high reconstruction error
- Threshold setting: percentile on validation set (95th/99th), ROC-based if labels exist
- LSTM autoencoders for time series — capture temporal dependencies
- VAE adds probabilistic scoring via KL divergence
- Production: recalibrate threshold periodically for drift

### One-Class SVM / SVDD
- OCSVM: hyperplane separating data from origin in kernel space
- SVDD: smallest hypersphere enclosing normal data
- With RBF kernel, equivalent in practice
- nu parameter controls outlier fraction
- O(n²)-O(n³) training — doesn't scale

### Production Challenges
- Concept drift types: sudden, gradual, incremental, recurring
- Label scarcity/delay — can't evaluate quickly
- Retraining strategies: scheduled, event-triggered, online learning
- Shadow deployment for safety
- Monitor reconstruction error distribution shift

### Interview-Depth Insights
- Why not classification? 99.97% accuracy by always predicting normal
- Contamination parameter is the critical knob in IF
- PR-AUC >> ROC-AUC for imbalanced anomaly detection
- LOF novelty=True for production (train on clean, score new)
- Extended IF fixes axis-aligned bias of original IF
