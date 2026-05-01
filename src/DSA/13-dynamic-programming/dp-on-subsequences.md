# DP on Subsequences & Partitions

> Half of all DP interview problems boil down to "include this element or skip it." Master this family and you unlock subset sum, knapsack, interval DP, and bitmask DP in one shot.

## Core Idea

Every subsequence problem is a binary decision tree — for each element, you either **include** it or **exclude** it. That's 2ⁿ choices brute-force, but overlapping subproblems let DP collapse it to polynomial time. The trick is figuring out *what state* you need to remember after each include/exclude decision (usually an index + some running value like a remaining capacity or a current sum).

## What You Need to Know

### Include/Exclude vs 1D DP

In 1D DP (like climbing stairs), each state depends on a fixed number of previous states. In subsequence DP, each state branches into **two** futures — take or skip — and the "take" branch usually changes a second dimension (remaining sum, remaining capacity, etc.). That second dimension is what makes this 2D.

```
1D DP:      dp[i] depends on dp[i-1], dp[i-2], ...
Subseq DP:  dp[i][target] depends on dp[i-1][target] (skip) 
                                  OR dp[i-1][target - arr[i]] (take)
```

### The Three Big Families

| Family | Core Question | State Shape | Examples |
|--------|--------------|-------------|----------|
| **Subset/Knapsack** | Can we pick items to hit a target? | `dp[i][remaining]` | Subset Sum, Partition Equal Subset, Target Sum |
| **Interval DP** | What's optimal for subarray `[i..j]`? | `dp[i][j]` | Burst Balloons, Matrix Chain Multiply, Palindrome Partition |
| **Bitmask DP** | Optimal over all subsets of n items? | `dp[mask]` where mask is a bitmask | TSP, Task Assignment, Partition into K Equal Subsets |

### Subset Sum / 0-1 Knapsack

The foundation. Given `nums`, can you pick a subset that sums to `target`?

**Recurrence:**
```
dp[i][s] = dp[i-1][s]              # skip nums[i]
         | dp[i-1][s - nums[i]]    # take nums[i] (if s >= nums[i])
```

**Why it works:** After deciding on element `i`, the remaining problem is identical but with one fewer element and a (possibly reduced) target. Classic overlapping subproblems.

