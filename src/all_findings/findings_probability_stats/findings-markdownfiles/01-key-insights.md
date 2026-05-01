# Key Insights from Research

## Core Themes for Rewrite
1. **Brandon Rohrer style**: Build from absolute zero, personal confession opening, running example throughout, vulnerability moments, toy examples for every concept
2. **Running example**: Build a spam filter from scratch — starts tiny (3 emails), grows naturally
3. **Concept ladder**: Uncertainty → Probability basics → Conditional probability → Bayes → Distributions → MLE/MAP → Hypothesis testing → Bayesian inference → Real-world applications
4. **Rest stop**: After Bayes' theorem and distributions — reader has useful mental model

## What the Current Version Gets Wrong
- Reads like a textbook/reference, not a journey
- No running example threading through
- No personal confession opening
- No vulnerability moments
- Bullet-point listicles for explanations
- Jumps into formulas without motivation
- No rest stop

## Key Topics to Cover (Interview Depth)
- Bayes' theorem with base rate fallacy (medical test example is good, keep it)
- MLE → loss function connection (MSE = Gaussian MLE, cross-entropy = Bernoulli MLE)
- MAP → regularization (Gaussian prior = L2, Laplace = L1)
- Distributions: when to use which (Gaussian, Beta, Dirichlet, Poisson)
- CLT and why it matters for SGD batch size
- Hypothesis testing, p-value pitfalls
- A/B testing (Bayesian vs frequentist)
- Chain rule → autoregressive models (GPT)
- MCMC vs Variational Inference
- Thompson sampling / multi-armed bandits

## Vulnerability Moments
1. "I avoided probability for years because every explanation started with the axioms"
2. "I still sometimes confuse P(A|B) with P(B|A)"
3. "The base rate result shocked me the first time"
4. "I'm still developing my intuition for why variational inference works as well as it does"
5. "No one really has a clean mental model for high-dimensional distributions"

## Analogies to Recur
1. **Weather forecast analogy**: Probability as degree of belief, updating with new evidence
2. **Courtroom analogy**: Prior (innocent until proven guilty), evidence (likelihood), verdict (posterior)
