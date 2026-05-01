# Monotonic Queue (Deque)

> The monotonic deque gives you the sliding window maximum or minimum in O(n) — a huge upgrade over the naive O(nk) approach that interviewers love to test.

## Core Idea

A **monotonic deque** maintains a deque of *candidates* for the window's max (or min), pruning elements that can never win. It's like a waiting line where anyone shorter than the new arrival gets kicked out because they'll never be the tallest while the new person is still in the window. The front of the deque is always the current answer.

## What You Need to Know

### How It Works (Sliding Window Maximum)

For a **monotonic decreasing deque** (front = maximum of current window):

1. **Add new element**: Pop from the *back* while the new element is larger — those elements are now useless because the new element is bigger and will stay in the window longer.
2. **Remove expired element**: Pop from the *front* if its index is outside the window.
3. **Read answer**: The front of the deque is the current window maximum.

Every element enters and leaves the deque at most once → **O(n) total**.

### Increasing vs Decreasing

| Deque Type | Front Contains | Use For | Pop Back When |
|-----------|---------------|---------|--------------|
| **Monotonic decreasing** | Window maximum | Sliding window max | New element > back |
| **Monotonic increasing** | Window minimum | Sliding window min | New element < back |

### Sliding Window Maximum (LC 239) — The Core Problem

```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()  # indices, values are monotonically decreasing
    result = []
    for i, num in enumerate(nums):
        # Remove elements outside the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Maintain decreasing order: remove smaller elements from back
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        # Window is full, record the max (front of deque)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

Time: O(n) — each index is appended and removed from the deque at most once
Space: O(k) — deque holds at most k elements

**Why store indices, not values?** Because you need to check if the front element has left the window (`dq[0] < i - k + 1`). You can't do that with just values.

### Sliding Window Minimum (Flip the Comparison)

```python
from collections import deque

def min_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()  # indices, values are monotonically increasing
    result = []
    for i, num in enumerate(nums):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] >= num:  # flip: remove larger elements
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Shortest Subarray with Sum at Least K (LC 862)

This is a hard problem that combines **prefix sums** with a **monotonic increasing deque**. Unlike the basic sliding window, the array can have negative numbers, so the window isn't simply expandable.

Key insight: Use prefix sums. For each `i`, you want the largest `j < i` such that `prefix[i] - prefix[j] >= k`. A monotonic increasing deque on prefix sums lets you efficiently find the best `j`.

```python
from collections import deque

def shortest_subarray(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    dq = deque()  # indices into prefix, values are increasing
    result = float('inf')
    for i in range(n + 1):
        # If current prefix minus front prefix >= k, we have a valid subarray
        while dq and prefix[i] - prefix[dq[0]] >= k:
            result = min(result, i - dq.popleft())
        # Maintain increasing order of prefix sums
        while dq and prefix[dq[-1]] >= prefix[i]:
            dq.pop()
        dq.append(i)
    return result if result != float('inf') else -1
```

Time: O(n) | Space: O(n)

Why pop from front when we find a valid answer? Because no future `i` can give a *shorter* subarray with that same `j` — the distance only grows.

Why maintain increasing prefix sums? If `prefix[b] >= prefix[a]` and `b > a`, then `a` is always better than `b` as a starting point (smaller prefix, earlier index).

### Longest Continuous Subarray With Absolute Diff ≤ Limit (LC 1438)

Track both the sliding window max and min simultaneously using *two* monotonic deques. If `max - min > limit`, shrink the window from the left.

```python
from collections import deque

def longest_subarray(nums: list[int], limit: int) -> int:
    max_dq = deque()  # decreasing: front = max
    min_dq = deque()  # increasing: front = min
    left = 0
    result = 0
    for right, num in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= num:
            max_dq.pop()
        while min_dq and nums[min_dq[-1]] >= num:
            min_dq.pop()
        max_dq.append(right)
        min_dq.append(right)
        # Shrink window if constraint violated
        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
        result = max(result, right - left + 1)
    return result
```

Time: O(n) | Space: O(n)

### Jump Game VI (LC 1696)

DP where `dp[i] = nums[i] + max(dp[i-k] ... dp[i-1])`. The "max of last k dp values" is a sliding window maximum — use a monotonic deque.

```python
from collections import deque

def max_result(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dq = deque([0])  # indices, dp values are decreasing
    for i in range(1, n):
        # Remove indices outside the window
        if dq[0] < i - k:
            dq.popleft()
        dp[i] = nums[i] + dp[dq[0]]  # best previous value
        # Maintain decreasing order
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
    return dp[-1]
```

