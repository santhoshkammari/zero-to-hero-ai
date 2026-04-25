# DP on Trees

> Trees + DP = DFS that returns smart summaries from children, letting each node make optimal local decisions.

## Core Idea

Every tree DP boils down to one trick: **post-order DFS** where each node computes its answer from its children's answers. The "DP" part is that each node returns a compact state (often a tuple) so its parent can decide without re-exploring the subtree. Think of it like a company org chart — each manager collects reports from direct reports and summarizes upward.

## What You Need to Know

### Why Trees Make DP Natural

A tree has no cycles, so each subtree is an independent subproblem — exactly what DP needs. The recursion *is* the traversal. No memoization table required because each node is visited exactly once.

### The Two Return Patterns

| Pattern | What DFS Returns | Global Variable? | When to Use |
|---------|-----------------|-------------------|-------------|
| **Include/Exclude** | `(take_this, skip_this)` tuple | No | Node selection problems (rob, color, independent set) |
| **Path Sum / Diameter** | Best single-arm value | Yes — tracks cross-node answer | Path problems where optimal path passes *through* a node |

**Include/Exclude pattern**: Each node has two choices — participate or don't. Children's choices constrain the parent. DFS returns both options so the parent can pick.

**Path sum pattern**: The optimal *path* might pass through any node as a "turning point." You can't return a path that branches — only a single arm goes up to the parent. So you track the best branching answer in a global variable, but *return* the best single-direction extension.

### Catalan Numbers for BST Counting

**Unique BSTs (LC 96)** uses a different flavor — no actual tree traversal. The number of structurally unique BSTs with `n` nodes follows the **Catalan number** recurrence:

```
dp[n] = Σ dp[i-1] * dp[n-i]  for i = 1..n
```

Why? Pick root `i`. Left subtree has `i-1` nodes, right has `n-i`. These are independent, so multiply. Sum over all root choices.

```python
def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1  # empty tree and single node = 1 way each
    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    return dp[n]
# Time: O(n²) | Space: O(n)
```

### Re-rooting Technique

For problems like "find the node that minimizes some tree metric," brute-force roots every node in O(n²). **Re-rooting** computes the answer for one root, then shifts the root to each neighbor in O(1) by adjusting the contribution of the old and new subtrees. Total: O(n).

The idea: when you move the root from node `u` to its child `v`, `v`'s subtree shrinks (loses `v`'s branch) and the "rest of tree" grows. You update both parts algebraically instead of recomputing.

## Key Patterns & Templates

### Template 1: Include/Exclude (House Robber III Style)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: TreeNode) -> int:
    """LC 337 — Each node: rob it or skip it."""
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, skip_this)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # Rob this node → must skip both children
        rob_this = node.val + left[1] + right[1]
        # Skip this node → take best option from each child
        skip_this = max(left) + max(right)
        
        return (rob_this, skip_this)
    
    return max(dfs(root))
# Time: O(n) | Space: O(h) where h = tree height
```

Why the tuple? The parent *needs* to know both options for its child — if parent robs, child must be skipped. Without the tuple, you'd recompute subtrees.

### Template 2: Path Sum with Global Tracker

```python
def maxPathSum(root: TreeNode) -> int:
    """LC 124 — Max path sum, path can start/end anywhere."""
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Only take a child's contribution if it's positive
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        
        # Path *through* this node (uses both arms — can't extend further up)
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        
        # Return best single arm to parent (parent can only extend one direction)
        return node.val + max(left_gain, right_gain)
    
    dfs(root)
    return max_sum
# Time: O(n) | Space: O(h)
```

Why `max(..., 0)`? Negative contributions make the path worse — better to start fresh. This is the same logic as Kadane's algorithm but on a tree.

### Template 3: Diameter / Height Tracking

```python
def diameterOfBinaryTree(root: TreeNode) -> int:
    """LC 543 — Longest path (in edges) between any two nodes."""
    diameter = 0
    
    def height(node):
        nonlocal diameter
        if not node:
            return 0
        
        left_h = height(node.left)
        right_h = height(node.right)
        
        # Path through this node = left height + right height
        diameter = max(diameter, left_h + right_h)
        
        # Return height of this subtree
        return 1 + max(left_h, right_h)
    
    height(root)
    return diameter
# Time: O(n) | Space: O(h)
```

Same pattern as LC 124 — global tracks the "through" answer, return sends the "single arm" answer up.

### Template 4: General Tree DP (Adjacency List)

```python
def tree_dp(adj: list[list[int]], root: int = 0) -> int:
    """General tree DP on adjacency list. Handles arbitrary (non-binary) trees."""
    n = len(adj)
    dp = [[0, 0] for _ in range(n)]  # [include, exclude] per node
    
    def dfs(node, parent):
        include_val = 1  # or node's weight
        exclude_val = 0
        
        for child in adj[node]:
            if child == parent:  # skip edge back to parent
                continue
            dfs(child, node)
            include_val += dp[child][1]        # include node → exclude children
            exclude_val += max(dp[child])      # exclude node → best of each child
        
        dp[node][0] = include_val
        dp[node][1] = exclude_val
    
    dfs(root, -1)
    return max(dp[root])
# Time: O(n) | Space: O(n)
```

### Template 5: Longest Zigzag Path

```python
def longestZigZag(root: TreeNode) -> int:
    """LC 1372 — Longest path alternating left-right."""
    max_len = 0
    
    def dfs(node):
        """Returns (longest ending going left, longest ending going right)."""
        nonlocal max_len
        if not node:
            return (-1, -1)  # -1 so leaf becomes 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If we go left from this node, then from left child we must go right
        go_left = 1 + left[1]
        # If we go right from this node, then from right child we must go left
        go_right = 1 + right[0]
        
        max_len = max(max_len, go_left, go_right)
        return (go_left, go_right)
    
    dfs(root)
    return max_len
