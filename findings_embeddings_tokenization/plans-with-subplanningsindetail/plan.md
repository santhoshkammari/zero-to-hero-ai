# Rewrite Plan for ch11/s02.html - Embeddings & Tokenization

## Running Example
A movie recommendation chatbot that needs to understand user reviews.
- Start with tiny vocabulary: "love", "loved", "loving", "hate", "hated", "great", "movie"
- Use this throughout to show why one-hot fails, how Word2Vec learns, how tokenization handles morphology

## Concept Ladder (dependency order)
1. One-hot encoding and its limitations (the bedrock)
2. The distributional hypothesis - words known by their company
3. Word2Vec Skip-gram - predicting neighbors
4. Word2Vec CBOW - predicting the center
5. The softmax bottleneck and negative sampling
6. GloVe - the global view
7. FastText - breaking words into pieces
8. **REST STOP** - static embeddings mental model
9. The polysemy problem - why static fails
10. ELMo - context-dependent representations
11. BERT and contextual embeddings
12. The vocabulary problem - why tokenization matters
13. BPE algorithm
14. WordPiece
15. Unigram/SentencePiece
16. Byte-level BPE
17. Vocabulary size and embedding dimension tradeoffs
18. Positional embeddings recap
19. Wrap-up

## Recurring Analogies
1. **Address book analogy**: One-hot = storing people by numbered slots (no relationship info). Embeddings = placing people on a map where neighbors share traits.
2. **Lego analogy**: Subword tokens are like Lego bricks - you can build any word from reusable pieces.

## Vulnerability Moments
1. Opening confession about avoiding embeddings
2. "I still find it wild that..." about king-queen analogy
3. Admitting GloVe vs Word2Vec equivalence surprised me
4. "I'm still developing my intuition for..." why 3/4 power works
5. Acknowledging tokenizer equity issues
