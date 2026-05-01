# Binary Search on Answer

> When you're not searching an array but searching the *answer space* itself — this pattern unlocks 20+ LeetCode problems with one template.

## Core Idea

Instead of searching for a target in a data structure, you **binary search over all possible answers**. The key insight: if answer `x` is feasible, then all answers ≥ `x` (or ≤ `x`) are also feasible. This **monotonic property** lets you binary search. You define a `feasible(candidate)` function and binary search for the smallest (or largest) candidate that passes.

## What You Need to Know

### When to Recognize This Pattern

You'll see it whenever a problem asks you to **minimize the maximum** or **maximize the minimum** of something, and you can verify a candidate answer in O(n) or O(n log n).

| Signal in Problem Statement | Translation |
|-----------------------------|-------------|
| "Minimize the maximum X" | Binary search on X, find smallest feasible |
| "Maximize the minimum X" | Binary search on X, find largest feasible |
| "What's the minimum speed/capacity/time such that..." | Binary search on speed/capacity/time |
| "Can you do X within Y constraint?" | `Y` is fixed, binary search on `X` |

### The Template — O(n log S) where S = answer range

Every "search on answer" problem follows this exact structure:

```python
def search_on_answer(data, constraint):
    left, right = MIN_POSSIBLE, MAX_POSSIBLE
    
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid, data, constraint):
            right = mid  # mid works, but maybe something smaller works too
        else:
            left = mid + 1  # mid doesn't work, need larger
    
    return left  # smallest feasible answer
```

The **only thing that changes** between problems is:
1. The bounds (`left` and `right`)
2. The `feasible()` function

### The Three Steps

1. **Define the search space**: What are the minimum and maximum possible answers?
2. **Write the feasibility check**: Given candidate `mid`, can you satisfy the constraint?
3. **Binary search**: Find the boundary where feasible flips from False to True (or vice versa).

### Example 1: Koko Eating Bananas (LC 875) — O(n log m)

Koko eats bananas at speed `k`. For each pile, she takes `ceil(pile/k)` hours. Find minimum `k` to finish within `h` hours.

```python
import math

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        # Feasibility: can Koko finish at speed mid?
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            right = mid  # can do it, try slower
        else:
            left = mid + 1  # too slow
    
    return left
```

**Why it works**: If speed `k` finishes in time, any speed > `k` also finishes. Monotonic ✓

### Example 2: Capacity to Ship Packages (LC 1011) — O(n log S)

Ship packages in order within `days` days. Find minimum ship capacity.

```python
def ship_within_days(weights, days):
    left, right = max(weights), sum(weights)
    
    while left < right:
        mid = left + (right - left) // 2
        # Feasibility: can we ship with capacity mid?
        day_count, current_load = 1, 0
        for w in weights:
            if current_load + w > mid:
                day_count += 1
                current_load = 0
            current_load += w
        
        if day_count <= days:
            right = mid
        else:
            left = mid + 1
    
    return left
```

**Bounds**: `left = max(weights)` because capacity must hold the heaviest package. `right = sum(weights)` because that ships everything in 1 day.

### Example 3: Split Array Largest Sum (LC 410) — O(n log S)

Split array into `k` subarrays. Minimize the largest subarray sum.

```python
def split_array(nums, k):
    left, right = max(nums), sum(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        # Feasibility: can we split into ≤ k parts, each ≤ mid?
        splits, current_sum = 1, 0
        for num in nums:
            if current_sum + num > mid:
                splits += 1
                current_sum = 0
            current_sum += num
        
        if splits <= k:
            right = mid  # possible, try smaller max sum
        else:
            left = mid + 1  # too many splits needed
    
    return left
```

Notice how LC 410 and LC 1011 have **nearly identical** feasibility checks — the underlying greedy logic is the same.

### Example 4: Aggressive Cows / Magnetic Balls — O(n log D)

Place `k` cows in stalls to **maximize the minimum distance** between any two cows.

```python
def max_min_distance(positions, k):
    positions.sort()
    left, right = 1, positions[-1] - positions[0]
    
    while left < right:
        mid = left + (right - left + 1) // 2  # round UP for maximize
        # Feasibility: can we place k cows with min distance >= mid?
        count, last_pos = 1, positions[0]
        for pos in positions[1:]:
            if pos - last_pos >= mid:
                count += 1
                last_pos = pos
        
        if count >= k:
            left = mid  # can do it, try larger distance
        else:
            right = mid - 1  # too spread out
    
    return left
```

