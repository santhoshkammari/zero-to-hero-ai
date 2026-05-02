# Missing Topics: Ch04 Ml Fundamentals

Now I have a comprehensive picture. Let me compile the findings into the markdown file. Here's my analysis:

**What's ALREADY covered in Chapter 4:**
- PAC learning, VC dimension, Rademacher complexity (learning-theory-foundations.html)
- No Free Lunch theorem (ml-overview-workflow.html, learning-theory-foundations.html, nice-to-know.html)
- Bias-complexity tradeoff formal treatment (learning-theory-foundations.html)
- Curse of dimensionality (nice-to-know.html)
- Double descent, benign overfitting, NTK, implicit regularization, grokking (learning-theory-foundations.html)
- SHAP basics (model-selection.html:589-618)
- Bayesian optimization, TPE, Optuna (model-selection.html:476-520)
- AutoML brief mention (model-selection.html:623-631)
- Learning curves interpretation (bias-variance-overfitting.html:456-520)
- A/B testing brief mention (evaluation-metrics.html:668, ml-overview-workflow.html)
- Semi-supervised learning overview (ml-overview-workflow.html:379-385)
- ML debugging: dead neurons, gradient issues, data leakage detection, distribution shift (ml-implementation-patterns.html)
- Calibration (evaluation-metrics.html:531-544)
- Conformal prediction (nice-to-know.html:377)
- Goodhart's Law (nice-to-know.html:391)

**What's covered in OTHER chapters (not Ch 4):**
- Ensemble theory: stacking, bagging, boosting (ch05/ensemble-methods.html)
- Bandits, multi-armed bandits (ch05/online-learning-bandits.html)
- SHAP, LIME, PDP, ICE, counterfactual explanations, TCAV, mechanistic interp (ch16/dl-interpretability-methods.html)
- Fairness: demographic parity, equalized odds, calibration, impossibility theorem, four-fifths rule (ch16/fairness-bias-detection.html)
- Active learning mentioned in ch03

Now let me write the gap analysis:

Based on my thorough analysis, here are the findings written as the markdown content for the gap file:

---

# Ch 04 — ML Fundamentals & Core Concepts: Missing Topics

## Summary

Chapter 4 is strong on learning theory (PAC, VC dimension, Rademacher complexity, double descent) and core workflow (bias-variance, cross-validation, evaluation metrics, optimization). However, after cross-referencing with Stanford CS 229, Cornell CS 4780, Chip Huyen's ML Interviews Book, Shalev-Shwartz/Ben-David's "Understanding Machine Learning," Hastie/Tibshirani ESL, Christoph Molnar's Interpretable ML Book, and multiple interview prep resources, several important ML fundamentals gaps remain. Notably: topics either only briefly mentioned without proper depth (AutoML, A/B testing, SHAP) or entirely absent (Hyperband/BOHB, error analysis methodology, multi-task learning, causal reasoning basics, sample complexity intuitions).

**Key caveat:** Several requested topics are already well-covered in other chapters — ensemble theory (Ch 5), fairness metrics (Ch 16), LIME/SHAP/PDP (Ch 16), multi-armed bandits (Ch 5). This analysis focuses on what's missing from the BOOK as a whole AND what deserves deeper treatment specifically in Ch 4 as "ML Fundamentals."

---

## 1. AutoML & Advanced Hyperparameter Optimization (SIGNIFICANT GAP)

### What's Currently Covered
- Bayesian optimization / TPE: solid explanation (`ch04/model-selection.html:476-484`)
- Optuna with pruning: good practical coverage (`ch04/model-selection.html:487-520`)
- AutoML: brief 2-paragraph mention of Auto-sklearn and FLAML (`ch04/model-selection.html:623-631`)

### What's Missing

