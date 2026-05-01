# Binary Search Fundamentals

> Binary search is the single most important algorithmic technique that separates O(n) thinkers from O(log n) thinkers — and interviewers notice.

## Core Idea

Binary search eliminates half the search space at every step by exploiting **sorted order** (or a monotonic property). You maintain two pointers `left` and `right`, compute `mid`, and decide which half to discard. The key is knowing **what `left` points to when the loop ends** — this determines which template you use.

## What You Need to Know

### The Three Templates

| Template | Loop Condition | Mid Calc | When `left > right` | Use Case |
|----------|---------------|----------|---------------------|----------|
| **Exact match** | `left <= right` | `left + (right - left) // 2` | Element not found | Find target in sorted array |
| **Left boundary** | `left < right` | `left + (right - left) // 2` | `left` = first valid position | First occurrence, lower bound |
| **Right boundary** | `left < right` | `left + (right - left + 1) // 2` | `left` = last valid position | Last occurrence, upper bound |

**Why `left + (right - left) // 2` instead of `(left + right) // 2`?** Prevents integer overflow. Python handles big ints natively, but interviewers expect you to know this — it matters in Java/C++.

### Template 1: Exact Match — O(log n)

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # left is now the insertion point
```

### Template 2: Find First Occurrence (Lower Bound) — O(log n)

```python
def first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # keep searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Template 3: Find Last Occurrence (Upper Bound) — O(log n)

```python
def last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1  # keep searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Python's `bisect` Module — Know This for Interviews

```python
import bisect

# bisect_left: index of first element >= target (lower bound)
pos = bisect.bisect_left(nums, target)

# bisect_right: index of first element > target (upper bound)
pos = bisect.bisect_right(nums, target)

# Insert while maintaining sort order
bisect.insort_left(nums, target)
```

| Function | Returns | Equivalent to |
|----------|---------|---------------|
| `bisect_left(a, x)` | First index where `x` can be inserted | Lower bound of `x` |
| `bisect_right(a, x)` | Last index where `x` can be inserted | Upper bound of `x` |

### Search in Rotated Sorted Array — O(log n)

The trick: **one half is always sorted**. Determine which half, then check if target falls in it.

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

### Find Minimum in Rotated Sorted Array — O(log n)

You're binary searching for the **inflection point** where the array wraps.

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1  # min is in right half
        else:
            right = mid  # mid could be the min
    return nums[left]
```

**With duplicates** (LC 154): when `nums[mid] == nums[right]`, you can't decide — shrink `right` by 1. Worst case degrades to O(n).

### Search a 2D Matrix — O(log(m × n))

If rows are sorted and first element of each row > last of previous, treat it as a flat sorted array.

```python
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // n][mid % n]  # flatten index to 2D
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

## Key Patterns & Templates

### The Universal Binary Search Template

When in doubt, use this template — it works for almost every binary search variant:

```python
def binary_search_template(condition):
    left, right = MIN_VALUE, MAX_VALUE
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid  # mid is a valid answer, but there might be a smaller one
        else:
            left = mid + 1  # mid is not valid, search right
    return left  # smallest value where condition is True
```

This finds the **leftmost position** where `condition(mid)` becomes `True`. Flip it for rightmost by adjusting mid calculation and branch logic.

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Binary Search | 704 | Easy | Master the `left <= right` invariant and what `left` means after the loop |
| Search in Rotated Sorted Array | 33 | Medium | One half is always sorted — check which, then decide |
| Find Minimum in Rotated Sorted Array | 153 | Medium | Compare `mid` with `right`, not `left` — you're finding the inflection |
| Search a 2D Matrix | 74 | Medium | Flatten 2D → 1D with `mid // n` and `mid % n` |
| Find First and Last Position | 34 | Medium | Two binary searches: one for left bound, one for right |
| Time Based Key-Value Store | 981 | Medium | `bisect_right` then check `pos - 1` for largest timestamp ≤ query |
| Search in Rotated Array II (dupes) | 81 | Medium | When `nums[left] == nums[mid]`, just `left += 1` — can't decide |

## Common Mistakes

- **Infinite loop with `left = mid`**: If you use `left < right` and set `left = mid`, you need `mid = left + (right - left + 1) // 2` (round up). Otherwise `left` never advances when `left + 1 == right`.
- **Wrong comparison in rotated array**: Comparing `nums[mid]` with `nums[left]` works differently than with `nums[right]`. Pick one and be consistent.
- **Forgetting that `left` after the loop = insertion point**: In template 1, when target isn't found, `left` is where it *would* go. Many problems rely on this.
- **Off-by-one on `right` initialization**: `right = len(nums) - 1` (inclusive) vs `right = len(nums)` (exclusive) — must match your loop condition.
- **Not handling empty array**: Always check `if not nums: return -1` up front.

## Interview Questions

- "Walk me through binary search on this sorted array. What happens when the target isn't present?"
- "Why do we use `left + (right - left) // 2` instead of `(left + right) // 2`?"
- "How would you find the first occurrence of a duplicate element in a sorted array?"
- "Search for a target in a rotated sorted array. What changes if duplicates are allowed?" (Google)
- "Given a sorted matrix where each row's first element is greater than the last of the previous row, find a target." (Amazon)
- "Design a time-based key-value store that returns the value at the largest timestamp ≤ a given time." (Google)
- "What's the difference between `bisect_left` and `bisect_right`? When would you use each?"
- "Find the minimum in a rotated sorted array. What's the time complexity with duplicates?"

## Quick Reference

```
Binary Search Decision Guide:
─────────────────────────────
Sorted array, find exact target     → Template 1 (left <= right)
Find first/last occurrence          → Template 2/3 (track result, keep searching)
Find boundary/transition point      → Universal template (left < right, condition-based)
Rotated array                       → Determine sorted half, then standard logic
2D sorted matrix                    → Flatten to 1D index

Complexity:
  Sorted array search    → O(log n) time, O(1) space
  Rotated array search   → O(log n) time, O(1) space  [O(n) worst with dupes]
  2D matrix search       → O(log(m×n)) time, O(1) space

Key Invariant:
  After loop ends, `left` = smallest index where condition holds
  (or insertion point if target not found)
```
