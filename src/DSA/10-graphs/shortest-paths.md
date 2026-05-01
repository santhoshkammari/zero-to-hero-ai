# Shortest Paths

> "Find the cheapest/fastest/shortest route" — this is Dijkstra's, Bellman-Ford, or BFS depending on edge weights. Pick wrong and your solution is broken.

## Core Idea

Different graph properties demand different algorithms. **Unweighted** → BFS. **Non-negative weights** → Dijkstra's. **Negative weights** → Bellman-Ford. **All pairs** → Floyd-Warshall. **Weights are 0 or 1** → 0-1 BFS with a deque. There's no universal shortest path algorithm — the choice depends on constraints.

## What You Need to Know

### Algorithm Selection

| Algorithm | Time | Space | Handles Negative | Use Case |
|-----------|------|-------|-----------------|----------|
| **BFS** | O(V + E) | O(V) | N/A (unweighted) | Unweighted graphs |
| **Dijkstra's** | O((V+E) log V) | O(V) | ❌ No | Non-negative weights |
| **Bellman-Ford** | O(V·E) | O(V) | ✅ Yes | Negative weights, detects negative cycles |
| **Floyd-Warshall** | O(V³) | O(V²) | ✅ Yes | All-pairs shortest path |
| **0-1 BFS** | O(V + E) | O(V) | N/A (0 or 1) | Weights are only 0 or 1 |

### Dijkstra's Algorithm

Greedy: always process the closest unvisited node. Uses a **min-heap** (priority queue).

**Why it fails with negative weights:** Once a node is "finalized" (popped from heap), Dijkstra assumes its distance is optimal. A negative edge later could reduce it — but Dijkstra won't revisit it.

```python
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:  # skip stale entries
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

**Key detail:** The `if d > dist[u]: continue` line is critical — it skips outdated heap entries instead of using a visited set. This is the lazy deletion approach, which is simpler and works perfectly.

**Time: O((V + E) log V)** — each edge potentially adds to the heap, each pop is O(log V).

### Bellman-Ford Algorithm

Relax all edges V-1 times. If any edge can still be relaxed after V-1 rounds, there's a **negative cycle**.

```python
def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Negative cycle detection
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # negative cycle exists
    return dist
```

**Why V-1 rounds?** Shortest path has at most V-1 edges. Each round guarantees at least one more node gets its correct distance.

### Bellman-Ford with K Stops Constraint

For "cheapest flight with at most K stops" (LC 787), limit to K+1 relaxation rounds and **copy the dist array each round** to prevent cascading updates.

```python
def cheapest_flights(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0
    
    for _ in range(k + 1):
        prev = dist[:]  # copy to prevent cascading
        for u, v, w in flights:
            if prev[u] != float('inf') and prev[u] + w < dist[v]:
                dist[v] = prev[u] + w
    
    return dist[dst] if dist[dst] != float('inf') else -1
```

### Floyd-Warshall (All-Pairs)

```python
def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
    
    for k in range(n):          # intermediate node
        for i in range(n):      # source
            for j in range(n):  # destination
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

**Loop order matters:** `k` (intermediate) must be the outermost loop. Think of it as: "what's the shortest path from i to j using only nodes {0..k} as intermediates?"

### 0-1 BFS

When edge weights are only 0 or 1, use a **deque**: push weight-0 neighbors to the front, weight-1 neighbors to the back. This gives O(V + E) — same as regular BFS.

```python
from collections import deque

def zero_one_bfs(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])
    
    while dq:
        u = dq.popleft()
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist
```

## Key Patterns & Templates

### Network Delay Time (LC 743) — Classic Dijkstra

```python
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = dijkstra(graph, k, n + 1)  # 1-indexed
    ans = max(dist[1:n+1])
    return ans if ans < float('inf') else -1
```

### Word Ladder (LC 127) — BFS Shortest Path

The graph isn't given explicitly — you build it. The trick: use wildcard patterns instead of O(n²) pairwise comparison.

```python
def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, steps = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word == endWord:
                    return steps + 1
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))
    return 0
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Network Delay Time | 743 | Medium | Textbook Dijkstra; answer = max of all distances |
| Cheapest Flights Within K Stops | 787 | Medium | Bellman-Ford with K+1 rounds; copy dist array each round |
| Word Ladder | 127 | Hard | BFS shortest path; wildcard neighbor generation |
| Path With Minimum Effort | 1631 | Medium | Dijkstra where weight = max abs diff along path |
| Swim in Rising Water | 778 | Hard | Dijkstra/binary search; minimize max edge on path |
| Shortest Path in Binary Matrix | 1091 | Medium | BFS 8-directional |

## Common Mistakes

- **Using Dijkstra with negative weights** — it gives wrong answers. Use Bellman-Ford.
- **Not skipping stale heap entries in Dijkstra** — without the `if d > dist[u]: continue` check, you process the same node at worse distances, wasting time
- **Bellman-Ford with K stops: not copying the distance array** — without the copy, updates cascade within the same round, violating the stop limit
- **Floyd-Warshall: wrong loop order** — `k` must be outermost. Getting this wrong gives incorrect results silently.
- **Using visited set in Dijkstra instead of lazy deletion** — a visited set works but the `d > dist[u]` check is simpler and handles edge cases better with Python's heapq

## Interview Questions

- "Find the shortest time for a signal to reach all nodes in a network." (LC 743 — Dijkstra)
- "Find the cheapest flight with at most K stops." (LC 787 — why can't you use plain Dijkstra here?)
- "Why doesn't Dijkstra work with negative edges? Give an example."
- "What's the difference between Dijkstra and Bellman-Ford? When would you use each?"
- "Transform word A to word B, one letter at a time, using a dictionary. Minimum steps?" (LC 127)
- "How would you find shortest paths between ALL pairs of nodes?" (Floyd-Warshall)
- "Can you solve shortest path in O(V+E) when weights are only 0 and 1?" (0-1 BFS)
- "What happens if there's a negative cycle? How do you detect it?"

## Quick Reference

```
Decision flowchart:
  Unweighted?           → BFS                    O(V + E)
  Non-negative weights? → Dijkstra               O((V+E) log V)
  Negative weights?     → Bellman-Ford            O(V·E)
  All pairs?            → Floyd-Warshall          O(V³)
  Weights 0 or 1?       → 0-1 BFS (deque)        O(V + E)
  With stop limit?      → Bellman-Ford (K rounds) O(K·E)

Dijkstra:  heap + lazy deletion          — greedy, no negative
Bellman:   relax all edges V-1 times     — brute force, handles negative
Floyd:     k-i-j triple loop             — DP, all pairs
0-1 BFS:   deque (front for 0, back for 1) — clever BFS variant
```
