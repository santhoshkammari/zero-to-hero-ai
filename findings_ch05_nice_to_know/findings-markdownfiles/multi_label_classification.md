# Multi-Label Classification Findings

## Core Distinction
- Multiclass: exactly ONE label per sample (mutually exclusive)
- Multi-label: MULTIPLE labels per sample simultaneously
- Examples: movie genres, paper tags, medical diagnosis codes

## Three Main Approaches
1. **Binary Relevance**: independent binary classifier per label
   - Simple, scalable, but ignores label correlations
   - In deep learning: sigmoid output per label + binary cross-entropy
2. **Classifier Chains**: each classifier gets previous predictions as features
   - Captures label dependencies
   - Order matters — ensemble of chains (ECC) helps
3. **Specialized architectures**: attention/graph networks for label dependencies

## Deep Learning Approach
- Sigmoid activation (not softmax!) on output layer
- Binary cross-entropy loss (BCEWithLogitsLoss in PyTorch)
- Key distinction: softmax forces probabilities to sum to 1 (mutually exclusive), sigmoid doesn't

## Interview Gotcha
- Using softmax for multi-label is a common mistake
- Evaluation metrics differ: subset accuracy, hamming loss, micro/macro F1
- Label imbalance is typically worse than class imbalance in multiclass
