# Rewrite Plan: EM Algorithm & Gaussian Mixtures

## Running Example
- A music streaming service trying to discover listener personas from play history
- Start with 50 users, 2 features (hours of pop, hours of rock)
- Three hidden personas: pop lovers, rock fans, eclectic listeners
- No labels — we only see the listening data

## Concept Ladder (dependency order)
1. The hidden variable problem (motivation: you see the data but not the groups)
2. The guess-and-refine loop (EM intuition before math)
3. E-step: soft assignments via Bayes' rule (responsibilities)
4. M-step: weighted statistics update
5. Walking through the toy example step by step
6. Why it always improves: the ELBO and Jensen's inequality
7. K-Means as the "hard" special case of EM
8. Gaussian Mixture Models: what the Gaussians buy us
9. Covariance types and what shapes they allow
10. Model selection: BIC/AIC for choosing K
11. The singularity trap and how to avoid it
12. Beyond GMMs: where EM shows up in the wild
13. Bayesian GMMs: letting the data choose K
14. Interview-depth: what senior engineers get asked

## Rest Stop Placement
- After walking through the toy example (concept 5)
- Reader has working mental model of E-step/M-step cycle

## Vulnerability Moments
1. "I avoided EM for years because the math looked like it was designed to intimidate"
2. "I still sometimes mix up which step is E and which is M when I'm tired"
3. "The ELBO derivation felt like a magic trick the first time — I had to trace it three times"
4. "I'm still developing intuition for why linear convergence feels so painfully slow"
5. "No one fully agrees on the best way to initialize — it's more art than science"

## Recurring Analogies
1. Detective analogy: suspects (clusters) and evidence (data points) — detective guesses who did what, then refines profile, then re-guesses
2. Sculptor analogy: starting with rough clay (random init), each iteration refines the shape
