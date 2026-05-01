# Hopfield Networks & Modern Hopfield Networks

## Classic Hopfield Networks (1982)
- Recurrent neural network for associative memory
- Fully connected, symmetric weights, energy function
- Given partial/noisy input, network settles into nearest stored pattern
- Storage capacity: ~0.14N patterns (N = number of neurons)
- Pioneered energy-based models in neural networks

## Modern Hopfield Networks (Ramsauer et al., 2020)
- "Hopfield Networks is All You Need" — deliberate echo of "Attention is All You Need"
- Continuous states, exponential storage capacity (up to e^cN patterns)
- Key insight: the update rule is MATHEMATICALLY EQUIVALENT to transformer attention
- Query matches keys via softmax-weighted sum → same as attention mechanism

## The Connection to Transformers
- Attention = one step of a modern Hopfield network energy minimization
- Both use: similarity scores + softmax + weighted retrieval
- This unified view shows attention is a form of associative memory retrieval
- Deep theoretical bridge between 1980s associative memory and 2017 transformers

## Why It Matters
- Shows transformers aren't entirely new — they're a rediscovery of energy-based associative memory
- Provides theoretical tools for understanding attention's behavior
- Exponential storage explains why transformers handle such large contexts

## Interview Angle
- Know the historical arc: Hopfield (1982) → Boltzmann machines → modern Hopfield → attention
- The connection between energy-based models and attention is increasingly tested
