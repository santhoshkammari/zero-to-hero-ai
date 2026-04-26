# Web Search Research Summary

## Bayes' Theorem
- #1 confusion: P(A|B) vs P(B|A) — prosecutor's fallacy
- Base rate fallacy: even 99% accurate tests produce mostly false positives for rare diseases
- Spam classification as canonical Bayesian example
- Medical diagnosis example is universally used and effective

## MLE/MAP/Regularization
- MLE = no prior = no regularization
- MAP + Gaussian prior = L2 regularization (weight decay)
- MAP + Laplace prior = L1 regularization (sparsity)
- Every loss function is negative log-likelihood under a distributional assumption
- MSE = Gaussian MLE, Cross-entropy = Bernoulli/Categorical MLE

## Distributions
- Gaussian dominates due to CLT
- Beta: conjugate prior for Bernoulli, perfect for modeling probabilities
- Dirichlet: multivariate Beta, used in LDA topic models
- Student-t: robust to outliers, heavy tails

## CLT and SGD
- Mini-batch gradient = mean of per-sample gradients
- By CLT, approximately Gaussian for reasonable batch sizes
- Variance decreases as 1/batch_size
- Some noise is beneficial (escapes local minima)

## Hypothesis Testing
- p-value is NOT probability that H0 is true
- Statistical significance ≠ practical significance
- With large samples, even tiny meaningless effects become "significant"
- Always report effect size alongside p-value

## A/B Testing
- Frequentist: fixed sample size, p-values, used by Google/LinkedIn
- Bayesian: sequential analysis, probability statements, used by Netflix/Booking.com
- Thompson sampling: Bayesian approach to exploration/exploitation

## MCMC vs VI
- Metropolis-Hastings: simple, works for discrete params, slow in high dimensions
- HMC/NUTS: gradient-based, efficient for continuous high-dim, used by Stan/PyMC
- VI: optimization-based approximation, fast but approximate, powers VAEs