**1a. Multi-Fidelity Optimization: Hyperband & BOHB**
- **Hyperband** (Li et al., 2018) — the dominant paradigm for expensive evaluations. Successive Halving + adaptive resource allocation. Not mentioned anywhere in Ch 4.
- **BOHB** (Bayesian Optimization + Hyperband, Falkner et al. 2018) — combines TPE with Hyperband's early stopping. State-of-the-art for neural architecture tuning.
- **Successive Halving** as a concept — allocate budget, evaluate all configs cheaply, prune bottom half, repeat. The conceptual foundation for Hyperband.
- **Why it matters for interviews:** "How would you efficiently tune hyperparameters for a model that takes 4 hours to train?" is a standard senior MLE question. The answer is multi-fidelity methods.
- **Source:** Li et al., "Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization" (JMLR 2018); Falkner et al., "BOHB: Robust and Efficient Hyperparameter Optimization at Scale" (ICML 2018)

**1b. Neural Architecture Search (NAS) Basics**
- The book's nav references a `ch16/s10.html` section on NAS, but Ch 4 has zero treatment of NAS as a concept.
- At minimum, Ch 4 should cover: the search space (what choices are being made), the search strategy (random, RL-based, evolutionary, differentiable/DARTS), and the evaluation strategy (full training vs. weight sharing vs. supernet).
- **NAS-Bench** as a concept for reproducible NAS research.
- **Source:** Zoph & Le, "Neural Architecture Search with Reinforcement Learning" (ICLR 2017); Liu et al., "DARTS: Differentiable Architecture Search" (ICLR 2019)

