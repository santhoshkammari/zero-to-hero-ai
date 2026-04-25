# 2D Dynamic Programming — Grids, Knapsacks & State Machines

> Half of all DP interview problems are 2D. Master grids and knapsack, and you've covered the majority of what FAANG asks.

## Core Idea

In 2D DP, each subproblem is defined by **two changing parameters** — a row and column in a grid, a capacity and item index in knapsack, or a day and state in stock problems. You fill a 2D table where each cell depends on previously computed cells. The trick is figuring out what those two dimensions *are* and how cells relate to each other.

## What You Need to Know

### The Three Families of 2D DP

| Family | Dimensions | Direction | Space Optimization |
|--------|-----------|-----------|-------------------|
| Grid DP | `(row, col)` | top-left → bottom-right | Previous row only → O(cols) |
| 0/1 Knapsack | `(item, capacity)` | row by row | 1D array, iterate **backwards** |
| Unbounded Knapsack | `(item, capacity)` | row by row | 1D array, iterate **forwards** |
| State Machine DP | `(day, state)` | day by day | O(states) variables |

### 1. Grid DP

The simplest 2D DP. You have an `m × n` grid and need to count paths, find minimum cost, or check reachability.

**Pattern:** each cell depends on the cell above and to the left.

```
dp[i][j] = f(dp[i-1][j], dp[i][j-1])
```

**Why first row and column are base cases:** you can only reach them by going straight right or straight down — there's exactly one way, so they're all 1 (for path counting) or cumulative sums (for min cost).

**Space optimization:** since each row only depends on the previous row, keep a single 1D array and update left-to-right. `dp[j]` holds the "above" value before update and the "left" value after update — both are available when you need them.

| Variant | Recurrence | Base Case |
|---------|-----------|-----------|
| Unique Paths (LC 62) | `dp[i][j] = dp[i-1][j] + dp[i][j-1]` | First row/col = 1 |
| Unique Paths II (LC 63) | Same, but `dp[i][j] = 0` if obstacle | Stop filling base case at first obstacle |
| Minimum Path Sum (LC 64) | `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])` | Cumulative sum along edges |

### 2. 0/1 Knapsack

You have `n` items, each with a weight and value. Pick a subset that maximizes value without exceeding capacity `W`. Each item is used **at most once**.

```
dp[i][w] = max(dp[i-1][w],                        # skip item i
               dp[i-1][w - weight[i]] + value[i])  # take item i
```

**Why iterate backwards for space optimization:** when you compress to 1D, `dp[w]` needs the value from the *previous* row at `dp[w - weight[i]]`. If you iterate forwards, you'd overwrite smaller capacities first — meaning you'd read the *current* row's value and effectively reuse items. Iterating backwards ensures you always read stale (previous row) values.

**Partition Equal Subset Sum (LC 416):** "Can we split the array into two subsets with equal sum?" Reduce to: "Is there a subset summing to `total // 2`?" That's a boolean 0/1 knapsack where weight = value = each element.

### 3. Unbounded Knapsack

Same as 0/1, but each item can be used **unlimited** times. The only change: iterate forwards in the space-optimized version (or reference `dp[i][w - weight[i]]` instead of `dp[i-1][w - weight[i]]`).

**Coin Change (LC 322)** and **Coin Change II (LC 518)** are unbounded knapsack in disguise — coins are items with unlimited supply.

### 4. Interleaving String (LC 97)

Given strings `s1`, `s2`, `s3` — can `s3` be formed by interleaving `s1` and `s2`?

**State:** `dp[i][j]` = can we form `s3[0:i+j]` using `s1[0:i]` and `s2[0:j]`?

```
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
```

**Why it's 2D:** you need to track how much of each source string you've consumed. A greedy approach fails because choosing from `s1` vs `s2` when both match affects future decisions.

### 5. State Machine DP — Stock Problems

