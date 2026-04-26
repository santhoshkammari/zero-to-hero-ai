# Log-Sum-Exp Trick

## The Problem
- Need: log(Σ e^xi)
- Large xi → e^xi overflows to inf
- Very negative xi → all e^xi underflow to 0, log(0) = -inf

## The Trick
- log(Σ e^xi) = max(x) + log(Σ e^(xi - max(x)))
- Largest exponent becomes e^0 = 1, no overflow
- At least one term is 1, so log argument > 0

## Why It Works (Proof)
- Factor out e^max: Σ e^xi = e^max · Σ e^(xi-max)
- Take log: log(e^max · Σ e^(xi-max)) = max + log(Σ e^(xi-max))
- Mathematically identical, numerically safe

## Softmax Application
- softmax(xi) = e^xi / Σ e^xj = e^(xi-max) / Σ e^(xj-max)
- Constant cancels in ratio — result identical
- Max exponent is 0, all others ≤ 0

## Why Log-Probabilities
- Probability 10^-300 underflows to 0
- Log probability -690.7 is perfectly fine
- Multiplying probabilities → adding logs
