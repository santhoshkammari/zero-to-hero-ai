# Association Rules Mining

## Core Concepts
- **Support**: P(X ∩ Y) — how often items co-occur
- **Confidence**: P(Y|X) — conditional probability
- **Lift**: confidence / P(Y) — does the combo beat random chance? Lift > 1 = real association

## Algorithms
- **Apriori**: bottom-up, prunes infrequent itemsets level-by-level. Simple but slow for large itemsets (multiple DB scans)
- **FP-Growth**: builds compressed FP-tree, mines without candidate generation. Much faster for large datasets

## Why lift matters when we have confidence
- High confidence can be misleading if the consequent is already very frequent
- Example: "people who buy bread also buy milk" — confidence 80%, but milk is bought by 70% of all shoppers anyway. Lift = 80/70 = 1.14 — barely above random
- Lift normalizes for base rate — the real test of association strength

## Practical reality in 2024
- Classic market basket analysis largely replaced by collaborative filtering and embeddings
- Still appears in: retail analytics, recommendation explanations, fraud pattern detection
- Very common interview question topic — especially interpreting lift values
