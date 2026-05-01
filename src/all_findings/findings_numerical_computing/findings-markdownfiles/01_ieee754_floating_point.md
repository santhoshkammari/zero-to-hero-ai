# IEEE 754 Floating Point

## Key Insights
- Every float: (-1)^sign × 1.mantissa × 2^(exponent - bias)
- float32: 1 sign + 8 exp + 23 mantissa = ~7 decimal digits
- float64: 1 sign + 11 exp + 52 mantissa = ~15-16 decimal digits
- float16: 1 sign + 5 exp + 10 mantissa = ~3.3 decimal digits
- bfloat16: 1 sign + 8 exp + 7 mantissa = ~2.4 decimal digits but same range as float32

## Denormalized Numbers
- When exponent bits all zero: subnormal numbers
- Fill the gap between 0 and smallest normal number
- Performance penalty on some hardware (10-100x slower)
- Important: gradients near zero need these

## Special Values
- All exponent bits 1, mantissa 0: ±Infinity
- All exponent bits 1, mantissa nonzero: NaN
- NaN propagates: any op with NaN = NaN
- NaN != NaN (the only value not equal to itself)

## Machine Epsilon
- float32: ~1.19e-7
- float64: ~2.22e-16
- Fundamental resolution limit

## ML Relevance
- NumPy defaults float64, PyTorch defaults float32
- Gradient accumulation: adding small to large loses the small
- 0.1 + 0.2 != 0.3 — never use == for floats