**⚠️ Note the difference**: When **maximizing**, use `left = mid` with `mid = left + (right - left + 1) // 2` (round up) to avoid infinite loops.

## Key Patterns & Templates

### Minimize Template (most common)

```python
# Find SMALLEST x where feasible(x) is True
left, right = lo, hi
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left
```

### Maximize Template

```python
# Find LARGEST x where feasible(x) is True
left, right = lo, hi
while left < right:
    mid = left + (right - left + 1) // 2  # round UP!
    if feasible(mid):
        left = mid
    else:
        right = mid - 1
return left
```

### Feasibility Check Cheat Sheet

| Problem | Bounds | Feasible(mid) |
|---------|--------|---------------|
| Koko Eating Bananas | `[1, max(piles)]` | `sum(ceil(p/mid)) <= h` |
| Ship Packages | `[max(w), sum(w)]` | Greedy pack: `days <= d` |
| Split Array Largest Sum | `[max(nums), sum(nums)]` | Greedy split: `parts <= k` |
| Aggressive Cows | `[1, max_pos - min_pos]` | Greedy place: `placed >= k` |
| Minimize Max Distance (gas) | `[0, max_gap]` | Insert stations: `total <= k` |

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Koko Eating Bananas | 875 | Medium | Gateway problem — search on speed, ceil division for hours |
| Capacity to Ship Packages | 1011 | Medium | Identical to Koko but with greedy packing feasibility |
| Split Array Largest Sum | 410 | Hard | Same greedy feasibility as Ship Packages — minimize max subarray |
| Magnetic Force Between Two Balls | 1552 | Medium | Maximize minimum distance — use the maximize template |
| Minimum Number of Days to Make Bouquets | 1482 | Medium | Search on days, check consecutive flowers bloomed |
| Find the Smallest Divisor | 1283 | Medium | Search on divisor, sum of `ceil(num/mid)` ≤ threshold |
| Minimized Maximum of Products Distributed | 2064 | Medium | Search on max products per store |

## Common Mistakes

- **Wrong bounds**: Too tight → miss the answer. Too loose → slower but still correct. When unsure, go loose (e.g., `left = 0, right = 10**9`).
- **Maximize vs Minimize confusion**: Minimize uses `right = mid`. Maximize uses `left = mid` with **round-up mid**. Mixing these causes infinite loops.
- **Feasibility check direction flipped**: If `feasible(mid)` means "mid is enough," then passing should shrink toward smaller (minimize) or larger (maximize). Think carefully about what "feasible" means.
- **Off-by-one on bounds**: For Koko, `left = 1` not `0` (can't eat 0 bananas/hour). For Ship, `left = max(weights)` not `0` (must fit the heaviest item).
- **Forgetting to handle edge cases**: Single-element arrays, `k = 1` (everything in one group), or `k = n` (each element alone).

## Interview Questions

- "Koko eats bananas at speed k. Find the minimum k to finish within h hours." (Meta/Amazon)
- "Split an array into k subarrays to minimize the maximum subarray sum. How?" (Google)
- "You have packages that must be shipped in order within d days. Find minimum ship capacity." (Amazon)
- "Place k objects to maximize the minimum distance between any two. Walk me through your approach."
- "How do you decide the search bounds for a binary search on answer problem?"
- "What makes a problem suitable for binary search on answer? What property must hold?"
- "Compare binary search on answer with DP for the Split Array problem. When would you choose which?"
- "Your feasibility check runs in O(n). What's the overall time complexity? Why?"

## Quick Reference

```
Binary Search on Answer Checklist:
──────────────────────────────────
1. Can I verify a candidate answer in O(n)?        → Yes? Use this pattern
2. Is the answer space monotonic?                   → If x works, does x+1 also work?
3. What are the bounds?                             → [smallest possible, largest possible]
4. Am I minimizing or maximizing?                   → Determines template choice

Complexity:  O(n × log(answer_range))
  n = cost of feasibility check
  answer_range = right - left

Template selector:
  MINIMIZE → right = mid,     mid rounds DOWN
  MAXIMIZE → left  = mid,     mid rounds UP

Same feasibility logic:
  LC 410 (Split Array) ≈ LC 1011 (Ship Packages) ≈ LC 1231 (Divide Chocolate)
```
