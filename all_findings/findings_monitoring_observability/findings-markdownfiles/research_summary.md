# Monitoring & Observability Research Summary

## Key Concepts
- Data drift: covariate shift (P(X) changes), concept drift (P(Y|X) changes), label/prior probability shift (P(Y) changes)
- PSI: bins data, compares proportions, sum of (Ai - Ei) * ln(Ai/Ei). Thresholds: <0.1 stable, 0.1-0.25 moderate, >0.25 significant
- KS test: max distance between two CDFs, nonparametric, returns p-value. Best for continuous features
- KL divergence: asymmetric, measures info lost when approximating one dist with another. Needs binning for continuous
- PSI is actually a symmetrized form related to KL divergence

## Shadow Mode / Champion-Challenger
- Champion serves real traffic, challenger runs in parallel logging predictions
- Both see same data, only champion affects users
- Compare when ground truth arrives, promote if better

## Retraining Triggers
- Time-based (scheduled), performance-based, drift-based, data-volume-based, manual
- Best practice: combine multiple triggers

## NannyML CBPE
- Estimates performance WITHOUT ground truth using model confidence calibration
- Key assumption: calibration relationship holds post-deployment

## Tools Comparison
- Evidently: open source, great visualizations, batch monitoring
- WhyLabs: enterprise SaaS, privacy-first, real-time
- NannyML: open source, specializes in delayed labels/CBPE
- Prometheus+Grafana: DIY, ops teams know it

## Observability Stack
- Three pillars: logs, metrics, traces (applied to ML)
- OpenTelemetry as standard
- Correlation IDs across all three pillars
