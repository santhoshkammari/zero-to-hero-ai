# Web Research Summary

## Advanced RAG Patterns
- Query rewriting: LLM reformulates vague queries before retrieval
- HyDE: Generate hypothetical answer first, embed THAT, retrieve similar docs
- Step-back prompting: Decompose complex question into sub-questions, retrieve for each

## ColBERT Late Interaction
- Each token gets its own embedding (not one vector per passage)
- MaxSim: for each query token, find max similarity with any doc token, sum all
- Score(Q,D) = Σ max(qi · dj) for all qi
- Middle ground: precompute doc embeddings (like bi-encoder) but token-level matching (like cross-encoder)

## GraphRAG
- Build knowledge graph from documents (entities + relationships)
- Community detection → community summaries
- Query uses both vector search AND graph traversal
- Excels at "what are the main themes" type global queries where naive RAG fails

## RAGAS Evaluation
- Faithfulness: is answer grounded in retrieved context?
- Answer relevance: does it actually answer the question?
- Context precision: how much of retrieved context is relevant?
- Context recall: did we retrieve all needed information?

## Agentic RAG
- LLM decides when to retrieve, what query to use
- Self-corrective: reflects on answer quality, re-retrieves if needed
- Can use multiple tools: vector search, web search, SQL, etc.

## Long-context vs RAG
- Lost-in-the-middle: models ignore info in middle of very long contexts
- RAG: cheaper per query, scales to millions of docs
- Long-context: better for tightly interrelated info, sequential data
- Hybrid: retrieve top chunks, feed into moderate context window

## Embedding Fine-tuning
- MultipleNegativesRankingLoss most popular for sentence-transformers
- Hard negatives crucial for quality
- Domain-specific pairs needed
- LoRA for parameter-efficient tuning
