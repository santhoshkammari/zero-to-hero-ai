# Complexity Analysis

> Every interview answer ends with "and the time complexity is..." — get this wrong and nothing else matters.

## Core Idea

Big-O measures how runtime or space **scales** with input size `n` — not the exact time, but the growth rate.

- **Big-O (O)**: Upper bound — worst case. "At most this bad."
- **Big-Ω (Ω)**: Lower bound — best case. "At least this good."
- **Big-Θ (Θ)**: Tight bound — when O and Ω match. "Exactly this growth."

Interviewers care about **worst-case Big-O** almost always. The exception: randomized algorithms like quicksort where you discuss **average-case O(n log n)** and acknowledge **worst-case O(n²)**.

Constants and lower-order terms are dropped: `O(3n² + 5n + 100)` = `O(n²)`.

## What You Need to Know

### Common Complexities (Slowest to Fastest)

| Complexity | Name | Example | n=1000 ops |
|---|---|---|---|
| O(1) | Constant | Hash map lookup, array index | 1 |
| O(log n) | Logarithmic | Binary search | ~10 |
| O(n) | Linear | Array scan, single pass | 1,000 |
| O(n log n) | Linearithmic | Merge sort, heap sort | ~10,000 |
| O(n²) | Quadratic | Nested loops (brute force pairs) | 1,000,000 |
| O(2^n) | Exponential | All subsets, recursive Fibonacci | ~10^301 |
| O(n!) | Factorial | All permutations | ~10^2567 |

**Rule of thumb**: ~10^8 operations/second in Python. For n=10^5, O(n²) = 10^10 → TLE. Need O(n log n) or better.

### Analyzing Loops

```python
# O(n) — single loop
for i in range(n):
    do_something()  # O(1) work

# O(n²) — independent nested loops
for i in range(n):
    for j in range(n):
        do_something()

# O(n²) — dependent nested loop (this trips people up!)
for i in range(n):
    for j in range(i):  # j goes 0, 1, 2, ..., n-1
        do_something()
# Total: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n²)

# O(n log n) — outer O(n), inner halves each time
for i in range(n):
    j = n
    while j > 0:
        j //= 2  # O(log n) iterations

# O(log n) — halving
i = n
while i > 1:
    i //= 2

# O(√n) — square root pattern
i = 1
while i * i <= n:
    i += 1
```

### Amortized Analysis

Dynamic array (Python `list.append`): individual append can be O(n) when resizing, but over n appends the total is O(n), so **amortized O(1) per append**.

The doubling strategy: when full, allocate 2× space and copy. Copies happen at sizes 1, 2, 4, 8, ..., n. Total copy cost = 1 + 2 + 4 + ... + n ≈ 2n = O(n). Spread over n appends → O(1) each.

```python
# This is O(n) total, NOT O(n²)
result = []
for i in range(n):
    result.append(i)  # amortized O(1)
```

### Space Complexity

- **Auxiliary space**: extra space beyond input (what interviewers usually ask about)
- **Total space**: auxiliary + input
- **Recursion stack**: each call frame is O(1), depth d calls = O(d) space

```python
# O(1) auxiliary space
def find_max(arr):
    mx = arr[0]
    for x in arr:
        mx = max(mx, x)
    return mx

# O(n) auxiliary space — new array
def double_values(arr):
    return [x * 2 for x in arr]

# O(n) space from recursion stack
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)  # stack depth = n
```

### Master Theorem

For recurrences of the form **T(n) = aT(n/b) + O(n^d)**:

| Case | Condition | Result | Example |
|---|---|---|---|
| 1 | d < log_b(a) | O(n^(log_b(a))) | T(n) = 8T(n/2) + O(n) → O(n³) |
| 2 | d = log_b(a) | O(n^d · log n) | T(n) = 2T(n/2) + O(n) → O(n log n) (merge sort) |
| 3 | d > log_b(a) | O(n^d) | T(n) = 2T(n/2) + O(n²) → O(n²) |

**Binary search**: T(n) = T(n/2) + O(1) → a=1, b=2, d=0 → log₂(1)=0=d → Case 2 → O(log n).

**Merge sort**: T(n) = 2T(n/2) + O(n) → a=2, b=2, d=1 → log₂(2)=1=d → Case 2 → O(n log n).

### Log Rules You Need

- Binary search halves search space each step: n → n/2 → n/4 → ... → 1 takes log₂(n) steps.
- Merge sort: log₂(n) levels, O(n) work per level → O(n log n).
- `log(a*b) = log(a) + log(b)` — why merging sorted arrays is efficient.
- Any algorithm that repeatedly multiplies or divides by a constant → O(log n).

### Common Operations Complexity Table

| Data Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) |
| Dynamic Array (append) | O(1) | O(n) | O(1)* | O(n) |
| Linked List | O(n) | O(n) | O(1)† | O(1)† |
| Hash Map | — | O(1) avg | O(1) avg | O(1) avg |
| BST (balanced) | — | O(log n) | O(log n) | O(log n) |
| Heap | — | O(n) | O(log n) | O(log n) |
| Sorted Array | O(1) | O(log n) | O(n) | O(n) |