Time: O(n) | Space: O(n)

## Key Patterns & Templates

### Pattern 1: Sliding Window Max/Min Template

```python
from collections import deque

def sliding_window_extremum(nums, k, find_max=True):
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        # Expire front
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Maintain monotonic property
        if find_max:
            while dq and nums[dq[-1]] <= num:
                dq.pop()
        else:
            while dq and nums[dq[-1]] >= num:
                dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Pattern 2: DP Optimization with Monotonic Deque

When your DP transition looks like `dp[i] = min/max(dp[j] for j in range(i-k, i)) + cost[i]`, replace the O(k) scan with a monotonic deque for O(1) amortized per transition.

```python
from collections import deque

def dp_with_deque(costs, k):
    n = len(costs)
    dp = [float('inf')] * n
    dp[0] = costs[0]
    dq = deque([0])
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = dp[dq[0]] + costs[i]
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
    return dp[-1]
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Sliding Window Maximum | 239 | Hard | Monotonic decreasing deque of indices; front = window max; O(n) |
| Shortest Subarray with Sum ≥ K | 862 | Hard | Prefix sums + monotonic increasing deque; pop front on valid, pop back on decreasing prefix |
| Longest Subarray With Diff ≤ Limit | 1438 | Medium | Two deques (max + min) with sliding window; shrink when `max - min > limit` |
| Jump Game VI | 1696 | Medium | DP transition uses sliding window max → deque makes it O(n) instead of O(nk) |
| Constrained Subsequence Sum | 1425 | Hard | Same pattern as Jump Game VI — DP + monotonic deque |
| Max Value of Equation | 1499 | Hard | Rewrite as `yi + yj + |xi - xj|` = `(yj - xj) + (yi + xi)` → deque on `(yj - xj)` |

## Common Mistakes

- **Removing from the wrong end**: New elements compete at the *back* (pop smaller/larger from back). Expired elements leave from the *front*. Mixing these up breaks everything.
- **Off-by-one on window boundaries**: The front element is expired when `dq[0] < i - k + 1` (strictly less), not `<=`. Draw out a small example if unsure.
- **Using `<` instead of `<=` when maintaining the deque**: For sliding window max, use `nums[dq[-1]] <= num` (not strict `<`) to pop equal elements. Keeping duplicates wastes space and doesn't affect correctness, but using strict inequality *does* affect some problems (like when you need distinct candidates).
- **Forgetting this is a deque, not a stack**: You need O(1) operations on *both* ends. A regular stack or queue won't work. In Python, `collections.deque` gives you both.
- **Not recognizing the pattern in DP problems**: Any time a DP recurrence takes a min/max over a sliding window of the previous `k` states, a monotonic deque optimizes it from O(nk) to O(n).

## Interview Questions

1. **Conceptual**: Why can't you solve sliding window maximum with just a regular queue? What property does the monotonic deque maintain?
2. **Conceptual**: Prove that the amortized time complexity of the monotonic deque approach is O(n).
3. **Problem**: Find the maximum of every contiguous subarray of size `k`. Walk through your deque approach on `[1, 3, -1, -3, 5, 3, 6, 7]` with `k=3`. (LC 239)
4. **Problem**: Given an array with negative numbers, find the shortest subarray with sum ≥ K. Why doesn't a simple sliding window work here? (LC 862)
5. **Follow-up**: How would you find both the sliding window max *and* min simultaneously? (LC 1438)
6. **Problem**: You can jump up to `k` steps. Each position has a score. Maximize total score. How does a monotonic deque help? (LC 1696)
7. **Design**: How would you extend sliding window maximum to support dynamic window sizes?

## Quick Reference

```
Monotonic Deque = deque where values are sorted (increasing or decreasing)

Sliding Window Maximum (decreasing deque):
  1. Expire front:  if dq[0] < i - k + 1 → popleft
  2. Clean back:    while nums[dq[-1]] <= nums[i] → pop
  3. Add:           dq.append(i)
  4. Read:          nums[dq[0]] is the window max

Sliding Window Minimum (increasing deque):
  Same but flip <=  to  >=

Complexity: O(n) time, O(k) space

When to use:
  ├─ Sliding window max/min
  ├─ DP with recurrence: dp[i] = f(min/max of dp[i-k..i-1])
  └─ Any "best in a range" that slides

vs Monotonic Stack:
  Stack → "next greater/smaller" (one-directional)
  Deque → "max/min in a window" (bounded range)
```
