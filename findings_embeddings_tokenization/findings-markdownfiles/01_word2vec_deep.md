# Word2Vec Deep Notes

## Key Insights
- Skip-gram: predict context from center word. Better for rare words.
- CBOW: predict center from context. Faster training.
- Negative sampling: binary classification (real vs fake pairs) instead of softmax over V
- 3/4 power on unigram distribution: empirical, flattens distribution so rare words get sampled more
- Two weight matrices: input (embedding we keep) and output (context matrix, usually discarded)
- Subsampling frequent words: randomly discard "the", "a" etc with probability proportional to frequency

## The Real Insight
Word2Vec doesn't understand meaning. It understands co-occurrence patterns. "King" and "queen" end up close not because the model knows about royalty, but because they appear in nearly identical contexts ("The ___ of England", "crowned ___").

## Negative Sampling Math
- For real pair (w, c): maximize sigmoid(v_c · v_w)
- For k negative samples: maximize sigmoid(-v_neg · v_w)
- Reduces O(V) to O(k) per training step
- k=5-15 typical. Smaller k for large datasets, larger k for small.

## Levy & Goldberg (2014) showed Word2Vec implicitly factorizes a shifted PMI matrix
