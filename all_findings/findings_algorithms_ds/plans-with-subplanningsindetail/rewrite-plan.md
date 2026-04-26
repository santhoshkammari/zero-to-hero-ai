# Rewrite Plan: Algorithms & Data Structures for ML

## Running Example
A recommendation engine that suggests movies to users — starts tiny (3 movies, 5 users), grows naturally.

## Concept Ladder (dependency order)
1. Arrays & contiguous memory → why vectorized ops are fast
2. Hash maps → feature stores, vocab lookups, O(1) serving
3. Trees → decision trees in models, KD-trees for neighbor search, B-trees in databases
4. The curse of dimensionality → KD-trees fail, motivates ANN
5. HNSW & approximate nearest neighbors → the real solution for embeddings
6. Graphs → computation graphs, autograd as topological sort, GNNs
7. Heaps & priority queues → beam search, top-K retrieval
8. Dynamic programming → Viterbi, beam search connection
9. Tries → tokenizer vocabulary lookup, BPE
10. Bloom filters → training data deduplication at scale
11. Algorithmic complexity → Big-O intuition, offline vs online
12. Self-attention quadratic cost → why it matters, efficient alternatives

## Rest Stop
After: arrays, hash maps, trees, graphs, heaps — the "data structures" half
Before: complexity analysis, ANN, bloom filters, DP — the "algorithms" half

## Vulnerability Moments
1. Opening: avoided DS&A, felt like academic gatekeeping
2. KD-trees: "I assumed KD-trees would work for embeddings. They don't."
3. HNSW: "I'm still building intuition for why the layered structure works so well"
4. Complexity: "I got burned by an O(n²) operation in production"
5. Bloom filters: "The idea that 'probably yes, definitely no' is useful felt wrong at first"

## Recurring Analogies
1. Library/warehouse: data structures as different ways to organize a warehouse
2. City navigation: HNSW as expressways → highways → local roads
3. Filing cabinet vs pile: organized retrieval vs brute force
