# GNN Section Rewrite Plan

## Running Example: Social Movie Recommendation
- 3 friends (Alice, Bob, Carol) with movie preferences
- Grows to small social graph, then molecules, then knowledge graphs

## Concept Ladder (dependency order):
1. Why graphs? (data that doesn't fit grids/sequences) - motivate with social network
2. Graph basics: nodes, edges, adjacency matrix, node features - toy example with 3 friends
3. The neighbor problem: how to learn from structure - motivate message passing
4. Message passing framework: message → aggregate → update
5. GCN (Kipf & Welling): simplest instantiation - weighted average of neighbors
6. REST STOP
7. GAT: when not all neighbors are equal - attention on graphs
8. GraphSAGE: when graphs are too big - sampling
9. Task types: node-level, edge-level, graph-level + pooling
10. Over-smoothing: the trap of going deep
11. Expressiveness: WL test and what GNNs can't see
12. Applications tour: molecules, social, recommendations, knowledge graphs
13. Frameworks: PyG and DGL

## Analogies (recurring):
1. "Neighborhood gossip" - nodes learning from neighbors like neighbors chatting
2. "Blurring an image" - over-smoothing = blurring, each layer = another blur pass

## Vulnerability moments:
1. Opening confession about avoiding graphs
2. Adjacency matrix notation initially confusing
3. Still developing intuition for why symmetric normalization works
4. Nobody fully knows optimal depth
5. WL test limitations are genuinely surprising