**1c. AutoML Frameworks: Deeper Treatment**
- Current coverage is two paragraphs. Missing: **AutoGluon** (Amazon's framework, dominant on tabular benchmarks), **H2O AutoML**, comparison table of frameworks by use case.
- Missing the concept of **meta-learning** in AutoML — how Auto-sklearn uses past dataset performance to warm-start.
- Missing **ensemble selection** in AutoML — how AutoGluon builds multi-layer stacking ensembles automatically.
- **Source:** AutoGluon documentation (auto.gluon.ai); Feurer et al., "Auto-sklearn 2.0" (JMLR 2022)

### Suggested Section Title
**"AutoML & Efficient Hyperparameter Search"** — expand from current 2 paragraphs to a full subsection covering Hyperband, BOHB, NAS basics, and framework comparison.

---

## 2. Experiment Design for ML: A/B Testing & Statistical Rigor (SIGNIFICANT GAP)

### What's Currently Covered
- A/B testing mentioned in one sentence each in two places:
  - `ch04/ml-overview-workflow.html:635` — "Consider A/B testing new models"
  - `ch04/evaluation-metrics.html:668` — "Use A/B tests to measure what actually happens"
- Statistical significance briefly touched in cross-validation (`ch04/cross-validation.html:576-620`)

### What's Missing

**2a. A/B Testing for ML Models — Full Treatment**
- How to design an A/B test for model deployment: randomization unit, sample size calculation, test duration
- **Power analysis**: how to determine required sample size before running a test (Type I error α, Type II error β, minimum detectable effect)
- **Multiple testing correction**: Bonferroni, Benjamini-Hochberg FDR — when you A/B test multiple metrics simultaneously
- **Peeking problem**: why checking results early inflates false positives; sequential testing as the fix
- **Interference/network effects**: when treatment on user A affects user B's outcome (common in social/marketplace ML)
- **Source:** Kohavi et al., "Trustworthy Online Controlled Experiments" (Cambridge, 2020) — the definitive reference; widely tested in FAANG interviews

**2b. Offline Evaluation vs. Online Evaluation Bridge**
- The chapter mentions both but doesn't connect them systematically
- **Interleaving experiments** — faster than A/B tests for ranking systems (used at Netflix, Spotify)
- **Counterfactual evaluation / off-policy evaluation** — evaluating a new model using logged data from an old model (inverse propensity scoring)
- This is a critical gap because it bridges Ch 4 (evaluation) with production ML
- **Source:** Gilotte et al., "Offline A/B Testing for Recommender Systems" (WSDM 2018); Li et al., "Unbiased Offline Evaluation" (WSDM 2011)

**2c. Statistical Hypothesis Testing for Model Comparison**
- Currently cross-validation section mentions p-values but doesn't explain the tests
- Missing: **paired t-test on CV folds**, **McNemar's test** for classifier comparison, **Wilcoxon signed-rank test**
- **5×2 cross-validation paired t-test** (Dietterich, 1998) — the recommended test for comparing two classifiers
- Corrected resampled t-test to avoid inflated Type I error from correlated CV folds
- **Source:** Dietterich, "Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms" (Neural Computation, 1998); Demšar, "Statistical Comparisons of Classifiers over Multiple Data Sets" (JMLR 2006)

### Suggested Section Title
**"Experiment Design & Statistical Testing for ML"** — a new section covering A/B testing design, power analysis, multiple comparisons, and proper statistical tests for model comparison.

---

## 3. ML Debugging & Error Analysis Methodology (MODERATE GAP)

### What's Currently Covered
- Dead neuron detection, gradient diagnosis, data leakage detection, distribution shift detection (`ch04/ml-implementation-patterns.html:906-1051`)
- Learning curves for diagnosing underfitting/overfitting (`ch04/bias-variance-overfitting.html:456-520`)

### What's Missing

**3a. Systematic Error Analysis Framework**
- **Confusion matrix deep analysis**: beyond computing it — stratified error analysis by subgroup, feature value ranges, data slices
- **Error categorization taxonomy**: systematic labeling of misclassified examples into error types (e.g., "label noise," "hard examples," "distribution gap," "missing feature")
- **Andrew Ng's error analysis workflow** from CS 229: manually examine 100 misclassified dev set examples, categorize errors, estimate ceiling for each category, prioritize
- This is a STANDARD interview question: "Your model accuracy is 90%. How do you get to 95%?" The answer is systematic error analysis, not random model swapping.
- **Source:** Stanford CS 229 section notes on "Advice on Applying ML"; Andrew Ng's "Machine Learning Yearning" (chapters 14-19)

**3b. Ablation Studies**
- Zero mention in the chapter. Ablation = systematically removing components to measure their contribution.
- Feature ablation: remove features one at a time, measure performance drop
- Architecture ablation: remove layers, attention heads, skip connections
- Data ablation: train on different data subsets to understand contribution
- **Why it matters:** Every ML paper requires ablation tables. Every senior interview asks "how do you know component X is helping?"
- **Source:** Standard in all top ML conference papers (NeurIPS, ICML, ICLR)

**3c. Failure Mode Analysis**
- **Spurious correlations detection**: how to identify when models latch onto shortcuts (e.g., "hospital tag → pneumonia" in CheXpert)
- **Stress testing**: adversarial examples, edge cases, out-of-distribution detection basics
- **Slice-based evaluation**: evaluating model on meaningful data subgroups (Slice Finder, Domino)
- **Source:** Oakden-Rayner et al., "Hidden Stratification" (2020); Eyuboglu et al., "Domino: Discovering Systematic Errors" (ICLR 2022)

### Suggested Section Title
**"Error Analysis & ML Debugging Methodology"** — expand from code-level debugging to systematic error investigation.

---

## 4. Interpretability Basics in ML Workflow (MINOR GAP — mostly in Ch 16)

### What's Currently Covered
- SHAP: good introduction with code in model-selection (`ch04/model-selection.html:589-620`)
- Permutation importance: one paragraph (`ch04/model-selection.html:620`)
- Full SHAP/LIME/PDP/ICE/counterfactuals/TCAV treatment exists in Ch 16

### What's Missing FROM Chapter 4 Specifically

**4a. LIME as Complement to SHAP**
- SHAP is covered but LIME is not mentioned in Ch 4 at all. Since the model-selection section discusses "explaining yourself," LIME deserves a paragraph as the faster/simpler alternative.
- When to use LIME vs. SHAP: LIME for quick debugging, SHAP for rigorous analysis

**4b. Partial Dependence Plots (PDP) and ICE**
- Not in Ch 4. These are the simplest global interpretability tools and belong in the ML workflow discussion.
- One paragraph + one code example would complete the interpretability toolkit in Ch 4's model selection workflow.

**4c. Feature Importance Methods Comparison**
- The chapter mentions permutation importance but doesn't compare: impurity-based importance (biased toward high-cardinality), permutation importance (model-agnostic but slow), SHAP importance (theoretically grounded).
- A comparison table would help practitioners choose.

### Recommendation
**Don't create a new section** — expand the existing SHAP subsection in model-selection to include a brief LIME mention and a feature importance comparison table. The full treatment rightly lives in Ch 16.

---

## 5. Semi-Supervised Learning: Deeper Treatment (MODERATE GAP)

### What's Currently Covered
- Brief conceptual overview: one paragraph mentioning pseudo-labeling, consistency regularization, FixMatch, MixMatch (`ch04/ml-overview-workflow.html:379-385`)

### What's Missing

**5a. Core Algorithms**
- **Self-training** (pseudo-labeling): train on labeled data → predict on unlabeled → add high-confidence predictions as labels → retrain. The simplest SSL method. Deserves explicit algorithm description.
- **Co-training** (Blum & Mitchell, 1998): two models trained on different feature views, each labels data for the other. Classic theoretical result.
- **Label propagation / label spreading**: graph-based approach where labels spread through a similarity graph. Implemented in scikit-learn (`sklearn.semi_supervised.LabelPropagation`).
- **Consistency regularization**: the key modern principle — if you perturb an input slightly, the prediction shouldn't change. Foundation of MixMatch, FixMatch, UDA.

**5b. When SSL Helps and When It Hurts**
- The **cluster assumption** and **smoothness assumption** — the theoretical conditions under which SSL works
- SSL can HURT when assumptions are violated (Oliver et al., "Realistic Evaluation of Deep Semi-Supervised Learning Algorithms," NeurIPS 2018)
- This is a common interview question: "When would semi-supervised learning fail?"

### Suggested Treatment
Expand the existing semi-supervised paragraph into a 2-page subsection with algorithm sketches for self-training and label propagation + a "when it works / when it fails" callout.

---

## 6. Multi-Task Learning Basics (GAP — Not Covered Anywhere)

### What's Currently Covered
- Transfer learning is covered in Ch 9
- Multi-task learning: NO dedicated coverage found anywhere in the book

### What's Missing

**6a. Core Concepts**
- **Hard parameter sharing** vs. **soft parameter sharing**: shared trunk with task-specific heads vs. separate networks with regularization
- **When to use MTL**: related tasks with shared structure, limited data per task, tasks that act as regularizers for each other
- **Task weighting**: how to balance losses from multiple tasks (uncertainty weighting, GradNorm)
- **Negative transfer**: when jointly training hurts performance on one or more tasks

**6b. Practical Examples**
- NLP: BERT fine-tuning on multiple downstream tasks simultaneously
- Computer vision: object detection = classification + bounding box regression (inherently multi-task)
- Recommendation: predicting click AND purchase AND dwell time

**6c. Connection to Inductive Bias**
- MTL as implicit regularization — auxiliary tasks prevent overfitting on the main task
- This connects beautifully to Ch 4's existing coverage of inductive bias and regularization

### Suggested Treatment
- **Source:** Caruana, "Multitask Learning" (Machine Learning, 1997); Ruder, "An Overview of Multi-Task Learning in Deep Neural Networks" (2017 survey)
- Add as a subsection in "Nice to Know" or as part of the ML Overview section's "Modern Paradigms."

---

## 7. Sample Complexity & Data Requirements (MODERATE GAP)

### What's Currently Covered
- PAC learning's sample complexity bound (`ch04/learning-theory-foundations.html:333-378`)
- Learning curves showing data vs. performance (`ch04/bias-variance-overfitting.html:456-520`)

### What's Missing

**7a. Practical Sample Size Estimation**
- Rules of thumb: 10× features for linear models, 1000+ per class for neural nets, etc.
- **Learning curve extrapolation**: fitting a power law to predict performance at larger data sizes
- **How to decide "do I need more data?"** — the most common practical question, addressed theoretically (PAC bounds) but not practically
- Chip Huyen's ML Interviews Book explicitly asks: "How do you know you've collected enough samples to train your ML model?" (`chiphuyen/ml-interviews-book:contents/7.2-sampling-and-creating-training-data.md`, Q9)

**7b. Data-Efficient Methods Overview**
- When you CAN'T get more data: data augmentation, transfer learning, few-shot learning, active learning
- **Active learning** basics: uncertainty sampling, query-by-committee, expected model change — the framework for choosing which examples to label next
- Active learning is mentioned in Chip Huyen's book (Q1 in 7.1-basics.md) and in interview questions, but not covered in Ch 4 of this book
- **Source:** Settles, "Active Learning" (Morgan & Claypool, 2012)

### Suggested Treatment
Add practical sample size heuristics to the ML Overview or Bias-Variance section, and add active learning as a "Nice to Know" topic.

---

## 8. Ensemble Theory Deep Dive (MINOR GAP — Mostly in Ch 5)

### What's Currently Covered
- Ch 5 has comprehensive ensemble coverage: bagging, boosting, random forests, XGBoost, LightGBM, CatBoost, stacking (`ch05/ensemble-methods.html`)
- Ch 4 mentions ensembles as a variance reduction tool (`ch04/bias-variance-overfitting.html`)

### What's Missing (from the BOOK, not just Ch 4)

**8a. Bayesian Model Averaging (BMA)**
- Not found anywhere in the book. BMA weights models by their posterior probability rather than using learned stacking weights.
- Connection to model uncertainty: BMA naturally provides uncertainty estimates.
- **Source:** Hoeting et al., "Bayesian Model Averaging: A Tutorial" (Statistical Science, 1999)

**8b. Mixture of Experts (MoE)**
- Modern relevance: MoE is the architecture behind Mixtral, Switch Transformer
- The gating mechanism that selects which expert processes each input
- May be better placed in a deep learning chapter, but the core concept (conditional computation, learned routing) is an ensemble principle

### Recommendation
BMA could be added as a "Nice to Know" item in Ch 5. MoE probably belongs in a DL architecture chapter.

---

## 9. Causal Reasoning Basics for ML (GAP — Not Covered Anywhere)

### What's Currently Covered
- Correlation vs. causation: implicitly discussed in data leakage sections
- No formal treatment of causal inference concepts found anywhere in the book

### What's Missing

**9a. Why ML Practitioners Need Causal Thinking**
- **Simpson's Paradox**: a trend that appears in several groups reverses when the groups are combined — directly relevant to model evaluation and feature selection
- **Confounders in feature selection**: why correlated features can mislead; the difference between predictive and causal features
- **When prediction ≠ intervention**: a model can predict hospital readmission perfectly but changing the predicted features might not reduce readmission
- **Collider bias**: conditioning on a collider creates spurious associations — relevant to data filtering and sample selection

**9b. Practical Relevance**
- Common interview question: "Your model shows Feature X is the most important predictor of Y. Should we intervene on X?"
- A/B testing is a causal method — connecting experiment design to causal language
- **Source:** Pearl, "The Book of Why" (2018) — accessible introduction; Hernán & Robins, "Causal Inference: What If" (2020) — practical treatment

### Suggested Treatment
Add 1-2 pages as a "Nice to Know" topic covering Simpson's Paradox, confounders, and the prediction-vs-intervention distinction. This fills a genuine gap that no other chapter addresses.

---

## 10. Distribution Shift & Domain Adaptation (MODERATE GAP)

### What's Currently Covered
- Distribution shift detection code (`ch04/ml-implementation-patterns.html:1018-1051`)
- Brief mentions in evaluation metrics (`ch04/evaluation-metrics.html:664`)
- Input/output drift monitoring mentioned in workflow (`ch04/ml-overview-workflow.html:635`)

### What's Missing

**10a. Taxonomy of Distribution Shifts**
- **Covariate shift**: P(X) changes but P(Y|X) stays the same — most common, fixable with importance weighting
- **Label shift / prior probability shift**: P(Y) changes but P(X|Y) stays the same
- **Concept drift**: P(Y|X) changes — the relationship itself changes. Hardest to handle.
- **Dataset shift** as the umbrella term
- This taxonomy is in d2l.ai's treatment and is standard in Quiñonero-Candela et al., "Dataset Shift in Machine Learning" (MIT Press, 2009)

**10b. Detection and Adaptation Methods**
- **Importance weighting** for covariate shift correction
- **Population Stability Index (PSI)** for monitoring feature distributions
- **Kolmogorov-Smirnov test** and **Maximum Mean Discrepancy (MMD)** for detecting shift
- When to retrain vs. when to adapt
- **Source:** Sugiyama et al., "Covariate Shift Adaptation" (MIT Press, 2012); Rabanser et al., "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift" (NeurIPS 2019)

### Suggested Treatment
Consolidate the scattered drift mentions into a cohesive subsection, possibly in "Nice to Know" or expanding the existing implementation patterns section.

---

## Priority Ranking

| Priority | Topic | Reason | Suggested Location |
|----------|-------|--------|--------------------|
| 🔴 HIGH | Experiment Design (A/B testing, power analysis, statistical tests) | Zero coverage; critical for interviews and production ML | New section |
| 🔴 HIGH | AutoML deep dive (Hyperband, BOHB, NAS basics, framework comparison) | Currently 2 paragraphs; heavily tested in interviews | Expand model-selection |
| 🔴 HIGH | Error Analysis Methodology (systematic debugging, ablation studies) | Standard interview question; no systematic treatment | New section or expand ML debugging |
| 🟡 MEDIUM | Semi-Supervised Learning algorithms (self-training, label propagation) | Currently 1 paragraph; core ML paradigm needing depth | Expand ml-overview-workflow |
| 🟡 MEDIUM | Distribution Shift taxonomy | Scattered mentions; needs consolidation | Expand nice-to-know or new subsection |
| 🟡 MEDIUM | Multi-Task Learning basics | Not covered anywhere in the book | Nice to Know or ml-overview |
| 🟡 MEDIUM | Sample Complexity practical guidance + Active Learning | Theory exists (PAC) but practical guidance missing | Expand existing sections |
| 🟢 LOW | Causal reasoning basics (Simpson's paradox, confounders) | Valuable but tangential to core ML fundamentals | Nice to Know |
| 🟢 LOW | LIME + PDP brief mention in Ch 4 | Full treatment in Ch 16; just needs cross-reference | Expand model-selection SHAP section |
| 🟢 LOW | Bayesian Model Averaging | Niche; stacking/boosting well-covered in Ch 5 | Ch 5 Nice to Know |
| ⚪ SKIP | Fairness metrics in Ch 4 | Thoroughly covered in Ch 16 | Just add cross-reference |
| ⚪ SKIP | Ensemble theory in Ch 4 | Thoroughly covered in Ch 5 | Just add cross-reference |
| ⚪ SKIP | Multi-armed bandits for model selection | Thoroughly covered in Ch 5 | Just add cross-reference |

---

## Sources Consulted

1. **Stanford CS 229** syllabus (cs229.stanford.edu) — learning theory, model selection, practical advice
2. **Cornell CS 4780** (Kilian Weinberger) — ML debugging, bias-variance, empirical risk minimization
3. **Chip Huyen, "Introduction to ML Interviews"** (github.com/chiphuyen/ml-interviews-book) — 200+ interview questions covering ML fundamentals
4. **Shalev-Shwartz & Ben-David, "Understanding Machine Learning"** (Cambridge, 2014) — PAC, VC dim, structural risk minimization, no free lunch
5. **Christoph Molnar, "Interpretable Machine Learning"** 3rd ed (christophm.github.io) — SHAP, LIME, PDP, ICE, LOFO
6. **Kohavi et al., "Trustworthy Online Controlled Experiments"** (Cambridge, 2020) — A/B testing methodology
7. **InterviewQuery.com** ML interview questions — system design, algorithms, theory
8. **d2l.ai** — distribution shift taxonomy
9. **AutoGluon** (auto.gluon.ai) — modern AutoML framework patterns
10. **Andrew Ng, "Machine Learning Yearning"** — error analysis methodology
