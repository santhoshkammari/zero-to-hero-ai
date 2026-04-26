# Rewrite Plan: Simple Classifiers (ch05/s03)

## Brandon Rohrer Style Requirements
- Personal confession opening
- Running example throughout
- Build concepts from scratch, one at a time
- Toy examples walked step by step
- Motivate each concept with frustration/limitation
- Rest stop with permission to leave
- Vulnerability moments (4-5)
- Recurring analogies
- No bullet-point explanations, narrative prose
- Define every term inline on first use

## Running Example
"Diagnosing fruit" - a fruit sorting machine at a farm market
- Start with 3 fruits: apple, orange, lemon
- 2 features: weight and color intensity
- Grows naturally as complexity increases
- Returns for both KNN and Naive Bayes sections

## Concept Ladder
1. The idea of "just ask your neighbors" (KNN intro via fruit sorting)
2. What "distance" means and why it matters (Euclidean, Manhattan)
3. The Voronoi insight (k=1 decision boundary)
4. What k does to the boundary (bias-variance via k)
5. The curse - when distance loses meaning (high dimensions)
6. Speed problem and solutions (KD-tree, ball tree, ANN)
7. REST STOP - you now have KNN, good enough for many problems
8. A different approach: counting evidence (Naive Bayes motivation)
9. Bayes theorem from scratch with fruit example
10. The "naive" trick and why it works anyway
11. Three variants matched to data types
12. Text classification - the killer app
13. Laplace smoothing and the zero-probability catastrophe
14. Log space - the numerical survival trick
15. When simple beats complex

## Vulnerability Moments
1. "I avoided these for longer than I should have" (opening)
2. "The first time I saw Voronoi diagrams..." (KNN boundaries)
3. "I still don't have great intuition for why naive works" (NB)
4. "I'll be honest, the log trick felt like cheating" (log space)
5. "No one fully knows why NB works as well as it does" (NB success)

## Analogies
1. "Neighborhood poll" - asking neighbors, recurring for KNN
2. "Courtroom evidence" - features as witnesses, recurring for NB
