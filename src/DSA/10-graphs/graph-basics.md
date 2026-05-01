# Graph Basics

> Graphs are the backbone of ~20% of all FAANG interview questions — if you can't model a problem as a graph, you're stuck.

## Core Idea

A **graph** is a set of **vertices** (nodes) connected by **edges**. The trick in interviews isn't implementing graphs — it's *recognizing* that a problem IS a graph problem. Grids, dependency chains, social networks, word transformations — all graphs in disguise.

## What You Need to Know

### Representations

| Representation | Space | Check Edge | Get Neighbors | Best For |
|---------------|-------|-----------|---------------|----------|
| **Adjacency List** | O(V + E) | O(degree) | O(degree) | Sparse graphs (most interviews) |
| **Adjacency Matrix** | O(V²) | O(1) | O(V) | Dense graphs, quick edge lookup |
| **Edge List** | O(E) | O(E) | O(E) | Kruskal's, simple storage |

**Almost always use an adjacency list.** Interview graphs are sparse.

### Key Terminology

| Term | Meaning |
|------|---------|
| **Directed vs Undirected** | Edges have direction (A→B) or not (A—B) |
| **Weighted vs Unweighted** | Edges carry costs or not |
| **Cycle** | Path that returns to its start |
| **DAG** | Directed Acyclic Graph — has direction, no cycles |
| **Connected** | Every node reachable from every other (undirected) |
| **Strongly Connected** | Every node reachable from every other (directed) |
| **In-degree / Out-degree** | Number of incoming / outgoing edges at a node |
| **Bipartite** | Nodes split into two groups, edges only between groups |

### Building Graphs in Python

```python
# Adjacency list from edge list (most common interview setup)
from collections import defaultdict

def build_graph(edges, directed=False):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# Weighted graph
def build_weighted(edges, directed=False):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph
```

### Grid as Graph

Grids are implicit graphs. Each cell is a node, neighbors are adjacent cells.

```python
# Standard 4-directional movement
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbors(r, c, rows, cols):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```

### Cycle Detection

| Graph Type | Method | How |
|-----------|--------|-----|
| Undirected | DFS | Visit neighbor that's already visited AND isn't parent |
| Directed | DFS with 3 colors | White (unvisited) → Gray (in stack) → Black (done). Gray→Gray = cycle |
| Undirected | Union-Find | If two nodes in same component get an edge → cycle |

```python
# Directed cycle detection with 3-color DFS
def has_cycle(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY:    # back edge → cycle
                return True
            if color[nei] == WHITE and dfs(nei):
                return True
        color[node] = BLACK
        return False

    return any(color[i] == WHITE and dfs(i) for i in range(n))
```

### Bipartite Check

Two-color the graph. If any neighbor shares a color → not bipartite. O(V + E).

```python
def is_bipartite(graph, n):
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    queue.append(nei)
                elif color[nei] == color[node]:
                    return False
    return True
```

## Key Patterns & Templates

### Clone Graph (LC 133)

DFS + hash map — the map acts as both "visited" set and clone registry.

```python
def cloneGraph(node):
    if not node:
        return None
    clones = {}

    def dfs(n):
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy  # register BEFORE recursing (handles cycles)
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Number of Islands | 200 | Medium | Count DFS/BFS launches = count components |
| Clone Graph | 133 | Medium | Hash map as visited + clone registry |
| Is Graph Bipartite? | 785 | Medium | 2-color BFS/DFS |
| Number of Connected Components | 323 | Medium | DFS count or Union-Find |
| Graph Valid Tree | 261 | Medium | Connected + no cycle = tree (edges == n-1) |
| Surrounded Regions | 130 | Medium | Reverse thinking — DFS from border |

## Common Mistakes

- **Forgetting to handle disconnected components** — always loop over ALL nodes, not just node 0
- **Grid DFS without marking visited before recursion** — causes infinite loops on undirected/grid graphs
- **Building directed graph when problem needs undirected** (or vice versa) — read the problem carefully
- **Not handling self-loops or parallel edges** — some problems have them
- **Using adjacency matrix for sparse graph** — wastes memory and time iterating neighbors

## Interview Questions

- "What's the difference between adjacency list and adjacency matrix? When would you pick each?"
- "How would you detect a cycle in a directed graph vs an undirected graph?"
- "Given a grid of 0s and 1s, how many islands are there?" (LC 200 — Amazon asks this weekly)
- "How do you clone a graph with cycles?" (LC 133)
- "Is this graph bipartite? How would you check?"
- "How would you represent a weighted graph? An unweighted graph?"
- "What's the time complexity of BFS/DFS on an adjacency list vs adjacency matrix?"
- "Given n nodes and a list of edges, is this a valid tree?" (LC 261)

## Quick Reference

```
Graph type → Representation:
  Sparse (E << V²)     → Adjacency List  ✓
  Dense (E ≈ V²)       → Adjacency Matrix
  Edge-centric algo    → Edge List

Problem recognition:
  "Connected components"  → DFS/BFS/Union-Find
  "Shortest path"         → BFS (unweighted) / Dijkstra (weighted)
  "Dependencies/ordering" → Topological Sort
  "Cycle?"                → DFS coloring (directed) / Union-Find (undirected)
  "Grid traversal"        → DFS/BFS with 4-directional neighbors

Complexity (adjacency list):
  DFS/BFS:  O(V + E) time, O(V) space
  Building: O(V + E)
```
