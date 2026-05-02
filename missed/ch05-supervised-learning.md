# Missing Topics: Ch05 Supervised Learning

Now I have enough information from multiple sources. Let me compile the comprehensive findings into the required markdown file.

Based on my research across multiple interview guides (InterviewQuery, Devinterview-io, alirezadir/Machine-Learning-Interviews, khangich/machine-learning-interview), scikit-learn documentation, and ML curricula, here are the comprehensive findings of missing topics for Chapter 5:

---

## Summary

Chapter 5 covers the fundamentals well (linear models, trees, ensembles, SVMs, time series, online learning, sparse/kernel methods) but is missing several high-interview-frequency and practically important supervised learning topics. The biggest gaps are: (1) **Gradient Boosting Deep Dive** (XGBoost/LightGBM/CatBoost internals — the #1 most asked ML interview topic for applied roles), (2) **Probability Calibration**, (3) **Nearest Neighbor Methods**, (4) **Advanced Regression Techniques**, (5) **Imbalanced Learning in depth**, (6) **Recommender Systems basics**, (7) **Survival Analysis**, (8) **Gaussian Processes**, (9) **Multi-label/Ordinal classification**, and (10) **Active Learning**.

## Key Sources

- **Devinterview-io/supervised-learning-interview-questions** — 70 fundamental interview questions covering supervised learning breadth
- **alirezadir/Machine-Learning-Interviews:src/ml-fundamental.md** — FAANG interview study guide listing essential ML topics
- **khangich/machine-learning-interview** — Minimum viable ML interview plan with links to boosting, quantile regression, SMOTE
- **InterviewQuery** (interviewquery.com) — 2025 ML interview questions covering system design, algorithms, case studies
- **scikit-learn documentation** — Calibration module (1.16), Gaussian Processes (1.7), and full supervised learning API

## Findings — Missing Topics

Here is the complete markdown content for the missed topics file:

---

# Chapter 5: Supervised Learning — Missing Topics

## 1. Gradient Boosting Deep Dive (XGBoost / LightGBM / CatBoost)

**Why critical:** This is the single most asked supervised learning interview topic for applied ML/data science roles. Every FAANG interview guide lists "explain XGBoost" and "compare gradient boosting frameworks."

### Topics to cover:
- **XGBoost internals**: Regularized objective (L1+L2 on leaf weights), exact greedy split finding vs. approximate algorithm, weighted quantile sketch, sparsity-aware split finding, shrinkage & column subsampling, system design (cache-aware access, out-of-core computation, block structure for parallel learning)
- **LightGBM innovations**: Gradient-based One-Side Sampling (GOSS), Exclusive Feature Bundling (EFB), histogram-based split finding (discretize continuous features into bins), leaf-wise tree growth (vs. XGBoost's level-wise), categorical feature handling natively
- **CatBoost specifics**: Ordered boosting (prevents target leakage/prediction shift), symmetric oblivious decision trees, native categorical encoding (ordered target statistics), GPU training architecture
- **Comparison table**: Training speed, memory usage, handling of categorical features, default hyperparameters, overfitting tendency, missing value handling
- **Hyperparameter tuning strategies**: learning_rate vs n_estimators trade-off, max_depth/num_leaves, min_child_weight, subsample/colsample_bytree, regularization params (lambda, alpha, min_split_gain), early stopping, Bayesian optimization (Optuna/Hyperopt)
- **When to use which**: CatBoost for heavy categorical data, LightGBM for large datasets with speed requirements, XGBoost for robustness and wide ecosystem support

**Sources:** khangich/machine-learning-interview (lists "Random forest vs GBDT" and "Explain boosting"), alirezadir/Machine-Learning-Interviews:src/ml-fundamental.md:lines covering "Boosting → Adaboost, GBM, XGBoost", InterviewQuery question on "bagging vs boosting"

---

## 2. Probability Calibration

**Why critical:** Production ML systems (ad CTR prediction, medical diagnosis, risk scoring) need well-calibrated probabilities, not just correct rankings. Frequently asked in applied ML interviews.

### Topics to cover:
- **What is calibration**: Predicted probability should match empirical frequency (if model says 80% → ~80% of those cases should be positive)
- **Reliability diagrams** (calibration curves): Plotting predicted probability bins vs. fraction of positives
- **Platt scaling**: Fitting a logistic regression on classifier outputs (sigmoid calibration), works well with small calibration sets
- **Isotonic regression**: Non-parametric calibration, fits a monotonically increasing step function, needs more data than Platt scaling
- **Which classifiers need calibration**: SVMs (sigmoid-shaped miscalibration), Random Forests (biased toward 0.5), Naive Bayes (push toward 0/1), Logistic Regression (generally well-calibrated)
- **Brier score**: Metric for assessing calibration quality
- **Expected Calibration Error (ECE)**: Weighted average of per-bin calibration errors
- **Temperature scaling** (for neural networks): Single scalar parameter applied to logits before softmax
- **Multi-class calibration**: Extension challenges and approaches

**Source:** scikit-learn documentation module 1.16 "Probability Calibration" — covers CalibratedClassifierCV, reliability diagrams, Platt scaling, isotonic regression

---

## 3. K-Nearest Neighbors & Approximate Nearest Neighbors

**Why critical:** KNN is a fundamental non-parametric method asked in virtually every ML fundamentals interview. ANN is critical for production recommendation/search systems.

### Topics to cover:
- **KNN theory**: Distance metrics (Euclidean, Manhattan, Minkowski, Cosine), choice of K (bias-variance), weighted KNN, computational complexity O(nd) for brute force
- **Curse of dimensionality**: Why KNN degrades in high dimensions, distance concentration phenomenon
- **Decision boundaries**: How KNN creates Voronoi tessellation, comparison to parametric models
- **Approximate Nearest Neighbors (ANN)**: For scaling to millions/billions of points
  - Locality-Sensitive Hashing (LSH): Random projections, hash families for different distance metrics
  - Tree-based methods: KD-trees, Ball trees (and when they fail in high dimensions)
  - Graph-based methods: HNSW (Hierarchical Navigable Small World) — state of the art for ANN
  - Quantization methods: Product Quantization (PQ), ScaNN
- **Libraries**: FAISS (Facebook), Annoy (Spotify), ScaNN (Google), Milvus, Pinecone
- **Applications**: Recommendation systems, semantic search, anomaly detection

**Source:** alirezadir/Machine-Learning-Interviews:src/ml-fundamental.md lists "K-Nearest Neighbors (KNN)" as core interview question; InterviewQuery lists "Compare K-means and KNN algorithms" as common question

---

## 4. Advanced Regression Techniques

**Why critical:** Linear regression variants are commonly asked to test depth beyond basics. Quantile regression specifically listed in khangich's ML interview guide.

### Topics to cover:
- **Quantile regression**: Predicting conditional quantiles (not just mean), pinball loss function, use in prediction intervals, applications in finance/demand forecasting
- **Robust regression**: RANSAC, Huber regression, Theil-Sen estimator — handling outliers without removing them
- **Bayesian linear regression**: Prior on weights, posterior distribution, predictive uncertainty quantification, comparison to frequentist ridge regression
- **Polynomial regression pitfalls**: Overfitting with high-degree polynomials, Runge's phenomenon, why regularization or splines are preferred
- **Spline regression**: Basis splines (B-splines), natural cubic splines, knot placement, comparison to polynomial regression
- **Generalized Linear Models (GLMs)**: Poisson regression (count data), negative binomial regression, gamma regression (positive continuous), link functions
- **Elastic Net**: Combining L1 and L2 penalties, when to use vs. pure Lasso/Ridge, mixing parameter selection

**Source:** khangich/machine-learning-interview explicitly lists "Quantile regression" as study topic; alirezadir lists "least squares, residuals, linear vs multivariate regression" — suggesting depth expected

---

## 5. Imbalanced Learning (In Depth)

**Why critical:** Nearly every real-world classification problem has class imbalance. Multiple interview guides list this as essential (fraud detection, medical diagnosis, churn prediction).

### Topics to cover:
- **Resampling methods**:
  - SMOTE (Synthetic Minority Oversampling Technique): How it generates synthetic examples via interpolation between neighbors
  - ADASYN (Adaptive Synthetic Sampling): Density-based generation — more synthetics near decision boundary
  - Borderline-SMOTE: Only oversample minority samples near the border
  - Random undersampling: Risks of information loss
  - Tomek Links & Edited Nearest Neighbors: Cleaning overlapping regions
- **Cost-sensitive learning**: Assigning higher misclassification cost to minority class, class_weight parameter, custom loss functions
- **Algorithmic approaches**: One-class SVM, isolation forest for extreme imbalance, ensemble approaches (EasyEnsemble, BalanceCascade, RUSBoost)
- **Evaluation under imbalance**: Why accuracy is misleading, Precision-Recall curves (preferred over ROC for severe imbalance), F-beta score, Matthews Correlation Coefficient (MCC), Cohen's Kappa
- **Threshold tuning**: Moving decision threshold based on business costs, optimizing for specific operating points
- **Stratified sampling**: Maintaining class proportions in train/test splits and cross-validation

**Source:** khangich/machine-learning-interview lists "SMOTE synthetic minority over-sampling technique" as key fundamental; alirezadir lists "Imbalanced data" under "Handling data" section; InterviewQuery's fraud detection questions involve imbalanced learning

---

## 6. Recommender Systems (Supervised Learning Perspective)

**Why critical:** Collaborative filtering and matrix factorization are supervised/semi-supervised techniques asked in virtually every big tech interview. InterviewQuery's #1 system design question is "Build Spotify's Discover Weekly."

### Topics to cover:
- **Collaborative filtering**: User-based CF vs. item-based CF, similarity measures (cosine, Pearson), cold start problem
- **Matrix factorization**: SVD, Non-negative Matrix Factorization (NMF), Alternating Least Squares (ALS), implicit vs explicit feedback
- **Content-based filtering**: Feature engineering for items, TF-IDF for text, combining item attributes with user preferences
- **Hybrid approaches**: Combining collaborative and content-based methods, weighted hybrid, switching hybrid, meta-level
- **Factorization Machines**: Generalization of matrix factorization to arbitrary feature interactions, connection to SVMs
- **Learning to Rank**: Pointwise (regression on relevance), pairwise (comparing document pairs), listwise (optimizing list metrics directly), NDCG, MAP metrics
- **Deep learning approaches**: Neural Collaborative Filtering (NCF), two-tower models, session-based recommendations with RNNs
- **Evaluation**: Hit rate, NDCG, MAP, coverage, diversity, A/B testing considerations

**Source:** InterviewQuery lists "How would you build Spotify's Discover Weekly?" as top question; Devinterview-io lists "Recommender Systems → Collaborative Filtering, Matrix Factorization" under supervised learning problems

---

## 7. Survival Analysis

**Why critical:** Critical for healthcare ML, customer churn prediction, predictive maintenance — domains with censored data. Increasingly asked in applied science interviews.

### Topics to cover:
- **Core concepts**: Survival function S(t), hazard function h(t), censoring (right-censored, left-censored, interval-censored), time-to-event data
- **Kaplan-Meier estimator**: Non-parametric survival curve estimation, confidence intervals, log-rank test for comparing groups
- **Cox Proportional Hazards model**: Semi-parametric model, hazard ratio interpretation, partial likelihood estimation, proportional hazards assumption and testing it
- **Accelerated Failure Time (AFT) models**: Parametric approach (Weibull, log-normal, log-logistic distributions), when to prefer over Cox PH
- **Machine learning extensions**: Random Survival Forests, gradient boosting for survival (XGBoost survival), DeepSurv (neural network Cox model)
- **Applications**: Customer churn (time to churn), predictive maintenance (time to failure), clinical trials (time to event), credit risk (time to default)
- **Libraries**: lifelines (Python), scikit-survival, PySurvival

**Source:** Not covered in any section of current chapter; frequently appears in healthcare ML and applied science interview loops

---

## 8. Gaussian Processes for Regression & Classification

**Why critical:** Provides principled uncertainty quantification — increasingly important for Bayesian optimization, active learning, and safety-critical applications. Commonly asked in research-oriented interviews.

### Topics to cover:
- **GP fundamentals**: Function-space view vs. weight-space view, prior and posterior distributions over functions, mean and covariance functions
- **Kernel functions**: RBF (squared exponential), Matérn, periodic, rational quadratic, kernel composition (addition, multiplication)
- **GP Regression**: Predictive mean and variance in closed form, marginal likelihood for hyperparameter optimization, noise modeling
- **GP Classification**: Laplace approximation, EP (Expectation Propagation), non-Gaussian posterior challenge
- **Computational complexity**: O(n³) for exact GP, sparse approximations (inducing points, FITC, variational sparse GP)
- **When to use GPs**: Small to medium datasets, when uncertainty estimates are crucial, Bayesian optimization, surrogate modeling
- **Limitations**: Scalability (cubic in N), high dimensions, stationarity assumptions of common kernels
- **Connection to neural networks**: Neural Network Gaussian Processes (NNGP), infinite-width limit

**Source:** scikit-learn module 1.7 "Gaussian Processes" — GaussianProcessRegressor and GaussianProcessClassifier; InterviewQuery question on "quantifying uncertainty in predictions" references Gaussian Processes

---

## 9. Multi-Label Classification & Ordinal Regression

**Why critical:** Real-world classification often isn't simple multi-class. Multi-label (e.g., tagging articles with multiple topics) and ordinal targets (e.g., ratings 1-5) require specialized approaches.

### Topics to cover:
- **Multi-label classification**:
  - Problem transformation: Binary Relevance (independent classifiers per label), Classifier Chains (capturing label correlations), Label Powerset
  - Algorithm adaptation: ML-KNN, multi-label decision trees
  - Evaluation metrics: Hamming loss, subset accuracy, micro/macro F1, label-ranking average precision
  - Applications: Document tagging, medical diagnosis (multiple conditions), image annotation
- **Ordinal regression** (ordinal classification):
  - Why treating as regular classification loses ordering information
  - Threshold models: Proportional odds model, ordinal logistic regression
  - Reduction approaches: Converting to series of binary problems (Frank & Hall method)
  - Neural approaches: CORAL (Consistent Rank Logits)
  - Applications: Ratings prediction, severity scoring, education grading
- **Cost-sensitive classification**:
  - Non-uniform misclassification costs (e.g., false negative in cancer screening vs. false positive)
  - Cost matrix formulation, Bayes optimal decision under costs
  - MetaCost algorithm, cost-sensitive decision trees

**Source:** alirezadir/Machine-Learning-Interviews mentions "Extension of metrics to multi-class (n-ary) classification" — multi-label goes further; Devinterview-io lists classification subtypes

---

## 10. Active Learning

**Why critical:** Reduces labeling costs in production ML — increasingly relevant with expensive human annotation. Asked in applied ML interviews at companies with annotation pipelines.

### Topics to cover:
- **Core idea**: Iteratively selecting the most informative samples to label, minimizing annotation budget while maximizing model performance
- **Query strategies**:
  - Uncertainty sampling: Selecting samples where model is least confident (entropy, margin, least confidence)
  - Query-by-Committee (QBC): Maintaining ensemble of models, selecting samples with maximum disagreement
  - Expected Model Change: Selecting samples that would most change the model
  - Expected Error Reduction: Selecting samples that would most reduce generalization error
  - Diversity/representativeness: Ensuring queries cover the input space
- **Pool-based vs. stream-based vs. membership query synthesis**
- **Batch-mode active learning**: Selecting multiple samples at once, balancing informativeness and diversity
- **Stopping criteria**: When to stop querying
- **Applications**: Medical image annotation, NLP labeling, autonomous driving data curation, scientific discovery
- **Connection to Bayesian optimization**: Acquisition functions parallel query strategies

---

## 11. Model Interpretability & Explainability (for Supervised Models)

**Why critical:** Regulatory requirements (GDPR right to explanation), debugging models, building trust. Asked in virtually every senior ML interview.

### Topics to cover:
- **Intrinsic interpretability**: Linear model coefficients, decision tree paths, rule extraction
- **Post-hoc explanations**:
  - SHAP (SHapley Additive exPlanations): Game-theoretic feature attribution, TreeSHAP for tree ensembles, KernelSHAP for any model
  - LIME (Local Interpretable Model-agnostic Explanations): Local surrogate models, perturbation-based
  - Partial Dependence Plots (PDP): Marginal effect of features
  - Individual Conditional Expectation (ICE) plots
  - Permutation feature importance
- **Global vs. local explanations**
- **Fairness metrics**: Demographic parity, equalized odds, calibration across groups
- **Attention as explanation** (limitations and debates)

---

## 12. Naive Bayes & Probabilistic Classifiers

**Why critical:** Fundamental supervised learning algorithm frequently asked in interviews. alirezadir's guide lists it under "Bayesian algorithms" as essential.

### Topics to cover:
- **Naive Bayes variants**: Gaussian NB, Multinomial NB (text classification), Bernoulli NB, Complement NB
- **Independence assumption**: When it's violated and why NB still works (discrimination vs. estimation)
- **Laplace smoothing**: Handling zero probabilities for unseen feature values
- **Generative vs. discriminative**: NB as generative model, relationship to logistic regression (NB is its generative counterpart)
- **When NB beats more complex models**: Small datasets, high dimensions, text classification baseline
- **Linear Discriminant Analysis (LDA)**: Gaussian class-conditional distributions, dimensionality reduction + classification, Fisher's criterion, connection to Naive Bayes with Gaussian features

**Source:** alirezadir/Machine-Learning-Interviews lists "Naive Bayes, MAP estimation, ML estimation" under Statistical ML; InterviewQuery asks about LDA; Devinterview-io question on LDA

---

## 13. Evaluation Metrics Deep Dive

**Why critical:** Every interview asks "how would you evaluate this model?" Depth beyond accuracy/F1 is expected.

### Topics to cover:
- **Classification metrics in depth**: PR-AUC vs ROC-AUC (when to prefer which), Matthews Correlation Coefficient, Cohen's Kappa, log loss/cross-entropy
- **Regression metrics beyond MSE/MAE**: MAPE (and its issues with zeros), symmetric MAPE, R² pitfalls, quantile losses, RMSE vs MAE for different error distributions
- **Ranking metrics**: NDCG, MAP, MRR, precision@K, recall@K
- **Statistical significance in model comparison**: McNemar's test, paired t-test on cross-validation scores, bootstrap confidence intervals
- **Business metrics alignment**: Connecting ML metrics to business KPIs, decision-theoretic evaluation
- **Lift charts and cumulative gains**: Used in marketing/credit scoring

---

## 14. Feature Engineering & Selection for Supervised Learning

**Why critical:** "Features determine your ceiling, algorithms determine how close you get to it." Top interview topic per InterviewQuery and alirezadir.

### Topics to cover:
- **Encoding categorical variables**: One-hot, target encoding, frequency encoding, embedding layers, hashing trick (for high-cardinality), James-Stein estimator
- **Feature selection methods**: Filter (mutual information, chi-squared, ANOVA), Wrapper (recursive feature elimination, forward/backward selection), Embedded (L1 regularization, tree-based importance)
- **Feature interactions**: Polynomial features, crossing features, automated interaction detection
- **Handling missing data**: Imputation strategies (mean/median/mode, KNN imputation, MICE/iterative imputation, missingness as feature)
- **Target leakage**: How it occurs, how to detect and prevent it
- **Feature scaling**: When it matters (distance-based, gradient-based) vs. when it doesn't (trees)

**Source:** InterviewQuery question "You have a categorical variable with thousands of distinct values; how would you encode it?"; alirezadir lists "Feature selection → Feature importance"

---

## 15. Hyperparameter Optimization

**Why critical:** Practical skill tested in coding interviews and system design. Goes beyond grid search.

### Topics to cover:
- **Grid search**: Exhaustive but exponential in dimensions
- **Random search**: Why it outperforms grid search (Bergstra & Bengio 2012) — important dimensions get better coverage
- **Bayesian optimization**: Gaussian Process surrogate, acquisition functions (EI, UCB, PI), sequential model-based optimization
- **Tools**: Optuna (TPE sampler, pruning), Hyperopt, Ray Tune, Weights & Biases sweeps
- **Multi-fidelity methods**: Successive halving, Hyperband, BOHB
- **Practical heuristics**: Learning rate schedules, early stopping as implicit regularization, warm-starting

---

## Priority Ranking (by interview frequency and practical importance)

| Priority | Topic | Interview Frequency | Practical Importance |
|----------|-------|-------------------|---------------------|
| 🔴 P0 | Gradient Boosting Deep Dive (XGBoost/LightGBM/CatBoost) | Very High | Very High |
| 🔴 P0 | Imbalanced Learning | Very High | Very High |
| 🔴 P0 | Evaluation Metrics Deep Dive | Very High | High |
| 🟠 P1 | Probability Calibration | High | Very High |
| 🟠 P1 | KNN & Approximate Nearest Neighbors | High | High |
| 🟠 P1 | Feature Engineering & Selection | High | Very High |
| 🟠 P1 | Recommender Systems | High | High |
| 🟠 P1 | Model Interpretability (SHAP/LIME) | High | Very High |
| 🟡 P2 | Naive Bayes & Probabilistic Classifiers | Medium-High | Medium |
| 🟡 P2 | Advanced Regression (Quantile, Bayesian, GLMs) | Medium | High |
| 🟡 P2 | Hyperparameter Optimization | Medium | High |
| 🟡 P2 | Multi-label / Ordinal / Cost-sensitive | Medium | High |
| 🟢 P3 | Survival Analysis | Medium (domain-specific) | High |
| 🟢 P3 | Gaussian Processes | Medium (research roles) | Medium |
| 🟢 P3 | Active Learning | Low-Medium | Medium |

---

## Citations

- `Devinterview-io/supervised-learning-interview-questions:README.md` — 70 interview questions covering supervised learning fundamentals, classification types, recommender systems
- `alirezadir/Machine-Learning-Interviews:src/ml-fundamental.md` — FAANG study guide listing KNN, Naive Bayes, XGBoost, feature selection, imbalanced data as essential topics
- `khangich/machine-learning-interview:README.md` — Lists SMOTE, quantile regression, RF vs GBDT comparison, logistic regression from scratch as key preparation items
- InterviewQuery (interviewquery.com) — 2025 ML interview questions including system design (Spotify recommendations), encoding categorical features, bagging vs boosting, calibration
- scikit-learn docs (scikit-learn.org/stable/modules/calibration.html) — Platt scaling, isotonic regression, reliability diagrams, CalibratedClassifierCV
- scikit-learn docs (scikit-learn.org/stable/modules/gaussian_process.html) — GP regression/classification, kernel functions, O(n³) complexity, sparse approximations
