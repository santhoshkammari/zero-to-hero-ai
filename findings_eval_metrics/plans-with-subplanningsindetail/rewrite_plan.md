# Rewrite Plan for ch04/s05.html — Evaluation Metrics

## Brandon Rohrer Style Requirements
1. Personal confession opening
2. One-paragraph orientation
3. "Before we start" heads-up
4. Journey invitation
5. Running example throughout (fraud detection system)
6. Build from scratch: confusion matrix → accuracy trap → precision/recall → F1 → threshold → ROC/PR → calibration → regression → ranking → production
7. Rest stop after classification basics
8. Vulnerability moments (4-5)
9. Recurring analogies (smoke detector, courtroom)
10. Wrap-up with gratitude + recap + future hope

## Concept Ladder
1. The confusion matrix — four buckets, that's it
2. The accuracy trap — why 99% means nothing
3. Precision — the courtroom standard
4. Recall — the cancer screening standard
5. The tradeoff — smoke detector analogy
6. F1 and F-beta — the harmonic mean trick
7. [REST STOP]
8. Threshold selection — the dial you actually turn
9. ROC-AUC — ranking quality across all thresholds
10. PR-AUC — when positives are rare
11. Log loss — punishing overconfidence
12. MCC — the metric that's hard to game
13. Calibration — when probabilities need to mean something
14. Regression metrics — different game, different scoreboard
15. Ranking metrics — order matters
16. Goodhart's Law — when metrics go wrong in production

## Running Example
Fraud detection system: 10,000 transactions, 1% fraud
Thread from start to finish

## Analogies
1. Smoke detector sensitivity dial (precision-recall tradeoff)
2. Courtroom: innocent until proven guilty vs. never let a guilty person walk free
3. Weather forecaster confidence (calibration)
