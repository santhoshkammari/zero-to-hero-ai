# Minimum Spanning Tree

> "Connect all nodes at minimum cost" — classic MST. Less frequent in interviews than BFS/DFS/toposort, but when it shows up, you need to nail it.

## Core Idea

A **Minimum Spanning Tree** (MST) connects all vertices in an undirected, weighted graph with the minimum total edge weight, using exactly V-1 edges and no cycles. Two algorithms: **Kruskal's** (sort edges, greedily add with Union-Find) and **Prim's** (grow from a vertex using a min-heap). Both are greedy — MST is one of the cleanest greedy proofs in CS.

## What You Need to Know

### Kruskal's vs Prim's

| | Kruskal's | Prim's |
|---|---|---|
| Strategy | Sort all edges, add smallest that doesn't create cycle | Grow tree from a vertex, always add cheapest edge to a new node |
| Data structure | Union-Find | Min-heap (priority queue) |
| Time | O(E log E) | O(E log V) |
| Better for | Sparse graphs (E ≈ V) | Dense graphs (E ≈ V²) |
| Edge-centric | ✅ Works directly on edge list | ❌ Needs adjacency list |

In interviews, **Kruskal's is more common** because it pairs naturally with Union-Find, which is itself a frequent interview topic.

### Kruskal's Algorithm

```python
def kruskal(n, edges):
    """edges: list of (weight, u, v)"""
    edges.sort()  # sort by weight
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = 0
    
    for w, u, v in edges:
        if uf.union(u, v):  # no cycle
            mst_cost += w
            mst_edges += 1
            if mst_edges == n - 1:
                break
    
    return mst_cost if mst_edges == n - 1 else -1  # -1 if not connected
```

**Time: O(E log E)** for sorting. Union-Find operations are nearly O(1).

### Prim's Algorithm

```python
import heapq

def prim(n, graph):
    """graph: adjacency list with (neighbor, weight)"""
    visited = set()
    heap = [(0, 0)]  # (weight, node) — start from node 0
    mst_cost = 0
    
    while heap and len(visited) < n:
        w, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        mst_cost += w
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (weight, v))
    
    return mst_cost if len(visited) == n else -1
```

**Time: O(E log V)** — each edge push/pop is O(log V).

### When MST Comes Up in Interviews

MST problems are often disguised:
- "**Minimum cost to connect all cities**" → MST
- "**Minimum cost to add edges to make graph connected**" → MST
- "**Connecting points with minimum cost**" → build complete graph, run Kruskal's/Prim's

## Key Patterns & Templates

### Min Cost to Connect All Points (LC 1584)

Points in 2D plane. Cost between two points = Manhattan distance. Connect all with minimum total cost.

```python
def minCostConnectPoints(points):
    n = len(points)
    # Build edge list with Manhattan distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))
    
    # Kruskal's
    edges.sort()
    uf = UnionFind(n)
    cost = 0
    for w, u, v in edges:
        if uf.union(u, v):
            cost += w
            if uf.count == 1:
                break
    return cost
```

For large n, Prim's with a heap is better — avoids creating O(n²) edges upfront.

```python
def minCostConnectPoints_prim(points):
    n = len(points)
    visited = set()
    heap = [(0, 0)]  # (cost, point_index)
    total = 0
    
    while len(visited) < n:
        cost, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        total += cost
        for v in range(n):
            if v not in visited:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(heap, (dist, v))
    return total
```

### MST Properties to Know

- MST has exactly **V - 1** edges
- MST is **unique** if all edge weights are distinct
- **Cut property:** the lightest edge crossing any cut must be in the MST
- **Cycle property:** the heaviest edge in any cycle is NOT in the MST
- Adding any non-MST edge to the MST creates exactly one cycle

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Min Cost to Connect All Points | 1584 | Medium | MST on complete graph; Kruskal's or Prim's |
| Connecting Cities With Minimum Cost | 1135 | Medium | Direct Kruskal's application |
| Minimum Spanning Tree (generic) | — | — | Know both algorithms cold |
| Critical and Pseudo-Critical Edges | 1489 | Hard | Try MST without/with each edge to classify |
| Optimize Water Distribution | 1168 | Hard | Add virtual node for wells, then MST |

## Common Mistakes

- **Forgetting Union-Find optimizations in Kruskal's** — without path compression and union by rank, it's O(E·V) instead of O(E log E)
- **Not checking if graph is connected** — if MST has fewer than V-1 edges, graph isn't connected
- **Prim's: not skipping visited nodes after heap pop** — same issue as Dijkstra's lazy deletion
- **Building O(n²) edges when Prim's would be more efficient** — for dense/complete graphs, Prim's avoids materializing all edges
- **Confusing MST with shortest path** — MST minimizes total edge weight of the *tree*, not paths between specific nodes

## Interview Questions

- "Connect all cities at minimum cost." (LC 1135/1584)
- "What's the difference between Kruskal's and Prim's? When would you prefer each?"
- "Prove that the greedy choice in Kruskal's is correct." (Cut property)
- "How many edges does an MST have?"
- "If all edge weights are distinct, is the MST unique? Prove it."
- "Which edges are critical for the MST? Which are replaceable?" (LC 1489)
- "How would you find MST if some nodes already have connections (e.g., wells)?" (Virtual node trick)

## Quick Reference

```
MST = connect all V nodes with V-1 edges at minimum total weight

Kruskal's:                           Prim's:
  1. Sort edges by weight              1. Start from any node
  2. For each edge (small→large):      2. Add cheapest edge to unvisited node
     - If no cycle (UF), add it        3. Repeat until all nodes visited
  3. Stop at V-1 edges
  Time: O(E log E)                     Time: O(E log V)
  Uses: Union-Find                     Uses: Min-heap
  Best: Sparse graphs                  Best: Dense graphs

Key properties:
  Edges in MST:     V - 1
  Cut property:     lightest edge across any cut ∈ MST
  Cycle property:   heaviest edge in any cycle ∉ MST
  Unique MST:       guaranteed if all weights distinct
```
