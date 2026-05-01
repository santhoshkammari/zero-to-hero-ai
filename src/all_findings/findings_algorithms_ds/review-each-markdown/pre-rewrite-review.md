# Pre-Rewrite Review of Current s14.html

## What's Wrong (per GENERIC_SECTION_REVIEW guidelines)
1. Reads like a reference card — lists data structures with brief ML connections
2. No personal journey, no vulnerability, no running example
3. Doesn't go deep enough — misses HNSW, bloom filters, DP/Viterbi, tries in tokenizers
4. The Big-O table is useful but presented as a table, not built up through frustration
5. No rest stop, no progressive disclosure
6. Code examples are isolated snippets, not part of a narrative
7. Missing the "why" — just describes what things are, not why they matter when things break

## What to Keep
- The HTML structure (sidebar, nav, head, scripts)
- The general topic coverage (arrays, hash maps, trees, graphs, heaps, complexity)
- Page navigation links

## What to Add
- Brandon-style opening with personal confession
- Running example (recommendation engine)
- HNSW / ANN for embeddings (critical modern topic)
- Bloom filters for training data dedup
- Dynamic programming → Viterbi → beam search connection
- Tries in tokenizers
- Self-attention quadratic complexity
- Rest stop
- Proper wrap-up with gratitude and future hope
- Vulnerability moments throughout
