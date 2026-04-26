# SVM Practical Aspects and Modern Relevance

## When SVMs Still Win (2024)
- Text classification with TF-IDF: linear SVM competitive with transformers on small corpora
- Genomics/bioinformatics: few samples, many features (p >> n)
- Small datasets (hundreds to low thousands): margin maximization provides strong regularization
- No GPU required, fast inference, deterministic

## When to Use Alternatives
- Large datasets (>50k samples): O(n²)-O(n³) training is painful
- Tabular data: LightGBM/XGBoost faster and often more accurate
- Images/text/audio: deep learning with pretrained models dominates

## Historical Arc
- Vapnik & Cortes 1995: "Support-Vector Networks" paper
- Dominated ML from late 1990s to early 2010s
- Won many competitions (text categorization, digit recognition, bioinformatics)
- Fell when deep learning showed end-to-end feature learning > hand-engineered features + SVM
- Still a gold standard in certain niches

## Multi-class Strategies
- One-vs-Rest (OvR): k classifiers, each one class vs all others
- One-vs-One (OvO): k(k-1)/2 classifiers, each pair of classes
- sklearn default for SVC: OvO (faster per model, but quadratic number of models)

## Platt Scaling
- SVMs don't output probabilities natively
- Platt scaling: fit sigmoid to SVM scores on held-out data
- P(y=1|f) = 1/(1 + exp(Af + B))
- A and B learned by minimizing NLL on validation set
- In sklearn: probability=True enables this (slower training, uses internal CV)

## Nu-SVM
- Alternative parameterization using ν ∈ (0,1]
- ν upper bounds fraction of margin errors and lower bounds fraction of support vectors
- More interpretable than C in some cases

## SMO Algorithm
- Sequential Minimal Optimization (Platt 1998)
- Breaks QP into smallest subproblems (2 variables at a time)
- O(n²) to O(n³) in practice
- What libsvm (and sklearn's SVC) actually uses under the hood
