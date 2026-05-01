# Arrays Fundamentals

> Arrays are the #1 interview topic. ~25% of all interview questions are array-based.

## Core Idea

Arrays store elements in contiguous memory giving O(1) access by index. The trade-off: insertion/deletion in the middle is O(n) because elements must shift. Python's `list` is a dynamic array that doubles in capacity when full, giving amortized O(1) append.

## What You Need to Know

**Python list internals**: dynamic array backed by a C array of pointers. When capacity is exceeded, Python over-allocates (roughly 1.125x) to give amortized O(1) append.

| Operation | Time | Why |
|---|---|---|
| `list[i]` | O(1) | Direct pointer arithmetic |
| `list.append(x)` | O(1) amortized | Occasional resize doubles capacity |
| `list.insert(i, x)` | O(n) | Shifts everything after index i |
| `list.pop()` | O(1) | Remove last, no shifting |
| `list.pop(i)` | O(n) | Shifts everything after index i |
| `x in list` | O(n) | Linear scan |
| `list.sort()` | O(n log n) | Timsort |
| `list[a:b]` | O(b-a) | Copies the slice |

**In-place operations**: overwrite from the end to avoid shifting. Classic example: merging two sorted arrays into one (LC 88) — fill from the back. Swap-based partitioning avoids extra space.

**Kadane's algorithm**: max subarray sum in O(n) time, O(1) space. At each element decide: extend the current subarray or start fresh. `current_sum = max(num, current_sum + num)`. Update global max. Initialize `max_sum` to `nums[0]` (not 0) to handle all-negative arrays.

**Dutch National Flag (3-way partition)**: sort an array of 0s, 1s, 2s in a single pass. Three pointers — `low` (boundary of 0s), `mid` (current), `high` (boundary of 2s). Swap elements to their correct region.

**Common array operations**: reverse (two pointers), rotate by k (triple reverse), remove duplicates from sorted array (slow/fast pointers).

## Key Patterns & Templates

### 1. Kadane's Algorithm — Maximum Subarray Sum

```python
def max_subarray(nums: list[int]) -> int:
    max_sum = cur_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum
```

### 2. Dutch National Flag / Sort Colors

```python
def sort_colors(nums: list[int]) -> None:
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
            # don't advance mid — swapped element is unexamined
```

### 3. Remove Duplicates from Sorted Array In-Place

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1  # length of unique portion
```

### 4. Reverse Array In-Place

```python
def reverse(nums: list[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

### 5. Rotate Array by k Positions

```python
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n  # handle k > n
    reverse(nums, 0, n - 1)      # reverse entire array
    reverse(nums, 0, k - 1)      # reverse first k
    reverse(nums, k, n - 1)      # reverse the rest
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Best Time to Buy and Sell Stock | 121 | Easy | Track `min_price_so_far`, profit = `price - min_so_far`. Baby Kadane's. |
| Product of Array Except Self | 238 | Medium | Left-product pass then right-product pass. O(1) space: reuse output array + running variable. |
| Maximum Subarray | 53 | Medium | Kadane's: `current_sum = max(num, current_sum + num)`. Reset when negative. |
| Sort Colors | 75 | Medium | Dutch National Flag: 3 pointers (`low`, `mid`, `high`), single pass O(n). |
| Move Zeroes | 283 | Easy | Two pointers: `slow` tracks insertion point for non-zeros. |
| Rotate Array | 189 | Medium | Reverse entire → reverse first k → reverse rest. O(1) space. |

## Common Mistakes

- **Modifying array while iterating forward** — use reverse iteration or two-pointer instead
- **Off-by-one in rotation** — always do `k = k % n` to handle `k > len(nums)`
- **Kadane's with all-negative arrays** — initialize `max_sum` to `nums[0]`, not `0`
- **String concatenation in loops** — `s += char` is O(n²) because strings are immutable; use list + join
- **Forgetting empty array edge case** — check `if not nums` before accessing `nums[0]`

## Interview Questions

- "Solve Best Time to Buy and Sell Stock in O(n) — explain why you don't need to look backward."
- "Product of array except self without division — and can you do it in O(1) extra space?"
- "Sort an array of 0s, 1s, and 2s in one pass."
- "Explain Kadane's algorithm. What if the array is all negative?"
- "What's the time complexity of Python's `list.insert(0, x)`? Why?"
- "Rotate an array by k positions in-place with O(1) extra space."
- "How does a dynamic array achieve amortized O(1) append?"

## Quick Reference

| Operation | Time |
|---|---|
| `list[i]` | O(1) |
| `list.append(x)` | O(1) amortized |
| `list.insert(i, x)` | O(n) |
| `list.pop()` | O(1) |
| `list.pop(i)` | O(n) |
| `x in list` | O(n) |
| `list.sort()` | O(n log n) |
| `list[a:b]` | O(b-a) |
