# Data Quality & Preparation — Research Findings

## Key Frameworks & Tools
- **Great Expectations**: Declarative expectations, JSON-stored, checkpoints, HTML reports. Best for team-wide data documentation.
- **Pandera**: Lightweight schema validation for pandas. Perfect inside pipeline code without full GX infra.
- **TFDV (TensorFlow Data Validation)**: Schema inference + drift detection, Google/TFX ecosystem.
- **Deequ**: Amazon/Spark-based. Unit tests for big data.
- **Evidently AI**: ML-specific monitoring — data drift, target drift, quality. Rich dashboards.
- **Soda Core**: SQL-based data quality checks. Cloud-first.

## Drift Detection Methods
- **KS Test**: Non-parametric, compares CDFs. Good for continuous univariate data.
- **PSI**: Binned distribution comparison. Standard in finance. PSI < 0.1 = no drift, 0.1-0.2 = moderate, ≥ 0.2 = significant.
- **Chi-square**: For categorical features.
- **Evidently** computes all three automatically with visual reports.

## Label Quality
- **Cleanlab / Confident Learning**: Flags likely mislabeled examples using model prediction probabilities vs given labels.
- Cross-validate, collect out-of-sample probabilities, identify where model confident in different class than label.
- Practical: can clean 5-10% of labels in real datasets, often improving model accuracy.

## Weak Supervision (Snorkel)
- Labeling functions: Python heuristics that guess labels. Each noisy, but combining many = good.
- LabelModel resolves conflicts between LFs.
- Production results: 70% reduction in manual labeling, 15% model performance boost in real cases.
- Trade: label quality for quantity. Works for spam, info extraction, medical coding. Bad for subjective tasks.

## Active Learning
- Uncertainty sampling: label examples model is most confused about.
- Query by committee: ensemble disagreement.
- Real results: 50-80% labeling cost reduction vs random sampling.
- Need infrastructure for train/score/label/retrain loop.

## Data Contracts
- Formal agreements between data producers and consumers.
- Define schemas, SLAs, quality metrics.
- Prevent breaking changes in data pipelines.
- Growing adoption in data mesh architectures.

## Data Augmentation
- CutMix: patch from one image onto another, mix labels proportionally. Good for occlusion, detection.
- MixUp: linear blend of two images + labels. Good for classification, noisy labels.
- Both are strong regularizers. Can be combined.
- Text augmentation: back-translation (best quality), synonym replacement, LLM paraphrasing (most expensive).
- TTA: average predictions over augmented copies. 1-2% accuracy boost at inference.
