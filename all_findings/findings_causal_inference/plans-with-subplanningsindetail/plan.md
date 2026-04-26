# Causal Inference Section Rewrite Plan

## Running Example
An e-commerce company trying to understand if showing a promotional banner increases purchases.
- Starts tiny: 6 users, 2 groups
- Grows organically through each concept

## Concept Ladder (dependency order)
1. Correlation vs Causation (ice cream/drowning → Simpson's paradox with real Berkeley example)
2. The Fundamental Problem: you can only observe one reality per person (potential outcomes)
3. Potential Outcomes Framework (Rubin) — Y(1), Y(0), the missing data problem
4. ATE, ATT, CATE — what we're estimating
5. Randomized Experiments — the gold standard that physically implements do()
6. **REST STOP** — you now know enough to run an A/B test
7. Observational Studies — when you can't randomize
8. Propensity Score Matching — find a lookalike
9. Inverse Probability Weighting — reweight the population
10. Difference-in-Differences — use time as your friend
11. Instrumental Variables — nature's experiments
12. Regression Discontinuity — exploiting arbitrary cutoffs
13. Pearl's Structural Causal Models — DAGs, do-calculus, backdoor/frontdoor
14. Causal Discovery — learning the DAG from data (PC, FCI)
15. **REST STOP 2** — you now have the classical toolkit
16. Double ML & Causal Forests — ML meets causality
17. Applications in Tech — uplift modeling, personalization, CATE in production

## Recurring Analogies
1. **The courtroom** — causal inference as building a legal case (evidence, reasonable doubt, counterfactual "but-for" test)
2. **The parallel universe** — potential outcomes as alternate timelines you can't visit

## Vulnerability Moments
1. Opening confession about avoiding the topic
2. "I still get confused about when to condition on a variable vs when not to"
3. "No one is completely certain which DAG is correct for a real-world problem"
4. Admitting the oversimplification of treating confounders as simple
5. "I haven't figured out a great way to visualize do-calculus intuitively"
