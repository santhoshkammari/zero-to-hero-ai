# Web Search Insights Summary

## Searches Performed
1. McCulloch-Pitts to Rosenblatt perceptron history and math
2. Universal approximation theorem intuition and limitations
3. Xavier vs He initialization
4. GELU activation intuition for transformers
5. SiLU/Swish vs GELU comparison 2024
6. Depth vs width tradeoffs
7. XOR problem geometric intuition
8. Dying ReLU real-world impact and solutions

## Key Insights Gathered
- UAT is existence proof, not practical guide — depth makes it efficient
- GELU's smooth gating is "probabilistic" — scales by likelihood of being positive under Gaussian
- He init specifically compensates for ReLU zeroing out negatives (needs 2x variance)
- Deep networks compose features hierarchically — exponentially fewer params than wide shallow
- 20-40% dead neurons common with bad init in practice
- SiLU and GELU differ by < 0.1 across most of range — use what architecture paper specifies
