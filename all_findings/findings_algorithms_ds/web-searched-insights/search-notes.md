# Web Search Insights

## Search 1: KD-trees and curse of dimensionality
- KD-trees partition space recursively, fail when dims > 20-30
- Alternatives: LSH, HNSW, Annoy (Spotify), Product Quantization (FAISS)
- Ball trees/cover trees also struggle in very high dims
- GPU brute-force (FAISS) surprisingly viable for moderate datasets

## Search 2: Graph algorithms in ML
- Computation graph = DAG, autograd = reverse topological sort
- GNN message passing operates on graph-structured data
- BFS/DFS used in autograd implementation, subgraph optimization

## Search 3: Complexity of training
- Standard matmul O(n³), self-attention O(n²) in seq length
- Efficient transformers: sparse attention, low-rank, kernel methods
- Longformer, Performer, Linformer, BigBird — all reduce to O(n) or O(n log n)

## Search 4: Hash tables in production ML
- Feature stores backed by hash maps — O(1) per lookup
- Embedding tables: hash user/item IDs to dense vectors
- At scale: Redis Cluster, distributed hash tables
- Feast, Uber's Michelangelo use hash-based feature retrieval

## Search 5: HNSW algorithm
- Multi-layer navigable small world graph
- Top layers sparse (long jumps), bottom layers dense (local)
- Greedy search from top to bottom — sub-linear query time
- Industry standard: Milvus, FAISS, Vespa, Pinecone, Redis

## Search 6: Dynamic programming in ML
- Viterbi: exact DP decoding for HMMs — O(T * S²)
- Beam search: approximate, keeps top-K hypotheses
- Used in LLM text generation, machine translation

## Search 7: Tries in tokenizers
- BPE tokenizers use tries for longest-prefix matching
- HuggingFace tokenizers library: Rust trie implementation
- O(L) lookup vs O(N) linear scan of vocabulary

## Search 8: Top-K selection
- np.argpartition: O(n) selection vs O(n log n) sort
- torch.topk built-in for GPU
- Critical for ranking, beam search, metrics computation

## Search 9: Bloom filters in ML
- Probabilistic dedup for billion-scale training corpora
- No false negatives, tunable false positive rate
- Used in web-crawl deduplication for LLM training
