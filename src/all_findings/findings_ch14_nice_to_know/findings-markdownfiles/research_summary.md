# Ch14 Nice to Know - Research Summary

## Topics to cover:
1. Bayesian Deep Learning (MC Dropout, Bayes by Backprop, Laplace Approximation)
2. Expectation Propagation (EP vs VI, KL direction)
3. Causal Inference (do-calculus, Pearl's framework, counterfactuals, instrumental variables)
4. Bayesian Nonparametrics (Dirichlet Process, Chinese Restaurant Process)
5. Information Geometry (Fisher information metric, natural gradient)
6. PAC-Bayes Bounds (generalization bounds for stochastic/Bayesian learners)
7. Conformal Prediction (distribution-free uncertainty, coverage guarantee)

## Key Insights:
- Laplace approx: train normally, then fit Gaussian at MAP using Hessian. Post-hoc, nearly free.
- EP minimizes KL(p||q) = mass-covering vs VI minimizes KL(q||p) = mode-seeking
- Pearl's causal ladder: association → intervention → counterfactual
- Dirichlet Process: distribution over distributions, CRP metaphor (rich get richer)
- Information geometry: parameter space as curved manifold, Fisher metric as natural distance
- PAC-Bayes: generalization gap bounded by KL(posterior||prior) / sqrt(n)
- Conformal prediction: distribution-free, model-agnostic, guarantees coverage
