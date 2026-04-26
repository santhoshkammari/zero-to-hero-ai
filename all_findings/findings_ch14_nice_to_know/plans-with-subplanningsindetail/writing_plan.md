# Writing Plan for Ch14 Nice to Know

## Running Example: Medical diagnosis system
- Start with a clinic trying to diagnose rare diseases
- Builds naturally: uncertainty in diagnosis, causal questions about treatments, 
  group-level patterns across clinics, guarantees for patients

## Concept Ladder:
1. Opening: confession about avoiding these advanced topics
2. Bayesian Deep Learning (the need for uncertainty in neural nets)
   - MC Dropout, Bayes by Backprop, Laplace Approximation
3. Expectation Propagation (when VI isn't enough)
4. Causal Inference (correlation isn't causation - finally formalized)
   - do-calculus, counterfactuals, instrumental variables
5. Bayesian Nonparametrics (when you don't know how many clusters)
   - Dirichlet Process, CRP
6. Information Geometry (the shape of probability space)
   - Fisher metric, natural gradient
7. PAC-Bayes Bounds (theoretical guarantees for Bayesian methods)
8. Conformal Prediction (distribution-free guarantees anyone can use)
9. Wrap-up

## Rest Stop: After Causal Inference (halfway point, useful mental model)

## Vulnerability moments:
1. Opening confession about avoiding these topics
2. Causal inference: "I still occasionally mix up the three rungs"
3. Information geometry: "I won't pretend I have deep intuition for Riemannian manifolds"
4. PAC-Bayes: "The math can feel impenetrable at first"
5. Admission that some of these are research-active areas

## Recurring Analogies:
1. Weather forecast analogy (uncertainty, calibration)
2. Map/terrain analogy (information geometry, parameter space)
