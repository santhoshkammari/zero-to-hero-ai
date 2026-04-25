# Dynamic Programming Fundamentals

> DP is the single most tested topic at Google/Amazon/Microsoft — and the mental model you build here determines whether you solve DP problems in 20 minutes or stare blankly for 45.

## Core Idea

Dynamic programming is just **recursion without redundant work**. If a problem has **optimal substructure** (optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems get solved repeatedly), you can store results instead of recomputing them. That's it — everything else is technique.

Think of it like filling out a spreadsheet: each cell depends on other cells, you figure out the formula (recurrence), fill in the obvious cells first (base cases), then compute the rest in order.

## What You Need to Know

### The Two Requirements for DP

| Requirement | What It Means | Example |
|---|---|---|
| **Optimal substructure** | The best answer to the whole problem uses the best answers to smaller pieces | Shortest path: best path A→C through B uses best A→B + best B→C |
| **Overlapping subproblems** | The same smaller pieces appear again and again in the recursion tree | `fib(5)` calls `fib(3)` twice, `fib(2)` three times |

If you only have optimal substructure but no overlap, that's **divide and conquer** (merge sort). If you don't have optimal substructure, DP won't work — consider greedy or exhaustive search.

### Top-Down (Memoization) vs Bottom-Up (Tabulation)

| | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|---|---|---|
| **Approach** | Recursive + cache results | Iterative, fill table from base cases up |
| **Time** | Same | Same |
| **Space** | Call stack + cache | Table only (no stack overhead) |
| **Pros** | Only computes needed subproblems; natural to write from recurrence | No recursion limit; easier to space-optimize |
| **Cons** | Python recursion limit (~1000); function call overhead | Must figure out fill order; computes all subproblems even if unneeded |
| **When to use** | Problem has sparse subproblem space; prototyping your recurrence quickly | Need max performance; want to optimize space; problem has dense subproblem space |

**Practical rule:** Start top-down in interviews (faster to write, fewer bugs), then optimize to bottom-up if asked.

### State Definition — The Hardest Part

The **state** is the minimal set of information that uniquely identifies a subproblem. Getting this right is 80% of solving a DP problem.

Ask yourself: **"What do I need to know at this point to make the optimal decision?"**

