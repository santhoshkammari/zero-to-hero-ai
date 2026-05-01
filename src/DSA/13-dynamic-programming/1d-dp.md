# 1D Dynamic Programming

> Half of all DP interview problems have a single-dimension state — master these patterns and you unlock the rest.

## Core Idea

In **1D DP**, the state depends on a single variable — usually an index `i` or an amount `a`. You build a `dp` array where each entry answers: "What's the optimal answer considering elements up to index `i`?" or "What's the answer for target value `a`?" Every problem boils down to defining that state, writing the recurrence, and nailing the base cases.

Think of it like filling in a row of dominoes — each one depends on the few before it.

## What You Need to Know

### The Two Requirements for DP

Your problem needs **both** of these or DP is the wrong tool:

| Requirement | What It Means | Example |
|---|---|---|
| **Optimal substructure** | Best solution to the whole uses best solutions to parts | Max robbery of houses 1..n uses max robbery of 1..n-1 or 1..n-2 |
| **Overlapping subproblems** | Same subproblems get solved repeatedly | `fib(5)` calls `fib(3)` twice in naive recursion |

### Top-Down vs Bottom-Up

| | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|---|---|---|
| **Approach** | Recursion + cache | Iterative, fill array left-to-right |
| **Pros** | Only solves needed subproblems; easier to write | No recursion overhead; easier to space-optimize |
| **Cons** | Stack overflow risk on deep inputs | Must determine correct fill order |
| **Interview default** | Quick prototype | What you should present as final |

### Space Optimization

Most 1D DP only looks back 1–2 steps. That means you can replace the whole array with 2–3 variables and drop space from O(n) to **O(1)**.

```python
# Before: O(n) space
dp = [0] * n
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

# After: O(1) space — just track prev two values
prev2, prev1 = dp[0], dp[1]
for i in range(2, n):
    curr = max(prev1, prev2 + nums[i])
    prev2, prev1 = prev1, curr
```

## Key Patterns & Templates

### 1. Include/Exclude Pattern (House Robber)

The backbone of 1D DP. At every element you ask: **take it or skip it?**

**Recurrence:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

- Skip element `i` → best answer is `dp[i-1]`
- Take element `i` → its value + best from two back `dp[i-2]` (because adjacent is forbidden)

```python
def rob(nums: list[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    return prev1
```

**Time: O(n) | Space: O(1)**

For **House Robber II (LC 213)** — circular arrangement — run the same logic twice: once on `nums[1:]`, once on `nums[:-1]`, take the max. Breaking the circle into two linear problems eliminates the first-last adjacency conflict.

```python
def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))
```

### 2. Coin Change (Unbounded Knapsack)

**State:** `dp[a]` = minimum coins to make amount `a`.

**Recurrence:** `dp[a] = min(dp[a - coin] + 1)` for each coin that fits.

Why initialize to `amount + 1`? It's a sentinel — any real solution uses at most `amount` coins (all 1s), so `amount + 1` means "impossible." Using `float('inf')` also works but `amount + 1` keeps it as an int.

```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1
```

**Time: O(amount × len(coins)) | Space: O(amount)**

### 3. Coin Change II — Counting Combinations

**⚠️ CRITICAL: Loop order determines combinations vs permutations.**