\* amortized  † given pointer to node

## Key Patterns & Templates

### Empirical Timing

```python
import time

def time_complexity_test(func, sizes=[100, 1000, 10000, 100000]):
    """Run func on increasing input sizes to empirically verify complexity."""
    for n in sizes:
        data = list(range(n))
        start = time.perf_counter()
        func(data)
        elapsed = time.perf_counter() - start
        print(f"n={n:>7}: {elapsed:.4f}s")
    # Compare ratios: O(n) → 10x input = 10x time
    # O(n²) → 10x input = 100x time
    # O(n log n) → 10x input ≈ 13x time

# Example usage
time_complexity_test(sorted)       # should show ~n log n growth
time_complexity_test(lambda a: [x for x in a])  # should show linear growth
```

### Recognizing Patterns

```python
# Pattern → Complexity cheat sheet:

# Single loop over n elements → O(n)
for i in range(n): ...

# Two nested loops over n → O(n²)
for i in range(n):
    for j in range(n): ...

# Loop that halves → O(log n)
while n > 0:
    n //= 2

# Recursion that branches into 2 calls → O(2^n)
def f(n):
    if n <= 0: return
    f(n-1); f(n-1)

# Recursion with halving and linear merge → O(n log n)
def f(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = f(arr[:mid])    # T(n/2)
    right = f(arr[mid:])   # T(n/2)
    return merge(left, right)  # O(n)

# Generating all subsets → O(2^n)
# Generating all permutations → O(n!)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Climbing Stairs | 70 | Easy | Recursion → memoization shows exponential → linear transformation |
| Pow(x, n) | 50 | Medium | Fast exponentiation: O(log n) by squaring, handle negative n |
| Count Primes | 204 | Medium | Sieve of Eratosthenes O(n log log n), only mark from p² |
| Fibonacci Number | 509 | Easy | Compare O(2^n) recursive vs O(n) DP vs O(log n) matrix exponentiation |
| Maximum Subarray | 53 | Medium | Kadane's O(n) — recognize that O(n²) brute force is unnecessary |

## Common Mistakes

- **Nested loop miss**: Saying O(n) when a dependent nested loop (`for j in range(i)`) makes it O(n²) — always sum the inner loop iterations.
- **Stack space forgotten**: Recursion uses O(depth) stack space. A recursive DFS on a tree is O(h) space, not O(1).
- **Average vs worst case**: Quicksort is O(n log n) average but O(n²) worst case. Hash table lookup is O(1) average but O(n) worst case.
- **Amortized misunderstanding**: `list.append()` is amortized O(1), not worst-case O(1). A single append can be O(n) during resize.
- **Dropping constants wrong**: O(2n) = O(n) in Big-O, but in practice 2n operations is twice as slow as n. Big-O ignores constants; real performance doesn't.

## Interview Questions

- **"What's the time complexity of this code?"** (nested loops with varying inner bound) — Sum the series. `for i in range(n): for j in range(i)` → 0+1+...+(n-1) = O(n²).
- **"Explain the difference between O(n log n) and O(n²) — at what input size does it matter?"** — At n=1000, n² is 100x slower. At n=10^6, it's the difference between 1 second and 11 days.
- **"What's amortized analysis? Give an example."** — Average cost per operation over a sequence. Dynamic array: most appends O(1), occasional resize O(n), but n appends total O(n).
- **"Why is building a heap O(n) and not O(n log n)?"** — Bottom-up heapify: most nodes are near leaves and sift down very little. Mathematical proof: sum of (n/2^(h+1)) × h for each height h converges to O(n).
- **"What's the space complexity of a recursive function with depth d?"** — O(d) for the call stack, plus any auxiliary space per call.
- **"How would you optimize an O(n²) solution to O(n log n)?"** — Common strategies: sorting + two pointers, binary search inside loop, divide and conquer, or using a balanced BST/heap.
- **"What's the Master Theorem and when can't you use it?"** — Solves T(n) = aT(n/b) + O(n^d). Can't use when: subproblems are different sizes, non-polynomial extra work, or the recurrence isn't in this form.

## Quick Reference

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Hash map lookup, arithmetic |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array scan, hash map build |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2^n) | Exponential | All subsets, naive Fibonacci |
| O(n!) | Factorial | All permutations |

**Interview sizing guide**: Given 1 second time limit in Python (~10^7-10^8 ops):
- n ≤ 10 → O(n!) or O(2^n) is fine
- n ≤ 20 → O(2^n) feasible
- n ≤ 500 → O(n³) feasible
- n ≤ 10^4 → O(n²) feasible
- n ≤ 10^6 → O(n log n) needed
- n ≤ 10^8 → O(n) needed
- n > 10^8 → O(log n) or O(1) needed
