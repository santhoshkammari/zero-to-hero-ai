# RAG Research Findings

## Why LLMs Hallucinate
- Autoregressive: next-token prediction optimized for fluency, not accuracy
- No internal fact database - pattern completion engine
- Training data cutoff - no real-time knowledge
- No built-in "I don't know" mechanism
- Confidence != correctness

## RAG Architecture
- Retrieve-then-generate paradigm
- Lewis et al. 2020 original paper (end-to-end training)
- Modern practice: off-the-shelf embedder + separate LLM
- Pipeline: chunk → embed → index → retrieve → rerank → augment prompt → generate

## Chunking Strategies
- Fixed-size (256-512 tokens, 50-100 overlap)
- Recursive character splitting (paragraph → sentence → word fallback)
- Semantic chunking (embedding-based topic shift detection)
- Too small = no context, too large = diluted signal

## Embedding Models
- Bi-encoders: encode query and doc separately, compare via dot product
- Key models: BGE, E5, MiniLM, OpenAI text-embedding-3, Cohere embed-v3
- MTEB benchmark for comparison
- Contrastive learning training: positive pairs closer, negatives apart

## Vector Databases
- FAISS (Meta, local), Pinecone (managed), Chroma (lightweight), Weaviate (hybrid), Qdrant (Rust)
- ANN algorithms: HNSW (skip-list inspired multi-layer graph), IVF
- HNSW: top layers = coarse long-range, bottom layers = fine local search

## Similarity Search
- Cosine similarity: direction only, magnitude-invariant
- Dot product: direction + magnitude (equivalent to cosine when normalized)
- Euclidean: straight-line distance

## Reranking
- Bi-encoder: fast but limited (no cross-attention)
- Cross-encoder: query+doc together through transformer, much more accurate but slow
- Two-stage: retrieve 50-100 with bi-encoder, rerank top 3-5 with cross-encoder

## Advanced RAG
- HyDE: generate hypothetical answer, embed that for retrieval
- Self-RAG: model decides when to retrieve, generates retrieval tokens
- CRAG: quality check after retrieval, fallback to web search or LLM knowledge
- GraphRAG: knowledge graph + vector retrieval

## Evaluation (RAGAS)
- Faithfulness: answer supported by context?
- Answer Relevance: answer addresses question?
- Context Precision: retrieved docs relevant?
- Context Recall: all relevant docs retrieved?

## Production Considerations
- Latency: pre-embed, ANN, caching, parallel retrieval
- Cost: caching, hybrid search, smaller models
- Freshness: re-embed on update, versioning, real-time sync
- Lost in the middle: reranking, place relevant at start/end
