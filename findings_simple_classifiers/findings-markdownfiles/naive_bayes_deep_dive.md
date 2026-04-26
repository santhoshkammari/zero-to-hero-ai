# Naive Bayes Deep Dive Findings

## Core Idea
- Bayes theorem: P(class|features) ∝ P(features|class) × P(class)
- "Naive" = conditional independence assumption
- Factorizes joint into product of individual feature probs
- Only need d parameters per class instead of exponential joint

## Why Naive Works
- Classification needs correct RANKING, not calibrated probabilities
- Errors in individual probs often cancel out
- Decision boundary is what matters, not exact probability values
- Probability VALUES are garbage - pushed toward 0 and 1

## Variants
1. GaussianNB: continuous features, assumes normal distribution per class
   - Estimates mean + variance per feature per class
   - No hyperparameters to tune
   - Fragile if features aren't normal

2. MultinomialNB: non-negative counts (word frequencies)
   - Workhorse for text classification
   - Models class as multinomial over feature counts
   - Fast, effective with TF-IDF

3. BernoulliNB: binary features (word presence/absence)
   - Explicitly penalizes ABSENCE of features
   - Better for short documents
   - Ignores frequency, focuses on presence

4. ComplementNB: complement of each class
   - Designed for imbalanced classes (Rennie et al. 2003)
   - Uses statistics from all OTHER classes
   - Better minority class recall
   - Often outperforms MultinomialNB on benchmarks

## Laplace Smoothing
- Prevents zero-probability catastrophe
- P(word|class) = (count + α) / (total + α × vocab_size)
- α=1: add-one smoothing (standard)
- Larger α: more aggressive smoothing toward uniform
- Without it, one unseen word kills entire prediction

## Log Space Computation
- Multiplying many small probs → numerical underflow
- Solution: work in log space, turn products into sums
- log P(class) + Σ log P(word_i|class)
- Numerically stable, standard implementation technique

## Text Classification
- NB + TF-IDF: classic combo, remarkably effective
- On small text data, often beats neural nets
- 20 newsgroups classified in under a second
- Always start text project with this baseline

## Strengths
- Blazing fast training (single pass) and prediction
- Works with tiny datasets
- Handles high-dimensional sparse data (50k+ features)
- Naturally multiclass
- Great baseline/diagnostic tool

## Weaknesses
- Poor probability calibration
- Correlated features double-counted
- Cannot learn feature interactions
- Gaussian assumption often violated in practice
