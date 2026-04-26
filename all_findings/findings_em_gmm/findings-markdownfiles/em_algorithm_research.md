# EM Algorithm & Gaussian Mixtures — Research Findings

## Core Insights

### EM Algorithm Derivation
- EM is coordinate ascent on the ELBO (Evidence Lower Bound)
- Jensen's inequality provides the lower bound: log p(X|θ) ≥ E_q[log p(X,Z|θ)/q(Z)]
- E-step: set q(Z) = p(Z|X, θ_old) — makes bound tight (touches true likelihood)
- M-step: maximize the tightened bound w.r.t. θ
- Each iteration guaranteed non-decreasing log-likelihood
- Converges to LOCAL optimum only — landscape riddled with local maxima

### EM as Special Case of Variational Inference
- EM uses exact posterior in E-step (unconstrained q)
- VI approximates posterior with restricted q family
- When posterior intractable → VI generalizes EM
- Same ELBO objective, different optimization constraints
- Key insight: EM is "exact VI" — variational inference is "approximate EM"

### K-Means as Special Case of EM
- Hard assignments (responsibility 0 or 1) = degenerate E-step
- Spherical equal covariances (σ²I) 
- Uniform mixing weights
- "Assign to nearest centroid" = argmax responsibility
- "Recompute centroids" = M-step with hard assignments

### Convergence Properties
- Linear convergence rate near optimum
- Dramatically slow near saddle points or flat regions
- No curvature info (unlike Newton methods)
- Acceleration: SQUAREM, Aitken, hybrid EM→Newton switching
- Multiple restarts with different init is the practical fix

### Singularity Problem
- Component collapses onto single point → variance→0 → likelihood→∞
- Degenerate solution, not useful
- Fix: add λI to diagonal (ridge regularization), typically λ=1e-6
- Also: restrict covariance type (diag, spherical), Bayesian priors

### BIC/AIC Model Selection
- BIC = -2·log(L) + k·log(n) — penalizes more, consistent (true K as n→∞)
- AIC = -2·log(L) + 2k — tends to overfit with more components
- BIC generally preferred for GMM component selection

### Bayesian GMMs (Dirichlet Process)
- BayesianGaussianMixture in sklearn
- Set large n_components, let model deactivate unused ones
- weight_concentration_prior controls cluster formation tendency
- Natural regularization prevents singularity

### Applications Beyond GMM
- HMMs: Baum-Welch = EM for sequential data
- Missing data imputation: treat missing as latent variables
- Topic models (LDA): variational EM
- Semi-supervised learning: labeled + unlabeled data
- Speech recognition, bioinformatics, finance

### Interview Depth Points
- Prove monotonic convergence via Jensen's inequality
- Walk through one EM iteration on whiteboard
- Compare EM vs VI (point estimates vs distributions)
- Discuss initialization strategies and why they matter
- Know ELBO decomposition: ELBO = log p(X) - KL(q||p(Z|X))
