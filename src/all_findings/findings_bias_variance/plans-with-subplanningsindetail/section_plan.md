# Section Rewrite Plan: Bias-Variance & Overfitting

## Running Example
A weather temperature prediction model — starts with 3 data points, grows naturally.
Predicting tomorrow's high temperature from historical data.

## Concept Ladder (dependency order)
1. The prediction problem — what IS error, really?
2. The two ways to be wrong — bias and variance via toy example
3. The dartboard (recurring analogy)
4. The mathematical decomposition — built up from the toy
5. Seeing it in code — polynomial regression experiment
6. Learning curves — the diagnostic tool
7. **REST STOP** — you now know enough to diagnose and fix 80% of model problems
8. The remedy toolkit — what to do for each failure mode
9. Regularization deep dive — L1/L2 geometry, dropout as ensemble
10. The plot twist — Zhang et al.'s random labels experiment
11. Double descent — the classical story was incomplete
12. Epoch-wise double descent and grokking — brief
13. Benign overfitting and implicit regularization — why big models work
14. Learning theory foundations — VC dim, PAC, Rademacher (brief, nice-to-know)
15. Wrap-up

## Recurring Analogies
1. Dartboard — bias = center offset, variance = spread (recurs in regularization, ensembles)
2. Landscape/map — model as a map of territory, simple map vs detailed map vs hallucinated map
3. The musician analogy — memorizing a song vs understanding music theory

## Vulnerability Moments
1. Opening confession about avoiding the topic
2. "I still get tripped up by which direction to move the lever"
3. "No one fully understands why SGD finds good solutions"
4. "I oversimplified when I said more complexity always hurts"
5. "I'm still building intuition for when benign overfitting applies"
