# Key Research Findings

## Vanilla RNN
- h_t = tanh(W_hh * h_{t-1} + W_xh * x_t + b)
- Weight sharing across time steps → handles variable length
- Unrolling = copying the same cell T times
- Hidden state = compressed summary of everything seen so far

## BPTT & Vanishing Gradients
- Gradient: product of (f'(a_j) * W_hh) for each step
- tanh derivative max is 1, usually much less
- If spectral norm of Jacobian < 1: exponential decay → vanishing
- If > 1: exponential growth → exploding (fixable with clipping)
- Practical limit: ~10-20 steps for vanilla RNN

## LSTM (Hochreiter & Schmidhuber, 1997)
- Cell state: additive update = gradient highway
- C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t (THE KEY LINE)
- When f_t ≈ 1, i_t ≈ 0: cell state passes unchanged
- Forget gate bias init to 1 (Jozefowicz 2015) — critical practical tip
- Peephole connections (Gers 2000): gates peek at cell state

## GRU (Cho et al., 2014)
- 2 gates: update (z) and reset (r)
- h_t = (1-z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t — interpolation
- No separate cell state
- Fewer parameters: 3(n² + nd + n) vs LSTM's 4(n² + nd + n)
- Empirically comparable performance

## Bidirectional RNNs
- Forward + backward pass, concatenate hidden states
- Doubles output dimension
- Can't use for real-time generation
- Great for classification, NER, encoding

## Why Transformers Won
- Sequential bottleneck: can't parallelize RNN computation
- Long-range deps: attention connects any two positions directly
- Training speed: massive GPU parallelism
