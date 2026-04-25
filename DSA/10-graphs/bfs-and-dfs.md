# BFS and DFS

> BFS finds shortest paths in unweighted graphs. DFS explores everything reachable. Picking the wrong one costs you the interview.

## Core Idea

**BFS** (Breadth-First Search) explores level by level using a queue — it naturally finds shortest paths in unweighted graphs. **DFS** (Depth-First Search) goes as deep as possible before backtracking using a stack (or recursion) — it's simpler to code and great for exhaustive exploration, connected components, and cycle detection.

## What You Need to Know

### BFS vs DFS Decision Guide

| Use Case | BFS | DFS |
|----------|-----|-----|
| Shortest path (unweighted) | ✅ Guaranteed | ❌ Not guaranteed |
| Connected components | ✅ | ✅ |
| Level-order traversal | ✅ Natural | ❌ Awkward |
| Cycle detection (directed) | Via toposort | ✅ 3-color method |
| Topological sort | ✅ Kahn's | ✅ Post-order reverse |
| Path existence | ✅ | ✅ |
| Space on wide graphs | ❌ O(width) | ✅ O(depth) |
| Space on deep graphs | ✅ O(width) | ❌ O(depth), stack overflow risk |

### BFS Template

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)       # mark BEFORE enqueuing
                queue.append(nei)
```

**Critical:** Mark visited **before** enqueuing, not when dequeuing. Otherwise you'll enqueue the same node multiple times → TLE.

### BFS Shortest Path (Unweighted)

```python
def shortest_path(graph, start, end):
    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    return -1  # unreachable
```

### Multi-Source BFS

When the problem has multiple starting points (rotting oranges, 01 matrix), enqueue ALL sources at once. This avoids running BFS from each source separately.

```python
def multi_source_bfs(grid, rows, cols):
    queue = deque()
    visited = set()
    
    # Enqueue all sources at once
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == SOURCE:
                queue.append((r, c, 0))
                visited.add((r, c))
    
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
```

### DFS Template (Recursive)

```python
def dfs(graph, node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)
```

### DFS Template (Iterative)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                stack.append(nei)
```

**Note:** Iterative DFS processes nodes in different order than recursive DFS (reversed neighbor order). Doesn't matter for most problems, but be aware.

### Grid BFS/DFS

```python
# BFS on grid — e.g., Number of Islands
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                # BFS to sink the entire island
                queue = deque([(r, c)])
                grid[r][c] = '0'
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'  # mark before enqueuing
                            queue.append((nr, nc))
    return count
```

### BFS with State

Some problems require tracking extra state beyond just the node. Use a tuple `(node, state)` as your BFS key.

```python
# Example: shortest path with obstacles elimination (LC 1293)
# State = (row, col, remaining_removals)
def shortest_path_with_state(grid, k):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, k, 0)])  # r, c, removals_left, steps
    visited = {(0, 0, k)}
    
    while queue:
        r, c, rem, steps = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return steps
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_rem = rem - grid[nr][nc]
                if new_rem >= 0 and (nr, nc, new_rem) not in visited:
                    visited.add((nr, nc, new_rem))
                    queue.append((nr, nc, new_rem, steps + 1))
    return -1
```

## Key Patterns & Templates

### Pattern: Count Connected Components

Launch DFS/BFS from each unvisited node. Number of launches = number of components.

```python
def count_components(n, graph):
    visited = set()
    count = 0
    for node in range(n):
        if node not in visited:
            count += 1
            dfs(graph, node, visited)  # or BFS
    return count
```

### Pattern: Reverse-Direction Thinking

Instead of asking "can this cell reach the target?", ask "can the target reach this cell?" DFS/BFS from the destination inward.

```python
# Pacific Atlantic Water Flow (LC 417)
# DFS from ocean borders inward, find intersection
def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    
    def dfs(r, c, reachable, prev_height):
        if (r, c) in reachable or r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if heights[r][c] < prev_height:
            return
        reachable.add((r, c))
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(r + dr, c + dc, reachable, heights[r][c])
    
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows-1][c])
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols-1])
    
    return list(pacific & atlantic)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Number of Islands | 200 | Medium | DFS/BFS launches = island count |
| Rotting Oranges | 994 | Medium | Multi-source BFS; time = max distance |
| 01 Matrix | 542 | Medium | Multi-source BFS from all 0s simultaneously |
| Pacific Atlantic Water Flow | 417 | Medium | Reverse: BFS/DFS from oceans inward |
| Word Ladder | 127 | Hard | BFS + wildcard pattern for neighbors |
| Clone Graph | 133 | Medium | DFS + hash map prevents cycles |
| Surrounded Regions | 130 | Medium | DFS from border O's, flip the rest |
| Shortest Path in Binary Matrix | 1091 | Medium | BFS with 8-directional movement |

## Common Mistakes

- **Marking visited on dequeue instead of enqueue (BFS)** — same node gets enqueued multiple times, causes TLE. Always mark *before* adding to queue.
- **Grid DFS without marking before recursing** — infinite loop between adjacent cells
- **Using DFS for shortest path in unweighted graph** — DFS doesn't guarantee shortest. Use BFS.
- **Forgetting to handle disconnected graphs** — iterate over all nodes, not just start
- **Stack overflow on large grids with recursive DFS** — use iterative DFS or BFS for grids with 10⁴+ cells

## Interview Questions

- "Find the shortest path between two nodes in an unweighted graph. What's the time complexity?" (BFS, O(V+E))
- "How many islands are in this grid?" (LC 200 — Amazon's most-asked graph question)
- "What's the minimum time for all oranges to rot?" (LC 994 — Multi-source BFS)
- "Transform word A to word B changing one letter at a time. Minimum steps?" (LC 127 — Google/Microsoft)
- "When would you use BFS over DFS? Give a concrete example."
- "Can you convert this recursive DFS to iterative? Why would you want to?"
- "How would you find shortest path if each move has a constraint (e.g., limited fuel)?" (BFS with state)
- "How does marking visited before vs after enqueueing affect correctness?"

## Quick Reference

```
BFS                              DFS
─────────────────────────        ─────────────────────────
Data structure: Queue            Data structure: Stack/Recursion
Explores: Level by level         Explores: Deep then backtrack
Shortest path: ✅ (unweighted)   Shortest path: ❌
Space: O(max level width)        Space: O(max depth)
Time: O(V + E)                   Time: O(V + E)

When to use what:
  "Shortest/minimum" → BFS
  "All paths / exhaustive" → DFS
  "Level by level" → BFS
  "Connected components" → Either
  "Cycle in directed graph" → DFS (3-color)
  "Grid flood fill" → Either (BFS avoids stack overflow)
```
