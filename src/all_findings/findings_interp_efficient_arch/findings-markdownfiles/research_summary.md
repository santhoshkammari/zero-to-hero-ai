# Research Summary: Interpretability & Efficient Architectures

## Key Topics Covered

### Interpretability
1. **Attention Visualization** - heatmaps of attention weights, BertViz, Jain & Wallace 2019 debate
2. **Probing Classifiers** - freeze model, train linear classifier on hidden states, map what layers encode
3. **BERTology** - Rogers et al. 2020 survey: early layers = surface, middle = syntax, late = semantics
4. **Mechanistic Interpretability** - Anthropic's work: induction heads, superposition, circuit tracing, sparse autoencoders

### Efficient Architectures
1. **The O(n²) Problem** - standard attention computes all-pairs scores
2. **Sparse Attention** - Longformer (local window + global), BigBird (local + global + random)
3. **Linear Attention** - Linformer (low-rank projection), Performer (FAVOR+ kernel approximation)
4. **FlashAttention** - IO-aware, tiling, online softmax trick, exact computation, 2-4x speedup
5. **KV Cache** - cache K,V from previous tokens during autoregressive generation
6. **MQA/GQA** - Multi-Query (single K,V head) vs Grouped-Query (groups of K,V heads)
7. **PagedAttention** - vLLM's virtual memory approach to KV cache management
8. **Speculative Decoding** - draft model proposes tokens, target model verifies in parallel

## Running Example Idea
- Building a chatbot for a small company. Start with 5-word sentences, then need to handle longer documents.
- This naturally motivates: wanting to understand what the model learned (interpretability), then needing it to handle longer inputs (efficiency).

## Concept Ladder
1. The black box problem → attention visualization
2. Attention ≠ explanation → probing classifiers
3. Probing tells what, not how → mechanistic interpretability
4. REST STOP
5. The quadratic wall → sparse attention patterns
6. Sparse loses info → linear attention approximations
7. Approximation quality gap → FlashAttention (exact + fast)
8. Training done, inference bottleneck → KV cache
9. KV cache too big → MQA/GQA
10. Still slow token-by-token → speculative decoding
