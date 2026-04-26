# ML Overview & Workflow — Research Findings

## Key Concepts to Cover

### 1. ML Taxonomy
- Supervised (Classification + Regression)
- Unsupervised (Clustering, Dimensionality Reduction, Anomaly Detection)
- Reinforcement Learning (Agent, Environment, Reward, Policy)
- Semi-supervised (few labels + lots unlabeled)
- Self-supervised (no human labels, pretext tasks — GPT, BERT, CLIP)

### 2. Inductive Bias
- Every algorithm makes assumptions about the data
- Linear regression assumes linearity; decision trees assume axis-aligned splits; NNs assume compositionality
- Inductive bias is what lets ML generalize at all — without it, infinite models fit any finite dataset
- This connects directly to No Free Lunch

### 3. No Free Lunch Theorem
- No single algorithm is universally best across all problems
- Performance is entirely problem-dependent
- Practical implication: you MUST experiment, you MUST use domain knowledge
- This is why model selection is a skill, not a lookup table

### 4. Generalization Theory (Light Touch)
- PAC learning: "with enough data, probably approximately correct"
- VC dimension: capacity/flexibility of model family
- Sample complexity: more complex model → need more data
- Occam's Razor in ML: prefer simpler models unless complexity is justified

### 5. End-to-End ML Workflow
1. Problem Definition (business → ML translation)
2. Data Collection & Exploration
3. Data Preprocessing & Feature Engineering
4. Model Selection & Training
5. Evaluation
6. Deployment & Monitoring

### 6. Data Leakage — The Silent Killer
- Train-test contamination
- Target leakage
- Temporal leakage
- Preprocessing leakage
- Prevention: Pipelines, time-based splits, entity-based splits

### 7. When NOT to Use ML
- Rules are clear and stable → use if/else
- Data is insufficient
- Full interpretability required
- Cost of errors is unacceptable
- Start simple, add ML when rules break down

## Key Insights from Research
- Self-supervised learning is THE paradigm shift of modern ML (GPT, CLIP, etc.)
- Data-centric ML (focus on data quality) is the 2024 trend
- Hybrid approaches (rules + ML) are very common in production
- Real-world leakage examples: hospital readmission models, fraud detection, loan default
- Inductive bias and NFL theorem are deeply connected — bias is what makes learning possible
