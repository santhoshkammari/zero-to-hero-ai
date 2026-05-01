# Comparison Sorts

> Every FAANG interview expects you to know merge sort and quicksort cold — not just the code, but *when* to pick each one and *why*.

## Core Idea

Comparison sorts order elements by comparing pairs. The **information-theoretic lower bound** is **Ω(n log n)** — you can't do better with comparisons alone because a decision tree with n! leaves needs at least log₂(n!) ≈ n log n height. Know the trade-offs: merge sort buys stability and guaranteed O(n log n) at the cost of O(n) space; quicksort trades that guarantee for in-place performance.

---

## What You Need to Know

### The Big Picture

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable? | In-Place? |
|-----------|:-----------:|:----------:|:------------:|:-----:|:-------:|:---------:|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |

### Stability — Why It Matters

A **stable** sort preserves the relative order of elements with equal keys. This matters when you've already sorted by one criterion and now sort by a second — stability keeps the first sort's ordering intact for ties.

```
Records sorted by name, then stable-sorted by age:
  (Alice, 25), (Bob, 25), (Carol, 30)
  → Bob stays after Alice because stable sort doesn't shuffle equal-age records

Unstable sort might flip Alice and Bob — your multi-key ordering breaks.
```

**Stable:** Merge Sort, Insertion Sort, Counting Sort, Timsort (Python's built-in)
**Unstable:** Quick Sort, Heap Sort

### Merge Sort

**Divide & conquer**: split in half, recursively sort each half, merge two sorted halves.

Why O(n) space? The merge step needs an auxiliary array to combine two halves without overwriting elements you haven't compared yet.

**Exception — linked lists:** Merge sort on linked lists uses **O(1) extra space** (excluding recursion stack) because you can re-link nodes directly without copying. This is why merge sort is the go-to for linked list sorting.

**Counting inversions** — a classic variation. An **inversion** is a pair (i, j) where i < j but arr[i] > arr[j]. During the merge step, when you pick from the right half, every remaining element in the left half forms an inversion with it. This gives you the count for free.

### Quick Sort

**Partition-based**: pick a pivot, rearrange so everything < pivot is left and everything > pivot is right, then recurse on each side.

**Why O(n²) worst case?** If you always pick the smallest (or largest) element as pivot, one partition has n-1 elements and the other has 0 → n levels of recursion × O(n) work each.

**Fix:** **Randomized pivot** — pick a random element as pivot. This makes the expected time O(n log n) regardless of input order. In practice, `random.randint(lo, hi)` before partition.

**Lomuto vs Hoare partition:**

| | Lomuto | Hoare |
|---|--------|-------|
| Pivot position | End of array | Can be any position |
| Pointers | Single pointer i scans left-to-right | Two pointers scan inward from both ends |
| # Swaps | ~n/2 on average | ~n/3 on average |
| Equal elements | Degrades to O(n²) | Handles better |
| Simplicity | Easier to code correctly | Trickier off-by-one |

**Space:** O(log n) average for the recursion stack (the depth of balanced partitions). O(n) stack space in the worst case — another reason to randomize.

### Quick Select (Kth Smallest/Largest)

Same idea as quicksort, but you only recurse into the side that contains position k. Average O(n) because you do n + n/2 + n/4 + ... ≈ 2n work. Worst case is O(n²), but randomized pivot makes this extremely unlikely.

### Heap Sort

Build a max-heap in O(n), then repeatedly extract-max in O(log n), n times → O(n log n) total with O(1) extra space.

Why it's rarely the best choice: cache-unfriendly (jumps around the array following parent/child indices), higher constant factors than quicksort, and not stable. But it's useful when you need **guaranteed O(n log n) with O(1) space** — no other comparison sort offers both.

### Insertion Sort

Walk left to right, insert each element into its correct position in the already-sorted prefix. O(n) on nearly-sorted data because each element moves at most a few positions.

**Why it matters:** Python's built-in `sorted()` uses **Timsort**, which is a hybrid of merge sort and insertion sort. It identifies "runs" (already sorted subsequences) and uses insertion sort for small chunks (< 64 elements), then merges runs. This is why `sorted()` is O(n) on nearly-sorted data.

---

## Key Patterns & Templates

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= ensures stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Merge Sort — Count Inversions

```python
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    merged, split_inv = merge_count(left, right)
    return merged, left_inv + right_inv + split_inv

def merge_count(left, right):
    result = []
    inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i  # all remaining left elements are inversions
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions
```

### Quick Sort (Lomuto Partition, Randomized)

```python
import random

def quicksort(arr, lo, hi):
    if lo < hi:
        pivot_idx = partition(arr, lo, hi)
        quicksort(arr, lo, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    # Randomized pivot avoids O(n²) on sorted input
    rand_idx = random.randint(lo, hi)
    arr[rand_idx], arr[hi] = arr[hi], arr[rand_idx]
    
    pivot = arr[hi]
    i = lo  # i tracks the boundary of "elements < pivot"
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i
```

### Quick Select (Kth Smallest)

```python
def quick_select(arr, lo, hi, k):
    """Find kth smallest element (0-indexed). Modifies arr in-place."""
    if lo == hi:
        return arr[lo]
    
    pivot_idx = partition(arr, lo, hi)  # reuse partition from quicksort
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quick_select(arr, lo, pivot_idx - 1, k)
    else:
        return quick_select(arr, pivot_idx + 1, hi, k)

# For kth largest: quick_select(arr, 0, len(arr)-1, len(arr)-k)
```

### Dutch National Flag (3-Way Partition)

```python
def sort_colors(nums):
    """LC 75: Sort array of 0s, 1s, 2s in one pass."""
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
            # don't advance mid — swapped element needs inspection
```

### Merge Sort on Linked List

```python
def sort_list(head):
    """LC 148: O(n log n) time, O(1) extra space (ignoring recursion stack)."""
    if not head or not head.next:
        return head
    
    # Find middle with slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None  # cut the list in half
    
    left = sort_list(head)
    right = sort_list(mid)
    return merge_lists(left, right)

def merge_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Sort an Array | 912 | Medium | Implement merge sort or randomized quicksort from scratch — interviewers use this to test fundamentals |
| Kth Largest Element in an Array | 215 | Medium | Quick Select gives O(n) average; heap gives O(n log k). Know both — interviewer may ask you to optimize from one to the other |
| Sort Colors | 75 | Medium | Dutch National Flag: 3 pointers, one pass O(n) O(1). Don't use counting — they want the partition |
| Sort List | 148 | Medium | Merge sort on linked list — O(1) extra space because you re-link nodes. Find middle with slow/fast |
| Count of Smaller Numbers After Self | 315 | Hard | Modified merge sort: track original indices, count how many elements from right half get merged before each left element |
| Kth Largest Element in a Stream | 703 | Easy | Min-heap of size k — the root is always the kth largest. Good warm-up before LC 215 |

---

## Common Mistakes

- **Always picking first/last pivot in quicksort** → O(n²) on sorted or nearly-sorted input. Always randomize or use median-of-three.
- **Forgetting merge sort's O(n) space** — interviewers *will* ask about space complexity. If they want O(1) space, you need heap sort or quicksort, not merge sort.
- **Using O(n²) sort when O(n log n) is possible** — if n can be 10⁵+, insertion/bubble/selection sort will TLE. Default to merge sort or quicksort.
- **Incorrect stability assumption** — Python's `sorted()` is stable (Timsort), but if you implement quicksort, it's not. If the problem needs stability, use merge sort or Python's built-in.
- **Off-by-one in partition** — Lomuto partition is especially tricky. Trace through a 3-element array by hand before coding.

---

## Interview Questions

1. **"Implement merge sort from scratch."** — Test if you can write the merge step without bugs. Watch for `<=` (stability) and proper index handling.
2. **"What's the time and space complexity of merge sort vs quicksort? When would you prefer each?"** — Merge sort: guaranteed O(n log n), O(n) space, stable. Quicksort: O(n log n) average, O(log n) space, in-place, but O(n²) worst case.
3. **"Find the kth largest element. Can you do better than O(n log n)?"** — Start with sort, optimize to heap O(n log k), then Quick Select O(n) average.
4. **"How would you sort a linked list?"** — Merge sort, because it's O(n log n) and doesn't need random access. Quicksort on linked lists is painful because partitioning requires sequential access.
5. **"Given an array, count the number of inversions."** — Merge sort variant. During merge, when picking from right, add `len(left) - i` to count.
6. **"Why is quicksort faster than merge sort in practice, despite same O(n log n)?"** — Cache locality: quicksort works in-place on a contiguous array, so CPU cache hits are high. Merge sort copies to auxiliary arrays, causing cache misses.
7. **"Sort an array of 0s, 1s, and 2s in one pass."** — Dutch National Flag with three pointers. Can't do counting sort because they want one pass with constant swaps.
8. **"What is Timsort and why does Python use it?"** — Hybrid of merge sort and insertion sort. Exploits existing "runs" in data. O(n) on nearly-sorted data, O(n log n) worst case. Stable.
9. **"How do you handle duplicate elements efficiently in quicksort?"** — 3-way partition (Dutch National Flag): elements equal to pivot go in the middle. Avoids O(n²) when many duplicates.

---

## Quick Reference

### Decision Flowchart

```
Need to sort?
├── n ≤ ~50? → Insertion Sort (low overhead, great on small arrays)
├── Need stability? → Merge Sort (or Python's sorted())
├── Need guaranteed O(n log n)? 
│   ├── O(1) space required? → Heap Sort
│   └── O(n) space OK? → Merge Sort
├── Linked list? → Merge Sort (O(1) extra space on LL)
├── Average case matters most? → Quick Sort (randomized pivot)
└── Need kth element, not full sort? → Quick Select O(n)
```

### Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|:----:|:-------:|:-----:|:-----:|:------:|
| Merge Sort | n log n | n log n | n log n | O(n) | ✅ |
| Quick Sort | n log n | n log n | n² | O(log n) | ❌ |
| Heap Sort | n log n | n log n | n log n | O(1) | ❌ |
| Insertion Sort | n | n² | n² | O(1) | ✅ |
| Quick Select | n | n | n² | O(1) | — |

### Key Recurrences

- **Merge Sort:** T(n) = 2T(n/2) + O(n) → O(n log n) by Master Theorem
- **Quick Sort (avg):** T(n) = 2T(n/2) + O(n) → O(n log n)
- **Quick Sort (worst):** T(n) = T(n-1) + O(n) → O(n²)
- **Quick Select (avg):** T(n) = T(n/2) + O(n) → O(n)
