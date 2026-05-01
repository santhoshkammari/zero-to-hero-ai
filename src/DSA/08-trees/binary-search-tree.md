# Binary Search Tree (BST)

> BSTs turn O(n) lookups into O(log n) — but only if you truly understand the invariant. Interviewers love catching people who check only the immediate parent instead of the full range.

## Core Idea

A **Binary Search Tree** enforces one rule: for every node, **all** nodes in its left subtree are smaller, and **all** nodes in its right subtree are larger. Not just the immediate children — the *entire* subtree. This property makes search, insert, and delete O(h) where h is the tree height. For a balanced BST, h = O(log n). The single most important BST insight: **inorder traversal gives sorted order**.

## What You Need to Know

### BST Operations

| Operation | Average | Worst (Skewed) | Approach |
|-----------|---------|----------------|----------|
| Search | O(log n) | O(n) | Compare and go left/right |
| Insert | O(log n) | O(n) | Search for position, add leaf |
| Delete | O(log n) | O(n) | 3 cases: leaf, one child, two children |
| Find min/max | O(log n) | O(n) | Go all the way left/right |

### Search

```python
def search_bst(root, target):
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)
```

### Insert

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

### Delete — The Tricky One

Three cases:
1. **Leaf node**: Just remove it
2. **One child**: Replace node with its child
3. **Two children**: Replace with **inorder successor** (smallest in right subtree), then delete the successor

```python
def delete_bst(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # Case 1 & 2: no child or one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Case 3: two children — find inorder successor
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = delete_bst(root.right, successor.val)
    return root
```

### Validate BST (LC 98) — O(n)

The classic mistake: only comparing a node with its direct children. Node 5 might be in the left subtree of node 3, which violates the BST property even though 5 > its parent.

**Correct approach**: Pass valid range `(low, high)` down the tree.

```python
def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    return validate(root)
```

**Alternative**: Inorder traversal should produce strictly increasing values.

```python
def is_valid_bst_inorder(root):
    prev = float('-inf')
    def inorder(node):
        nonlocal prev
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= prev:
            return False
        prev = node.val
        return inorder(node.right)
    return inorder(root)
```

### Kth Smallest Element (LC 230) — O(h + k)

Inorder traversal of BST = sorted order. Visit k nodes and stop.

```python
def kth_smallest(root, k):
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
```

### BST Iterator (LC 173) — O(h) space, O(1) amortized next()

Controlled inorder traversal using an explicit stack. Only push left children initially.

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self):
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val
    
    def hasNext(self):
        return len(self.stack) > 0
```

**Why O(1) amortized**: Each node is pushed and popped exactly once across all `next()` calls. Total work across n calls = O(n), so each call averages O(1).

### Convert Sorted Array to BST (LC 108) — O(n)

Pick the middle element as root to ensure balance.

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    return root
```

### LCA in BST (LC 235) — O(h)

Use the BST property: if both values are smaller, go left. Both larger, go right. Otherwise, you're at the split point — that's the LCA.

```python
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root  # split point = LCA
```

**Why O(h) instead of O(n)?** You never visit both subtrees — you always go in one direction, like search.

## Key Patterns & Templates

### Inorder = Sorted Order (The Master Key)

Nearly every BST problem reduces to "inorder traversal with a twist":

```python
# Pattern: process BST in sorted order
def bst_sorted_operation(root):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        # PROCESS node.val HERE (it's in sorted order)
        inorder(node.right)
    inorder(root)
```

This pattern solves: kth smallest, validate BST, convert BST to sorted list, find mode in BST, recover BST (swapped nodes).

### Range-Based Validation Pattern

```python
def bst_with_range(node, lo, hi):
    if not node:
        return base_case
    if node.val outside (lo, hi):
        return failure
    left_result = bst_with_range(node.left, lo, node.val)
    right_result = bst_with_range(node.right, node.val, hi)
    return combine(left_result, right_result)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Validate Binary Search Tree | 98 | Medium | Pass `(low, high)` range, not just parent comparison |
| Kth Smallest Element in a BST | 230 | Medium | Iterative inorder, stop at k — O(h + k) |
| Lowest Common Ancestor of a BST | 235 | Medium | BST property → always go one direction, O(h) |
| Convert Sorted Array to Balanced BST | 108 | Easy | Pick middle as root recursively |
| BST Iterator | 173 | Medium | Controlled inorder with stack — O(h) space, O(1) amortized |
| Delete Node in a BST | 450 | Medium | Three cases: leaf, one child, two children (inorder successor) |
| Recover Binary Search Tree | 99 | Medium | Inorder finds exactly two swapped nodes — O(1) space with Morris |
| Trim a BST | 669 | Medium | If node < low, return trimmed right subtree; if > high, return trimmed left |

## Common Mistakes

- **Validate BST with parent-only check**: Comparing `node.val > node.left.val` is insufficient. The value must be within the range inherited from all ancestors.
- **Using `<=` instead of `<` for BST property**: Standard BST has strictly less on left, strictly greater on right. Duplicates break standard BST property — clarify with interviewer.
- **Delete with two children: not finding true inorder successor**: The successor is the leftmost node in the right subtree, not just `root.right`.
- **BST Iterator memory**: Claiming O(n) space. The stack holds at most O(h) nodes at any time because you only push the left spine.
- **LCA in BST: using the generic O(n) binary tree LCA**: You're wasting the BST property. The O(h) solution follows a single path down.

## Interview Questions

- "Validate whether a binary tree is a valid BST. What's the most common mistake people make?" (Microsoft/Google)
- "Find the kth smallest element in a BST. What if the BST is modified frequently — how would you optimize?" (Follow-up: augmented BST with subtree counts)
- "Implement a BST iterator with O(h) memory and O(1) amortized next(). Explain why it's O(1) amortized."
- "Delete a node from a BST. Walk through all three cases."
- "Find the LCA of two nodes in a BST. How is this different from LCA in a regular binary tree?"
- "Convert a sorted array into a balanced BST. Why pick the middle element?"
- "Two nodes in a BST were swapped by mistake. Find and fix them in O(1) space." (LC 99 — use Morris traversal)
- "What's the time complexity of BST operations? When does it degrade to O(n)?"

## Quick Reference

```
BST Invariant:
  For every node: ALL left subtree values < node < ALL right subtree values

BST Operations:
  Search/Insert/Delete → O(h) time, O(h) space (recursion)
  Balanced h = O(log n), Skewed h = O(n)

BST ↔ Sorted Order:
  Inorder traversal = sorted ascending
  Reverse inorder    = sorted descending

Key Patterns:
  Validate   → pass (low, high) range downward
  Kth element → inorder traversal, count to k
  LCA in BST → follow split point, O(h) not O(n)
  Build BST  → pick middle of sorted input for balance

BST vs Hash Map:
  Hash map: O(1) average lookup, no ordering
  BST: O(log n) lookup, but supports range queries, kth element, floor/ceiling
  → Use BST when you need ORDERED operations
```
