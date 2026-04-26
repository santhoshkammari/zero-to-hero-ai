# Probabilistic Models & Inference - Research Summary

## Key concepts to cover:
1. **Graphical models** - Bayesian networks (directed), MRFs (undirected)
2. **Plate notation** - compact representation for repeated structures
3. **D-separation** - reading conditional independence from graph structure
4. **Exact inference** - variable elimination, belief propagation
5. **MCMC** - Metropolis-Hastings, Gibbs sampling, HMC/NUTS
6. **Variational inference** - ELBO, mean-field, stochastic VI
7. **Amortized inference** - VAE connection
8. **When to use which** - practical decision guide

## Running example idea: Medical diagnosis system
- Small clinic with 3 diseases and 4 symptoms
- Build up from "how do symptoms relate to diseases" to full inference
- Natural for graphical models (diseases cause symptoms)
- Natural for inference (given symptoms, what's the disease?)

## Key analogies:
1. **Map analogy** - graphical model is a map of relationships, like a city map showing which roads connect which neighborhoods
2. **Detective analogy** - inference is like being a detective: you see clues (evidence) and work backward to figure out what happened (hidden causes)

## Concept ladder:
1. Joint distributions are huge → need compact representation → graphical models
2. Bayesian networks: directed, causal stories
3. MRFs: undirected, correlations
4. Plate notation: handling repetition
5. D-separation: reading independence
6. Need to answer questions (inference) → exact methods
7. Variable elimination, belief propagation
8. Exact methods break on big graphs → need approximation
9. MCMC: sampling approach (MH → Gibbs → HMC)
10. VI: optimization approach (ELBO, mean-field)
11. Amortized VI: neural network does inference
12. When to use which

## Vulnerability moments:
- Confess avoiding graphical models because notation looked intimidating
- Admit d-separation colliders still trip me up
- HMC physics connection took a while to click
- ELBO derivation - admit the algebra is not the insight
- Still developing intuition for when VI underestimates uncertainty badly
