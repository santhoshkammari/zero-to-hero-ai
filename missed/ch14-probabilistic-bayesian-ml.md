# Missing Topics: Ch14 Probabilistic Bayesian Ml

Now I have a thorough picture. Let me compile the findings into the missing topics report. Based on my analysis:

**Already covered well:**
- Bayesian fundamentals (Bayes theorem, priors, conjugates, MAP vs MLE, credible intervals, decision theory)
- Graphical models (Bayesian networks, MRFs, d-separation, plate notation)
- Exact inference (variable elimination, belief propagation, junction trees)
- MCMC (Metropolis-Hastings, Gibbs, HMC, NUTS - mentioned but brief)
- VI (ELBO, mean-field, amortized inference, reparameterization trick, VAE connection)
- Sequential models (HMMs, Kalman filters, particle filters)
- PPLs (PyMC, Stan, NumPyro, Pyro)
- GPs & BO (kernels, regression, sparse GPs, EI/UCB/PI, multi-fidelity)
- BNNs (MC Dropout, Bayes by Backprop, Laplace approximation)
- Uncertainty (aleatoric vs epistemic)
- Bayesian deep learning (3 approaches)
- EP, Information geometry, PAC-Bayes, Conformal prediction
- Bayesian nonparametrics (Dirichlet process, IBP)
- Causal inference (comprehensive: RCTs, propensity scores, IPW, DiD, IV, RDD, SCMs, do-calculus, CATE, causal forests, uplift)

**Missing/Thin topics I can identify:**

Now let me provide my comprehensive findings:

Based on my thorough analysis of all six section files in Chapter 13, here is my complete report of what's covered and what's missing:

## Summary

The chapter is quite comprehensive, covering fundamentals through advanced topics. However, several important areas are either completely absent or only mentioned in passing (one sentence) without dedicated treatment. The biggest gaps are: (1) **MCMC convergence diagnostics** (mentioned in one sentence but never explained), (2) **Bayesian model comparison** (Bayes factors, marginal likelihood for model selection), (3) **Exponential family distributions**, (4) **Hierarchical/Empirical Bayes**, (5) **Normalizing flows for VI** (mentioned once but not explained), (6) **Deep ensembles** as a standalone method, (7) **Calibration metrics** (ECE, temperature scaling), (8) **Approximate Bayesian Computation** (likelihood-free inference), (9) **Stochastic VI and scalability tricks**, and (10) several advanced BO topics.

---

## Detailed Gap Analysis

### 1. MCMC Convergence Diagnostics (CRITICAL GAP — Interview Staple)
**Current coverage:** One sentence in `probabilistic-models-inference.html:642`: "Reviewers in Bayesian statistics will expect convergence diagnostics: R̂ < 1.01, effective sample sizes above 400, no divergent transitions, and trace plots that look like hairy caterpillars."

