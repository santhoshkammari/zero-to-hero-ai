# Decision Trees Section Rewrite Plan

## Running Example
A small fruit classification problem: given color, diameter, and surface texture, classify fruit as apple/orange/lemon.
Start with 6 fruits. Scale up as concepts demand.

## Concept Ladder (dependency order)
1. **What is a decision tree?** — Personal confession, the flowchart idea, running example intro
2. **How splits are chosen** — Start with intuition (purity), then Gini, then entropy. Toy example walkthrough.
3. **The CART algorithm** — Greedy search. Walk through the algorithm on running example. Show the cascade effect.
4. **REST STOP** — You now have a working mental model of tree building.
5. **Pruning** — Motivation: unchecked trees memorize. Pre-pruning vs post-pruning. ccp_alpha.
6. **Feature importance** — Built-in but biased. Permutation importance fix.
7. **The variance problem** — The big insight. Why single trees aren't enough. Bridge to ensembles.
8. **What trees can't do** — Extrapolation, axis-aligned boundaries, categoricals, missing values.
9. **Wrap-up** — Gratitude, recap, future hope.

## Vulnerability Moments
1. Opening: "I used to think trees were too simple to be interesting"
2. Gini vs entropy: "I'll be honest — I spent way too long trying to understand when to pick one over the other"
3. Greedy algorithm: "The fact that finding the optimal tree is NP-hard still bothers me"
4. Variance: "I still get surprised when I retrain a tree and get something completely different"

## Recurring Analogies
1. Twenty Questions game — the analogy for recursive splitting
2. Gardening/pruning — literal pruning analogy that recurs
