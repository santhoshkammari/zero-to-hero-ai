# Non-Comparison Sorts

> When elements are integers in a known range, you can break the Ω(n log n) barrier and sort in O(n). Interviewers use this to test whether you understand *why* the lower bound exists — and when it doesn't apply.

## Core Idea

The Ω(n log n) lower bound only applies to **comparison-based** sorting (where you learn about elements by comparing pairs). If you can exploit the *structure* of the data — integers in a bounded range, fixed-length strings, uniformly distributed floats — you can sort in linear time. Think of it like this: comparison sort asks "is A > B?" over and over; counting/radix/bucket sort asks "what slot does A go in?" and skips the comparison entirely.

---

## What You Need to Know

### Algorithm Overview

| Algorithm | Time | Space | Constraint | Stable? |
|-----------|:----:|:-----:|-----------|:-------:|
| Counting Sort | O(n + k) | O(k) | Integers in range [0, k) | ✅ |
| Radix Sort | O(d × (n + k)) | O(n + k) | d-digit numbers, each digit in [0, k) | ✅ |
| Bucket Sort | O(n) average | O(n + k) | Uniformly distributed data, k buckets | ✅ (if bucket sort is stable) |

### Counting Sort

**When to use:** Elements are non-negative integers (or can be mapped to them) with a small, known range k.

**How it works:**
1. Count occurrences of each value in a `count` array of size k.
2. Compute prefix sums so `count[i]` tells you the *final position* of value i.
3. Walk the original array in reverse (for stability), placing each element at its computed position.

**Why O(n + k):** One pass to count (O(n)), one pass for prefix sums (O(k)), one pass to place (O(n)).

**Limitation:** If k >> n (e.g., values in range [0, 10⁹] but only 100 elements), the O(k) space and time make it impractical. Use comparison sort instead.

### Radix Sort

**When to use:** Integers (or fixed-length strings) where each element has d "digits" and each digit has range k.

**How it works:** Sort by the **least significant digit** first, then next digit, up to the most significant digit. Each digit-level sort uses a **stable** sub-sort (typically counting sort). Stability is what makes this work — sorting by digit 2 doesn't undo the ordering from digit 1.

**Why LSD (least significant) first?** Because stability propagates the ordering from previous passes. If you sorted MSD first, you'd need recursion into sub-buckets (MSD radix sort exists but is more complex).

**For 32-bit integers:** d = 32/b where b is the bit-width per pass. Common choice: b = 8 (byte-level), so d = 4 passes, k = 256 → O(4 × (n + 256)) ≈ O(n).

### Bucket Sort

**When to use:** Data is **uniformly distributed** over a known range.

**How it works:**
1. Create k empty buckets spanning the data range.
2. Place each element in its bucket: `bucket_index = int(n * (val - min_val) / (max_val - min_val + 1))`.
3. Sort each bucket individually (insertion sort works because buckets should be small).
4. Concatenate all buckets.

**Why O(n) average?** With uniform distribution and n buckets, each bucket gets ~1 element on average. Sorting each tiny bucket is O(1). Total: O(n) for placement + O(n) for sorting ≈ O(n).

**Worst case O(n²):** If all elements land in one bucket, you're back to comparison sort on the whole array. This only happens with highly skewed distributions.

### When to Use Which

```
Integer values with small range k?
├── Yes → Counting Sort (simplest, O(n+k))
│
Multi-digit integers / fixed-length strings?
├── Yes → Radix Sort (O(d(n+k)), handles larger ranges)
│
Uniformly distributed floats/values?
├── Yes → Bucket Sort (O(n) average)
│
None of the above?
└── Comparison sort (merge/quick sort, O(n log n))
```

---

## Key Patterns & Templates

### Counting Sort