Think of yourself as a **state machine** transitioning between states each day. The states (hold stock, don't hold stock, in cooldown, transactions used) define your DP dimensions.

| Problem | LC# | States | Key Constraint |
|---------|-----|--------|---------------|
| Best Time to Buy and Sell Stock | 121 | One transaction max | Just track min price |
| Buy and Sell Stock II | 122 | Unlimited transactions | hold / not-hold |
| Buy and Sell Stock III | 123 | At most 2 transactions | hold / not-hold × 2 transactions |
| Buy and Sell Stock IV | 188 | At most k transactions | hold / not-hold × k transactions |
| With Cooldown | 309 | Cooldown after sell | hold / not-hold / cooldown |
| With Transaction Fee | 714 | Fee on each sell | hold / not-hold, subtract fee on sell |

**The general framework:** on each day, for each state, compute the best profit by considering all valid transitions.

```
hold[i]     = max(hold[i-1], not_hold[i-1] - price[i])   # keep holding or buy
not_hold[i] = max(not_hold[i-1], hold[i-1] + price[i])   # keep idle or sell
```

**With cooldown:** add a third state. After selling, you must wait one day.

```
hold[i]     = max(hold[i-1], cooldown[i-1] - price[i])
not_hold[i] = max(not_hold[i-1], hold[i-1] + price[i])
cooldown[i] = not_hold[i-1]
```

**With k transactions:** add a transaction counter dimension. `hold[i][j]` = best profit on day `i` holding stock with `j` transactions used.

## Key Patterns & Templates

### Grid DP Template

```python
def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    
    # Base case: first row is cumulative sum
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    
    for i in range(1, m):
        dp[0] += grid[i][0]  # first column: can only come from above
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j - 1])  # min(above, left)
    
    return dp[-1]
# Time: O(m * n) | Space: O(n)
```

### 0/1 Knapsack Template (Space-Optimized)

```python
def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    
    for w, v in zip(weights, values):
        # BACKWARDS to avoid reusing the same item
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    
    return dp[capacity]
# Time: O(n * capacity) | Space: O(capacity)
```

**Boolean variant — Partition Equal Subset Sum (LC 416):**

```python
def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for t in range(target, num - 1, -1):  # backwards!
            dp[t] = dp[t] or dp[t - num]
    
    return dp[target]
# Time: O(n * target) | Space: O(target)
```

### Stock Buy/Sell State Machine Template

```python
def max_profit_with_cooldown(prices: list[int]) -> int:
    # States: hold (have stock), sold (just sold), idle (no stock, not in cooldown)
    hold = -prices[0]
    sold = 0
    idle = 0
    
    for price in prices[1:]:
        prev_hold = hold
        hold = max(hold, idle - price)      # keep holding or buy from idle
        idle = max(idle, sold)               # keep idle or come out of cooldown
        sold = prev_hold + price             # sell what we held
    
    return max(sold, idle)  # can't end holding stock
# Time: O(n) | Space: O(1)
```

**With k transactions (LC 188):**

```python
def max_profit_k_transactions(k: int, prices: list[int]) -> int:
    if not prices:
        return 0
    
    # If k >= n//2, unlimited transactions (same as LC 122)
    n = len(prices)
    if k >= n // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
    
    # hold[j] = best profit holding stock with j transactions used
    # sold[j] = best profit not holding stock with j transactions used
    hold = [-float('inf')] * (k + 1)
    sold = [0] * (k + 1)
    
    for price in prices:
        for j in range(1, k + 1):
            hold[j] = max(hold[j], sold[j - 1] - price)  # buy uses a transaction
            sold[j] = max(sold[j], hold[j] + price)       # sell
    
    return max(sold)
# Time: O(n * k) | Space: O(k)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Unique Paths | 62 | Medium | Pure grid DP. First row/col all 1s. Space-optimize to 1D array. |
| Unique Paths II | 63 | Medium | Same as 62 but set `dp = 0` at obstacles. Watch the base case — obstacle in first row blocks everything after it. |
| Minimum Path Sum | 64 | Medium | Grid DP with `min` instead of `+`. Good template problem. |
| Partition Equal Subset Sum | 416 | Medium | Reduce to "does a subset sum to total/2?" — that's boolean 0/1 knapsack. |
| Target Sum | 494 | Medium | Reduce to subset sum: find subset summing to `(total + target) / 2`. |
| Interleaving String | 97 | Medium | 2D boolean DP. State = how much of s1 and s2 consumed. Greedy fails. |
| Best Time to Buy and Sell Stock III | 123 | Hard | State machine with 2 transactions. Track hold/sold for each transaction. |
| Best Time to Buy and Sell Stock IV | 188 | Hard | Generalize III to k transactions. Optimize: if k ≥ n/2, treat as unlimited. |
| Best Time to Buy and Sell Stock with Cooldown | 309 | Medium | Three states: hold, sold, idle. `idle` handles the 1-day cooldown. |

## Common Mistakes

- **0/1 knapsack iterating forwards instead of backwards** — this silently reuses items, turning it into unbounded knapsack. Your answer will be too high and you won't know why. Always iterate capacity **backwards** for 0/1 problems.
- **Wrong state definition** — too many dimensions causes TLE (e.g., tracking unnecessary info), too few gives wrong answers (e.g., forgetting the cooldown state in stock problems). Ask: "What's the minimum info I need to make the next decision?"
- **Forgetting obstacles block the entire base case row/column** — in Unique Paths II, if `grid[0][3]` is an obstacle, then `dp[0][3]` through `dp[0][n-1]` are all 0, not 1.
- **Off-by-one in grid DP** — mixing up 0-indexed grid with 1-indexed DP table. Stick with 0-indexed for both in Python.
- **Not handling the `k ≥ n/2` optimization in Stock IV** — without it, creating a `k × n` table when `k = 10^9` causes MLE. When `k` is large enough, it's just the unlimited case.

## Interview Questions

1. **Unique Paths (LC 62):** How many ways to go from top-left to bottom-right moving only right/down? Can you do it in O(n) space?
2. **Minimum Path Sum (LC 64):** Find the path from top-left to bottom-right with minimum sum. What changes from Unique Paths?
3. **Partition Equal Subset Sum (LC 416):** Can you partition an array into two subsets with equal sum? How does this reduce to knapsack?
4. **Target Sum (LC 494):** Assign `+` or `-` to each number to reach a target. What's the knapsack reduction?
5. **Best Time to Buy and Sell Stock with Cooldown (LC 309):** What states do you need? Draw the state machine transitions.
6. **Best Time to Buy and Sell Stock IV (LC 188):** Handle at most `k` transactions. What's the edge case when `k` is very large?
7. **Interleaving String (LC 97):** Why can't you solve this greedily? What are the two dimensions of your DP?
8. **Unique Paths II (LC 63):** How do obstacles change your base case initialization?
9. Explain why 0/1 knapsack iterates backwards but unbounded knapsack iterates forwards in the space-optimized version.
10. You have a 2D DP with `O(m × n)` space. Walk me through how you'd optimize it to `O(n)`.

## Quick Reference

```
┌─────────────────────────────────────────────────────────┐
│              2D DP Decision Flowchart                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Grid with paths/costs?                                 │
│    → Grid DP: dp[i][j] = f(dp[i-1][j], dp[i][j-1])   │
│    → Space: O(n) with rolling 1D array                  │
│                                                         │
│  Pick items with capacity limit?                        │
│    → Each item once? → 0/1 Knapsack (backwards)        │
│    → Items reusable? → Unbounded Knapsack (forwards)   │
│    → Space: O(capacity)                                 │
│                                                         │
│  Buy/sell with constraints?                             │
│    → State Machine DP                                   │
│    → States: hold, not-hold, [cooldown], [txn count]   │
│    → Space: O(states) = O(1) or O(k)                   │
│                                                         │
│  Can string be formed by interleaving two others?       │
│    → 2D boolean DP on (i, j) = chars consumed          │
│    → Space: O(n) with rolling row                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

| Pattern | Time | Space (Optimized) |
|---------|------|-------------------|
| Grid DP (m × n) | O(m·n) | O(n) |
| 0/1 Knapsack | O(n·W) | O(W) |
| Unbounded Knapsack | O(n·W) | O(W) |
| Partition Subset Sum | O(n·sum) | O(sum) |
| Stock with k txns | O(n·k) | O(k) |
| Stock with cooldown | O(n) | O(1) |
| Interleaving String | O(m·n) | O(n) |

**The Golden Rule of Space Optimization:**
- 0/1 (use once) → iterate capacity **backwards**
- Unbounded (reuse) → iterate capacity **forwards**
- Grid → rolling 1D array, iterate **left to right**
