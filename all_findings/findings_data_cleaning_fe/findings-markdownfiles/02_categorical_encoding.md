# Categorical Encoding Findings

## Key Insights

### Target Encoding Leakage Problem
- Using whole dataset to compute mean "sees" target value for the row being encoded
- Proper approaches: CV encoding, Leave-One-Out, add noise, regularization (blend global mean with category mean)
- For rare categories, MUST regularize toward global mean

### Embedding Layers vs One-Hot
- One-hot: explodes with high cardinality, can't generalize to unseen values
- Embeddings: learn dense low-dim representations, capture similarities, scale to millions of categories
- Embeddings are standard for deep learning on high-cardinality (user IDs, product IDs)

### Hashing Trick
- Hash categories into fixed number of buckets
- No need to know all categories beforehand (great for streaming)
- Collisions inevitable but often acceptable noise
- Irreversible—can't decode back

### Frequency Encoding
- Replace category with its frequency count
- Problem: categories with same frequency become indistinguishable
- Works when frequency itself is informative

### Practical Decision Framework
- Classical ML + low cardinality → one-hot
- Classical ML + high cardinality → target encoding (with CV) or hashing
- Deep learning → embedding layers
- Streaming/online → hashing trick
