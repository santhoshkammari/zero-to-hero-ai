# Precision, Recall, F1 — Deep Findings

## Why Harmonic Mean
- Arithmetic mean of P=1.0 and R=0.01 gives 0.505 — misleadingly rosy
- Harmonic mean gives 0.0198 — correctly screams "broken"
- Harmonic mean is bounded by the minimum: it punishes lopsided performance
- Only gives a high score when BOTH precision and recall are high

## F1 Limitations
- Ignores true negatives entirely — blind to how well you classify the majority class
- Treats precision and recall equally — not always appropriate
- On extreme imbalance, F1 can still be misleading (MCC is better)

## F-beta Selection
- β > 1 weights recall more (β=2 → recall 2x as important)
- β < 1 weights precision more (β=0.5 → precision 2x as important)
- The key: β² is the ratio of importance of recall to precision
- Practical: cancer screening → F2, spam filter → F0.5

## Interview Depth
- "Why not arithmetic mean?" is a classic trick question
- Understanding that F1 ignores TN distinguishes senior from junior
- Knowing when F1 breaks (extreme imbalance) → MCC discussion
