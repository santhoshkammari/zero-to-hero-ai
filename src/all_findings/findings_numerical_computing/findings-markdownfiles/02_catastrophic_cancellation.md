# Catastrophic Cancellation & Numerical Stability

## What It Is
- Subtracting two nearly equal numbers destroys significant digits
- Example: 1.000000001 - 1.000000000 in float32 → 0 (all precision lost)

## Where It Shows Up in ML
1. **Variance**: E[X²] - E[X]² — small variance + large mean = disaster
2. **Softmax derivatives**: close output values
3. **Batch normalization**: mean/variance computation
4. **Cross-entropy loss**: log(1-p) when p ≈ 1

## Solutions
- Welford's algorithm for online variance (one-pass, stable)
- Two-pass algorithms (compute mean first, then deviations)
- Kahan compensated summation for gradient accumulation
- Reformulate: use log1p(x) instead of log(1+x) for small x
- Use expm1(x) instead of exp(x)-1 for small x
