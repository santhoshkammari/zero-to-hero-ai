# Advanced Binary Search

> The problems that separate "knows binary search" from "gets offers at Google" — peak finding on unsorted arrays and the infamous median of two sorted arrays.

## Core Idea

Advanced binary search applies the technique to problems that **don't look like binary search** at first glance. The unifying insight: you don't need a sorted array — you just need a way to **eliminate half the search space** at each step. A peak element uses the slope. Median of two arrays uses partition balance. These are O(log n) solutions where most people default to O(n).

## What You Need to Know

### Find Peak Element (LC 162) — O(log n)

A **peak** is an element greater than its neighbors. The array isn't sorted, but binary search still works because of the **slope property**: if `nums[mid] < nums[mid + 1]`, a peak must exist to the right (values are going up). If `nums[mid] > nums[mid + 1]`, a peak must exist to the left (or mid is the peak).

Think of it like hiking: if the ground is going uphill to your right, there's a peak somewhere to your right (because the array ends, forcing a "descent").

```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # peak is to the right
        else:
            right = mid  # peak is at mid or to the left
    return left
```

**Why this works**: The boundary condition `nums[-1] = nums[n] = -∞` guarantees at least one peak exists. By always walking "uphill," you're guaranteed to find one.

### Median of Two Sorted Arrays (LC 4) — O(log(min(m, n)))

The hardest standard binary search problem. You're binary searching on the **partition position** in the shorter array.

**The Idea**: You need to split both arrays such that:
- Left halves combined have exactly `(m + n + 1) // 2` elements
- Every element in the combined left half ≤ every element in the combined right half

```python
def find_median_sorted_arrays(nums1, nums2):
    # Always binary search on the shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2
    left, right = 0, m
    
    while left <= right:
        i = left + (right - left) // 2  # partition in nums1
        j = half - i                     # partition in nums2
        
        # Edge values (use -inf/inf for out-of-bounds)
        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')
        
        if left1 <= right2 and left2 <= right1:
            # Valid partition found
            if (m + n) % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            right = i - 1  # too far right in nums1
        else:
            left = i + 1   # too far left in nums1
```

**The mental model**: Imagine laying both arrays side by side. You're sliding a divider across `nums1` — as you move it right in `nums1`, it automatically moves left in `nums2` (since the total left-half size is fixed). You're searching for the divider position where the "cross" condition holds: `max(left sides) ≤ min(right sides)`.

### Minimize Maximum / Maximize Minimum on Arrays

This is a generalization of "search on answer" that appears in harder problems. You're binary searching on the answer and using a greedy or DP-based feasibility check.

**Minimize the Maximum Distance Between Gas Stations (LC 774)**:

```python
def min_max_distance(stations, k):
    left, right = 0, stations[-1] - stations[0]
    
    while right - left > 1e-6:  # floating point binary search
        mid = (left + right) / 2
        # Count stations needed to ensure no gap > mid
        count = 0
        for i in range(1, len(stations)):
            count += int((stations[i] - stations[i-1]) / mid)
        
        if count <= k:
            right = mid
        else:
            left = mid
    
    return right
```

**Note**: Floating-point binary search uses an epsilon-based termination condition instead of `left < right`.

### Staircase Search in Row-Sorted Column-Sorted Matrix — O(m + n)

Not true binary search, but a related technique. When rows are sorted left-to-right and columns sorted top-to-bottom (LC 240):

```python
def search_matrix_ii(matrix, target):
    if not matrix:
        return False
    row, col = 0, len(matrix[0]) - 1  # start top-right
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # too big, go left
        else:
            row += 1  # too small, go down
    return False
```

**Why top-right?** It's a decision point — going left decreases, going down increases. Top-left doesn't work because both directions increase.

## Key Patterns & Templates

### Floating-Point Binary Search Template

For problems where the answer is a real number (not integer):

```python
def float_binary_search(lo, hi, feasible, eps=1e-7):
    while hi - lo > eps:
        mid = (lo + hi) / 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid
    return hi
```

Alternative: run a fixed number of iterations (e.g., 100) instead of epsilon — more robust against precision issues.

### Binary Search + Prefix Sum/Sorting

Many advanced problems combine binary search with preprocessing:

```python
# Example: count elements ≤ x in each row of a row-sorted matrix
# Binary search per row: O(m log n)
import bisect

def count_le(matrix, x):
    return sum(bisect.bisect_right(row, x) for row in matrix)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Find Peak Element | 162 | Medium | Walk uphill — if `mid < mid+1`, peak is right |
| Median of Two Sorted Arrays | 4 | Hard | Binary search the partition on the shorter array |
| Search a 2D Matrix II | 240 | Medium | Staircase from top-right corner, O(m+n) |
| Find K-th Smallest Pair Distance | 719 | Hard | Binary search on distance + count pairs ≤ mid |
| Kth Smallest Element in Sorted Matrix | 378 | Medium | Binary search on value + count elements ≤ mid |
| Median of a Row-Wise Sorted Matrix | — | Hard | Binary search on value, count via bisect per row |

## Common Mistakes

- **Peak element: comparing wrong neighbors**. Compare `nums[mid]` with `nums[mid + 1]`, not `nums[mid - 1]`. This avoids boundary issues when `mid = 0`.
- **Median of two arrays: not handling the shorter-array constraint**. Always binary search on the shorter array — searching the longer one gives wrong `j` values that go negative.
- **Median of two arrays: edge cases with empty partitions**. When `i = 0` or `i = m`, use `-inf`/`inf` for the missing boundary. Forgetting this causes index-out-of-bounds.
- **Floating-point binary search: using `left < right` termination**. Floats need epsilon-based or fixed-iteration termination. `left < right` may never terminate due to precision.
- **Staircase search: starting from wrong corner**. Top-left or bottom-right don't give you a decision point where one direction increases and the other decreases.

## Interview Questions

- "Find a peak element in an unsorted array in O(log n). Why does binary search work here?" (Google)
- "Find the median of two sorted arrays in O(log(min(m,n))). Walk through your partition approach." (Google on-site classic)
- "In the median problem, why do we binary search on the shorter array?"
- "Given a matrix where each row and column is sorted, find a target in O(m+n)." (Microsoft)
- "Find the k-th smallest pair distance among all pairs. Can you do better than O(n² log n)?" (Google)
- "How would you binary search when the answer is a floating-point number? What changes?"
- "What's the time complexity of finding median of two sorted arrays? Break down the log factor."
- "Find the k-th smallest element in a sorted matrix. Compare heap vs binary search approaches."

## Quick Reference

```
Advanced Binary Search Decision Guide:
──────────────────────────────────────
Unsorted array, find peak           → Slope-based: compare mid with mid+1
Median of two sorted arrays         → Partition-based: binary search on shorter array
Row+col sorted matrix search        → Staircase search from top-right, O(m+n)
K-th smallest in sorted structure   → Binary search on VALUE, count elements ≤ mid
Floating-point answer               → Epsilon termination or fixed iterations

Complexities:
  Peak Element              → O(log n) time, O(1) space
  Median of Two Arrays      → O(log(min(m,n))) time, O(1) space
  Staircase Matrix Search   → O(m + n) time, O(1) space
  K-th Smallest Pair Dist   → O(n log n + n log D) time

Key Insight:
  You don't need sorted data for binary search.
  You need a way to ELIMINATE HALF the search space at each step.
```
