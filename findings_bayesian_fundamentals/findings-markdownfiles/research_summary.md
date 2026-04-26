# Bayesian Fundamentals Research Summary

## Key Concepts to Cover
1. Bayes' theorem from first principles - toy example (disease testing, sneezing kids)
2. Prior / Likelihood / Posterior / Evidence - each piece's job
3. Conjugate priors - Beta-Binomial workhorse, closed-form updates
4. MAP vs MLE - regularization connection (Gaussian=L2, Laplace=L1)
5. Bayesian vs Frequentist philosophy - probability as belief vs frequency
6. Credible intervals vs confidence intervals - the thing everyone confuses
7. Bayesian updating (sequential) - today's posterior = tomorrow's prior
8. Beta-binomial example worked through step by step
9. Prior selection strategies - Gelman's weakly informative priors
10. Bayesian decision theory - expected posterior loss, optimal actions

## Running Example: A/B testing a website button color
- Start with whether a new button color converts better
- Tiny example: 10 visitors, track clicks
- Builds through conjugate updates, sequential updating, decision theory

## Concept Ladder (dependency order)
1. What is probability? (The two camps)
2. Conditional probability (flipping the question)
3. Bayes' theorem (the engine)
4. Prior, likelihood, posterior, evidence (the four characters)
5. Toy example walked through
6. Conjugate priors (making updates tractable)
7. Beta-binomial fully worked
8. Sequential updating
9. MAP vs MLE (point estimates from posteriors)
10. MAP = regularization connection
11. Credible vs confidence intervals
12. Prior selection strategies
13. Bayesian decision theory

## Analogies
1. Courtroom trial analogy: prior = initial assessment, evidence = testimony, posterior = verdict
2. GPS/map analogy: prior = your general sense of location, likelihood = GPS signal, posterior = refined position
