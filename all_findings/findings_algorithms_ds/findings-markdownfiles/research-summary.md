# Algorithms & Data Structures for ML — Research Findings

## Key Insights from Web Research

### 1. KD-Trees and the Curse of Dimensionality
- KD-trees work well for <20-30 dimensions but degenerate to O(n) in high dims
- Modern ML embeddings are 100-1000+ dimensions — KD-trees fail here
- This is the *motivating frustration* for ANN methods like HNSW, LSH, FAISS

### 2. HNSW (Hierarchical Navigable Small World)
- State-of-the-art for vector similarity search
- Multi-layer graph: sparse top layers (expressways), dense bottom (local roads)
- Search: start at top, greedy traverse down — sub-linear time
- Powers Pinecone, Milvus, FAISS, Redis vector search
- The city analogy: expressways → highways → local roads

### 3. Hash Tables in Production ML
- Feature stores are hash maps (O(1) lookup for user/item features)
- Embedding tables in recommendation systems (user_id → dense vector)
- Vocabulary mappings (token_to_index)
- At scale: distributed hash tables, sharding across machines

### 4. Graph Algorithms
- Computation graphs are DAGs — autograd uses reverse topological sort
- loss.backward() literally runs a graph algorithm
- GNN message passing: nodes aggregate info from neighbors
- ML pipeline orchestration (Airflow DAGs)

### 5. Algorithmic Complexity in Training
- Matrix multiplication: O(n³) standard, O(n^2.81) Strassen
- Self-attention: O(n²) in sequence length — THE bottleneck
- Efficient transformers: Longformer O(n), Performer O(n), Reformer O(n log n)
- Practical rule: O(n²) works up to ~50K; at 1M it's pain

### 6. Dynamic Programming in ML
- Viterbi algorithm: DP for optimal decoding in HMMs
- Beam search: approximate DP when state space too large
- Connection: Viterbi is exact, beam search is practical for neural models

### 7. Tries in Tokenizers
- BPE tokenizers use tries for longest-prefix matching
- O(L) per token (L = token length) vs O(N) scanning vocab
- HuggingFace tokenizers library implements tries in Rust
- Also powers autocomplete systems

### 8. Top-K Selection
- np.argpartition: O(n) for top-k vs O(n log n) full sort
- Critical for beam search, recommendation ranking, metrics (Recall@K)
- torch.topk, tf.math.top_k built-in operations

### 9. Bloom Filters
- Probabilistic set membership — no false negatives, possible false positives
- Used for training data deduplication at scale (billions of web documents)
- Memory-efficient: fraction of hash set memory
- Used in LLM training data pipelines (OpenAI, etc.)
