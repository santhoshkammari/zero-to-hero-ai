# Bias-Variance Core Research

## Mathematical Decomposition
- E[(y - f̂(x))²] = Bias²(f̂(x)) + Variance(f̂(x)) + σ²
- Bias² = [E[f̂(x)] - f(x)]² — systematic error from model architecture being wrong
- Variance = E[(f̂(x) - E[f̂(x)])²] — jitter across different training sets
- σ² = irreducible noise floor

## Key Insights for Deep Treatment
1. The decomposition is for a FIXED point x — often confused
2. The expectation is over all possible training sets from same distribution
3. Bias measures what the model CANNOT learn (architectural limitation)
4. Variance measures what the model learns that it SHOULDN'T (noise memorization)
5. You can't observe bias and variance separately from a single model — you need the thought experiment of retraining

## Double Descent (Belkin 2019, Nakkiran 2019)
- Classical U-curve is incomplete
- Past interpolation threshold, test error DECREASES again
- Epoch-wise double descent: training longer can help after initial overfitting
- Why: overparameterized models have many interpolating solutions, SGD picks simplest (min norm)

## Benign Overfitting
- Coined by Belkin et al.
- Conditions: high-dimensional, certain data structure, implicit regularization from SGD
- Interpolation isn't always bad — depends on HOW you interpolate

## Grokking (Power et al. 2022)
- Networks memorize first, then suddenly generalize after much more training
- Competition between memorization and generalization circuits
- Weight decay accelerates grokking
- Challenges early stopping dogma

## Zhang et al. 2017 — Rethinking Generalization
- DNNs can memorize completely random labels
- Standard regularization doesn't prevent this
- Classical capacity-based theory doesn't explain why real DNNs generalize
- Implies implicit regularization from optimization is the key