```python
def counting_sort(arr):
    """Sort non-negative integers. O(n+k) time and space."""
    if not arr:
        return arr
    
    k = max(arr) + 1
    count = [0] * k
    
    for val in arr:
        count[val] += 1
    
    # Prefix sum: count[i] = number of elements <= i
    for i in range(1, k):
        count[i] += count[i - 1]
    
    output = [0] * len(arr)
    # Traverse in reverse for stability
    for val in reversed(arr):
        count[val] -= 1
        output[count[val]] = val
    
    return output
```

### Counting Sort — Simplified (When Stability Isn't Needed)

```python
def counting_sort_simple(arr):
    """When you just need sorted output, not stability."""
    if not arr:
        return arr
    count = [0] * (max(arr) + 1)
    for val in arr:
        count[val] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result
```

### Radix Sort (LSD, Base 10)

```python
def radix_sort(arr):
    """Sort non-negative integers using LSD radix sort."""
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1  # current digit position (1s, 10s, 100s, ...)
    
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    """Stable sort by the digit at position exp."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9
    
    for val in arr:
        digit = (val // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for val in reversed(arr):  # reverse for stability
        digit = (val // exp) % 10
        count[digit] -= 1
        output[count[digit]] = val
    
    return output
```

### Bucket Sort

```python
def bucket_sort(arr, num_buckets=None):
    """O(n) average for uniformly distributed data."""
    if not arr:
        return arr
    
    n = len(arr)
    num_buckets = num_buckets or n
    min_val, max_val = min(arr), max(arr)
    
    if min_val == max_val:
        return arr[:]
    
    buckets = [[] for _ in range(num_buckets)]
    spread = max_val - min_val
    
    for val in arr:
        idx = int((val - min_val) / spread * (num_buckets - 1))
        buckets[idx].append(val)
    
    # Sort each bucket (insertion sort is ideal for small buckets)
    result = []
    for bucket in buckets:
        bucket.sort()  # Python's Timsort, O(k log k) per bucket
        result.extend(bucket)
    
    return result
```

### Bucket Sort Frequency Pattern (Top K Frequent)

