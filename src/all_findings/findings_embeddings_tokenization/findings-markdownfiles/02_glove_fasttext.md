# GloVe and FastText Notes

## GloVe
- Builds global co-occurrence matrix X where X_ij = count of word j near word i
- Factorizes: w_i · w_j + b_i + b_j ≈ log(X_ij)
- Weighted least squares with f(X_ij) weighting function
- Key insight from paper: ratio of co-occurrence probabilities encodes meaning
  - P(ice|solid)/P(ice|gas) >> 1, P(steam|solid)/P(steam|gas) << 1
- Final vectors: w + w_tilde (sum of word and context vectors)

## FastText
- Each word = bag of character n-grams (n=3 to 6 typically)
- "where" → <wh, whe, her, ere, re>, <where>
- Word vector = sum of all n-gram vectors
- Handles OOV by composing from known n-grams
- Great for morphologically rich languages (Turkish, Finnish, German)
- Training: same as Word2Vec skip-gram + negative sampling

## Key comparison
- Word2Vec: local context windows, no global stats
- GloVe: global co-occurrence, explicit matrix factorization
- Levy & Goldberg showed they're equivalent under certain conditions
- FastText: adds subword info on top of Word2Vec architecture
