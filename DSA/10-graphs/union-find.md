# Union-Find (Disjoint Set Union)

> When you need to group things and ask "are these two in the same group?" — Union-Find does it in nearly O(1) per operation.

## Core Idea

**Union-Find** maintains a collection of disjoint sets. It supports two operations: **find** (which set does this element belong to?) and **union** (merge two sets). With **path compression** and **union by rank**, both operations run in **O(α(n)) ≈ O(1)** amortized time, where α is the inverse Ackermann function — effectively constant.

## What You Need to Know

### Why Not Just DFS?

Union-Find shines in **online/dynamic** scenarios — when edges arrive one at a time and you need to answer connectivity queries between additions. DFS would require re-traversal each time. Union-Find handles it incrementally.

| | DFS/BFS | Union-Find |
|---|---|---|
| Static graph queries | ✅ O(V+E) once | ✅ O(V+E) total |
| Dynamic edge additions | ❌ Re-run each time | ✅ O(α(n)) per edge |
| Cycle detection (undirected) | ✅ | ✅ |
| Need actual paths | ✅ | ❌ |

### The Template

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of connected components
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected
        # union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1
        return True  # successfully merged
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Why Path Compression Matters

Without it: `find` is O(n) in the worst case (long chains).
With it: every `find` call flattens the tree — nodes point directly to root.

```
Before find(4):  0 ← 1 ← 2 ← 3 ← 4

After find(4):   0 ← 1
                 0 ← 2
                 0 ← 3
                 0 ← 4
```

One line does it: `self.parent[x] = self.find(self.parent[x])`

### Why Union by Rank

Without it: trees can become tall (O(n)). By always attaching the shorter tree under the taller one, height stays O(log n). Combined with path compression, we get O(α(n)).

### Complexity

| Operation | Without Optimizations | With Path Compression + Union by Rank |
|-----------|----------------------|---------------------------------------|
| find | O(n) | O(α(n)) ≈ O(1) |
| union | O(n) | O(α(n)) ≈ O(1) |
| Space | O(n) | O(n) |

## Key Patterns & Templates

### Number of Connected Components (LC 323)

```python
def countComponents(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count
```

### Cycle Detection in Undirected Graph

If `find(u) == find(v)` before `union(u, v)`, adding edge (u,v) creates a cycle.

```python
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.connected(u, v):
            return True  # u and v already in same set → cycle
        uf.union(u, v)
    return False
```

### Redundant Connection (LC 684)

Find the edge that creates a cycle. Return the last one.

```python
def findRedundantConnection(edges):
    uf = UnionFind(len(edges) + 1)  # 1-indexed
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
```

### Accounts Merge (LC 721)

Group emails that belong to the same person. Emails in the same account are connected. Emails across accounts are connected if they share any email.

```python
from collections import defaultdict

def accountsMerge(accounts):
    uf = UnionFind(len(accounts))
    email_to_id = {}
    
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            email_to_id[email] = i
    
    # Group emails by root account
    groups = defaultdict(set)
    for email, idx in email_to_id.items():
        groups[uf.find(idx)].add(email)
    
    return [[accounts[root][0]] + sorted(emails) 
            for root, emails in groups.items()]
```

### Number of Islands II (LC 305) — Online

Islands appear one by one. After each addition, report the island count. Classic Union-Find because it's dynamic.

```python
def numIslands2(m, n, positions):
    uf = UnionFind(m * n)
    uf.count = 0  # start with 0 islands
    grid = set()
    result = []
    
    for r, c in positions:
        if (r, c) in grid:
            result.append(uf.count)
            continue
        grid.add((r, c))
        idx = r * n + c
        uf.parent[idx] = idx  # activate this cell
        uf.count += 1
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in grid:
                uf.union(idx, nr * n + nc)
        
        result.append(uf.count)
    return result
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Number of Connected Components | 323 | Medium | Direct Union-Find application; count = uf.count |
| Redundant Connection | 684 | Medium | Edge that fails union = cycle-creating edge |
| Accounts Merge | 721 | Medium | Union accounts sharing emails; group by root |
| Number of Islands II | 305 | Hard | Online connectivity; UF beats repeated BFS |
| Graph Valid Tree | 261 | Medium | Tree = connected + no cycles (edges == n-1, or UF detects cycle) |
| Longest Consecutive Sequence | 128 | Medium | Union consecutive numbers; track component sizes |

## Common Mistakes

- **Forgetting path compression** — without `self.parent[x] = self.find(self.parent[x])`, operations degrade to O(n)
- **Forgetting union by rank** — without it, trees can become skewed
- **Not returning False from union when already connected** — needed to detect cycles and count components correctly
- **Using union-find for problems needing actual paths** — UF only tells you connectivity, not the path between nodes
- **Grid problems: not mapping 2D coordinates to 1D index** — use `r * cols + c`

## Interview Questions

- "Given n nodes and edges, how many connected components are there?" (LC 323)
- "Find the extra edge that creates a cycle in a tree." (LC 684)
- "Merge accounts that share emails." (LC 721 — Amazon)
- "How does path compression work? What's the amortized complexity?"
- "When would you use Union-Find over DFS for connected components?"
- "Islands appear one at a time. After each, how many islands?" (LC 305 — online vs offline)
- "What's the inverse Ackermann function? Why does it matter?"
- "Is this graph a valid tree?" (LC 261 — connected + no cycle)

## Quick Reference

```
Union-Find Operations:
  find(x)      → root of x's set              O(α(n)) ≈ O(1)
  union(x, y)  → merge sets of x and y        O(α(n)) ≈ O(1)
  connected    → find(x) == find(y)            O(α(n)) ≈ O(1)

Two optimizations (ALWAYS use both):
  1. Path compression: parent[x] = find(parent[x])
  2. Union by rank: attach shorter tree under taller

When to use:
  ✅ Dynamic connectivity (edges added over time)
  ✅ Count/track connected components
  ✅ Detect cycles in undirected graph
  ✅ Group merging (accounts, equivalence classes)
  ❌ Need shortest paths
  ❌ Need actual path between nodes
  ❌ Directed graphs (use toposort/DFS instead)
```
