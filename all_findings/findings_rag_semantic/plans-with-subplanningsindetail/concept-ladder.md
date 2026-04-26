# RAG & Semantic Search — Concept Ladder & Plan

## Running Example
**Building a company knowledge assistant** — "AskIntern" — a bot that answers employee questions about internal docs (HR policies, engineering runbooks, product specs). Starts with 3 documents, scales up.

## Concept Ladder (dependency order)

1. **Why parametric memory fails** — LLMs hallucinate, freeze at cutoff, can't see your data
2. **The retrieval idea** — fetch relevant text, stuff into prompt (the library analogy)
3. **Embeddings as semantic coordinates** — how text becomes vectors, cosine similarity
4. **Chunking — the art of slicing documents** — why chunk size matters, toy example with 3 docs
5. **Vector search mechanics** — ANN, HNSW intuition, FAISS vs managed stores
6. **Naive RAG pipeline end-to-end** — chunk → embed → store → retrieve → generate
7. **REST STOP** — you can build a working RAG system now
8. **Where naive RAG breaks** — wrong chunks retrieved, multi-hop fails, ambiguous queries
9. **Hybrid retrieval** — BM25 + dense, Reciprocal Rank Fusion
10. **Reranking — the cross-encoder upgrade** — bi-encoder vs cross-encoder tradeoff
11. **ColBERT and late interaction** — the middle ground, MaxSim scoring
12. **Advanced query strategies** — query rewriting, HyDE, step-back prompting
13. **Multi-hop RAG** — iterative retrieval for complex questions
14. **GraphRAG** — knowledge graphs meet retrieval
15. **Agentic RAG** — the LLM decides when and what to retrieve
16. **Long-context vs RAG** — when 1M tokens beats retrieval, lost-in-the-middle
17. **Embedding fine-tuning** — domain adaptation with contrastive learning
18. **RAG evaluation** — RAGAS framework, faithfulness, relevance, context metrics
19. **Production patterns** — LangChain/LlamaIndex, parent document retrieval, metadata filtering

## Analogies (recurring)
1. **Library analogy** — RAG is like having a librarian fetch relevant books before answering; evolves throughout
2. **GPS coordinates analogy** — embeddings are semantic GPS coordinates in meaning-space

## Vulnerability moments
1. Opening: avoided RAG because "it seemed like a hack"
2. Chunking: "I still don't have a universal intuition for optimal chunk size"  
3. ColBERT: "I'm still developing my intuition for when late interaction matters vs a good reranker"
4. GraphRAG: "no one is completely certain how much the graph structure helps vs naive retrieval on different query types"
5. Evaluation: "I'll be honest — evaluating RAG systems felt more subjective than I expected"

## Rest Stop placement
After naive RAG pipeline (section 7) — reader has a working mental model