# Time: O(n) | Space: O(h)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| House Robber III | 337 | Medium | Include/exclude tuple — rob node means skip children |
| Binary Tree Maximum Path Sum | 124 | Hard | Global tracks "through" path, return single arm up. `max(gain, 0)` to drop negatives |
| Diameter of Binary Tree | 543 | Easy | Diameter at node = left_height + right_height. Same global/return split as LC 124 |
| Unique Binary Search Trees | 96 | Medium | Not tree traversal — Catalan numbers. `dp[n] = Σ dp[i-1] * dp[n-i]` |
| Longest ZigZag Path in a Binary Tree | 1372 | Medium | Return (left_zigzag, right_zigzag) tuple, alternate directions |
| Binary Tree Cameras | 968 | Hard | Three states per node: has camera, covered, not covered. Greedy from leaves up |
| Sum of Distances in Tree | 834 | Hard | Classic re-rooting. Compute answer for root 0, then shift root in O(1) per edge |
| Maximum Product of Splitted Binary Tree | 1339 | Medium | Compute total sum, then for each subtree sum `s`, product is `s * (total - s)` |

## Common Mistakes

- **Forgetting `max(gain, 0)` in path problems**: If a subtree has negative sum, don't include it. This is the #1 bug in LC 124. You can always "start fresh" from the current node.
- **Returning the global answer instead of the local one**: `dfs` must return the single-arm value for the parent. The "best through this node" answer goes into the global variable, *not* up the call stack.
- **Not handling `None` base case carefully**: Returning 0 vs -1 matters. For edge-counted problems (diameter), `None → 0` works because `1 + max(left, right)` gives correct height. For zigzag, `None → -1` so the `1 + ...` gives 0 at leaves.
- **Recomputing subtrees instead of passing state**: If you call `dfs(node.left)` twice, you've doubled your work. Capture the result once.
- **Confusing node count vs edge count**: Diameter is in *edges*. A single node has diameter 0. Height functions count edges (0 at leaf) or nodes (1 at leaf) — pick one and be consistent.

## Interview Questions

1. **Conceptual**: Why does tree DP not need a memo table, unlike grid/string DP?
   *Each node is visited once in post-order. The tree structure guarantees no overlapping subproblems across subtrees.*

2. **LC 337**: How would you solve House Robber III without the tuple trick? What's the time complexity?
   *Naive: recurse with/without robbing, leads to O(2ⁿ). With memo on node → O(n). The tuple approach avoids the hash map entirely.*

3. **LC 124**: Why can't you return the "through" path sum to the parent?
   *A path can't fork. If a path goes left-child → node → right-child, extending to node's parent would create a branch, not a path.*

4. **LC 543**: The diameter might not pass through the root. How does your solution handle this?
   *The global variable captures the best diameter seen at any node. We don't assume root is on the optimal path.*

5. **LC 96**: Prove that Unique BSTs follows the Catalan number formula.
   *Choose root i. Left subtree: i-1 nodes, right: n-i nodes. Independent structures multiply. Sum over all root choices = Catalan recurrence.*

6. **LC 834**: Explain the re-rooting technique for Sum of Distances in Tree.
   *Root at 0, compute subtree sizes and distance sum. When shifting root from u to child v: nodes in v's subtree get 1 closer, all others get 1 farther. `ans[v] = ans[u] - count[v] + (n - count[v])`.*

7. **Design**: How would you find the maximum independent set on a general tree?
   *Include/exclude DP. Include node → exclude all children. Exclude node → take max(include, exclude) for each child. O(n).*

8. **Follow-up**: Can tree DP be done iteratively?
   *Yes — use topological order (process leaves first via BFS). But recursive DFS is cleaner and expected in interviews.*

## Quick Reference

```
┌─────────────────────────────────────────────────────────┐
│              TREE DP DECISION FLOWCHART                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  "Select/skip nodes?"                                   │
│     YES → Include/Exclude tuple pattern                 │
│           return (take, skip)                           │
│           e.g., LC 337, LC 968                          │
│                                                         │
│  "Best path through the tree?"                          │
│     YES → Path pattern: global + single-arm return      │
│           max_sum = max(max_sum, left + node + right)   │
│           return node + max(left, right)                │
│           e.g., LC 124, LC 543, LC 1372                 │
│                                                         │
│  "Count structures?"                                    │
│     YES → Catalan / counting DP (no tree traversal)     │
│           dp[n] = Σ dp[left] * dp[right]                │
│           e.g., LC 96                                   │
│                                                         │
│  "Optimal answer for every root?"                       │
│     YES → Re-rooting technique                          │
│           Compute for one root, shift in O(1)           │
│           e.g., LC 834                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘

COMPLEXITY SUMMARY
┌──────────────────────┬──────────┬──────────────────────┐
│ Pattern              │ Time     │ Space                │
├──────────────────────┼──────────┼──────────────────────┤
│ Include/Exclude      │ O(n)     │ O(h) recursive stack │
│ Path Sum / Diameter  │ O(n)     │ O(h) recursive stack │
│ Catalan counting     │ O(n²)    │ O(n)                 │
│ Re-rooting           │ O(n)     │ O(n)                 │
│ General tree DP      │ O(n)     │ O(n)                 │
└──────────────────────┴──────────┴──────────────────────┘
h = tree height: O(log n) balanced, O(n) worst case (skewed)
```
