# Recursion

> If you can't think recursively, trees and graphs become impossible. This is the unlock.

## Core Idea

A function calls itself with a smaller input until hitting a base case. Every recursion has:
1. **Base case** — stops the recursion (without it → infinite loop → stack overflow)
2. **Recursive case** — shrinks the problem toward the base case
3. **Call stack** — each call gets its own frame with local variables; the stack tracks where to return

Think of it as: **trust that the recursive call solves the smaller problem**, then combine results. Don't try to trace every call mentally — define the contract and trust it.

## What You Need to Know

### Call Stack Mechanics

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Call stack for factorial(4):
# factorial(4) → waits for factorial(3)
#   factorial(3) → waits for factorial(2)
#     factorial(2) → waits for factorial(1)
#       factorial(1) → returns 1
#     returns 2 * 1 = 2
#   returns 3 * 2 = 6
# returns 4 * 6 = 24
# Stack depth = n → O(n) space
```

Each frame holds its own `n`. Python's default recursion limit is **1000** — hit it and you get `RecursionError`. Increase with `sys.setrecursionlimit()`, but the real solution is usually converting to iteration.

### Base Case Design

The base case must be **reachable** and handle **all edge cases**:

```python
# Bad — misses n=0
def fib(n):
    if n == 1: return 1  # What about n=0?
    return fib(n-1) + fib(n-2)

# Good — handles both edges
def fib(n):
    if n <= 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
```

### Recursion vs Iteration

Any recursion can be converted to iteration with an explicit stack. The call stack IS a stack — we're just making it explicit.

```python
# Recursive DFS
def dfs_recursive(node):
    if not node:
        return
    process(node)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

# Iterative DFS — explicit stack
def dfs_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        process(node)
        if node.right: stack.append(node.right)  # right first so left is processed first
        if node.left: stack.append(node.left)
```

### Tail Recursion

When the recursive call is the **last operation** — no computation after it returns. Some languages optimize this to reuse the stack frame (tail call optimization). **Python does NOT optimize tail recursion** — convert to iteration yourself.

```python
# Tail recursive — last thing is the recursive call
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n - 1, acc * n)

# Convert to iterative (since Python doesn't optimize)
def factorial_iter(n):
    acc = 1
    while n > 1:
        acc *= n
        n -= 1
    return acc
```

### Recursion Tree & Memoization

Visualize the recursion tree to spot **overlapping subproblems**:

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ←── computed again!
│   │   └── fib(1)
│   └── fib(2) ←── computed again!
└── fib(3) ←── entire subtree repeated!
    ├── fib(2)
    └── fib(1)
```

