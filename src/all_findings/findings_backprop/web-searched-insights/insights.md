# Web Search Insights — Backpropagation

## Key Insights Gathered

1. **History is richer than commonly told**: Linnainmaa (1970) → Werbos (1974) → Rumelhart/Hinton/Williams (1986). The math existed 16 years before the famous paper.

2. **VJP vs JVP distinction is crucial**: Reverse mode computes vector-Jacobian products (v^T·J). Forward mode computes Jacobian-vector products (J·v). The choice depends on which dimension is smaller — inputs or outputs.

3. **Expression swell is why symbolic diff fails for deep nets**: Each application of chain rule symbolically doubles the expression. AD avoids this by computing values, not expressions.

4. **Sigmoid's max derivative of 0.25 is the smoking gun**: Four layers of sigmoid means gradient is at most 0.25^4 ≈ 0.004 — the signal is 99.6% gone. This is why people couldn't train deep nets for decades.

5. **Second-order methods exist but rarely used**: K-FAC, L-BFGS, Hessian-free optimization approximate curvature. In practice, Adam dominates because it's simple and works.

6. **BPTT for RNNs**: Backprop through time unrolls the recurrence — same algorithm, but the "depth" is the sequence length. This is why RNNs struggle with long sequences.

7. **Gradient checkpointing is standard for LLM training**: Store only √n checkpoints, recompute activations during backward pass. ~30% more compute, ~60% less memory.
