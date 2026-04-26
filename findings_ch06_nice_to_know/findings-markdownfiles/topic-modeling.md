# Topic Modeling: LDA vs BERTopic

## LDA (Latent Dirichlet Allocation)
- Classical probabilistic model from 2003 (Blei, Ng, Jordan)
- Each document = mixture of topics, each topic = mixture of words
- Bag-of-words assumption — ignores word order and semantics
- Fast, scalable, interpretable, lightweight
- Still found in legacy NLP pipelines
- Struggles with short text, synonyms, multilingual data

## BERTopic (2022+)
- Pipeline: sentence embeddings → UMAP reduction → HDBSCAN clustering → c-TF-IDF topic representation
- Captures semantic meaning, handles synonyms, short texts
- Supports dynamic topics over time, multilingual
- Heavier — needs transformer embeddings (GPU helps)
- Modern default for topic modeling in 2024+

## NMF (Non-negative Matrix Factorization)
- V ≈ W × H with non-negative constraint
- Parts-based decomposition — components only add, never subtract
- More interpretable than PCA for non-negative data
- Used in topic modeling, recommender systems, audio source separation
- Quick alternative to LDA for topic extraction

## Key insight
LDA asks "what distribution of topics generated this document?" — a generative story.
BERTopic asks "which documents are semantically similar?" — an embedding + clustering story.
NMF says "decompose this matrix into additive parts" — a linear algebra story.