| Outer Loop | Inner Loop | Counts |
|---|---|---|
| **Coins** | Amounts | **Combinations** (order doesn't matter) ✅ |
| Amounts | Coins | Permutations (order matters) ❌ for this problem |

Why? When coins are in the outer loop, each coin is "introduced" once. You process all amounts using coin `c` before ever considering coin `c+1`. This prevents counting `[1,2]` and `[2,1]` as different.

```python
def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0: use no coins
    for coin in coins:            # outer: coins
        for a in range(coin, amount + 1):  # inner: amounts
            dp[a] += dp[a - coin]
    return dp[amount]
```

**Time: O(amount × len(coins)) | Space: O(amount)**

### 4. Decode Ways

**State:** `dp[i]` = number of ways to decode `s[:i]`.

At each position, check: can the last 1 digit form a valid letter (1–9)? Can the last 2 digits (10–26)?

```python
def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    prev2, prev1 = 1, 1  # dp[0]=1 (empty prefix), dp[1]=1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != '0':             # single digit valid
            curr += prev1
        two = int(s[i-1:i+1])
        if 10 <= two <= 26:          # two digits valid
            curr += prev2
        prev2, prev1 = prev1, curr
    return prev1
```

**Time: O(n) | Space: O(1)**

### 5. Word Break

**State:** `dp[i]` = can we segment `s[:i]` using the dictionary?

For every `i`, try every possible last word: check all `j < i` where `dp[j]` is True and `s[j:i]` is in the word set. You're asking: "Is there a valid segmentation up to position `j`, followed by a dictionary word that lands exactly at position `i`?"

```python
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is valid
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break  # no need to check further
    return dp[n]
```

**Time: O(n² × k)** where k = average word length for substring hashing | **Space: O(n)**

**Optimization:** Instead of checking all `j`, only check `j` values where `i - j` ≤ max word length:

```python
def word_break_optimized(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    max_len = max(len(w) for w in words) if words else 0
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
```

### 6. Longest Increasing Subsequence (LIS)

#### O(n²) DP

**State:** `dp[i]` = length of LIS ending at index `i`.

For each `i`, look at all `j < i`. If `nums[j] < nums[i]`, we can extend that subsequence.

```python
def length_of_lis(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n  # every element is a subsequence of length 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

**Time: O(n²) | Space: O(n)**

#### O(n log n) Patience Sort — The Google-Expected Approach

Maintain a `tails` array where `tails[k]` = smallest tail element of any increasing subsequence of length `k+1`. For each number, binary search for its position in `tails`:

- If it's larger than all tails → append (extends the longest subsequence)
- Otherwise → replace the first tail ≥ it (keeps tails as small as possible for future extension)

The length of `tails` *is* the LIS length. Think of it like patience sorting (the card game Solitaire): you're trying to keep pile tops as low as possible.

```python
from bisect import bisect_left

def length_of_lis_fast(nums: list[int]) -> int:
    tails = []
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

**Time: O(n log n) | Space: O(n)**

> **Note:** `tails` is NOT the actual LIS — it's a tool for computing LIS *length*. To reconstruct the actual subsequence, track parent pointers.

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|------------|-------------|
| Climbing Stairs | 70 | Easy | `dp[i] = dp[i-1] + dp[i-2]` — Fibonacci in disguise |
| House Robber | 198 | Medium | Include/exclude: rob this house + two-back, or skip |
| House Robber II | 213 | Medium | Circular → run linear twice excluding first/last |
| Coin Change | 322 | Medium | Unbounded knapsack; BFS also works but DP is cleaner |
| Coin Change II | 518 | Medium | **Loop order!** Coins outer = combinations |
| Decode Ways | 91 | Medium | Check last 1 and 2 digits; handle '0' carefully |
| Word Break | 139 | Medium | DP + set lookup; try every possible last word |
| Longest Increasing Subsequence | 300 | Medium | Know both O(n²) and O(n log n); Google expects the fast one |

## Common Mistakes

- **Coin Change II loop order:** Putting coins in the inner loop counts permutations `[1,2]` and `[2,1]` as different. Coins must be the **outer** loop for combinations. Draw out a small example if you forget.
- **LIS: only knowing O(n²):** At Google-level interviews, O(n²) gets a "can you do better?" The O(n log n) patience sort approach is expected. Practice it until `bisect_left` is muscle memory.
- **Wrong state definition:** If your DP has too many dimensions you'll TLE; too few and you'll get wrong answers. Ask yourself: "What's the minimum information I need to make a decision at step `i`?"
- **Forgetting base cases:** `dp[0]` is almost always a special case. For Coin Change it's `0`, for Decode Ways it's `1` (empty string has one decoding), for Word Break it's `True`. Get this wrong and everything cascades.
- **Not space-optimizing when asked:** If the recurrence only looks back 1–2 steps, the interviewer expects you to mention (and ideally implement) the O(1) space version. It's free points.

## Interview Questions

1. **Conceptual:** "When would top-down memoization be better than bottom-up tabulation?" → When only a sparse subset of states is reachable (e.g., Word Break with a short dictionary).
2. **House Robber follow-up:** "What if houses are in a circle?" → Run linear DP twice, excluding first and last house respectively. (LC 213)
3. **Coin Change:** "Why does BFS also work for minimum coins?" → Each BFS level = one more coin used. First time you hit the target amount = minimum coins. DP is more standard though.
4. **Coin Change II:** "Explain why loop order matters for counting combinations vs permutations." → Draw the table: coins outer means each coin is introduced once across all amounts.
5. **Word Break:** "How would you return all valid segmentations, not just true/false?" → Backtracking with memoization (LC 140). DP alone finds if it's possible; DFS reconstructs paths.
6. **LIS:** "Walk me through the patience sort approach. Why does binary search work here?" → `tails` maintains the smallest possible ending value for each subsequence length. Binary search finds where a new number fits.
7. **LIS follow-up:** "How do you reconstruct the actual subsequence, not just its length?" → Track parent indices alongside the tails array, then backtrack.
8. **General:** "How do you decide if a problem is 1D DP vs 2D DP?" → Count how many independent variables define a subproblem. One index or one target → 1D. Two strings, a grid, or index + capacity → 2D.
9. **Decode Ways:** "How do you handle strings with leading zeros like '06'?" → `s[i] == '0'` means that digit can't stand alone; it must pair with the previous digit (and `10 ≤ pair ≤ 26`), otherwise it's an invalid encoding.
10. **Space optimization:** "This DP uses O(n) space. Can you do better?" → If the recurrence only references `dp[i-1]` and `dp[i-2]`, replace the array with two variables.

## Quick Reference

### Decision Flowchart

```
Is the state a single variable (index, amount, length)?
├── YES → 1D DP
│   ├── "Take or skip adjacent?" → Include/Exclude (House Robber)
│   ├── "Min/max using unlimited items?" → Unbounded Knapsack (Coin Change)
│   ├── "Count ways with unlimited items?" → Unbounded Knapsack (Coin Change II — watch loop order!)
│   ├── "Can we segment/partition a string?" → Word Break pattern
│   └── "Longest increasing/decreasing?" → LIS (use O(n log n))
└── NO → Consider 2D DP or other approaches
```

### Complexity Table

| Problem | Time | Space | Space (Optimized) |
|---------|------|-------|--------------------|
| House Robber | O(n) | O(n) | O(1) |
| House Robber II | O(n) | O(n) | O(1) |
| Coin Change | O(n × c) | O(n) | — |
| Coin Change II | O(n × c) | O(n) | — |
| Decode Ways | O(n) | O(n) | O(1) |
| Word Break | O(n² × k) | O(n) | — |
| LIS (DP) | O(n²) | O(n) | — |
| LIS (Patience Sort) | O(n log n) | O(n) | — |

*n = input size or target amount, c = number of coins, k = avg word length for hashing*

### Key Recurrences at a Glance

```
House Robber:    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
Coin Change:     dp[a] = min(dp[a - coin] + 1) for each coin
Coin Change II:  dp[a] += dp[a - coin]          (coins in OUTER loop)
Decode Ways:     dp[i] = (dp[i-1] if valid_1) + (dp[i-2] if valid_2)
Word Break:      dp[i] = any(dp[j] and s[j:i] in words for j < i)
LIS:             dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
```
