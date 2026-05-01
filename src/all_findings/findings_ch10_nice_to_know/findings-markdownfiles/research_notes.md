# Ch10 Nice to Know - Research Notes

## Topics to Cover (with depth)

### 1. Transformer-XL (Segment-Level Recurrence)
- Problem: Standard transformers split text into fixed segments, lose context at boundaries ("context fragmentation")
- Solution: Cache hidden states from previous segment, attend to them in current segment
- Relative positional encoding (not absolute) so model understands "3 tokens back" not "position 47"
- Effective context grows linearly with depth
- Key precursor to XLNet

### 2. XLNet (Permutation Language Model)
- Combines autoregressive (GPT) with bidirectional (BERT) advantages
- Instead of masking tokens, randomly permutes factorization order
- Each token trained to predict given ALL possible contexts
- No [MASK] token mismatch between train/test
- Uses two-stream self-attention (content stream + query stream)
- Built on Transformer-XL architecture

### 3. Reformer (LSH Attention)
- LSH hashing to bucket similar queries/keys together
- Only compute attention within buckets: O(n log n) instead of O(n²)
- Reversible layers to avoid storing activations (memory savings)
- Multiple rounds of hashing to reduce false negatives
- Historically important but Flash Attention solved the problem more cleanly

### 4. Neural Turing Machines & Memory-Augmented Networks
- External differentiable memory matrix (N x M)
- Controller (LSTM/FFN) outputs read/write instructions
- Soft addressing: continuous weights over all locations (like attention)
- Read = weighted sum over memory rows
- Write = erase then add, all differentiable
- DNC (Differentiable Neural Computer) improved on NTM with usage tracking, temporal links
- Can learn algorithms: sorting, copying, associative recall

### 5. Differentiable Programming
- Broader paradigm: all operations differentiable, optimize end-to-end
- Neural networks are a special case
- Enables: neural ODEs, physics simulations, learned optimizers
- Key insight: if you can compute gradients, you can learn

### 6. Mixture of Experts (Switch Transformer, GShard)
- Replace single FFN with many expert FFNs + router
- Router picks top-k experts per token
- Switch Transformer: top-1 routing (each token goes to one expert)
- GShard: framework for sharding across devices
- Mixtral: 8 experts, 2 active per token
- Load balancing is the hard problem
- Conditional computation: only activate parts of model per input

### 7. RetNet (Retentive Networks)
- Replace attention with retention mechanism
- Exponential moving average over sequence
- Decay coefficient controls how fast history fades
- Linear complexity in sequence length
- Can run in parallel (training) or recurrent (inference) mode
- Dual form is the key insight

### 8. RWKV
- RNN-Transformer hybrid
- Linear attention via rolling weighted averages
- Processes tokens one at a time (streaming) like RNN
- Architecture looks like transformer (layers, norm, FFN blocks)
- O(n) time and memory
- Used in practice for large language models (RWKV-LM)
