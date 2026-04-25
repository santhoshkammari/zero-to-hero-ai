# Binary Tree Basics

> Trees are ~20% of all coding interviews — if you can't think recursively about trees, you'll hit a wall at every top company.

## Core Idea

A **binary tree** is a recursive structure: each node has a value and at most two children. Almost every tree problem reduces to: **do something at the current node, then trust recursion for the subtrees**. The two DFS thinking modes — **top-down** (pass info from parent to child) and **bottom-up** (return info from child to parent) — cover 90% of tree problems.

## What You Need to Know

### Node Structure

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Tree Terminology

| Term | Definition | Why It Matters |
|------|-----------|----------------|
| **Depth** | Distance from root to node (root = 0) | Top-down problems pass depth down |
| **Height** | Distance from node to deepest leaf (leaf = 0) | Bottom-up problems return height up |
| **Full** | Every node has 0 or 2 children | |
| **Complete** | All levels filled except possibly last (filled left-to-right) | Heaps use this property |
| **Perfect** | All internal nodes have 2 children, all leaves at same level | Has `2^h+1 - 1` nodes |
| **Balanced** | Left and right subtree heights differ by ≤ 1 | Ensures O(log n) operations |

### Top-Down DFS (Pass Info Downward)

You carry information **from root toward leaves**. Think of it as "I'll tell my children what they need to know."

```python
# Maximum depth — top-down version
def max_depth_topdown(root):
    result = 0
    def dfs(node, depth):
        nonlocal result
        if not node:
            return
        result = max(result, depth)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    dfs(root, 1)
    return result
```

**Use when**: You need to pass constraints, paths, or accumulated values downward (e.g., path sum, validate BST with min/max bounds).

### Bottom-Up DFS (Return Info Upward)

You collect information **from leaves toward root**. Think of it as "I'll ask my children and combine their answers."

```python
# Maximum depth — bottom-up version (cleaner, preferred)
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Use when**: The answer at a node depends on its subtrees (e.g., height, diameter, balanced check).

### Diameter of Binary Tree (LC 543) — O(n)

The **diameter** is the longest path between any two nodes (count edges). It doesn't necessarily pass through the root. At each node, the path through it = `left_height + right_height`.

```python
def diameter_of_binary_tree(root):
    result = 0
    def height(node):
        nonlocal result
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        result = max(result, left + right)  # update diameter
        return 1 + max(left, right)         # return height to parent
    height(root)
    return result
```

**The trick**: What you *track globally* (diameter) is different from what you *return* (single-side height).

### Check If Balanced (LC 110) — O(n)

A tree is balanced if for **every** node, left and right heights differ by at most 1.

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1  # -1 signals "not balanced"
        return 1 + max(left, right)
    return check(root) != -1
```

**Why return -1?** Early termination — once any subtree is unbalanced, propagate failure upward instead of continuing pointless computation.

### Lowest Common Ancestor (LC 236) — O(n)

The LCA of two nodes `p` and `q` is the deepest node that has both as descendants.

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root    # p and q are in different subtrees → this is the LCA
    return left or right  # both are in the same subtree
```

**Aha**: You're asking each subtree "do you contain p or q?" If both sides say yes, you're the LCA. If only one says yes, pass it up.

### Invert Binary Tree (LC 226) — O(n)

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

### Maximum Path Sum (LC 124) — O(n)

The hardest standard tree problem. A path goes from any node to any node (not necessarily through root). At each node, decide whether to include left/right branches.

```python
def max_path_sum(root):
    result = float('-inf')
    def dfs(node):
        nonlocal result
        if not node:
            return 0
        left = max(dfs(node.left), 0)   # ignore negative paths
        right = max(dfs(node.right), 0)
        result = max(result, node.val + left + right)  # full path through node
        return node.val + max(left, right)  # single branch to parent
    dfs(root)
    return result
```

**Critical distinction**: You **return** single-branch max (because a path can't fork when continuing upward), but you **track** the two-branch path through the current node as a potential global answer.

## Key Patterns & Templates

### The Two-Value Return Pattern

Many hard tree problems require tracking a **global answer** while **returning a different value** to the parent:

```python
def solve(root):
    global_answer = initial_value
    def dfs(node):
        nonlocal global_answer
        if not node:
            return base_case
        left_val = dfs(node.left)
        right_val = dfs(node.right)
        global_answer = update(global_answer, left_val, right_val, node)
        return value_for_parent(left_val, right_val, node)
    dfs(root)
    return global_answer
```

Used in: diameter, max path sum, longest univalue path, and more.

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Maximum Depth of Binary Tree | 104 | Easy | `1 + max(left, right)` — the base bottom-up pattern |
| Invert Binary Tree | 226 | Easy | Swap children, recurse — trust the recursion |
| Diameter of Binary Tree | 543 | Easy | Track global diameter, return height — they're different values |
| Balanced Binary Tree | 110 | Easy | Return -1 to signal failure early |
| Lowest Common Ancestor | 236 | Medium | Both sides non-null → you're the LCA |
| Binary Tree Maximum Path Sum | 124 | Hard | Return single branch, track full path globally |
| Same Tree | 100 | Easy | Both null → True, one null → False, both match → recurse |
| Subtree of Another Tree | 572 | Easy | Check `is_same_tree` at every node |

## Common Mistakes

- **LCA: not handling when one node is the ancestor of the other**. The base case `root == p or root == q` handles this — if you find one, return it immediately because the other must be below.
- **Max path sum: returning the two-branch path to the parent**. A path can't go left-node-right *and then* continue upward. Return only the single best branch.
- **Confusing depth and height**. Depth is top-down (root = 0), height is bottom-up (leaf = 0). Interviewers will test if you know the difference.
- **Forgetting the null base case**. Every recursive tree function needs `if not node: return ...` as the first line.
- **Modifying the tree unintentionally**. In problems like "flatten to linked list," be careful about losing references to children before you've processed them.

## Interview Questions

- "Find the lowest common ancestor of two nodes in a binary tree. What changes if parent pointers are available?" (Amazon #1 tree question)
- "What's the diameter of a binary tree? Does the longest path always go through the root?"
- "Find the maximum path sum in a binary tree where the path can start and end at any node." (Google on-site)
- "How do you check if a binary tree is balanced? What's your time complexity?"
- "What's the difference between depth and height of a node?"
- "Explain top-down vs bottom-up DFS. When would you use each?"
- "Invert a binary tree. Can you do it iteratively?" (The famous Homebrew interview question)
- "Given a binary tree, find the longest path where each node has the same value."

## Quick Reference

```
Tree DFS Mental Model:
─────────────────────
Top-down:  "What do I tell my children?"   → Pass info via parameters
Bottom-up: "What do my children tell me?"   → Combine return values

Pattern Selector:
  Need subtree info (height, size)          → Bottom-up
  Need path from root (sum, constraints)    → Top-down
  Need global answer ≠ return value         → Two-value pattern (global + return)

Complexities (all standard tree problems):
  Time:  O(n) — visit each node once
  Space: O(h) — recursion stack depth
         O(n) worst case (skewed tree)
         O(log n) best case (balanced tree)

Key Formulas:
  Perfect tree nodes:    2^(h+1) - 1
  Complete tree height:  floor(log₂ n)
  Max nodes at depth d:  2^d
```