- Too few dimensions → wrong answers (you're conflating distinct subproblems)
- Too many dimensions → TLE or MLE (your state space is too large)

Examples of state definitions:

| Problem | State | Why |
|---|---|---|
| Climbing Stairs (LC 70) | `dp[i]` = ways to reach step `i` | Position is the only thing that matters |
| Min Cost Climbing Stairs (LC 746) | `dp[i]` = min cost to reach step `i` | Position determines future cost |
| House Robber (LC 198) | `dp[i]` = max money robbing from houses `0..i` | Which house you're at determines what's available |
| 0/1 Knapsack | `dp[i][w]` = max value using items `0..i` with capacity `w` | Need both item index AND remaining capacity |

### The Transition (Recurrence Relation)

The **recurrence** defines how a subproblem's answer is built from smaller subproblems. This is the "formula" in your spreadsheet.

Pattern: **at each state, enumerate your choices and pick the best.**

```
dp[current_state] = best(dp[previous_state] + cost_of_choice for each valid choice)
```

Where `best` is `min`, `max`, `sum`, etc. depending on what you're optimizing.

### Base Cases

**Base cases** are subproblems with trivially known answers — they're where recursion bottoms out and where table-filling starts. Getting these wrong silently corrupts everything above.

**How to find them:** ask "what's the smallest/simplest version of this problem where I know the answer without thinking?"

### Space Optimization

Key insight: if `dp[i]` only depends on `dp[i-1]` (or a fixed window of previous rows), you don't need the whole table.

| Dependency Pattern | Full Space | Optimized Space |
|---|---|---|
| `dp[i]` depends on `dp[i-1]` only | O(n) | O(1) — two variables |
| `dp[i]` depends on `dp[i-1]` and `dp[i-2]` | O(n) | O(1) — two/three variables |
| `dp[i][j]` depends on `dp[i-1][...]` | O(n×m) | O(m) — single row |
| `dp[i][j]` depends on `dp[i-1][j]` and `dp[i][j-1]` | O(n×m) | O(m) — single row, fill left-to-right |

## Key Patterns & Templates

### The 5-Step DP Framework

Every DP problem follows this recipe:

1. **Define state:** What does `dp[i]` (or `dp[i][j]`) represent?
2. **Recurrence:** How does `dp[i]` relate to smaller subproblems?
3. **Base case:** What are the trivially known values?
4. **Fill order:** In what order do you fill the table?
5. **Answer:** Where in the table is your final answer?

### Running Example: Climbing Stairs (LC 70)

> You can climb 1 or 2 steps at a time. How many distinct ways to reach step `n`?

Applying the framework:

1. **State:** `dp[i]` = number of ways to reach step `i`
2. **Recurrence:** `dp[i] = dp[i-1] + dp[i-2]` (you came from one step below OR two steps below)
3. **Base case:** `dp[0] = 1` (one way to stand at ground), `dp[1] = 1` (one way to reach step 1)
4. **Fill order:** Left to right, `i = 2, 3, ..., n`
5. **Answer:** `dp[n]`

Yes — this is literally Fibonacci.

### Top-Down Template (Memoization)

```python
from functools import lru_cache

def climb_stairs_topdown(n: int) -> int:
    @lru_cache(maxsize=None)
    def dp(i):
        if i <= 1:
            return 1
        return dp(i - 1) + dp(i - 2)
    return dp(n)
```

**Time:** O(n) — each state computed once  
**Space:** O(n) — cache + call stack

### Bottom-Up Template (Tabulation)

```python
def climb_stairs_bottomup(n: int) -> int:
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Time:** O(n)  
**Space:** O(n)

### Space-Optimized Template

Since `dp[i]` only needs `dp[i-1]` and `dp[i-2]`, just keep two variables:

```python
def climb_stairs_optimized(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
```

**Time:** O(n)  
**Space:** O(1)

### Generic Memoization Template

```python
from functools import lru_cache

def solve(params):
    @lru_cache(maxsize=None)
    def dp(state):
        # 1. Base case
        if is_base_case(state):
            return base_value

        # 2. Try all choices, pick the best
        result = initial_value  # float('inf') for min, -float('inf') for max, 0 for count
        for choice in get_choices(state):
            next_state = transition(state, choice)
            result = combine(result, dp(next_state) + cost(choice))

        return result

    return dp(initial_state)
```

### Generic Tabulation Template

```python
def solve(params):
    n = len(params)
    dp = [initial_value] * (n + 1)

    # 1. Base cases
    dp[0] = base_value

    # 2. Fill table in dependency order
    for i in range(1, n + 1):
        for choice in get_choices(i):
            dp[i] = combine(dp[i], dp[prev(i, choice)] + cost(choice))

    # 3. Answer
    return dp[n]
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---|---|---|---|
| Fibonacci Number | 509 | Easy | Pure intro — recursion → memo → tabulation → O(1) space. Master all four forms |
| Climbing Stairs | 70 | Easy | Same as Fibonacci but framed as a counting problem. The gateway DP problem |
| Min Cost Climbing Stairs | 746 | Easy | First "optimization" DP (minimize cost). `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` |
| N-th Tribonacci Number | 1137 | Easy | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`. Practice space optimization with 3 variables |
| House Robber | 198 | Medium | First "take or skip" DP: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Builds intuition for knapsack |
| Maximum Subarray | 53 | Medium | DP view of Kadane's: `dp[i] = max(nums[i], dp[i-1] + nums[i])`. Do you extend or restart? |
| Decode Ways | 91 | Medium | State transition has **conditional** branches — great for practicing careful case analysis |

## Common Mistakes

- **Wrong state definition** — too many dimensions and you TLE, too few and your answer is flat-out wrong. Ask: "can two different situations at this state lead to different optimal futures?" If yes, you need more dimensions.
- **Wrong base cases** — off-by-one on `dp[0]` vs `dp[1]` silently breaks everything. Always verify by hand with the smallest inputs (n=0, n=1, n=2).
- **Top-down without memoization** — writing the recursion but forgetting `@lru_cache`. Congrats, you just wrote brute-force O(2ⁿ). Interviewers notice.
- **Bottom-up in wrong fill order** — if `dp[i]` depends on `dp[i+1]`, you need to iterate right-to-left. Fill order must respect dependencies.
- **Premature space optimization** — get the O(n) or O(n×m) solution working first. Optimize only after correctness is confirmed. Interviewers prefer correct-then-optimize over clever-but-broken.

## Interview Questions

1. **"What are the two properties a problem must have for DP to apply?"** — Optimal substructure and overlapping subproblems. Explain both with an example.
2. **"Walk me through your approach to Climbing Stairs."** — Define state, write recurrence, set base cases, optimize space. Hit all 5 framework steps.
3. **"Why is naive recursive Fibonacci O(2ⁿ)? How does memoization make it O(n)?"** — The recursion tree has 2ⁿ nodes because of repeated work. Memo ensures each of the n subproblems is computed exactly once.
4. **"When would you prefer top-down over bottom-up?"** — Sparse subproblem space (not all states reachable), faster to code, and when recursion depth isn't an issue.
5. **"How do you determine the state for a DP problem?"** — Identify what changes between decisions. What minimal info do you need to make the optimal next choice? Common signals: index, remaining capacity, boolean flags.
6. **"Optimize Climbing Stairs to O(1) space."** — Only the last two values are needed. Replace array with two variables.
7. **"What goes wrong if your base case is off by one?"** — Every value in the table is built on base cases. A wrong base case propagates errors through the entire table. Show with a small example.
8. **"How do you decide fill order in bottom-up DP?"** — Look at the recurrence: if `dp[i]` depends on smaller indices, go left-to-right. If it depends on larger indices, go right-to-left. Draw the dependency arrows.

## Quick Reference

### The 5-Step Framework (Cheat Sheet)

```
1. STATE    → dp[?] = "what does this represent in English?"
2. RECURRENCE → dp[i] = f(dp[smaller subproblems])
3. BASE CASE  → dp[0] = ?, dp[1] = ?  (verify with tiny inputs)
4. ORDER      → follow dependency arrows (small → large, usually)
5. ANSWER     → dp[n], dp[n-1], max(dp), depends on problem
```

### Complexity Quick-Check

| Approach | Time | Space |
|---|---|---|
| Brute-force recursion (no memo) | O(2ⁿ) or worse | O(n) call stack |
| Top-down with memoization | O(number of states × work per state) | O(number of states) |
| Bottom-up tabulation | Same as memoized | O(number of states) |
| Space-optimized bottom-up | Same | Depends on dependency window |

### Decision Flowchart

```
Is the problem asking for min/max/count of something?
  └─ Yes → Can you define subproblems with optimal substructure?
              └─ Yes → Are subproblems overlapping?
                         └─ Yes → ✅ USE DP
                         └─ No  → Use divide and conquer
              └─ No  → Consider greedy or brute-force
  └─ No  → Probably not DP (but check — "is it possible?" can be DP too)
```

### Common Recurrence Patterns

| Pattern | Recurrence | Example |
|---|---|---|
| **Linear count** | `dp[i] = dp[i-1] + dp[i-2]` | Climbing Stairs (LC 70) |
| **Linear min/max** | `dp[i] = min(dp[i-1], dp[i-2]) + cost[i]` | Min Cost Climbing Stairs (LC 746) |
| **Take or skip** | `dp[i] = max(dp[i-1], dp[i-2] + val[i])` | House Robber (LC 198) |
| **Extend or restart** | `dp[i] = max(nums[i], dp[i-1] + nums[i])` | Maximum Subarray (LC 53) |
