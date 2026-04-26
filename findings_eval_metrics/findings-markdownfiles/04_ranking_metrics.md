# Ranking Metrics — Deep Findings

## MRR (Mean Reciprocal Rank)
- Where does FIRST correct result appear?
- Position 1 → 1.0, Position 3 → 0.333, Position 10 → 0.1
- Only cares about first hit — ignores all others
- Best for: navigational search, QA, entity linking

## MAP (Mean Average Precision)
- Considers ALL relevant results and their positions
- Precision@k at each relevant hit, averaged
- Binary relevance only (relevant/not relevant)
- Workhorse for IR with multiple relevant docs

## NDCG (Normalized Discounted Cumulative Gain)
- Handles GRADED relevance (not just binary)
- Discounts by log-position: top results matter more
- Normalized by ideal DCG → range [0,1]
- NDCG@10 is standard for search quality
- DCG = rel_1 + Σ(rel_i / log2(i+1))

## Key Insight
- MRR → "did you find THE answer?"
- MAP → "did you find ALL the answers and put them first?"
- NDCG → "did you rank BETTER answers higher?"