Overlapping subproblems → **memoize** to avoid recomputation:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
# O(2^n) → O(n) with memoization
```

### Common Recursive Patterns

**Divide and Conquer**: Split problem in half, solve each, combine.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Decrease and Conquer**: Reduce problem by a constant amount (usually 1).
```python
def binary_search(arr, target, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target: return binary_search(arr, target, mid + 1, hi)
    return binary_search(arr, target, lo, mid - 1)
```

## Key Patterns & Templates

### 1. Basic Recursion Template

```python
def solve(input):
    # Base case(s)
    if is_base_case(input):
        return base_result

    # Recursive case — shrink the problem
    smaller = make_smaller(input)
    sub_result = solve(smaller)

    # Combine and return
    return combine(input, sub_result)
```

### 2. Recursion with Memoization

```python
def solve(input, memo=None):
    if memo is None:
        memo = {}

    if input in memo:
        return memo[input]

    if is_base_case(input):
        return base_result

    result = combine(solve(sub1, memo), solve(sub2, memo))
    memo[input] = result
    return result

# Or use @lru_cache for hashable inputs:
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(input):
    if is_base_case(input):
        return base_result
    return combine(solve(sub1), solve(sub2))
```

### 3. Recursion → Iteration with Explicit Stack

```python
def solve_iterative(root):
    if not root:
        return

    stack = [(root, False)]  # (node, processed)
    result = []

    while stack:
        node, processed = stack.pop()
        if not node:
            continue
        if processed:
            result.append(node.val)  # process here
        else:
            # Push in reverse order of desired processing
            stack.append((node.right, False))
            stack.append((node, True))  # mark for processing
            stack.append((node.left, False))

    return result
```

### 4. Backtracking Template (Choose / Explore / Unchoose)

```python
def backtrack(candidates, path, result):
    if is_solution(path):
        result.append(path[:])  # copy! path is mutable
        return

    for choice in candidates:
        if not is_valid(choice, path):
            continue
        path.append(choice)          # choose
        backtrack(candidates, path, result)  # explore
        path.pop()                   # unchoose (restore state)
```

### 5. Tree Traversal Template

```python
def traverse(node):
    if not node:
        return

    # Pre-order: process BEFORE children
    process(node)

    traverse(node.left)

    # In-order: process BETWEEN children (BST gives sorted order)
    # process(node)

    traverse(node.right)

    # Post-order: process AFTER children (useful for computing heights, subtree results)
    # process(node)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Fibonacci Number | 509 | Easy | Naive O(2^n) → memoized O(n); visualize recursion tree |
| Climbing Stairs | 70 | Easy | Same as Fibonacci; recursion → memoization → DP transition |
| Pow(x, n) | 50 | Medium | Divide: x^n = (x^(n/2))² — O(log n) recursive |
| Reverse Linked List | 206 | Easy | Recursive: trust that `reverse(head.next)` works, then rewire |
| Merge Sort | — | Medium | Classic divide and conquer; split, recurse, merge |

## Common Mistakes

- **Missing base case** → infinite recursion → `RecursionError`. Always define what stops it.
- **Not restoring state in backtracking** — if you `path.append(choice)` before recursing, you must `path.pop()` after. Otherwise downstream branches see stale state.
- **Ignoring overlapping subproblems** — if your recursion tree has repeated nodes, you need memoization. Without it, exponential blowup.
- **Python recursion limit** — default is 1000. For problems with deep recursion (linked list of 10^4 nodes), convert to iterative or call `sys.setrecursionlimit(10**5 + 10)`.
- **Returning vs printing** — `print(recursive_call())` is not the same as `return recursive_call()`. Forgetting `return` means the result is lost.
- **Mutating input without copy** — passing a list into recursion and appending to it? Changes persist across branches unless you copy (`path[:]`) or pop.

## Interview Questions

- **"Convert this recursive solution to iterative."** — Use an explicit stack. Push state that the recursion would've tracked in local variables.
- **"What's the time and space complexity of this recursive function?"** — Time: count total calls × work per call. Space: max recursion depth (stack frames) + auxiliary space.
- **"When would you use recursion vs iteration?"** — Recursion: tree/graph traversal, divide & conquer, backtracking. Iteration: simple loops, when stack depth is a concern, performance-critical code.
- **"How does memoization change the complexity of Fibonacci from O(2^n) to O(n)?"** — Without memo: each call branches into 2, creating 2^n nodes. With memo: each `fib(k)` computed once, n unique subproblems, O(1) per lookup → O(n) total.
- **"Explain how the call stack works for this recursive function."** — Trace through a small input (n=3 or 4). Show each frame's local variables and return values.
- **"What is tail recursion and does Python support tail call optimization?"** — Tail recursion: recursive call is the last operation. Python does NOT optimize it — CPython always allocates a new frame. Convert to iteration manually.
- **"How would you handle stack overflow in a recursive solution?"** — Convert to iterative with explicit stack, increase recursion limit (risky), or restructure as bottom-up DP.

## Quick Reference

**When to use recursion:**
- Tree/graph traversal → almost always recursive (or explicit stack)
- Divide and conquer (merge sort, quicksort) → naturally recursive
- Generate all combinations/permutations → backtracking (recursive)
- Can convert to DP? → Start recursive + memo, then convert to bottom-up

**Recursion complexity cheat sheet:**

| Pattern | Time | Space | Example |
|---|---|---|---|
| Linear (one call, shrink by 1) | O(n) | O(n) | factorial, linked list traversal |
| Binary (two calls, shrink by 1) | O(2^n) | O(n) | naive Fibonacci |
| Divide & conquer (two calls, halve) | O(n log n)* | O(log n)† | merge sort |
| Binary + memoization | O(n) | O(n) | memoized Fibonacci |
| k-way branching to depth n | O(k^n) | O(n) | permutations (k=n) |

\* with O(n) merge step  
† O(n) for merge sort due to auxiliary array; O(log n) stack depth

**Quick decision flowchart:**
1. Can you define the problem in terms of smaller subproblems? → Recursion candidate
2. Are there overlapping subproblems? → Add memoization (or convert to DP)
3. Is the recursion depth too large (>1000)? → Convert to iterative
4. Do you need all possibilities? → Backtracking