```python
def top_k_frequent(nums, k):
    """LC 347: O(n) using bucket sort by frequency."""
    from collections import Counter
    
    freq = Counter(nums)
    
    # Bucket index = frequency, value = list of elements with that frequency
    # Max frequency is len(nums), so we need len(nums)+1 buckets
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Walk from highest frequency to lowest
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

### Maximum Gap (Pigeonhole / Bucket Principle)

```python
def maximum_gap(nums):
    """LC 164: O(n) time, O(n) space using bucket sort principle."""
    if len(nums) < 2:
        return 0
    
    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0
    
    n = len(nums)
    # With n numbers and range (hi-lo), the max gap is at least ceil((hi-lo)/(n-1))
    # by pigeonhole principle. Make buckets of this size so max gap
    # must span across buckets (never within a single bucket).
    bucket_size = max(1, (hi - lo) // (n - 1))
    num_buckets = (hi - lo) // bucket_size + 1
    
    # Each bucket stores only min and max (we only care about gaps between buckets)
    bucket_min = [float('inf')] * num_buckets
    bucket_max = [float('-inf')] * num_buckets
    
    for val in nums:
        idx = (val - lo) // bucket_size
        bucket_min[idx] = min(bucket_min[idx], val)
        bucket_max[idx] = max(bucket_max[idx], val)
    
    # Max gap = max difference between consecutive non-empty buckets
    max_gap = 0
    prev_max = bucket_max[0]
    for i in range(1, num_buckets):
        if bucket_min[i] == float('inf'):
            continue  # empty bucket
        max_gap = max(max_gap, bucket_min[i] - prev_max)
        prev_max = bucket_max[i]
    
    return max_gap
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Maximum Gap | 164 | Medium | Pigeonhole principle: max gap ≥ ceil((max-min)/(n-1)), so make buckets that size → gap must be *between* buckets, not within. Only track min/max per bucket |
| Top K Frequent Elements | 347 | Medium | Count frequencies, then bucket sort by frequency (index = count). Walk buckets right-to-left to collect top k. O(n) vs O(n log k) with heap |
| H-Index | 274 | Medium | Counting sort approach: count papers by citation count, then walk from high to low. Citations > n are clamped to n → bounded range |
| Sort Characters By Frequency | 451 | Medium | Same bucket-by-frequency pattern as LC 347. Count char frequencies, bucket sort by count, build result from highest bucket |
| Height Checker | 1051 | Easy | Counting sort the heights (range 1-100), compare to original. Good warm-up for understanding counting sort mechanics |
| Sort an Array | 912 | Medium | Can implement radix sort here for O(n) on integer inputs — but handle negatives by offsetting |

---

## Common Mistakes

- **Using counting sort when k >> n** — if values range to 10⁹ but you have 1000 elements, you're wasting massive space. Check that k is reasonable relative to n.
- **Forgetting to handle negative numbers** — counting sort and radix sort are defined for non-negative integers. For negatives, either offset all values by |min| or separate negatives/positives.
- **Unstable digit-level sort in radix sort** — if the sub-sort isn't stable, radix sort produces wrong results. The whole algorithm depends on stability preserving previous passes' ordering.
- **Assuming bucket sort is always O(n)** — it's O(n) *average* for *uniform* distributions. Skewed data → large buckets → O(n²) worst case.
- **Applying non-comparison sorts when a simple `sorted()` works** — in interviews, mention you *could* use radix/counting sort and explain why, but don't over-engineer. Use them when the problem specifically requires O(n) or the data structure invites it (e.g., LC 164).

---

## Interview Questions

1. **"Why can counting sort beat O(n log n)? Doesn't the lower bound say you can't?"** — The Ω(n log n) lower bound only applies to comparison-based sorts. Counting sort doesn't compare elements — it uses values as indices directly.
2. **"Sort an array of integers in O(n) time."** — Ask about the range. Small range → counting sort. Large range → radix sort. Interviewers want you to ask clarifying questions.
3. **"Find the maximum gap between successive elements in sorted order, in O(n) time."** — Bucket sort with pigeonhole principle. Key insight: bucket size = ceil(range / (n-1)) ensures max gap is between buckets.
4. **"Find the top k most frequent elements in O(n)."** — Bucket sort by frequency. Index = frequency count, walk from right.
5. **"How would you sort 1 million 32-bit integers?"** — Radix sort with 4 passes of 8-bit counting sort. O(4 × (n + 256)) ≈ O(n). Mention it's cache-friendly if done with byte-level passes.
6. **"When would you choose radix sort over counting sort?"** — When the range k is too large for counting sort but the number of digits d is small. Radix sort decomposes the problem into d passes of counting sort on a small alphabet (e.g., base 256).
7. **"Can you sort floating-point numbers with a non-comparison sort?"** — Bucket sort for uniformly distributed floats. Not counting/radix sort directly (they need discrete values), though you can radix sort on the IEEE 754 bit representation with care.

---

## Quick Reference

### When to Break the O(n log n) Barrier

| Condition | Algorithm | Complexity |
|-----------|-----------|:----------:|
| Integers in range [0, k), k ≈ O(n) | Counting Sort | O(n + k) |
| d-digit integers, digit range k | Radix Sort | O(d(n + k)) |
| Uniform distribution over known range | Bucket Sort | O(n) avg |
| None of the above | Comparison sort | Ω(n log n) |

### Key Formulas

- **Counting sort space:** O(k) where k = max_value - min_value + 1
- **Radix sort passes:** d = ⌈log_b(max_value)⌉ where b is the base
- **Bucket sort bucket count:** typically n buckets for n elements
- **Maximum gap lower bound:** ⌈(max - min) / (n - 1)⌉ (pigeonhole)

### Comparison Sort Lower Bound Proof Sketch

```
n! possible orderings of n elements
Decision tree with comparison at each node → binary tree
Binary tree with n! leaves needs height ≥ log₂(n!)
log₂(n!) = Θ(n log n)  (by Stirling's approximation)
∴ Any comparison sort needs Ω(n log n) comparisons in the worst case
```
