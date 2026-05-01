# Topological Sort

> "Given dependencies, find a valid order" — that's topological sort. Shows up in course scheduling, build systems, and alien dictionaries.

## Core Idea

**Topological sort** produces a linear ordering of vertices in a **DAG** (Directed Acyclic Graph) such that for every edge u→v, u appears before v. If the graph has a cycle, no valid ordering exists. Two approaches: **Kahn's algorithm** (BFS with in-degrees) and **DFS post-order reverse**.

## What You Need to Know

### Kahn's Algorithm (BFS-Based) — Preferred in Interviews

Why preferred: it naturally detects cycles (if you can't process all nodes, there's a cycle) and is easier to reason about.

```python
from collections import deque, defaultdict

def topological_sort_kahn(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    if len(order) != n:
        return []  # cycle detected — not all nodes processed
    return order
```

**Time: O(V + E)** | **Space: O(V + E)**

### DFS-Based Topological Sort

Add node to result in **post-order** (after all descendants are processed), then reverse.

```python
def topological_sort_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    order = []
    has_cycle = False
    
    def dfs(node):
        nonlocal has_cycle
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY:  # cycle
                has_cycle = True
                return
            if color[nei] == WHITE:
                dfs(nei)
        color[node] = BLACK
        order.append(node)  # post-order
    
    for i in range(n):
        if color[i] == WHITE:
            dfs(i)
    
    if has_cycle:
        return []
    return order[::-1]  # reverse post-order = topological order
```

### Kahn's vs DFS Comparison

| | Kahn's (BFS) | DFS Post-Order |
|---|---|---|
| Cycle detection | Built-in (count processed nodes) | Requires 3-color tracking |
| Implementation | Iterative (no stack overflow) | Recursive (or explicit stack) |
| Returns order | Naturally in order | Must reverse at end |
| Unique ordering | Use min-heap for lexicographic | Harder to control |
| Interview preference | ✅ More common | Good to know |

## Key Patterns & Templates

### Course Schedule (LC 207)

"Can you finish all courses?" = "Is the dependency graph a DAG?"

```python
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed = 0
    
    while queue:
        node = queue.popleft()
        processed += 1
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    return processed == numCourses
```

### Course Schedule II (LC 210)

Same as above but return the actual order.

```python
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    return order if len(order) == numCourses else []
```

### Alien Dictionary (LC 269)

The hard part isn't toposort — it's **building the graph from word comparisons**.

```python
def alienOrder(words):
    # Step 1: Initialize all characters
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    
    # Step 2: Build graph from adjacent word pairs
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # Edge case: "abc" before "ab" is invalid
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break  # only first difference matters
    
    # Step 3: Kahn's topological sort
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    order = []
    
    while queue:
        c = queue.popleft()
        order.append(c)
        for nei in graph[c]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    if len(order) != len(in_degree):
        return ""  # cycle
    return "".join(order)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Course Schedule | 207 | Medium | Can finish = is it a DAG? Kahn's algorithm |
| Course Schedule II | 210 | Medium | Return the actual ordering |
| Alien Dictionary | 269 | Hard | Build graph from word pair comparisons, then toposort |
| Parallel Courses | 1136 | Medium | Toposort level by level; answer = number of levels |
| Minimum Height Trees | 310 | Medium | Peel leaves layer by layer (reverse toposort idea) |
| Sequence Reconstruction | 444 | Medium | Check if toposort order is unique (queue never has >1 element) |

## Common Mistakes

- **Not checking if all nodes are processed** — if `len(order) != n`, there's a cycle. Forgetting this means returning an invalid "order" when a cycle exists.
- **Wrong edge direction** — `[course, prereq]` means prereq → course, not the other way around. Read the problem.
- **Alien Dictionary: not handling the prefix edge case** — if "abc" comes before "ab", the ordering is invalid. Many people miss this.
- **Forgetting to include nodes with no edges** — a node with no prerequisites still needs to be in the graph (in-degree 0).
- **DFS toposort: forgetting to reverse** — DFS post-order gives *reverse* topological order.

## Interview Questions

- "There are N courses with prerequisites. Can you finish all of them? In what order?" (LC 207/210)
- "Given a sorted alien dictionary, determine the character ordering." (LC 269 — Google favorite)
- "How do you detect if a topological ordering exists? What does a cycle mean?"
- "Can a graph have multiple valid topological orderings? When is it unique?"
- "What's the time complexity of topological sort? Why O(V + E)?"
- "How would you find the minimum number of semesters to take all courses?" (LC 1136 — BFS levels = semesters)
- "What's the difference between Kahn's and DFS-based topological sort?"
- "Could you compute topological sort in lexicographic order?" (Replace queue with min-heap)

## Quick Reference

```
Topological Sort = linear ordering where u comes before v for every edge u→v
Only works on DAGs (Directed Acyclic Graphs)

Kahn's (BFS):
  1. Compute in-degree for all nodes
  2. Enqueue all nodes with in-degree 0
  3. Process queue: for each neighbor, decrement in-degree
  4. If in-degree becomes 0, enqueue it
  5. If processed ≠ total nodes → cycle

DFS:
  1. Run DFS, append to result in post-order
  2. Reverse the result
  3. Cycle detection via gray/black coloring

Applications:
  Course scheduling    → LC 207, 210
  Build order          → dependency resolution
  Alien dictionary     → LC 269
  Parallel execution   → LC 1136 (toposort by levels)

Time: O(V + E)  |  Space: O(V + E)
```