**What's missing:**
- **R̂ (Gelman-Rubin) statistic** — what it measures (between-chain vs within-chain variance), how to interpret it, split-R̂ improvement
- **Effective Sample Size (ESS)** — autocorrelation in chains, how ESS is computed, why 400+ is the threshold
- **Trace plots and rank plots** — visual diagnostics, what "hairy caterpillar" vs pathological chains look like
- **Divergent transitions** — what they indicate (regions of high curvature the integrator can't handle), how to fix them (reparameterization, increase adapt_delta)
- **Thinning** — when it helps vs wastes samples
- **Burn-in/warmup** — why and how much
- **ArviZ diagnostics workflow** — practical code for az.summary(), az.plot_trace(), az.plot_rank()

**Why it matters:** This is asked in virtually every ML interview involving Bayesian methods. "How do you know your MCMC has converged?" is a standard question.

---

### 2. Bayesian Model Comparison & Selection (MISSING)
**Current coverage:** WAIC and LOO-CV are briefly mentioned in `sequential-models-ppl.html:690`, marginal likelihood mentioned for GP hyperparameters. But there's no dedicated treatment of:

**What's missing:**
- **Bayes factors** — ratio of marginal likelihoods, interpretation scales (Jeffreys scale), when to use vs posterior predictive checks
- **Marginal likelihood / model evidence** — p(D|M), why it automatically penalizes complexity (Occam's razor), connection to ELBO
- **BIC as approximation to log Bayes factor**
- **Bayesian model averaging** — weighting predictions across multiple models by their posterior model probabilities
- **Savage-Dickey density ratio** — computing Bayes factors from posterior samples
- **Practical comparison: WAIC vs LOO-CV vs Bayes factors** — when each is appropriate

---

### 3. Exponential Family Distributions (MISSING — Foundational)
**Current coverage:** Zero. Not mentioned anywhere.

**What's missing:**
- **Canonical form**: p(x|η) = h(x) exp(η^T T(x) - A(η))
- **Natural parameters (η)** — connection to canonical link functions in GLMs
- **Sufficient statistics T(x)** — why they're "sufficient" (Fisher-Neyman factorization)
- **Log-partition function A(η)** — cumulant generating function, derivatives give moments
- **Why conjugate priors exist** for exponential family (mathematical reason)
- **Connection to maximum entropy** — exponential family distributions are max-entropy given moment constraints
- **Members**: Gaussian, Bernoulli, Poisson, Gamma, Dirichlet, Multinomial, Wishart
- **Connection to variational inference** — mean-field updates have closed form for exponential families

**Why it matters:** This is fundamental for understanding why conjugate priors work, how GLMs are constructed, and how CAVI updates are derived. Interview question: "Why does the exponential family lead to conjugate priors?"

---

### 4. Hierarchical Bayesian Models & Empirical Bayes (MISSING)
**Current coverage:** Zero explicit treatment. The chapter mentions "choosing priors" but never discusses hierarchical modeling.

**What's missing:**
- **Hierarchical priors / hyperpriors** — e.g., school test scores with group-level and individual-level parameters
- **Shrinkage and partial pooling** — the hallmark of hierarchical Bayes, borrowing strength across groups
- **The three levels**: complete pooling, no pooling, partial pooling — and why hierarchical models give the sweet spot
- **Empirical Bayes** — estimating hyperparameters from data (Type II MLE), when it's a reasonable shortcut vs full Bayes
- **James-Stein estimator** — the frequentist connection to shrinkage
- **Hierarchical models in PyMC** — practical code example
- **Multi-level models** — random effects, mixed effects, and the Bayesian perspective

**Why it matters:** Hierarchical models are one of the most practical applications of Bayesian methods (sports analytics, clinical trials, recommendation systems). "Explain partial pooling" is a common interview question.

---

### 5. Normalizing Flows for Variational Inference (THIN)
**Current coverage:** One sentence in `probabilistic-models-inference.html:611`: "Normalizing flows can represent complex, multimodal distributions."

**What's missing:**
- **Change of variables formula** — how transforming a simple base distribution through an invertible function gives a complex one
- **Planar flows, radial flows** — simple flow architectures
- **RealNVP, MAF, IAF** — coupling layers, autoregressive flows
- **Why flows help VI** — the variational family becomes much richer, tighter ELBO
- **Flow-based posterior approximation** — how to use flows as q(z|x) in VAEs
- **Comparison with mean-field** — when the extra complexity pays off
- **Connection to normalizing flows as generative models** (may be in the generative models chapter)

---

### 6. Stochastic Variational Inference & Scalability (MISSING)
**Current coverage:** The word "stochastic" appears once in the context of Pyro. No treatment of how VI scales to large datasets.

**What's missing:**
- **Stochastic VI (SVI)** — Hoffman et al. 2013, using minibatches to compute noisy but unbiased ELBO gradients
- **Natural gradient for VI** — why it converges faster than standard gradient
- **Black-box VI** — Ranganath et al. 2014, gradient estimators that work for any model
- **Score function estimator (REINFORCE)** vs **pathwise gradient (reparameterization trick)** — when each applies, variance reduction
- **Control variates** — reducing gradient variance in stochastic VI
- **Stochastic gradient Langevin dynamics (SGLD)** — bridging MCMC and SGD, scalable MCMC
- **Practical implications** — why modern PPLs can fit models on millions of data points

**Why it matters:** This is how VI actually works at scale. Without this, readers can't understand how PyTorch/JAX-based PPLs handle real-world datasets.

---

### 7. Deep Ensembles (THIN — Deserves Its Own Treatment)
**Current coverage:** One sentence in `sequential-models-ppl.html:726`: "Deep ensembles — training multiple independent networks and looking at their disagreement — are technically not Bayesian, but they provide excellent uncertainty estimates in practice."

**What's missing:**
- **Lakshminarayanan et al. 2017 paper** — the landmark work showing ensembles beat BNNs on uncertainty
- **Implementation details** — random initialization + shuffled data, how many ensemble members (5 is usually enough)
- **Why ensembles work so well** — functional diversity argument, connection to the posterior
- **Ensembles vs MC Dropout vs BNNs** — practical comparison (accuracy, calibration, compute cost)
- **Ensemble distillation** — compressing an ensemble into one network with uncertainty
- **Hyperparameter deep ensembles** — varying architecture/hyperparameters across ensemble members
- **Limitations** — N× compute cost, when ensembles disagree vs when they all confidently wrong

---

### 8. Calibration & Reliability (MISSING)
**Current coverage:** The word "calibrated" appears several times informally, but there's no treatment of how to measure or achieve calibration.

**What's missing:**
- **What calibration means formally** — P(Y=1 | f(X)=p) = p
- **Reliability diagrams** — plotting predicted probability vs observed frequency
- **Expected Calibration Error (ECE)** — the standard metric
- **Maximum Calibration Error (MCE)**
- **Temperature scaling** — the simplest post-hoc calibration method (single parameter T)
- **Platt scaling** — logistic regression on logits
- **Isotonic regression** — nonparametric calibration
- **Why modern neural nets are miscalibrated** — Guo et al. 2017 finding that deeper = worse calibration
- **Calibration vs sharpness** — you want both (well-calibrated AND sharp predictions)
- **Connection to conformal prediction** — conformal gives coverage guarantees, calibration gives pointwise accuracy

**Why it matters:** "How would you calibrate a model?" is a standard ML interview question. This bridges the gap between uncertainty quantification theory and production deployment.

---

### 9. Approximate Bayesian Computation / Simulation-Based Inference (MISSING)
**Current coverage:** The phrase "approximate Bayesian computation" appears once in `nice-to-know.html:359` but refers to VI in general, not the specific ABC method.

**What's missing:**
- **ABC rejection sampling** — simulate from the prior, keep samples where simulated data ≈ observed data
- **Summary statistics** — dimensionality reduction of data for comparison
- **ABC-SMC** — sequential Monte Carlo version with adaptive tolerances
- **When ABC is needed** — intractable likelihoods (population genetics, epidemiology, complex physics simulators)
- **Neural density estimation for SBI** — replacing ABC with learned posterior approximations (SNPE, SNLE, SNRE)
- **sbi library** — practical tool for simulation-based inference in Python

**Why it matters:** With the rise of complex simulators in science (climate, biology, physics), SBI is increasingly important. It's the go-to when you can simulate from a model but can't write down the likelihood.

---

### 10. Advanced Bayesian Optimization Topics (PARTIALLY COVERED)
**Current coverage:** EI, UCB, PI, multi-fidelity BO are all covered. Missing:

**What's missing:**
- **Batch/parallel BO** — selecting multiple points simultaneously (q-EI, q-UCB, Thompson sampling for batch)
- **High-dimensional BO** — challenges when d > 20, random embeddings (REMBO), trust regions (TuRBO)
- **Multi-objective BO** — Pareto frontiers, Expected Hypervolume Improvement
- **Constrained BO** — handling unknown constraints alongside the objective
- **BO with categorical/mixed spaces** — SMAC, TPE (mentioned briefly but not explained)
- **Knowledge gradient** — an alternative acquisition function
- **Entropy search / Predictive entropy search** — information-theoretic acquisition functions
- **BoTorch** — the modern library for BO in PyTorch (only Optuna is shown)

---

### 11. Decision Theory Depth (THIN)
**Current coverage:** Good introduction in `bayesian-fundamentals.html:490-531` covering Bayes-optimal action and A/B test example.

**What's missing:**
- **Expected Value of Information (EVOI)** — how much would it be worth to collect more data? When to stop an experiment?
- **Expected Value of Perfect Information (EVPI)** — upper bound on the value of any experiment
- **Value of Information in active learning** — connection to query strategies
- **Multi-armed bandits from Bayesian perspective** — Thompson sampling derivation
- **Sequential decision making** — Bayesian optimal stopping, secretary problem
- **Utility theory** — von Neumann-Morgenstern axioms, risk aversion, concave utility functions
- **Minimax decisions** — worst-case vs Bayesian decisions, connection to adversarial robustness

---

### 12. Factor Graphs (THIN)
**Current coverage:** Belief propagation is explained for trees and loopy graphs in `probabilistic-models-inference.html`. Factor graphs mentioned in the section description meta but not explained.

**What's missing:**
- **Factor graph formalism** — bipartite graph of variables and factors, why it generalizes both Bayesian networks and MRFs
- **Message passing on factor graphs** — variable-to-factor and factor-to-variable messages
- **Max-product / max-sum algorithm** — for MAP inference
- **Applications** — error-correcting codes (LDPC, turbo codes), combinatorial optimization
- **Variational message passing** — connection to mean-field VI on factor graphs

---

### 13. Bayesian Nonparametrics Depth (THIN)
**Current coverage:** Dirichlet Process and Chinese Restaurant Process explained. IBP mentioned in one paragraph.

**What's missing:**
- **Stick-breaking construction** — the constructive definition of a DP, GEM distribution
- **DP Mixture Models** — full model specification, inference via collapsed Gibbs sampling
- **Hierarchical Dirichlet Process (HDP)** — for topic modeling (replaces LDA's fixed K)
- **Indian Buffet Process depth** — Beta process, applications to latent feature models
- **Gaussian Process as a Bayesian nonparametric model** — connection between GPs and infinite-width BNNs (Neal 1996)
- **Pitman-Yor process** — power-law behavior, Zipf's law
- **Practical inference** — truncated representations, variational inference for DPMMs

---

### 14. Causal Inference — Missing Advanced Topics
**Current coverage:** Excellent and thorough. Covers RCTs, propensity scores, IPW, DiD, IV, RDD, SCMs, do-calculus, backdoor criterion, causal forests, doubly robust, uplift.

**What's still missing:**
- **Front-door criterion** — the other identification strategy (when backdoor fails)
- **Mediation analysis** — direct and indirect effects, causal mediation formula
- **Sensitivity analysis** — Rosenbaum bounds, E-values, how robust are results to unmeasured confounders?
- **Synthetic control methods** — Abadie et al., for comparative case studies
- **Bounds and partial identification** — Manski bounds when point identification fails
- **Transportability** — generalizing causal effects across populations
- **Interference / spillover effects** — when one unit's treatment affects another's outcome (SUTVA violations)

---

### 15. Bayesian Linear Regression (MISSING as explicit worked example)
**Current coverage:** The chapter never walks through the canonical Bayesian linear regression example.

**What's missing:**
- **Prior on weights** — p(w) = N(0, α⁻¹I)
- **Posterior derivation** — closed-form Gaussian posterior for weights
- **Posterior predictive distribution** — predictions with uncertainty bands
- **Connection to ridge regression** — MAP estimate equals ridge estimate
- **Evidence approximation** — learning α and β from data
- **Visual progression** — prior → posterior → predictive with increasing data

**Why it matters:** This is THE pedagogical example for Bayesian ML. It appears in every textbook (Bishop PRML Ch. 3, Murphy PML). It's the concrete example that makes all the abstract machinery tangible.

---

### 16. Variational Autoencoders — Deeper Treatment (THIN)
**Current coverage:** VAE loss and reparameterization trick are shown in `probabilistic-models-inference.html:621-632`.

**What's missing (if not covered in generative models chapter):**
- **Posterior collapse** — when the decoder ignores z, KL term goes to zero
- **β-VAE** — weighted ELBO for disentangled representations
- **Importance-weighted ELBO (IWAE)** — tighter bound with K importance samples
- **VQ-VAE** — discrete latent spaces
- **Hierarchical VAEs** — NVAE, VDVAE

*Note: This may belong in the Generative Models chapter (ch14). Should cross-reference.*

---

### 17. Empirical Bayes / Type II Maximum Likelihood (MISSING)
**Current coverage:** Not mentioned.

**What's missing:**
- **Definition** — estimate hyperparameters by maximizing marginal likelihood p(D|α)
- **Connection to hierarchical Bayes** — empirical Bayes ≈ point estimate of hyperparameters instead of full posterior
- **Sparse Bayesian Learning / Relevance Vector Machine** — automatic relevance determination (ARD)
- **When empirical Bayes is appropriate** — many groups with few observations each
- **Robbins' compound decision theory** — the frequentist justification

---

### 18. Common Interview Questions Not Addressed
Several classic Bayesian ML interview questions aren't clearly answerable from the chapter:

- "Explain the bias-variance tradeoff from a Bayesian perspective" (connection to posterior spread)
- "When would you use Bayesian methods vs frequentist?" (practical decision guide)
- "How does the choice of prior affect results with limited vs abundant data?"
- "Derive the posterior for a Gaussian with known variance" (worked example)
- "What happens when your prior is wrong?" (prior misspecification, robustness)
- "Explain the reparameterization trick and why it's needed" (covered briefly but could be more explicit)
- "What is the difference between generative and discriminative models from a Bayesian perspective?"
- "How would you implement Bayesian A/B testing?" (partially covered in fundamentals)

---

### 19. Stein Variational Gradient Descent (SVGD) (MISSING)
A particle-based inference method that bridges MCMC and VI:
- **Key idea** — transport a set of particles to approximate the posterior using kernelized gradient flow
- **Comparison** — fewer particles than MCMC, richer than parametric VI
- **Connection to score matching** and Stein discrepancy

---

### 20. Laplace Approximation for Model Selection (PARTIALLY COVERED)
The Laplace approximation is covered for BNNs in nice-to-know, but its use for marginal likelihood approximation and model comparison (the "evidence framework" of MacKay) is missing:
- **log p(D) ≈ log p(D|θ_MAP) + log p(θ_MAP) + (d/2)log(2π) - (1/2)log|H|**
- **Bayesian Information Criterion (BIC)** as a cruder Laplace approximation
- **MacKay's evidence framework** — iterative evidence maximization

---

### Priority Ranking for Addition

**Must-have (interview-critical, conceptually foundational):**
1. MCMC convergence diagnostics (full treatment)
2. Hierarchical Bayes / partial pooling
3. Exponential family distributions
4. Calibration metrics & methods
5. Bayesian linear regression worked example

**Should-have (deepens understanding significantly):**
6. Bayesian model comparison (Bayes factors)
7. Stochastic VI / scalability
8. Deep ensembles (expanded)
9. Normalizing flows for VI
10. ABC / Simulation-based inference

**Nice-to-have (advanced/niche but valuable):**
11. Advanced BO (batch, high-dim, multi-objective)
12. Decision theory depth (EVOI, utility)
13. Front-door criterion, mediation, sensitivity analysis
14. SVGD
15. Bayesian nonparametrics depth (stick-breaking, HDP)
