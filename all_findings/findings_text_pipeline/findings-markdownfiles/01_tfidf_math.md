# TF-IDF Mathematical Intuition

## Why log in IDF
- Information theory connection: IDF mirrors Shannon's self-information = -log(P(event))
- Log prevents rare terms from exploding in weight
- Converts multiplicative ratios to additive scale
- Empirically matches diminishing returns of informativeness

## sklearn smoothed formula
- `log((1 + N) / (1 + df(t))) + 1` — avoids zero division, never fully zeroes a term
- L2 normalization applied per row — dot product of normalized vectors = cosine similarity

## Key insight for writing
- The log is NOT arbitrary — it comes from info theory. A word in 1/1000 docs is NOT 1000x more important than one in 1/100 docs. The log captures this diminishing return.
