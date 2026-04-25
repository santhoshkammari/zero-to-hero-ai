# Sliding Window

> "Longest substring with..." or "minimum window containing..." = sliding window. Recognizing this pattern is half the battle.

## Core Idea

Maintain a window `[left, right]` that expands right to explore and shrinks left to maintain validity. Converts nested O(n²) into single-pass O(n) by never re-processing elements you've already seen.

**Why it works**: each element enters the window at most once (right pointer) and leaves at most once (left pointer) → O(2n) = O(n).

---

## What You Need to Know

- **Fixed-size window**: window size `k` is given. Slide by removing leftmost, adding rightmost. Example: max sum of subarray of size k.
- **Variable-size window**: window grows/shrinks based on a condition. Template: expand right → check condition → shrink left while invalid → record answer.
- **When to use hash map vs array**: fixed alphabet (lowercase English) → `[0]*26` is faster. Variable characters → use `Counter`/`dict`.
- **What goes inside the window**: `set` (for uniqueness), `Counter` (for frequency), running sum, etc.
- **Shrink condition**: depends on the problem. "At most K distinct" → shrink when `distinct > K`. "No repeating chars" → shrink when duplicate found.

---

## Key Patterns & Templates

### 1. Fixed-Size Window (Max Sum of Subarray of Size k)

```python
def max_sum_subarray(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]  # add right, remove leftmost
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 2. Variable-Size Window (General Template)

```python
def variable_window_template(nums, condition_fn):
    """
    Template for variable-size sliding window.
    Expand right, shrink left while condition violated, record answer.
    """
    left = 0
    ans = 0  # or float('inf') for minimum problems
    window_state = {}  # Counter, set, sum — whatever the problem needs

    for right in range(len(nums)):
        # --- EXPAND: add nums[right] to window state ---
        # e.g., window_state[nums[right]] = window_state.get(nums[right], 0) + 1

        # --- SHRINK: while window is invalid, remove from left ---
        while not condition_fn(window_state):
            # remove nums[left] from window state
            left += 1

        # --- RECORD: window [left..right] is valid ---
        ans = max(ans, right - left + 1)  # or min() for minimum problems

    return ans
```

### 3. Longest Substring Without Repeating Characters (LC 3)

```python
def length_of_longest_substring(s: str) -> int:
    last_seen = {}  # char -> last index where it appeared
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1  # jump left past the duplicate
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len

# "abcabcbb" → 3 ("abc")
# Key: instead of shrinking one-by-one, jump left directly to last_seen[ch]+1
```

### 4. Minimum Window Substring (LC 76)

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)           # characters we need and their counts
    have = {}                   # characters we have in current window
    formed = 0                  # how many unique chars in t are fully satisfied
    required = len(need)        # total unique chars we need to satisfy

    left = 0
    ans = (float('inf'), 0, 0)  # (window_length, left, right)

    for right, ch in enumerate(s):
        # EXPAND: add s[right]
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        # SHRINK: while window is valid, try to minimize
        while formed == required:
            # record answer
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            # remove s[left] and move left forward
            out = s[left]
            have[out] -= 1
            if out in need and have[out] < need[out]:
                formed -= 1
            left += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

# s = "ADOBECODEBANC", t = "ABC" → "BANC"
# formed counter avoids comparing full dicts each iteration → O(1) per step
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Longest Substring Without Repeating Characters | 3 | Medium | Use hash map of last-seen index; jump left to `max(left, last_seen+1)` |
| Minimum Window Substring | 76 | Hard | Two counters (need/have), `formed` tracks satisfied chars. Expand → shrink → record. |
| Longest Repeating Character Replacement | 424 | Medium | Window is valid while `window_size - max_freq <= k`. Don't need to decrease `max_freq`. |
| Permutation in String | 567 | Medium | Fixed-size window of `len(s1)`, compare frequency counts |
| Minimum Size Subarray Sum | 209 | Medium | Shrink while `sum >= target`, track minimum length |
| Fruit Into Baskets | 904 | Medium | Longest subarray with at most 2 distinct elements |

---

## Common Mistakes

- **Forgetting to shrink** (infinite loop) or **shrinking too aggressively** (missing valid windows).
- **Not updating the answer at the right time** — for minimum problems, record *inside* the shrink loop; for maximum problems, record *after* shrinking.
- **Using `set` instead of `Counter`** for minimum window substring — you need to track frequencies, not just presence.
- **Longest Repeating Character Replacement**: trying to track exact `max_freq` across all shrinks is unnecessary — `max_freq` only needs to increase. The window size only grows when we find a better `max_freq`, so stale values don't produce wrong answers, just slightly suboptimal (but still correct) shrinking.
- **Off-by-one**: window size = `right - left + 1`, not `right - left`.

---

## Interview Questions

- **"Solve Longest Substring Without Repeating Characters — walk me through your sliding window."**
  - Expand right, if duplicate found jump `left` to `last_seen[ch]+1`. Track max length.
- **"Minimum Window Substring — explain when you expand vs shrink."**
  - Expand to find a valid window, shrink to minimize it. Record answer during shrink.
- **"What's the time complexity of your sliding window? Is each element processed more than once?"**
  - O(n). Each element enters once (right) and leaves once (left) = O(2n).
- **"When would you use a fixed vs variable size window?"**
  - Fixed: window size given or derivable. Variable: find longest/shortest satisfying a condition.
- **"How does sliding window differ from two pointers?"**
  - Sliding window is a specific type of two pointers where both move in the same direction to define a contiguous range.
- **"Longest Repeating Character Replacement — why don't you need to decrease `max_freq`?"**
  - The answer only improves when `max_freq` increases. A stale `max_freq` keeps the window at the current best size — it never grows incorrectly.

---

## Quick Reference

**Decision flowchart:**

```
Contiguous subarray/substring?
├── YES → Consider sliding window
│   ├── Fixed size given? → Fixed-size window
│   ├── "Longest/shortest with condition"? → Variable-size window
│   ├── Has negative numbers?
│   │   └── Sliding window may NOT work for sum → use prefix sum + hash map
│   ├── Minimum window → shrink after finding valid → track min
│   └── Maximum window → expand as much as possible → track max
└── NO → Different pattern (two pointers, hash map, etc.)
```