**Space optimization:** Since row `i` only depends on row `i-1`, use a 1D array and iterate `s` **right to left** (so you don't overwrite values you still need).

| Variant | Time | Space | Key Twist |
|---------|------|-------|-----------|
| Subset Sum (exists?) | O(n × target) | O(target) | 1D bool array |
| Count of subsets with sum | O(n × target) | O(target) | `dp[s] += dp[s - num]` instead of OR |
| 0/1 Knapsack (max value) | O(n × W) | O(W) | `dp[w] = max(dp[w], dp[w - wt[i]] + val[i])` |
| Unbounded Knapsack | O(n × W) | O(W) | Iterate `s` **left to right** (reuse allowed) |

### Partition Equal Subset Sum (LC 416)

**Reduction:** Can we split `nums` into two subsets with equal sum? That's just: "does a subset exist that sums to `total_sum / 2`?" If `total_sum` is odd, answer is immediately `False`.

Why this reduction works: if subset A sums to S/2, then subset B (everything else) also sums to S/2.

### Target Sum (LC 494)

You assign `+` or `-` to each number to reach `target`. Looks different, but it's subset sum in disguise.

**Math trick:** Let P = sum of numbers assigned `+`, N = sum assigned `-`.
- P + N = total_sum
- P - N = target
- So P = (total_sum + target) / 2

Now it's just "count subsets that sum to P." If `(total_sum + target)` is odd or `target > total_sum`, return 0.

### Interval DP

For problems on contiguous subarrays/substrings where you're merging or splitting. The pattern: **think about the last operation**, not the first.

**Recurrence:**
```
dp[i][j] = best over all split points k in [i..j]:
             combine(dp[i][k], dp[k+1][j], cost_of_merge)
```

**Why "last operation" works:** If you think about what happens *first*, the two resulting pieces aren't independent (they affect each other). Thinking about what happens *last* means the subproblems are already fully resolved and independent.

**Burst Balloons (LC 312):** Instead of "which balloon to pop first," ask "which balloon to pop **last** in range `[i..j]`?" If balloon `k` is popped last, it sees the boundary balloons `nums[i-1]` and `nums[j+1]` (everything else in the range is already gone). That makes subproblems `[i..k-1]` and `[k+1..j]` independent.

**Matrix Chain Multiplication:** Where to place parentheses to minimize scalar multiplications. Split at every `k`: cost = `dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]`.

**Iteration order:** Fill by **gap length** (length 1, then 2, then 3...) so smaller subproblems are solved first.

| Problem | Time | Space |
|---------|------|-------|
| Burst Balloons | O(n³) | O(n²) |
| Matrix Chain Multiplication | O(n³) | O(n²) |
| Palindrome Partitioning II (LC 132) | O(n²) | O(n²) |
| Minimum Cost Tree From Leaf Values (LC 1130) | O(n³) | O(n²) |

### Partition DP (Splitting Arrays into Segments)

Split an array into contiguous segments to optimize some cost. Different from interval DP — here segments don't merge, they're evaluated independently.

**Recurrence:**
```
dp[i] = min/max over all valid split points j < i:
          dp[j] + cost(j+1, i)
```

Think of `dp[i]` as the best answer for the first `i` elements. You try every possible "last segment" `[j+1..i]`.

### Bitmask DP

When you have n items (n ≤ 20ish) and need to track *which* items are used, represent the subset as a bitmask. Each bit = one item (1 = used, 0 = not used).

**Why bitmask and not just a set?** An integer is hashable, comparable, and copyable in O(1). A set of items isn't. This lets you use it as a DP key.

| Operation | Code | What It Does |
|-----------|------|-------------|
| Check bit i | `mask & (1 << i)` | Is item i in the subset? |
| Set bit i | `mask \| (1 << i)` | Add item i to subset |
| Clear bit i | `mask & ~(1 << i)` | Remove item i |
| Count bits | `bin(mask).count('1')` | Subset size |
| All n items | `(1 << n) - 1` | Full set mask |

**Classic use — TSP (Traveling Salesman):**
`dp[mask][i]` = min cost to visit exactly the cities in `mask`, ending at city `i`.

| Problem | Time | Space |
|---------|------|-------|
| TSP | O(2ⁿ × n²) | O(2ⁿ × n) |
| Task Assignment | O(2ⁿ × n) | O(2ⁿ) |
| Partition to K Equal Sum Subsets (LC 698) | O(2ⁿ × n) | O(2ⁿ) |

**When to use bitmask DP:** n ≤ 20 (since 2²⁰ ≈ 10⁶). If n > 20, look for greedy or other approaches.

## Key Patterns & Templates

### Subset Sum / Partition Template

```python
def can_partition(nums: list[int], target: int) -> bool:
    """Returns True if any subset of nums sums to target."""
    dp = [False] * (target + 1)
    dp[0] = True  # empty subset sums to 0

    for num in nums:
        # right to left so each num is used at most once
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


def count_subsets_with_sum(nums: list[int], target: int) -> int:
    """Counts subsets of nums that sum to target."""
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[target]


# Partition Equal Subset Sum (LC 416)
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    return can_partition(nums, total // 2)


# Target Sum (LC 494)
def findTargetSumWays(nums: list[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 or abs(target) > total:
        return 0
    return count_subsets_with_sum(nums, (total + target) // 2)
```

### Interval DP Template (Burst Balloons Style)

```python
def burst_balloons(nums: list[int]) -> int:
    """LC 312. Max coins from bursting all balloons."""
    # pad with 1 on both ends for boundary handling
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # gap = length of the range we're solving
    for gap in range(2, n):  # min gap is 2 (at least one balloon between boundaries)
        for i in range(0, n - gap):
            j = i + gap
            for k in range(i + 1, j):  # k is the LAST balloon popped in (i, j)
                coins = nums[i] * nums[k] * nums[j]
                dp[i][j] = max(dp[i][j], dp[i][k] + coins + dp[k][j])

    return dp[0][n - 1]


def matrix_chain_multiply(dims: list[int]) -> int:
    """
    Minimum scalar multiplications.
    dims[i] x dims[i+1] is the shape of matrix i.
    n matrices → len(dims) = n + 1.
    """
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]
```

### Bitmask DP Template

```python
def min_cost_tsp(dist: list[list[int]]) -> int:
    """
    Traveling Salesman: visit all n cities starting from 0, return to 0.
    dist[i][j] = cost from city i to city j.
    """
    n = len(dist)
    full_mask = (1 << n) - 1
    INF = float('inf')

    # dp[mask][i] = min cost to reach city i, having visited cities in mask
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0, only city 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    # return to start
    return min(dp[full_mask][i] + dist[i][0] for i in range(n))


def assign_tasks(cost: list[list[int]]) -> int:
    """
    Assign n tasks to n workers. cost[i][j] = cost of worker i doing task j.
    Minimize total cost.
    """
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        worker = bin(mask).count('1')  # which worker are we assigning next
        if worker >= n:
            continue
        for task in range(n):
            if mask & (1 << task):
                continue
            new_mask = mask | (1 << task)
            dp[new_mask] = min(dp[new_mask], dp[mask] + cost[worker][task])

    return dp[(1 << n) - 1]
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Partition Equal Subset Sum | 416 | Medium | Reduce to subset sum with target = total/2. If total is odd, instant False. |
| Target Sum | 494 | Medium | Algebra trick: count subsets summing to (total + target) / 2. |
| Coin Change | 322 | Medium | Unbounded knapsack — iterate left to right since coins are reusable. |
| Burst Balloons | 312 | Hard | Think about what's popped LAST, not first. That makes subproblems independent. |
| Palindrome Partitioning II | 132 | Hard | Precompute palindrome table, then 1D DP for min cuts. |
| Partition to K Equal Sum Subsets | 698 | Medium | Bitmask DP or backtracking with pruning. Bitmask is O(2ⁿ × n). |
| Last Stone Weight II | 1049 | Medium | Identical to partition equal subset sum — minimize difference between two groups. |
| Minimum Cost Tree From Leaf Values | 1130 | Medium | Interval DP: try every split point, cost = max(left) × max(right). |

## Common Mistakes

- **Iterating left to right in 0/1 knapsack.** You'll reuse the same item multiple times. Go right to left for 0/1; left to right is for unbounded knapsack. This single bug silently gives wrong answers on most test cases.
- **Forgetting the odd-sum early return.** In partition problems, if total sum is odd, no equal partition exists. Skip this check and you'll get index-out-of-range or wrong answers.
- **Interval DP: thinking about the first operation instead of the last.** Burst Balloons is the classic trap. If you pop a balloon first, the neighbors change and subproblems aren't independent. Thinking "last" fixes this.
- **Bitmask DP with n > 20.** 2²⁰ ≈ 1M states is fine. 2²⁵ ≈ 33M will TLE. Always check constraints before reaching for bitmask.
- **Not handling zeros in subset sum counting.** If `nums` contains 0, your count can be wrong. Zeros contribute to distinct subsets but not to the sum — handle them separately or be careful with the loop bounds.

## Interview Questions

1. **"Given an array, can you split it into two subsets with equal sum?"** — Partition Equal Subset Sum (LC 416). Reduce to subset sum targeting total/2.
2. **"Count the number of ways to assign + and - to elements to reach a target."** — Target Sum (LC 494). Show the algebra to reduce it to subset sum counting.
3. **"How does 0/1 knapsack differ from unbounded knapsack in implementation?"** — Loop direction. Right-to-left prevents reuse; left-to-right allows it. That's the only difference in the 1D optimization.
4. **"You have n balloons with values. Bursting balloon i gives nums[i-1] × nums[i] × nums[j+1] coins. Maximize coins."** — Burst Balloons (LC 312). Explain the "pop last" insight.
5. **"Why is the brute force for subset sum O(2ⁿ) and how does DP improve it?"** — 2ⁿ subsets, but many share the same (index, remaining_sum) state. DP merges these → O(n × target).
6. **"Find the minimum difference between two subset sums."** — Last Stone Weight II (LC 1049). Find the largest achievable sum ≤ total/2, answer is total - 2 × that sum.
7. **"How would you solve TSP for 15 cities?"** — Bitmask DP. O(2¹⁵ × 15²) ≈ 7M operations — comfortably fits in time.
8. **"What's the time complexity of interval DP and why?"** — O(n³): O(n²) subproblems (all pairs i,j), each trying O(n) split points.
9. **"When would you choose bitmask DP over backtracking?"** — When n ≤ 20 and you need exact answers (not just feasibility). Bitmask DP avoids redundant work that backtracking repeats. For n > 20, backtracking with pruning may be the only option.

## Quick Reference

```
DECISION FLOWCHART
──────────────────
"Pick a subset to optimize something"
  → Is it 0/1 (each item once)?
      YES → Subset Sum / 0-1 Knapsack template (loop right to left)
      NO  → Unbounded Knapsack (loop left to right)

"Optimize over a contiguous range [i..j]"
  → Interval DP. Think about the LAST operation.
    Fill by increasing gap length.

"Track which items are used (n ≤ 20)"
  → Bitmask DP. State = integer bitmask.

"Split array into K contiguous segments"
  → Partition DP. dp[i] = best for first i elements,
    try all last-segment boundaries.
```

| Pattern | Time | Space | Loop Direction |
|---------|------|-------|----------------|
| 0/1 Subset Sum | O(n × T) | O(T) | Right → Left |
| Unbounded Knapsack | O(n × W) | O(W) | Left → Right |
| Subset Sum (count) | O(n × T) | O(T) | Right → Left |
| Interval DP | O(n³) | O(n²) | By gap length |
| Bitmask DP | O(2ⁿ × n) | O(2ⁿ) | Ascending mask |
| Partition DP (K segs) | O(n² × K) | O(n × K) | By segment count |

```
SUBSET SUM 1D CHEAT SHEET
──────────────────────────
dp = [False] * (target + 1)
dp[0] = True
for num in nums:
    for s in range(target, num - 1, -1):   # RIGHT TO LEFT
        dp[s] |= dp[s - num]
```
