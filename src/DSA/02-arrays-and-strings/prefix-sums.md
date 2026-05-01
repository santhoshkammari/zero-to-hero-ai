# Prefix Sums

> "Subarray sum equals K" is a Google classic — and it's just prefix sums + hash map. This simple precomputation unlocks O(1) range queries.

## Core Idea

Build a prefix sum array where `prefix[i] = sum(nums[0..i-1])`. Then `sum(nums[i..j]) = prefix[j+1] - prefix[i]`. One-time O(n) precompute gives O(1) range sum queries.

---

## What You Need to Know

- **1D prefix sum**: `prefix[0] = 0` (sentinel!), `prefix[i] = prefix[i-1] + nums[i-1]`. Range sum = `prefix[right+1] - prefix[left]`.
- **Prefix sum + hash map**: for "subarray sum = k", at each index check if `(current_prefix - k)` exists in hash map. This is **Two Sum on prefix sums**.
- **Prefix + suffix products**: for "product except self" — left-to-right product pass, then right-to-left.
- **2D prefix sum**: for matrix region queries. `prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i][j]`. Region query uses inclusion-exclusion.
- **Difference array**: for range update operations. To add `val` to range `[l, r]`: `diff[l] += val`, `diff[r+1] -= val`. Prefix sum of diff gives final values. O(1) per update instead of O(n).

---

## Key Patterns & Templates

### 1. Build 1D Prefix Sum + Range Query

```python
def build_prefix_sum(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)  # prefix[0] = 0 sentinel
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix: list[int], left: int, right: int) -> int:
    """Sum of nums[left..right] inclusive."""
    return prefix[right + 1] - prefix[left]

# nums = [2, 4, 1, 3, 5]
# prefix = [0, 2, 6, 7, 10, 15]
# range_sum(prefix, 1, 3) = prefix[4] - prefix[1] = 10 - 2 = 8  (4+1+3)
```

### 2. Subarray Sum Equals K (LC 560)

```python
def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}  # sentinel: empty prefix has sum 0

    for num in nums:
        current_sum += num
        # if (current_sum - k) was a previous prefix sum,
        # then the subarray between them sums to k
        count += prefix_counts.get(current_sum - k, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count

# nums = [1, 2, 3], k = 3 → 2 (subarrays [1,2] and [3])
# This is Two Sum on prefix sums. Can't use two pointers — negative numbers break monotonicity.
```

### 3. Product of Array Except Self (LC 238)

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Left pass: answer[i] = product of everything to the left of i
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Right pass: multiply in the product of everything to the right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# nums = [1, 2, 3, 4] → [24, 12, 8, 6]
# O(n) time, O(1) extra space (output array doesn't count)
# No division — handles zeros correctly
```

### 4. 2D Prefix Sum Build and Query

```python
def build_2d_prefix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (matrix[i-1][j-1]
                          + prefix[i-1][j]
                          + prefix[i][j-1]
                          - prefix[i-1][j-1])
    return prefix

def region_sum(prefix, r1: int, c1: int, r2: int, c2: int) -> int:
    """Sum of matrix[r1..r2][c1..c2] inclusive (0-indexed in original matrix)."""
    return (prefix[r2+1][c2+1]
          - prefix[r1][c2+1]
          - prefix[r2+1][c1]
          + prefix[r1][c1])

# Inclusion-exclusion: add full rectangle, subtract two overlaps, add back double-subtracted corner
```

### 5. Difference Array for Range Updates

```python
def apply_range_updates(n: int, updates: list[tuple[int, int, int]]) -> list[int]:
    """
    updates = [(left, right, val), ...]
    Efficiently apply val to every element in [left, right].
    """
    diff = [0] * (n + 1)

    for left, right, val in updates:
        diff[left] += val
        diff[right + 1] -= val  # note: right + 1, not right

    # Reconstruct final array via prefix sum of diff
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i-1] + diff[i]

    return result

# n=5, updates=[(1,3,2),(0,2,3)] → [3, 5, 5, 2, 0]
# O(u + n) where u = number of updates — beats O(u*n) brute force
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Subarray Sum Equals K | 560 | Medium | `prefix_sum - k` in hash map = "Two Sum on prefix sums". O(n). |
| Product of Array Except Self | 238 | Medium | Left product pass + right product pass. O(1) space: reuse output + running var. |
| Range Sum Query - Immutable | 303 | Easy | Classic prefix sum. `prefix[right+1] - prefix[left]`. |
| Contiguous Array (0s and 1s) | 525 | Medium | Replace 0 with -1, find longest subarray with sum 0 using prefix + hash map. |
| Subarray Sums Divisible by K | 974 | Medium | `prefix_sum % k` in hash map. Two sums with same mod have divisible-by-k subarray between them. |
| Range Sum Query 2D - Immutable | 304 | Medium | 2D prefix sum with inclusion-exclusion for region queries. |

---

## Common Mistakes

- **Off-by-one**: `prefix[0] = 0` sentinel is **required**. Without it, subarrays starting at index 0 break. You'll miss valid subarrays or get wrong sums.
- **Subarray sum = k**: can't use two pointers because of negative numbers. Must use prefix + hash map.
- **Product except self**: don't use division (fails on zeros). Use separate left/right passes.
- **2D prefix sum**: inclusion-exclusion formula has 4 terms. Drawing a diagram prevents sign errors.
- **Difference array**: forgetting the `+1` offset on the right bound (`diff[r+1] -= val`, not `diff[r]`).
- **Hash map initialization**: always start with `{0: 1}` (or `{0: -1}` for longest-subarray variants). Missing this sentinel means subarrays starting at index 0 are invisible.

---

## Interview Questions

- **"Find the count of subarrays that sum to K. Can you do it in O(n)?"**
  - Prefix sum + hash map. At each index, check if `current_prefix - k` was seen before. This is Two Sum on prefix sums.
- **"Product of Array Except Self without division — how?"**
  - Two passes: left-to-right accumulates prefix product, right-to-left accumulates suffix product.
- **"Explain the prefix sum + hash map technique for subarray sum problems."**
  - If `prefix[j] - prefix[i] == k`, then `sum(nums[i..j-1]) == k`. Store prefix sums in hash map, check for complement.
- **"What's a difference array and when would you use it?"**
  - For batch range updates. Each update is O(1) instead of O(n). Reconstruct with one prefix sum pass.
- **"How do you extend prefix sums to 2D? What's the query formula?"**
  - Build with inclusion-exclusion. Query: `prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`.
- **"Why can't you use two pointers for Subarray Sum Equals K?"**
  - Two pointers requires monotonicity (all positive). Negative numbers mean moving the left pointer can increase *or* decrease the sum — no predictable direction.

---

## Quick Reference

| Technique | Precompute | Query | Use Case |
|---|---|---|---|
| 1D Prefix Sum | O(n) | O(1) range sum | Range sum queries |
| Prefix + Hash Map | O(n) | O(n) total | Subarray sum = k, count |
| 2D Prefix Sum | O(m×n) | O(1) region sum | Matrix region queries |
| Difference Array | O(n) | O(n) to reconstruct | Batch range updates |
