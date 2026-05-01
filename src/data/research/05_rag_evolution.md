# RAG Evolution: From Naive Retrieval to Agentic Knowledge Systems

> *"The best model in the world is useless if it confidently tells you something that isn't true."*

Large Language Models transformed how we interact with knowledge. But they have a fatal
flaw: they hallucinate. They state falsehoods with the same confidence as facts. They
can't tell you what happened yesterday. They can't access your company's internal docs.

**Retrieval-Augmented Generation (RAG)** was the answer — ground the model in real data
at inference time. But the journey from "just retrieve some chunks" to the sophisticated
agentic knowledge systems of 2025 is a story of failure, iteration, and architectural
ingenuity.

This document traces that entire evolution.

---

## Table of Contents

1. [Why This Matters](#why-this-matters)
2. [The RAG Paradigm — Where It All Started](#the-rag-paradigm)
3. [Naive RAG and Its Failures](#naive-rag-and-its-failures)
4. [Advanced RAG Techniques](#advanced-rag-techniques)
5. [GraphRAG — Knowledge-Graph-Enhanced Retrieval](#graphrag)
6. [Corrective RAG & Self-Reflective RAG](#corrective-rag--self-reflective-rag)
7. [Agentic RAG](#agentic-rag)
8. [Multimodal RAG](#multimodal-rag)
9. [Evaluation — How Do You Know Your RAG Works?](#evaluation)
10. [The Full Evolution Timeline](#the-full-evolution-timeline)
11. [Key Papers & Sources](#key-papers--sources)
12. [Concepts for Knowledge Tree](#concepts-for-knowledge-tree)

---

## Why This Matters

Three hard truths about LLMs in production:

1. **Knowledge cutoff**: GPT-4's training data ends months before you use it. Your
   company's latest policy doc? It's never seen it.

2. **Hallucination**: LLMs generate plausible-sounding text even when they have no
   factual basis. In healthcare, legal, or financial contexts, this is catastrophic.

3. **No attribution**: A raw LLM can't tell you *where* it got its information.
   RAG gives you citations, traceability, and auditability.

**RAG solves all three** — by retrieving relevant documents at query time and feeding
them as context to the generator. But as adoption exploded (50%+ of enterprise AI
deployments by 2025), practitioners discovered that naive RAG fails in subtle,
dangerous ways.

The evolution from naive RAG to agentic knowledge systems isn't academic — it's the
difference between a demo that impresses and a system you can trust.

```
THE CORE PROMISE OF RAG:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   User Question ──► Retrieve Relevant Docs ──► Generate     │
│                     from Knowledge Base        Grounded     │
│                                                Answer       │
│                                                             │
│   Result: Factual, up-to-date, attributable responses       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## The RAG Paradigm

### The Original RAG Paper (Lewis et al., 2020)

The term "Retrieval-Augmented Generation" was coined by Patrick Lewis and colleagues
at Facebook AI Research (now Meta AI) in their landmark 2020 paper. The core insight
was deceptively simple:

> *What if we gave a language model the ability to look things up?*

Instead of storing all world knowledge in model parameters (parametric memory), RAG
combines:
- **Non-parametric memory**: A searchable document index (Wikipedia, your docs, etc.)
- **Parametric memory**: The language model's learned parameters (BART, in the original)

```
ORIGINAL RAG ARCHITECTURE (Lewis et al., 2020):
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   Input Query: "What is the capital of France?"                   ║
║        │                                                          ║
║        ▼                                                          ║
║   ┌──────────────┐     ┌─────────────────────────────────────┐   ║
║   │  Query        │     │  Document Index (Wikipedia)          │   ║
║   │  Encoder      │────►│  ~21M passages, FAISS indexed       │   ║
║   │  (DPR)        │     │  Dense vectors for each passage     │   ║
║   └──────────────┘     └──────────────┬──────────────────────┘   ║
║                                        │                          ║
║                              Top-k passages                       ║
║                                        │                          ║
║                                        ▼                          ║
║                          ┌────────────────────────┐               ║
║                          │  Seq2Seq Generator      │               ║
║                          │  (BART-large)           │               ║
║                          │                         │               ║
║                          │  Input: query +         │               ║
║                          │         retrieved docs  │               ║
║                          │  Output: answer         │               ║
║                          └────────────────────────┘               ║
║                                        │                          ║
║                                        ▼                          ║
║                          Answer: "Paris"                          ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### Dense Passage Retrieval (DPR)

The retrieval engine behind the original RAG was **DPR** (Karpukhin et al., 2020),
which introduced the idea of using dual BERT encoders — one for queries, one for
passages — to create dense vector representations. This was revolutionary because:

- **Sparse retrieval** (BM25/TF-IDF) matches keywords but misses semantic meaning
- **Dense retrieval** captures meaning: "canine" matches "dog" even without shared words

```
DPR: DUAL-ENCODER ARCHITECTURE
                                                         
   Query: "dog breeds"     Passage: "Popular canine varieties..."
        │                           │
        ▼                           ▼
   ┌──────────┐              ┌──────────┐
   │  BERT     │              │  BERT     │
   │  Query    │              │  Passage  │
   │  Encoder  │              │  Encoder  │
   └─────┬────┘              └─────┬────┘
         │                         │
         ▼                         ▼
      q ∈ ℝ^768               p ∈ ℝ^768
         │                         │
         └─────── sim(q, p) ───────┘
                     │
                dot product or
               cosine similarity
                     │
                     ▼
              relevance score
```

The key innovation: you pre-compute all passage embeddings offline, store them in
a FAISS index, and at query time you only need to encode the query and do an
approximate nearest neighbor search. This makes retrieval over millions of documents
sub-second.

### Two RAG Variants from the Original Paper

Lewis et al. proposed two formulations:

1. **RAG-Sequence**: Retrieves documents, generates the *entire* output sequence
   conditioned on the *same* retrieved document. Each retrieved doc generates a
   complete answer candidate; final answer is marginalized over documents.

2. **RAG-Token**: At *each token generation step*, the model can attend to different
   retrieved documents. More flexible — different parts of the answer can draw from
   different sources.

```
RAG-Sequence vs RAG-Token:

RAG-Sequence:                     RAG-Token:
┌─────────┐                       ┌─────────┐
│ Doc 1   │──► Full Answer 1      │ Doc 1   │──► Token 1
│ Doc 2   │──► Full Answer 2      │ Doc 2   │──► Token 2
│ Doc 3   │──► Full Answer 3      │ Doc 3   │──► Token 3
└─────────┘                       └─────────┘
     │                                 │
     ▼                                 ▼
  Marginalize                     Per-token
  over answers                    marginalization
     │                                 │
     ▼                                 ▼
  Final Answer                    Final Answer
```

### Why RAG Beats Fine-Tuning

For knowledge-intensive tasks, RAG has decisive advantages over fine-tuning:

| Dimension              | Fine-Tuning             | RAG                          |
|------------------------|-------------------------|------------------------------|
| Knowledge updates      | Retrain the model       | Update the document index    |
| Cost of updates        | $$$ (GPU hours)         | $ (re-index new docs)        |
| Hallucination control  | Hard                    | Easier (cited sources)       |
| Domain adaptation      | Needs labeled data      | Just add domain documents    |
| Transparency           | Black box               | Retrievals are inspectable   |
| Scalability            | Knowledge in weights    | Knowledge in external store  |

The original RAG paper showed state-of-the-art results on Natural Questions, TriviaQA,
and WebQuestions — outperforming models with 3x more parameters.

---

## Naive RAG and Its Failures

### The Simple Pipeline Everyone Builds First

When RAG entered the mainstream through LangChain and LlamaIndex in 2023, most
implementations followed a dead-simple pattern:

```
NAIVE RAG PIPELINE:
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  INDEXING PHASE (offline):                                       │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ Load     │───►│ Chunk    │───►│ Embed    │───►│ Store in │  │
│  │ Documents│    │ (fixed   │    │ (OpenAI  │    │ Vector   │  │
│  │ (PDF,    │    │  512     │    │  ada-002)│    │ DB       │  │
│  │  TXT)    │    │  tokens) │    │          │    │ (Pinecone│  │
│  └──────────┘    └──────────┘    └──────────┘    │  Chroma) │  │
│                                                   └──────────┘  │
│                                                                  │
│  QUERY PHASE (online):                                           │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ User     │───►│ Embed    │───►│ Retrieve │───►│ Generate │  │
│  │ Query    │    │ Query    │    │ Top-k    │    │ Answer   │  │
│  │          │    │          │    │ Chunks   │    │ (GPT-4)  │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

This works for demos. It fails in production. Here's why.

### The Seven Deadly Sins of Naive RAG

**1. Wrong Chunks Retrieved**
The query embedding and the relevant passage embedding don't always align. A question
about "Python memory management" might retrieve chunks about "Python snake habitat"
because both contain "Python" and "environment."

**2. Lost Context from Fixed-Size Chunking**
Splitting a document every 512 tokens is arbitrary. A critical explanation spanning
tokens 500-520 gets split across two chunks. Neither chunk alone makes sense.

**3. The "Needle in a Haystack" Problem**
When you retrieve top-5 chunks, the answer might be in chunk #8. Or worse, the
relevant information is spread across 20 chunks but you only retrieve 5.

**4. Redundant Retrieval**
Top-5 chunks might all say the same thing (near-duplicates from similar passages),
wasting the context window while missing diverse relevant information.

**5. Hallucination Despite Retrieval**
Even with relevant context provided, the LLM might ignore it and hallucinate anyway.
This is especially common when the retrieved context contradicts the model's
parametric knowledge.

**6. No Retrieval Quality Signal**
Naive RAG has no way to tell if the retrieved chunks are actually relevant. It
blindly passes whatever the vector search returns to the generator.

**7. Query-Document Mismatch**
Users ask questions. Documents contain statements. The semantic gap between
"What's the deadline for filing taxes?" and "Tax returns must be submitted by
April 15th" is larger than you'd think in embedding space.

```
WHY NAIVE RAG FAILS — THE INFORMATION LOSS CASCADE:

Original Document (rich, structured, contextual)
        │
        ▼  [LOSS 1: Chunking destroys structure]
Fixed-Size Chunks (context-free fragments)
        │
        ▼  [LOSS 2: Embedding compresses meaning]
Dense Vectors (768-dim approximation of meaning)
        │
        ▼  [LOSS 3: Top-k discards relevant results]
Retrieved Chunks (incomplete, possibly irrelevant)
        │
        ▼  [LOSS 4: LLM may ignore or misinterpret context]
Generated Answer (potentially hallucinated)
```

Every stage in naive RAG is a lossy compression of information. The rest of this
document is about how the field systematically addressed each loss point.

---

## Advanced RAG Techniques

The leap from naive to advanced RAG happened across three phases: **pre-retrieval**
optimization, **retrieval** improvement, and **post-retrieval** refinement.

```
ADVANCED RAG — THE THREE OPTIMIZATION PHASES:

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  PRE-RETRIEVAL         RETRIEVAL             POST-RETRIEVAL         │
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────────┐   │
│  │• Query        │    │• Hybrid search │    │• Re-ranking        │   │
│  │  rewriting    │    │  (dense+sparse)│    │• Contextual        │   │
│  │• Query        │───►│• Multi-index   │───►│  compression       │   │
│  │  decomposition│    │  retrieval     │    │• Deduplication     │   │
│  │• HyDE         │    │• Parent doc    │    │• Citation          │   │
│  │• Semantic     │    │  retrieval     │    │  extraction        │   │
│  │  chunking     │    │• Multi-query   │    │• Answer            │   │
│  │               │    │  fusion        │    │  validation        │   │
│  └───────────────┘    └───────────────┘    └───────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Pre-Retrieval: Fix the Query Before You Search

#### Query Transformation — Rewriting

The user's query is often a poor search query. Query rewriting uses an LLM to
transform the user's question into a better search query:

```python
# Naive query (what the user types):
"Why is my Lambda function timing out?"

# Rewritten query (what we actually search for):
"AWS Lambda function timeout causes configuration 
 memory allocation cold start execution duration limit"
```

The rewriter expands the query with relevant technical terms, resolves ambiguities,
and aligns the query closer to how the answer appears in the documents.

#### Query Decomposition

Complex questions need to be broken into sub-questions:

```
Original: "Compare the memory management approaches of Rust and Go, 
           and explain which is better for real-time systems"

Decomposed:
  Q1: "How does Rust manage memory? (ownership, borrowing, lifetimes)"
  Q2: "How does Go manage memory? (garbage collection, GC pauses)"
  Q3: "What are the requirements for real-time systems regarding memory?"

Each sub-question retrieves its own context.
Final synthesis combines all retrieved information.
```

#### HyDE — Hypothetical Document Embeddings

**HyDE** (Gao et al., 2022) is one of the most elegant ideas in RAG. The insight:

> *Questions and answers live in different regions of embedding space.
> What if we generated a hypothetical answer first, then used THAT
> as the search query?*

```
HyDE WORKFLOW:
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  User Query: "What causes aurora borealis?"                      │
│       │                                                          │
│       ▼                                                          │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │ LLM generates hypothetical answer (may be imperfect):   │     │
│  │ "Aurora borealis is caused by charged particles from    │     │
│  │  the Sun interacting with Earth's magnetic field and    │     │
│  │  atmosphere, exciting gas molecules which then emit     │     │
│  │  photons of light at various wavelengths..."            │     │
│  └─────────────────────────┬───────────────────────────────┘     │
│                             │                                     │
│                             ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │ Embed the HYPOTHETICAL ANSWER (not the question)        │     │
│  │ This embedding lives closer to real answers in          │     │
│  │ the vector space than the question embedding would      │     │
│  └─────────────────────────┬───────────────────────────────┘     │
│                             │                                     │
│                             ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │ Retrieve documents similar to the hypothetical answer   │     │
│  │ → Gets REAL documents that explain aurora borealis      │     │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

WHY IT WORKS:

    Embedding Space:

    Questions cluster here ──► •  "What causes aurora?"
                                       ↕  (large gap)
    Answers cluster here ───► •  "Aurora is caused by solar wind..."
                              •  "Charged particles from the sun..."  ← real docs
                              •  HyDE hypothetical answer lands HERE
                                       ↕  (small gap — better retrieval!)
```

HyDE works because the hypothetical answer, even if factually imperfect, is
*stylistically and semantically* closer to the real documents than the question is.

#### Semantic Chunking

Instead of blindly splitting every N tokens, semantic chunking respects the
document's natural structure:

```
FIXED-SIZE CHUNKING (naive):
┌──────────────────────────────────────────────┐
│ "The TCP handshake involves three steps.     │  Chunk 1
│ First, the client sends a SYN packet to the  │  (512 tokens)
│ server. The server responds with SYN-ACK.    │
│ Then the client sends an ACK. This establish │◄── CUT HERE (mid-sentence!)
├──────────────────────────────────────────────┤
│ es the connection. [NEW TOPIC] UDP, unlike   │  Chunk 2
│ TCP, is connectionless. It doesn't require   │  (512 tokens)
│ a handshake..."                              │
└──────────────────────────────────────────────┘
  Problem: TCP explanation split. UDP mixed into TCP chunk.

SEMANTIC CHUNKING (advanced):
┌──────────────────────────────────────────────┐
│ "The TCP handshake involves three steps.     │  Chunk 1: TCP Handshake
│ First, the client sends a SYN packet to the  │  (complete concept)
│ server. The server responds with SYN-ACK.    │
│ Then the client sends an ACK. This           │
│ establishes the connection."                 │
├──────────────────────────────────────────────┤
│ "UDP, unlike TCP, is connectionless. It      │  Chunk 2: UDP Protocol
│ doesn't require a handshake..."              │  (complete concept)
└──────────────────────────────────────────────┘
  Solution: Each chunk = one coherent idea.
```

**Techniques for semantic chunking:**
- **Sentence-boundary aware splitting** with overlap windows
- **Embedding similarity**: compute cosine similarity between consecutive sentences;
  split where similarity drops (topic boundary)
- **Section/heading-based**: use document structure (H1, H2, paragraphs)
- **LLM-based segmentation**: ask an LLM to identify logical break points
- **Recursive splitting**: split by sections → paragraphs → sentences, respecting
  a max token budget at each level

### Retrieval Phase: Get Better Results

#### Re-Ranking with Cross-Encoders

The fundamental insight: **retrieval** (bi-encoder) is fast but imprecise;
**re-ranking** (cross-encoder) is slow but accurate. Use both.

```
BI-ENCODER (Stage 1: Retrieval)        CROSS-ENCODER (Stage 2: Re-ranking)
                                        
Query ──► [Encoder] ──► q_vec           Query + Doc ──► [Transformer] ──► score
                          │                              
Docs ──► [Encoder] ──► d_vecs          Jointly processes query AND document
                          │             Full cross-attention between them
        cos_sim(q, d_i)  │             
                          ▼             Much more accurate, but O(n) forward
        Top-100 candidates              passes (can't pre-compute)
              │                                    │
              └──────── Feed top-100 ─────────────►│
                                                    ▼
                                              Re-ranked top-5
                                                    │
                                                    ▼
                                              To generator (LLM)
```

**Why this two-stage approach works:**

- Bi-encoders: embed query and docs independently. O(1) query time with FAISS.
  But they compress semantics into a single vector — lossy.
- Cross-encoders: process query-doc pairs jointly. Full transformer attention
  captures nuanced relevance. But O(n) per candidate — too slow for millions of docs.
- **Solution**: Bi-encoder retrieves top-100 cheaply. Cross-encoder re-ranks
  those 100 into the best 5. Best of both worlds.

**Production re-rankers:**
- **Cohere Rerank**: API-based, drop-in re-ranker
- **ColBERT**: Late interaction model — multi-vector representations allow
  token-level matching while remaining efficient
- **bge-reranker**: Open-source cross-encoder from BAAI
- **FlashRank**: Lightweight, fast re-ranker for edge deployment

#### Multi-Query Retrieval and Fusion

Generate multiple search queries for one user question, retrieve for each,
then fuse results using **Reciprocal Rank Fusion (RRF)**:

```
MULTI-QUERY RETRIEVAL + RRF FUSION:

User Question: "How does photosynthesis affect climate change?"
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Query 1:     Query 2:     Query 3:
   "photosyn-   "carbon      "plants role
    thesis       dioxide      in climate
    process      absorption   regulation"
    mechanism"   by plants"
        │           │           │
        ▼           ▼           ▼
   Retrieve     Retrieve     Retrieve
   Top-10       Top-10       Top-10
        │           │           │
        └───────────┼───────────┘
                    │
                    ▼
         Reciprocal Rank Fusion:
         ┌──────────────────────────────────────────┐
         │ For each document d across all lists:     │
         │                                           │
         │   RRF(d) = Σ  1 / (k + rank_i(d))       │
         │            i                              │
         │                                           │
         │ where k = 60 (constant), i = each query  │
         │                                           │
         │ Documents ranked by total RRF score       │
         └──────────────────────────────────────────┘
                    │
                    ▼
         Final ranked list (diverse, robust)
```

**Why RRF works**: A document that appears in the top-10 for multiple query
formulations is almost certainly relevant. RRF naturally promotes documents
with broad relevance while still including uniquely relevant results from
individual queries.

#### Parent Document Retrieval

The problem: small chunks embed well but lack context. Large chunks have
context but embed poorly (too much noise in the vector).

**Solution**: Index small chunks, but retrieve their parent documents.

```
PARENT DOCUMENT RETRIEVAL:

Document: "Machine Learning Textbook, Chapter 5: Neural Networks"
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
 Section 5.1:   Section 5.2:   Section 5.3:
 "Perceptrons"  "Backprop"     "Activation
                                Functions"
    │               │               │
    ▼               ▼               ▼
 Child chunks    Child chunks    Child chunks
 (small, for     (small, for     (small, for
  embedding)      embedding)      embedding)

RETRIEVAL:
  1. User asks about "vanishing gradients in deep networks"
  2. Vector search matches a child chunk in Section 5.2
  3. Instead of returning JUST that child chunk...
  4. Return the ENTIRE Section 5.2 (the "parent")
  5. Parent has full context: backprop algorithm, chain rule,
     gradient flow, vanishing gradient problem, solutions

RESULT: Small chunks for precise matching, 
        large parents for rich context.
```

#### Contextual Compression

After retrieval, you often have more context than you need. Contextual
compression extracts only the relevant portions:

```
BEFORE COMPRESSION:
Retrieved chunk (500 tokens):
"Machine learning is a subset of AI. [200 tokens of history]
 The learning rate determines how quickly the model converges.
 A learning rate that is too high causes divergence, while one
 that is too low leads to slow convergence. [100 tokens of 
 tangential information about batch sizes]"

Query: "What happens if learning rate is too high?"

AFTER COMPRESSION:
Compressed context (50 tokens):
"A learning rate that is too high causes divergence — the model
 overshoots the optimal parameters and loss increases instead
 of decreasing."

BENEFIT: More room in context window for other relevant chunks.
```

**Compression techniques:**
- **LLM-based extraction**: Ask an LLM to extract only relevant sentences
- **Sentence scoring**: Score each sentence for query relevance, keep top-k
- **Abstractive compression**: Summarize the chunk focused on the query

#### Hybrid Search (Dense + Sparse)

Neither dense nor sparse retrieval is universally better. Combine them:

```
HYBRID SEARCH:

Query: "Python 3.12 match statement syntax"
              │
    ┌─────────┴─────────┐
    ▼                    ▼
Dense Search          Sparse Search
(Semantic)            (Keyword/BM25)
    │                    │
Finds docs about      Finds docs with
pattern matching,     exact term "match
structural matching   statement", "3.12"
in general            Python version
    │                    │
    └────────┬───────────┘
             ▼
    Weighted combination:
    final_score = α × dense_score + (1-α) × sparse_score
    
    (α typically 0.5–0.7)
             │
             ▼
    Best of both worlds:
    semantic understanding + keyword precision
```

---

## GraphRAG

### The Problem Vector RAG Can't Solve

Standard vector RAG excels at finding specific passages that answer specific
questions. But it fails at questions requiring **global understanding** or
**multi-hop reasoning**:

- "What are the main themes across all customer complaints this quarter?"
- "How does the marketing strategy connect to the engineering roadmap?"
- "Summarize the key relationships between characters in this novel."

These questions require synthesizing information scattered across many documents
— exactly what Microsoft's **GraphRAG** was designed for.

### Microsoft's GraphRAG Architecture

GraphRAG (Edge et al., 2024) builds a **knowledge graph** from your documents,
then uses that graph structure for retrieval and reasoning:

```
GRAPHRAG: END-TO-END ARCHITECTURE

PHASE 1: INDEXING (Offline)
═══════════════════════════════════════════════════════════════

Documents ──► Text Chunks ──► LLM Entity & Relationship Extraction
                                          │
                                          ▼
                              ┌──────────────────────┐
                              │   Knowledge Graph     │
                              │                       │
                              │  (Entities)           │
                              │   • "OpenAI" ─────┐   │
                              │   • "GPT-4"  ─────┤   │
                              │   • "Sam Altman" ──┤   │
                              │                    │   │
                              │  (Relationships)   │   │
                              │   OpenAI ──created──► GPT-4       │
                              │   Sam Altman ──CEO_of──► OpenAI   │
                              │   GPT-4 ──successor_of──► GPT-3.5 │
                              └──────────┬───────────┘
                                         │
                                         ▼
                              Community Detection
                              (Leiden algorithm)
                                         │
                                         ▼
                              ┌──────────────────────┐
                              │ Community Summaries   │
                              │                       │
                              │ Community 1: "AI      │
                              │  leadership & org     │
                              │  structure at OpenAI" │
                              │                       │
                              │ Community 2: "GPT     │
                              │  model family and     │
                              │  capabilities"        │
                              └──────────────────────┘

PHASE 2: QUERYING (Online)
═══════════════════════════════════════════════════════════════

          ┌─────────────────────────────────────┐
          │        Two Query Modes:              │
          │                                      │
          │  LOCAL SEARCH        GLOBAL SEARCH   │
          │  (specific facts)   (broad themes)   │
          │                                      │
          │  Starts from         Searches         │
          │  entity nodes,       community        │
          │  traverses graph     summaries,        │
          │  neighborhood        aggregates        │
          │                      across all        │
          │  Good for:           communities       │
          │  "Who is the                           │
          │   CEO of X?"        Good for:          │
          │                     "What are the      │
          │                      main themes?"     │
          └─────────────────────────────────────┘
```

### How GraphRAG Builds the Knowledge Graph

The process uses **LLM-powered extraction** — the same LLM that will answer
questions is first used to read every chunk and extract entities and relationships:

```
ENTITY & RELATIONSHIP EXTRACTION:

Input chunk: "In March 2023, OpenAI released GPT-4, a large 
multimodal model. Sam Altman, CEO of OpenAI, announced it 
could accept image inputs and demonstrated improved reasoning."

LLM extracts:
  Entities:
    - OpenAI (Organization)
    - GPT-4 (AI Model)
    - Sam Altman (Person)
    
  Relationships:
    - OpenAI ──released──► GPT-4 (March 2023)
    - Sam Altman ──CEO_of──► OpenAI
    - GPT-4 ──has_capability──► multimodal input
    - GPT-4 ──has_capability──► improved reasoning
```

### Community Detection and Summarization

The Leiden algorithm partitions the graph into communities — clusters of
densely connected entities. Each community gets an LLM-generated summary:

```
COMMUNITY HIERARCHY:

Level 0 (most granular):
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Community A  │  │ Community B  │  │ Community C  │
│ GPT models   │  │ OpenAI org   │  │ AI safety    │
│ & benchmarks │  │ & leadership │  │ research     │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        │
Level 1 (broader):      ▼
               ┌─────────────────┐
               │ Meta-Community   │
               │ "OpenAI's AI     │
               │  development     │
               │  ecosystem"      │
               └─────────────────┘
```

### When GraphRAG Beats Vector RAG

| Question Type                        | Vector RAG | GraphRAG |
|--------------------------------------|------------|----------|
| Specific factual lookup              | ✅ Great   | ⚠️ Overkill |
| Multi-hop reasoning                  | ❌ Fails   | ✅ Great |
| Global summarization ("main themes") | ❌ Fails   | ✅ Great |
| Entity relationship queries          | ⚠️ Partial | ✅ Great |
| Simple Q&A over short docs           | ✅ Great   | ⚠️ Overkill |
| Cost-sensitive applications          | ✅ Cheap   | ❌ Expensive |

**The cost caveat**: GraphRAG requires an LLM call for every chunk during indexing
to extract entities. For large corpora, this indexing cost can be substantial.

---

## Corrective RAG & Self-Reflective RAG

### The Core Problem: Retrieval Isn't Always Right

Advanced RAG improves retrieval quality, but no retrieval system is perfect.
Sometimes the retrieved chunks are simply wrong, irrelevant, or insufficient.
What then?

The next evolution introduced **self-aware retrieval** — systems that can
detect their own failures and correct them.

### CRAG: Corrective Retrieval-Augmented Generation

**CRAG** (Yan et al., 2024) adds a **retrieval evaluator** that grades the
quality of retrieved documents before passing them to the generator:

```
CRAG ARCHITECTURE:
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║  User Query ──► Retriever ──► Retrieved Documents                 ║
║                                      │                            ║
║                                      ▼                            ║
║                          ┌──────────────────────┐                 ║
║                          │  Retrieval Evaluator  │                 ║
║                          │  (Lightweight model)  │                 ║
║                          └──────────┬───────────┘                 ║
║                                     │                             ║
║                    ┌────────────────┼────────────────┐            ║
║                    ▼                ▼                ▼             ║
║               ┌────────┐    ┌────────────┐    ┌──────────┐       ║
║               │CORRECT │    │ AMBIGUOUS  │    │ INCORRECT│       ║
║               │        │    │            │    │          │       ║
║               │Use docs │    │Refine docs │    │Discard   │       ║
║               │as-is    │    │+ web search│    │docs, use │       ║
║               │         │    │for more    │    │web search│       ║
║               │         │    │context     │    │instead   │       ║
║               └────┬───┘    └─────┬──────┘    └────┬─────┘       ║
║                    │              │                  │             ║
║                    └──────────────┼──────────────────┘            ║
║                                   ▼                               ║
║                          ┌──────────────────┐                     ║
║                          │ Knowledge         │                     ║
║                          │ Refinement        │                     ║
║                          │ (strip irrelevant │                     ║
║                          │  sentences)       │                     ║
║                          └────────┬─────────┘                     ║
║                                   ▼                               ║
║                          ┌──────────────────┐                     ║
║                          │    Generator      │                     ║
║                          │    (LLM)          │                     ║
║                          └──────────────────┘                     ║
║                                   │                               ║
║                                   ▼                               ║
║                            Final Answer                           ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

**CRAG's three retrieval confidence actions:**

1. **Correct** (high confidence): Retrieved docs are relevant → use them directly
   after knowledge refinement (stripping irrelevant sentences)
2. **Incorrect** (low confidence): Retrieved docs are irrelevant → discard them
   entirely, fall back to web search for fresh information
3. **Ambiguous** (medium confidence): Uncertain → combine refined retrieved docs
   with supplementary web search results

The **knowledge refinement** step is critical: even when retrieval is "correct,"
CRAG decomposes each document into fine-grained knowledge strips and filters
out irrelevant sentences. This combats the problem of LLMs being distracted
by irrelevant information in long contexts.

### Self-RAG: The Model That Decides When to Retrieve

**Self-RAG** (Asai et al., 2023) goes further. Instead of always retrieving,
the model learns to **decide when retrieval is needed** and **critiques its
own outputs**:

```
SELF-RAG: ADAPTIVE RETRIEVAL WITH SELF-REFLECTION
═══════════════════════════════════════════════════════════════

Step 1: SHOULD I RETRIEVE?
┌──────────────────────────────────────────────────────────┐
│ Input: "What is the capital of France?"                  │
│                                                          │
│ Model generates token: [Retrieve] = YES                  │
│ (For "What is 2+2?", it would generate [No Retrieve])   │
└──────────────────────────────────────────────────────────┘
                    │
                    ▼ (if YES)
Step 2: RETRIEVE AND GENERATE
┌──────────────────────────────────────────────────────────┐
│ Retrieve passages → Generate response segments           │
│                                                          │
│ For each segment, model generates CRITIQUE TOKENS:       │
│                                                          │
│ [ISREL] — Is the retrieved passage relevant?             │
│           Values: {relevant, irrelevant}                 │
│                                                          │
│ [ISSUP] — Is this claim supported by the passage?        │
│           Values: {fully supported, partially supported, │
│                    no support}                            │
│                                                          │
│ [ISUSE] — Is the overall response useful?                │
│           Values: {5, 4, 3, 2, 1}                        │
└──────────────────────────────────────────────────────────┘
                    │
                    ▼
Step 3: SELECT BEST OUTPUT
┌──────────────────────────────────────────────────────────┐
│ Multiple candidate segments are scored by critique       │
│ tokens. The best-scoring segments are selected and       │
│ assembled into the final response.                       │
│                                                          │
│ If no segment scores well → re-retrieve with modified    │
│ query or generate without retrieval                      │
└──────────────────────────────────────────────────────────┘
```

**What makes Self-RAG special:**

1. **Adaptive retrieval**: Not every question needs retrieval. "What is 2+2?"
   doesn't need a document lookup. Self-RAG learns when to retrieve.

2. **Self-critique via special tokens**: The model is trained to emit reflection
   tokens that evaluate its own output's quality, support, and relevance.

3. **Training approach**: Self-RAG fine-tunes an LLM (Llama 2 in the paper)
   using a critic model to generate training data with reflection tokens.
   The model learns to generate both content and quality assessments.

### Comparing the Approaches

```
EVOLUTION OF RETRIEVAL AWARENESS:

Naive RAG:      Always retrieve → Always use → Hope for the best
                (no quality check at any stage)

Advanced RAG:   Always retrieve → Re-rank → Use top results
                (quality check on RETRIEVAL only)

CRAG:           Always retrieve → EVALUATE quality → Correct if bad
                (quality check on retrieval + correction)

Self-RAG:       DECIDE whether to retrieve → Retrieve if needed →
                Generate → CRITIQUE output → Select best
                (quality checks everywhere)

Agentic RAG:    PLAN retrieval strategy → Execute → Evaluate →
                Re-plan if needed → Multi-source → Synthesize
                (full autonomy over the entire process)
```

---

## Agentic RAG

### From Pipeline to Agent

All the RAG systems discussed so far are **pipelines** — fixed sequences of
steps. Agentic RAG transforms RAG into an **agent workflow** where the system
can plan, act, observe, and adapt dynamically.

```
PIPELINE RAG vs AGENTIC RAG:

Pipeline RAG (fixed flow):
Query ──► Retrieve ──► Generate ──► Answer
  (same steps every time, no adaptation)

Agentic RAG (dynamic, adaptive):
Query ──► Plan ──► Act ──► Observe ──► Reflect ──► Re-plan ──► ...
  │         │       │        │          │            │
  │         │       │        │          │            └─ "I need more info,
  │         │       │        │          │               let me try a
  │         │       │        │          │               different source"
  │         │       │        │          │
  │         │       │        │          └─ "This retrieval was
  │         │       │        │             low quality, retry"
  │         │       │        │
  │         │       │        └─ "Got 3 relevant docs,
  │         │       │           2 irrelevant, need more"
  │         │       │
  │         │       └─ Execute: vector search, SQL query,
  │         │          API call, web search, graph traversal
  │         │
  │         └─ "I'll need to: 1) search docs, 2) query DB,
  │            3) check latest data via API"
  │
  └─ "Compare Q3 revenue across regions including trends"
```

### The Agentic RAG Architecture

```
AGENTIC RAG — FULL ARCHITECTURE:
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   User Query                                                          ║
║       │                                                               ║
║       ▼                                                               ║
║   ┌───────────────────────────────────────────────────────────┐      ║
║   │              ORCHESTRATOR / CONTROLLER                     │      ║
║   │                                                            │      ║
║   │  • Maintains conversation state and memory                 │      ║
║   │  • Decides WHICH tools to use and in WHAT ORDER            │      ║
║   │  • Evaluates intermediate results                          │      ║
║   │  • Decides when to stop (answer is sufficient)             │      ║
║   │                                                            │      ║
║   └───────────────────┬───────────────────────────────────────┘      ║
║                       │                                               ║
║         ┌─────────────┼─────────────┐                                ║
║         ▼             ▼             ▼                                 ║
║   ┌──────────┐  ┌──────────┐  ┌──────────┐                          ║
║   │  TOOL 1  │  │  TOOL 2  │  │  TOOL 3  │                          ║
║   │  Vector  │  │  Graph   │  │  SQL      │   ...more tools          ║
║   │  Search  │  │  Query   │  │  Query    │                          ║
║   └────┬─────┘  └────┬─────┘  └────┬─────┘                          ║
║        │              │              │                                ║
║        ▼              ▼              ▼                                ║
║   ┌──────────┐  ┌──────────┐  ┌──────────┐                          ║
║   │ Pinecone │  │ Neo4j    │  │ Postgres │                          ║
║   │ / Chroma │  │ Graph DB │  │ / MySQL  │                          ║
║   └──────────┘  └──────────┘  └──────────┘                          ║
║                                                                       ║
║   ┌──────────┐  ┌──────────┐  ┌──────────┐                          ║
║   │  TOOL 4  │  │  TOOL 5  │  │  TOOL 6  │                          ║
║   │  Web     │  │  Code    │  │  API      │                          ║
║   │  Search  │  │  Exec    │  │  Call     │                          ║
║   └──────────┘  └──────────┘  └──────────┘                          ║
║                                                                       ║
║   ┌───────────────────────────────────────────────────────────┐      ║
║   │              RESPONSE SYNTHESIZER                          │      ║
║   │                                                            │      ║
║   │  • Aggregates results from all tools                       │      ║
║   │  • Resolves conflicts between sources                      │      ║
║   │  • Generates cited, coherent answer                        │      ║
║   │  • Self-validates before returning                         │      ║
║   └───────────────────────────────────────────────────────────┘      ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

### Routing: The Intelligence Layer

A key capability of agentic RAG is **routing** — deciding which retrieval
strategy to use based on the query:

```
QUERY ROUTING DECISION TREE:

User Query
    │
    ▼
┌─────────────────────────────────────────┐
│ ROUTER (LLM-based or classifier)        │
│                                          │
│ Analyzes query intent, complexity,       │
│ required data sources                    │
└──────────────────┬──────────────────────┘
                   │
    ┌──────────────┼──────────────┬──────────────┐
    ▼              ▼              ▼              ▼
 Factual        Analytical     Multi-hop      Temporal
 lookup         query          reasoning      query
    │              │              │              │
    ▼              ▼              ▼              ▼
 Vector         SQL +           Graph          Vector +
 search         Vector          traversal      date filter +
 (fast)         (structured)    (relational)   web search
                                               (freshness)

Examples:
"What is X?"        → Vector search
"Show Q3 revenue"   → SQL query
"How does A affect  → GraphRAG traversal
 B through C?"
"Latest news on X"  → Web search + vector search
```

### Multi-Agent RAG

For complex enterprise scenarios, multiple specialized agents collaborate:

```
MULTI-AGENT RAG:

                    ┌──────────────────┐
                    │  META-AGENT       │
                    │  (Orchestrator)   │
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                  ▼
    ┌────────────┐   ┌────────────┐    ┌────────────┐
    │ Research    │   │ Data       │    │ Compliance │
    │ Agent      │   │ Analyst    │    │ Agent      │
    │            │   │ Agent      │    │            │
    │ • Searches │   │ • SQL      │    │ • Checks   │
    │   papers   │   │   queries  │    │   policies │
    │ • Reads    │   │ • Charts   │    │ • Validates│
    │   docs     │   │ • Stats    │    │   claims   │
    └────────────┘   └────────────┘    └────────────┘
           │                 │                  │
           └─────────────────┼──────────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ SYNTHESIS AGENT   │
                    │ Combines results, │
                    │ resolves conflicts│
                    │ generates answer  │
                    └──────────────────┘
```

### Agentic RAG Design Patterns

**Pattern 1: Iterative Retrieval**
```
Retrieve → Read → "Not enough info" → Refine query → Retrieve again →
Read → "Now I have enough" → Generate answer
```

**Pattern 2: Tool Selection**
```
"Revenue data" → SQL tool
"Policy document" → Vector search tool
"Latest regulations" → Web search tool
All results → Synthesize
```

**Pattern 3: Verification Loop**
```
Generate answer → Fact-check against sources → If inconsistency found →
Re-retrieve → Re-generate → Verify again → Return when confident
```

**Pattern 4: Hierarchical Retrieval**
```
Broad search (thousands of docs) → Narrow to relevant set →
Deep dive into specific passages → Extract precise answer
```

### Frameworks for Agentic RAG

| Framework    | Key Strength                           | Best For                        |
|-------------|----------------------------------------|---------------------------------|
| LangGraph    | Graph-based agent workflows            | Complex, stateful RAG agents    |
| LlamaIndex   | Deep indexing & retrieval abstractions | Document-heavy RAG applications |
| CrewAI       | Multi-agent collaboration              | Team-of-agents RAG systems      |
| AutoGen      | Microsoft's agent framework            | Enterprise agentic workflows    |
| Haystack     | Production-ready pipelines             | Scalable RAG deployments        |

---

## Multimodal RAG

### Beyond Text: The Next Frontier

Real-world documents aren't just text. They contain tables, charts, diagrams,
photographs, and complex layouts. Multimodal RAG extends retrieval to handle
all of these:

```
MULTIMODAL RAG PIPELINE:
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  INDEXING:                                                        │
│  ┌──────────┐    ┌───────────────────────────────────────────┐  │
│  │ Document  │───►│  Multi-modal Processing:                  │  │
│  │ (PDF with │    │  • Text → text embeddings                │  │
│  │  tables,  │    │  • Tables → structured extraction OR     │  │
│  │  images,  │    │           table embeddings               │  │
│  │  charts)  │    │  • Images → vision model embeddings      │  │
│  └──────────┘    │  • Charts → description + data extraction │  │
│                   └───────────────────┬───────────────────────┘  │
│                                       │                          │
│                                       ▼                          │
│                              Multi-modal Vector Store             │
│                              (text, image, table vectors)        │
│                                                                  │
│  RETRIEVAL:                                                      │
│  ┌──────────┐    ┌───────────────────────────────────────────┐  │
│  │ Query:    │───►│  Cross-modal retrieval:                   │  │
│  │ "Show     │    │  Text query → matches text chunks        │  │
│  │  revenue  │    │  Text query → matches relevant tables    │  │
│  │  trends"  │    │  Text query → matches relevant charts    │  │
│  └──────────┘    └───────────────────────────────────────────┘  │
│                                       │                          │
│                                       ▼                          │
│                          ┌──────────────────────┐               │
│                          │ Multimodal LLM        │               │
│                          │ (GPT-4V, Gemini)      │               │
│                          │ Processes text +      │               │
│                          │ images + tables       │               │
│                          └──────────────────────┘               │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### ColPali: Vision-First Document Retrieval

**ColPali** (Faysse et al., 2024) represents a paradigm shift in document
retrieval. Instead of the traditional OCR → text extraction → embedding pipeline,
ColPali **directly embeds document page images** using a Vision Language Model:

```
TRADITIONAL DOCUMENT RETRIEVAL vs COLPALI:

Traditional Pipeline (lossy):
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Document  │───►│ OCR /    │───►│ Text     │───►│ Embed    │
│ Page Image│    │ Parser   │    │ Extract  │    │ Text     │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                     │
                  LOSES: layout, visual structure, table 
                  formatting, chart data, image context

ColPali Pipeline (preserves everything):
┌──────────┐    ┌──────────────────────────────┐    ┌──────────┐
│ Document  │───►│ Vision Language Model (PaliGemma)│───►│ Multi-   │
│ Page Image│    │ Processes the raw page image     │    │ vector   │
│           │    │ Understands text + layout +       │    │ embeddings│
│           │    │ tables + figures simultaneously   │    │ (patches) │
└──────────┘    └──────────────────────────────┘    └──────────┘

KEY: ColPali uses LATE INTERACTION (from ColBERT):
- Each page patch gets its own embedding vector
- Query tokens interact with page patch embeddings
- Token-level matching captures fine-grained relevance

                Query: "Q3 revenue table"
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
 "Q3"          "revenue"     "table"
 token          token         token
    │             │             │
    ▼             ▼             ▼
 MaxSim with   MaxSim with   MaxSim with
 all page      all page      all page
 patches       patches       patches
    │             │             │
    └─────────────┼─────────────┘
                  │
                  ▼
            Sum of MaxSim scores = page relevance
```

**Why ColPali matters:**

1. **No OCR needed**: Bypasses the entire text extraction pipeline and its errors
2. **Layout-aware**: Understands that a number in a table header means something
   different than the same number in body text
3. **Visual elements**: Can match queries to charts, diagrams, and figures
4. **Multilingual by default**: Vision models read text in any language/script
5. **Fast**: Late interaction allows efficient retrieval at scale

### Table Understanding

Tables are a particular pain point for traditional RAG:

```
THE TABLE PROBLEM:

Original table in PDF:
┌──────────┬──────────┬──────────┐
│ Region   │ Q3 2024  │ Q4 2024  │
├──────────┼──────────┼──────────┤
│ North    │ $2.1M    │ $2.4M    │
│ South    │ $1.8M    │ $1.9M    │
│ East     │ $3.2M    │ $3.5M    │
└──────────┴──────────┴──────────┘

After naive text extraction:
"Region Q3 2024 Q4 2024 North $2.1M $2.4M South 
$1.8M $1.9M East $3.2M $3.5M"
  → Structure LOST. Query "Q4 East revenue" may not match.

Multimodal RAG approaches:
1. TABLE SERIALIZATION: Convert to markdown/CSV format
2. TABLE EMBEDDING: Embed the table as a structured unit
3. TABLE DESCRIPTION: LLM generates natural language description
4. VISION-BASED: ColPali embeds the visual table directly
```

### Multimodal RAG Approaches Compared

| Approach            | Handles Text | Handles Tables | Handles Images | Complexity |
|---------------------|:------------:|:--------------:|:--------------:|:----------:|
| Text-only RAG       | ✅           | ⚠️ Lossy       | ❌             | Low        |
| Text + Table RAG    | ✅           | ✅             | ❌             | Medium     |
| Vision RAG (ColPali)| ✅           | ✅             | ✅             | Medium     |
| Full Multimodal RAG | ✅           | ✅             | ✅             | High       |

---

## Evaluation

### Why Evaluating RAG Is Hard

RAG evaluation is harder than evaluating a standalone LLM because there are
**two systems to evaluate** (retriever + generator) with **complex interactions**
between them:

```
RAG EVALUATION DIMENSIONS:

                    ┌─────────────────────────────────────┐
                    │         RETRIEVAL QUALITY            │
                    │                                      │
                    │  Did we find the RIGHT documents?    │
                    │  • Context Precision                 │
                    │  • Context Recall                    │
                    │  • Hit Rate / MRR                    │
                    └──────────────────┬──────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────┐
                    │        GENERATION QUALITY            │
                    │                                      │
                    │  Given context, is the answer good?  │
                    │  • Faithfulness (no hallucination)   │
                    │  • Answer Relevance                  │
                    │  • Completeness                      │
                    └──────────────────┬──────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────┐
                    │         END-TO-END QUALITY           │
                    │                                      │
                    │  Does the whole system work?         │
                    │  • Correctness vs ground truth       │
                    │  • User satisfaction                 │
                    │  • Latency / Cost                    │
                    └─────────────────────────────────────┘
```

### The RAGAS Framework

**RAGAS** (Retrieval Augmented Generation Assessment Suite) by Es et al. (2023)
provides automated, reference-free metrics for RAG evaluation:

```
RAGAS METRICS — THE FOUR PILLARS:
═══════════════════════════════════════════════════════════════

1. FAITHFULNESS
   ┌──────────────────────────────────────────────────────┐
   │ "Is every claim in the answer supported by the       │
   │  retrieved context?"                                  │
   │                                                       │
   │ Process:                                              │
   │ 1. Decompose answer into individual claims            │
   │ 2. For each claim, check if context supports it       │
   │ 3. Score = supported_claims / total_claims            │
   │                                                       │
   │ Score 1.0 = fully grounded                            │
   │ Score 0.0 = completely hallucinated                   │
   └──────────────────────────────────────────────────────┘

2. ANSWER RELEVANCE
   ┌──────────────────────────────────────────────────────┐
   │ "Does the answer actually address the question?"      │
   │                                                       │
   │ Process:                                              │
   │ 1. Generate N hypothetical questions from the answer  │
   │ 2. Compare these questions to the original question   │
   │ 3. Score = average similarity of generated questions  │
   │    to original question                               │
   │                                                       │
   │ High = answer addresses the question                  │
   │ Low = answer is off-topic or incomplete               │
   └──────────────────────────────────────────────────────┘

3. CONTEXT PRECISION
   ┌──────────────────────────────────────────────────────┐
   │ "Of the retrieved chunks, how many are relevant?"     │
   │                                                       │
   │ Precision = relevant_chunks / total_retrieved_chunks  │
   │                                                       │
   │ High = retriever returns mostly useful context        │
   │ Low = lots of irrelevant noise in retrieved context   │
   └──────────────────────────────────────────────────────┘

4. CONTEXT RECALL
   ┌──────────────────────────────────────────────────────┐
   │ "Did we retrieve all the information needed?"         │
   │                                                       │
   │ Recall = retrieved_relevant / total_relevant          │
   │                                                       │
   │ High = we found everything we need                    │
   │ Low = missing critical information                    │
   └──────────────────────────────────────────────────────┘
```

**RAGAS usage in Python:**
```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)

# Prepare evaluation dataset
eval_data = {
    "question": ["What is the capital of France?"],
    "answer": ["The capital of France is Paris."],
    "contexts": [["Paris is the capital and largest city of France."]],
    "ground_truth": ["Paris"]
}

# Run evaluation
results = evaluate(
    dataset=eval_data,
    metrics=[faithfulness, answer_relevancy, 
             context_precision, context_recall]
)
# Results: {faithfulness: 1.0, answer_relevancy: 0.95, 
#           context_precision: 1.0, context_recall: 1.0}
```

### Beyond RAGAS: Other Evaluation Approaches

| Method              | Type           | Best For                              |
|---------------------|----------------|---------------------------------------|
| RAGAS               | Automated, LLM | Component-level RAG metrics           |
| ARES                | Automated, LLM | Large-scale RAG evaluation            |
| RECALL              | Automated      | Retrieval quality focus               |
| LLM-as-Judge        | Automated, LLM | General quality assessment            |
| Human Evaluation    | Manual         | Ground truth, nuanced quality         |
| A/B Testing         | Statistical    | Production comparison                 |
| Unit Tests (RAG)    | Deterministic  | Regression testing for RAG changes    |

### The RAG Evaluation Checklist

```
PRODUCTION RAG EVALUATION CHECKLIST:

□ Retrieval Metrics:
  □ Context Precision: Are retrieved chunks relevant?
  □ Context Recall: Are all relevant chunks retrieved?
  □ MRR (Mean Reciprocal Rank): Is the best chunk ranked first?
  □ Retrieval Latency: How fast is retrieval?

□ Generation Metrics:
  □ Faithfulness: Does the answer stick to the evidence?
  □ Answer Relevance: Does it answer the actual question?
  □ Completeness: Does it cover all aspects of the question?
  □ Hallucination Rate: How often does it make things up?

□ System Metrics:
  □ End-to-End Latency: Total time from query to answer
  □ Cost per Query: LLM tokens + retrieval compute
  □ Throughput: Queries per second
  □ User Satisfaction: Thumbs up/down, feedback loops

□ Robustness:
  □ Out-of-scope queries: Does it say "I don't know"?
  □ Adversarial queries: Can it be tricked?
  □ Multi-turn consistency: Same facts across conversation?
```

---

## The Full Evolution Timeline

```
RAG EVOLUTION TIMELINE:
═══════════════════════════════════════════════════════════════

2020 │ FOUNDATIONS
     │ ├── Lewis et al.: Original RAG paper (Meta AI)
     │ ├── Karpukhin et al.: Dense Passage Retrieval (DPR)
     │ └── REALM (Google): Pre-training with retrieval
     │
2021 │ SCALING
     │ ├── RETRO (DeepMind): Retrieval-enhanced transformers
     │ ├── Atlas: Few-shot learning with retrieval
     │ └── FiD (Fusion-in-Decoder): Multi-passage generation
     │
2022 │ PRACTICAL RAG
     │ ├── HyDE: Hypothetical Document Embeddings
     │ ├── LangChain launches → RAG becomes accessible
     │ ├── InstructGPT + RAG patterns emerge
     │ └── Pinecone, Weaviate, Chroma: Vector DB boom
     │
2023 │ ADVANCED RAG
     │ ├── Self-RAG: Adaptive, self-reflective retrieval
     │ ├── LlamaIndex matures → production RAG patterns
     │ ├── RAGAS: First RAG evaluation framework
     │ ├── Cross-encoder re-ranking becomes standard
     │ ├── Semantic chunking techniques formalized
     │ ├── Multi-query retrieval + RRF fusion
     │ └── Hybrid search (dense + sparse) as best practice
     │
2024 │ GRAPH + AGENTIC RAG
     │ ├── Microsoft GraphRAG: Knowledge graph RAG
     │ ├── CRAG: Corrective retrieval augmented generation
     │ ├── ColPali: Vision-based document retrieval
     │ ├── Agentic RAG patterns emerge (LangGraph, CrewAI)
     │ ├── Contextual Retrieval (Anthropic)
     │ ├── Late chunking techniques
     │ └── Enterprise RAG adoption crosses 50%
     │
2025 │ MATURE AGENTIC SYSTEMS
     │ ├── Multi-agent RAG architectures
     │ ├── Modular, plug-and-play RAG components
     │ ├── Privacy-aware and temporal-decay retrieval
     │ ├── Multimodal RAG becomes production-ready
     │ └── RAG + Long-context models: complementary, not competing
     │
```

---

## Key Papers & Sources

### Foundational Papers
1. **RAG Original** — Lewis et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." https://arxiv.org/abs/2005.11401
2. **DPR** — Karpukhin et al. (2020). "Dense Passage Retrieval for Open-Domain Question Answering." https://arxiv.org/abs/2004.04906
3. **REALM** — Guu et al. (2020). "Retrieval Augmented Language Model Pre-Training." https://arxiv.org/abs/2002.08909
4. **FiD** — Izacard & Grave (2020). "Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering." https://arxiv.org/abs/2007.01282

### Advanced Techniques
5. **HyDE** — Gao et al. (2022). "Precise Zero-Shot Dense Retrieval without Relevance Labels." https://arxiv.org/abs/2212.10496
6. **Self-RAG** — Asai et al. (2023). "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." https://arxiv.org/abs/2310.11511
7. **CRAG** — Yan et al. (2024). "Corrective Retrieval Augmented Generation." https://arxiv.org/abs/2401.15884
8. **GraphRAG** — Edge et al. (2024). "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." https://arxiv.org/abs/2404.16130
9. **ColPali** — Faysse et al. (2024). "ColPali: Efficient Document Retrieval with Vision Language Models." https://arxiv.org/abs/2407.01449
10. **ColBERT** — Khattab & Zaharia (2020). "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction." https://arxiv.org/abs/2004.12832

### Evaluation
11. **RAGAS** — Es et al. (2023). "RAGAS: Automated Evaluation of Retrieval Augmented Generation." https://arxiv.org/abs/2309.15217
12. **ARES** — Saad-Falcon et al. (2023). "ARES: An Automated Evaluation Framework for RAG Systems." https://arxiv.org/abs/2311.09476

### Surveys & Overviews
13. **RAG Survey** — Gao et al. (2024). "Retrieval-Augmented Generation for Large Language Models: A Survey." https://arxiv.org/abs/2312.10997
14. **Advanced RAG Techniques** — WillowTree (2024). "15 Advanced RAG Techniques." https://www.willowtreeapps.com/guides/advanced-rag-techniques
15. **Systematic Review of RAG** — Brown et al. (2025). "A Systematic Literature Review of RAG." https://www.mdpi.com/2504-2289/9/12/320
16. **Microsoft GraphRAG GitHub** — https://github.com/microsoft/graphrag
17. **RAGAS GitHub** — https://github.com/explodinggradients/ragas
18. **Reciprocal Rank Fusion** — Cormack et al. (2009). https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf

### Practical Resources
19. **LangChain RAG Documentation** — https://python.langchain.com/docs/tutorials/rag/
20. **LlamaIndex RAG Guide** — https://docs.llamaindex.ai/en/stable/
21. **Anthropic Contextual Retrieval** — https://www.anthropic.com/news/contextual-retrieval

---

## Concepts for Knowledge Tree

1. **Retrieval-Augmented Generation (RAG)** — combining retrieval with generation
2. **Dense Passage Retrieval (DPR)** — dual-encoder dense vector retrieval
3. **Sparse Retrieval (BM25/TF-IDF)** — keyword-based document matching
4. **Hybrid Search** — combining dense and sparse retrieval
5. **Vector Databases** — specialized stores for embedding similarity search (FAISS, Pinecone, Chroma)
6. **Embedding Models** — encoding text into dense vector representations
7. **Chunking Strategies** — fixed-size, semantic, recursive, section-based
8. **Semantic Chunking** — splitting documents by meaning boundaries
9. **Query Transformation** — rewriting queries for better retrieval
10. **Query Decomposition** — breaking complex queries into sub-questions
11. **HyDE (Hypothetical Document Embeddings)** — generating fake answers for better search
12. **Re-ranking** — second-stage relevance scoring of retrieved results
13. **Cross-Encoder Re-rankers** — joint query-document scoring models
14. **Bi-Encoder Retrieval** — independent encoding of queries and documents
15. **ColBERT Late Interaction** — multi-vector retrieval with token-level matching
16. **Multi-Query Retrieval** — generating multiple queries per user question
17. **Reciprocal Rank Fusion (RRF)** — merging multiple ranked lists
18. **Parent Document Retrieval** — indexing small chunks, returning large parents
19. **Contextual Compression** — extracting only relevant parts of retrieved context
20. **GraphRAG** — knowledge-graph-enhanced retrieval and reasoning
21. **Knowledge Graph Construction** — extracting entities and relationships from text
22. **Community Detection (Leiden Algorithm)** — clustering graph nodes
23. **Multi-hop Reasoning** — answering questions requiring multiple inference steps
24. **Corrective RAG (CRAG)** — evaluating and correcting retrieval quality
25. **Self-RAG** — adaptive retrieval with self-reflection tokens
26. **Retrieval Evaluation Tokens** — special tokens for assessing retrieval quality
27. **Agentic RAG** — RAG as autonomous agent with planning and tool use
28. **Query Routing** — directing queries to appropriate retrieval backends
29. **Multi-Agent RAG** — multiple specialized agents collaborating on retrieval
30. **Multimodal RAG** — retrieval across text, images, tables, and charts
31. **ColPali** — vision-first document retrieval bypassing OCR
32. **Table Understanding** — extracting and querying structured table data
33. **RAGAS Evaluation Framework** — automated RAG quality metrics
34. **Faithfulness Metric** — measuring answer grounding in context
35. **Context Precision/Recall** — retrieval quality measurements
36. **Answer Relevance** — measuring if answers address the question
37. **Hallucination Detection** — identifying unsupported claims in generated text
38. **RAG vs Fine-Tuning** — tradeoffs between retrieval and parameter updates
39. **Fusion-in-Decoder (FiD)** — multi-passage generation architecture
40. **Contextual Retrieval** — Anthropic's approach to adding context to chunks before embedding

---

## Summary: The Arc of RAG Evolution

```
THE ARC OF RAG — FROM NAIVE TO AGENTIC:

NAIVE RAG (2022-2023):
  "Chunk it, embed it, retrieve it, hope for the best"
  Problem: Wrong chunks, lost context, hallucination
       │
       ▼
ADVANCED RAG (2023-2024):
  "Better chunking, better queries, better ranking"
  Solution: HyDE, re-ranking, semantic chunking, fusion
  Problem: Still a fixed pipeline, no self-awareness
       │
       ▼
MODULAR RAG (2024):
  "Composable components, plug-and-play"
  Solution: Swappable retrievers, rankers, generators
  Problem: No intelligence about WHEN and HOW to retrieve
       │
       ▼
SELF-AWARE RAG (2024):
  "Know when retrieval fails, correct it"
  Solution: CRAG, Self-RAG, retrieval evaluation
  Problem: Still limited to predefined strategies
       │
       ▼
AGENTIC RAG (2024-2025):
  "Plan, retrieve, evaluate, adapt, multi-source, multi-modal"
  Solution: Full agent autonomy, tool selection, verification loops
  Current frontier of the field
       │
       ▼
WHAT'S NEXT:
  • RAG + long-context models (complementary, not competing)
  • Personalized RAG (user-adaptive retrieval)
  • Streaming RAG (real-time knowledge updates)
  • Federated RAG (privacy-preserving cross-org retrieval)
  • Continuous learning RAG (model updates from retrieval patterns)
```

The evolution of RAG mirrors the broader evolution of AI systems: from rigid
pipelines to adaptive, self-aware agents. Each generation solved the failures
of the last while revealing new challenges.

The field isn't done. But the trajectory is clear: RAG is becoming less about
retrieval and more about **intelligent knowledge access** — systems that know
what they know, know what they don't know, and know how to find out.

---

*Last updated: 2025*
