# Greedy Algorithms

> Greedy = make the locally optimal choice at each step and never look back. When it works, it's elegant and fast. When it doesn't, you get wrong answers.

## Core Idea

A **greedy algorithm** makes the best-looking choice at each step without reconsidering past decisions. It works when the problem has the **greedy choice property** (a locally optimal choice leads to a globally optimal solution) and **optimal substructure**. The challenge: recognizing *when* greedy is correct — and being ready to prove it or switch to DP when it's not.

## What You Need to Know

### Greedy vs DP

| | Greedy | Dynamic Programming |
|---|---|---|
| Considers | One option (the "best" right now) | All options |
| Backtracks | Never | Implicitly (via subproblems) |
| Proof | Need exchange argument or greedy stays ahead | Optimal substructure + overlapping subproblems |
| Speed | Usually O(n) or O(n log n) | Usually O(n²) or O(n·k) |
| Use when | Locally optimal = globally optimal | Need to explore all possibilities |

**Rule of thumb:** If you can prove "choosing the best now never hurts the future," it's greedy. If choosing now affects future options in complex ways, it's DP.

### Common Greedy Strategies

| Strategy | Example | Why It Works |
|----------|---------|--------------|
| **Sort + greedily assign** | Activity selection, intervals | Sorting reveals optimal order |
| **Track running max/min** | Jump Game, Best Time to Buy Stock | One pass, accumulate |
| **Frequency-based** | Task Scheduler, Reorganize String | Handle most constrained first |
| **Two pointers greedy** | Container With Most Water | Move the bottleneck pointer |
| **Net gain analysis** | Gas Station | If total gain ≥ 0, solution exists |

## Key Patterns & Templates

### Jump Game (LC 55)

"Can you reach the last index?" — track the farthest reachable position.

```python
def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True
```

**O(n) time, O(1) space.** You don't simulate jumps — just track how far you *could* go.

### Jump Game II (LC 45)

"Minimum jumps to reach end" — implicit BFS by levels.

```python
def jump(nums):
    jumps = 0
    current_end = 0   # end of current BFS "level"
    farthest = 0      # farthest reachable from this level
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

**O(n) time, O(1) space.** Each "level" is the range of indices reachable with the current number of jumps.

### Non-overlapping Intervals (LC 435) — Activity Selection

"Minimum intervals to remove so none overlap" = "Maximum non-overlapping intervals to keep."

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by END time
    count = 0
    prev_end = float('-inf')
    
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end  # keep this interval
        else:
            count += 1      # remove (overlaps)
    return count
```

**Why sort by end time?** Choosing the earliest-ending interval leaves maximum room for future intervals. This is the classic **exchange argument** proof.

### Gas Station (LC 134)

"Find the starting station to complete a circular route."

```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1  # impossible
    
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1  # can't start from anywhere before i+1
            tank = 0
    return start
```

**The insight:** If you can't reach station j from station i, then no station between i and j works either — so jump start to j+1.

### Task Scheduler (LC 621)

"Minimum time to execute all tasks with cooldown n between same tasks."

```python
def leastInterval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    count_max = sum(1 for f in freq.values() if f == max_freq)
    
    # Formula: (max_freq - 1) groups of (n + 1) slots + final group
    result = (max_freq - 1) * (n + 1) + count_max
    return max(result, len(tasks))  # at minimum, we need len(tasks) time
```

**Why it works:** The most frequent task creates the "skeleton" — gaps between its executions must be filled. If there are enough tasks to fill all gaps, the answer is just `len(tasks)`.

### Partition Labels (LC 763)

"Partition string so each letter appears in at most one part."

```python
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    partitions = []
    start = end = 0
    
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
    return partitions
```

**The greedy idea:** for each character, the partition must extend to its last occurrence. Keep extending until current index == partition end.

### Merge Intervals (LC 56)

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Jump Game | 55 | Medium | Track farthest reachable, O(n) one pass |
| Jump Game II | 45 | Medium | Implicit BFS levels, count level transitions |
| Non-overlapping Intervals | 435 | Medium | Sort by end time, activity selection |
| Merge Intervals | 56 | Medium | Sort by start, merge overlapping |
| Gas Station | 134 | Medium | If total gas ≥ cost, solution exists; reset on deficit |
| Task Scheduler | 621 | Medium | Most frequent task sets the skeleton |
| Partition Labels | 763 | Medium | Extend partition to last occurrence of each char |
| Meeting Rooms II | 253 | Medium | Sweep line or sort starts/ends separately |

## Common Mistakes

- **Applying greedy when DP is needed** — if you can't prove the greedy choice property, it's probably DP. Example: 0/1 Knapsack is NOT greedy (fractional knapsack is).
- **Sorting by the wrong key** — intervals by start vs end produces different algorithms. Non-overlapping intervals needs sort by *end*; merge intervals needs sort by *start*.
- **Jump Game II: trying DP** → O(n²) instead of O(n) greedy. The BFS-level approach is the intended solution.
- **Gas Station: brute-forcing from each station** — O(n²). The key insight (skip all stations between i and j) gives O(n).
- **Not handling edge cases** — empty arrays, single elements, all intervals identical

## Interview Questions

- "Can you reach the last index given jump lengths?" (LC 55)
- "What's the minimum number of jumps to reach the end?" (LC 45)
- "Find the minimum number of intervals to remove to eliminate all overlaps." (LC 435 — prove your greedy is correct)
- "Given tasks with cooldown, what's the minimum execution time?" (LC 621 — Amazon/Microsoft)
- "Can you complete a circular route with gas stations?" (LC 134 — Amazon)
- "How would you prove a greedy algorithm is correct?" (Exchange argument or greedy stays ahead)
- "When does greedy fail? Give an example." (0/1 Knapsack: greedy by value/weight ratio fails)
- "Partition a string so each letter appears in at most one part." (LC 763)
- "How many meeting rooms do you need?" (LC 253 — sweep line or heap)
- "What's the difference between greedy and dynamic programming?"

## Quick Reference

```
Greedy works when:
  ✅ Locally optimal → globally optimal (provable)
  ✅ No need to reconsider past choices
  ✅ Problem has optimal substructure

Common greedy patterns:
  Intervals     → Sort by end (selection) or start (merge)
  Reachability  → Track farthest/running max
  Scheduling    → Handle most constrained first
  Net gain      → If total ≥ 0, solution exists
  Partitioning  → Extend to cover all constraints

Proof techniques:
  Exchange argument: "swapping greedy choice for any other ≠ better"
  Greedy stays ahead: "at each step, greedy ≥ any alternative"

Greedy FAILS:
  0/1 Knapsack, Coin Change (arbitrary denominations),
  Longest Increasing Subsequence, Edit Distance
  → Use DP instead
```
