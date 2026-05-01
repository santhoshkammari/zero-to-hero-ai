# Tree Traversals

> Every tree problem is secretly a traversal problem — knowing all traversal orders (and when to use each) is non-negotiable.

## Core Idea

There are four ways to visit every node in a binary tree: **inorder** (left-root-right), **preorder** (root-left-right), **postorder** (left-right-root), and **level-order** (BFS). Each has a specific use case. You must know recursive, iterative (stack-based), and for bonus points, **Morris traversal** (O(1) space). Level-order uses a queue and is the basis for 10+ BFS tree problems.

## What You Need to Know

### Traversal Orders at a Glance

| Order | Visit Sequence | Use Case | Key Property |
|-------|---------------|----------|--------------|
| **Inorder** | Left → Root → Right | BST gives sorted order | Sorted output for BST |
| **Preorder** | Root → Left → Right | Serialize tree, copy tree | Root comes first |
| **Postorder** | Left → Right → Root | Delete tree, evaluate expression | Process children before parent |
| **Level-order** | Level by level (BFS) | Level grouping, shortest path in tree | Uses queue, not stack |

### Recursive Traversals — O(n) time, O(h) space

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Iterative Inorder — O(n) time, O(h) space

The most important iterative traversal. Push all left children, pop and process, then go right.

```python
def inorder_iterative(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:            # go as far left as possible
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()     # process node
        result.append(curr.val)
        curr = curr.right      # move to right subtree
    return result
```

### Iterative Preorder — O(n) time, O(h) space

```python
def preorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:         # push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

### Iterative Postorder — O(n) time, O(h) space

Trick: modified preorder (root → right → left) then reverse the result.

```python
def postorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:          # push left first (opposite of preorder trick)
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]        # reverse gives postorder
```

### Level-Order Traversal (BFS) — O(n) time, O(w) space

**w** = max width of tree (up to n/2 for a complete tree).

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)  # snapshot size BEFORE processing
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

**The critical line**: `level_size = len(queue)` captures how many nodes are at the current level before we start adding the next level's children. This is what lets you group nodes by level.

### Level-Order Variants

All built on the same BFS template with minor tweaks:

```python
# Zigzag Level Order (LC 103)
# Even levels left-to-right, odd levels right-to-left
def zigzag_level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    left_to_right = True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result

# Right Side View (LC 199)
# Last node at each level
def right_side_view(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == len(queue):  # wrong! queue size changed
                pass
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(node.val)  # last node processed = rightmost
    return result
```

### Morris Traversal (Inorder) — O(n) time, O(1) space

Uses **threaded tree** concept: temporarily link rightmost node of left subtree back to current node. No stack, no recursion.

```python
def morris_inorder(root):
    result = []
    curr = root
    while curr:
        if not curr.left:
            result.append(curr.val)  # no left subtree, visit and go right
            curr = curr.right
        else:
            # Find inorder predecessor (rightmost in left subtree)
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            
            if not pred.right:
                pred.right = curr      # create thread
                curr = curr.left
            else:
                pred.right = None      # remove thread (already visited left)
                result.append(curr.val)
                curr = curr.right
    return result
```

**When to mention Morris**: If interviewer asks "can you do inorder traversal in O(1) space?" This is the answer. It modifies the tree temporarily but restores it.

### Serialization & Deserialization (LC 297)

**Serialize**: Preorder with null markers. **Deserialize**: Read sequentially, recurse.

```python
class Codec:
    def serialize(self, root):
        result = []
        def dfs(node):
            if not node:
                result.append("#")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)
    
    def deserialize(self, data):
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
```

**Why preorder + null markers?** Preorder gives you the root first, and null markers tell you exactly where subtrees end. This combination uniquely identifies any binary tree. Without null markers, you'd need *two* traversal orders (e.g., preorder + inorder) to reconstruct.

## Key Patterns & Templates

### Traversal Selector

```python
# When to use which traversal:
# Need sorted order from BST?        → Inorder
# Need to process parent before kids? → Preorder
# Need to process kids before parent? → Postorder  
# Need level-by-level processing?     → Level-order (BFS)
# Need O(1) space traversal?          → Morris
```

### The "Build Tree from Traversals" Pattern

```python
# Construct tree from preorder + inorder (LC 105)
def build_tree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])  # optimize with hashmap
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root
```

**Optimize**: Use a hashmap `{val: idx}` for inorder to avoid O(n) `index()` calls, bringing total from O(n²) to O(n).

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Binary Tree Inorder Traversal | 94 | Easy | Know both recursive and iterative (stack + go-left pattern) |
| Binary Tree Level Order Traversal | 102 | Medium | `for _ in range(len(queue))` to group by level |
| Binary Tree Zigzag Level Order | 103 | Medium | Flip insertion direction each level with deque |
| Binary Tree Right Side View | 199 | Medium | BFS — last node at each level is the rightmost |
| Serialize and Deserialize Binary Tree | 297 | Hard | Preorder + null markers; use iterator for deserialize |
| Construct Binary Tree from Preorder and Inorder | 105 | Medium | Preorder[0] = root, split inorder at root position |
| Flatten Binary Tree to Linked List | 114 | Medium | Reverse postorder: process right, left, then node |
| Binary Tree Vertical Order Traversal | 314 | Medium | BFS with column tracking, sort by column |

## Common Mistakes

- **Level-order: not snapshotting queue size**. `for _ in range(len(queue))` captures the size once. If you re-evaluate `len(queue)` inside the loop, you'll mix levels because children get added.
- **Iterative preorder: pushing left before right**. Stack is LIFO — push right first so left gets popped first.
- **Serialization: using inorder**. Inorder alone can't reconstruct a tree (even with null markers, the root position is ambiguous). Use preorder or level-order.
- **Build tree from traversals: O(n²) from `index()` calls**. Always mention the hashmap optimization in interviews.
- **Morris traversal: forgetting to restore threads**. If you don't remove the temporary links, you've corrupted the tree structure.

## Interview Questions

- "Implement inorder traversal iteratively. Explain the state your stack maintains." (Microsoft)
- "Traverse a binary tree level by level. How do you know when one level ends and the next begins?"
- "Serialize and deserialize a binary tree. Why do you need null markers?" (Google/Amazon)
- "Given preorder and inorder traversals, reconstruct the binary tree. What's the time complexity?" (Meta)
- "Can you do inorder traversal in O(1) space? How?" (Google — Morris traversal)
- "What's the difference between DFS and BFS on a tree? When would you prefer BFS?"
- "Implement right-side view of a binary tree. Can you do it with DFS instead of BFS?"
- "What traversal order gives sorted output for a BST? Why?"

## Quick Reference

```
Traversal Cheat Sheet:
─────────────────────
             Recursive    Iterative    Morris
Time:          O(n)         O(n)        O(n)
Space:         O(h)         O(h)        O(1)

Level-order: O(n) time, O(w) space (w = max width)

Traversal → Use Case Mapping:
  Inorder   → BST sorted order, kth smallest
  Preorder  → Serialize, copy, top-down problems
  Postorder → Delete, evaluate, bottom-up problems
  BFS       → Level grouping, shortest depth, right-side view

Reconstruct Tree:
  Preorder + Inorder  → Unique tree ✓
  Postorder + Inorder → Unique tree ✓
  Preorder + Postorder → NOT unique (ambiguous for single-child nodes)
  Single traversal + null markers → Unique tree ✓
```
