# Segment Trees & Binary Indexed Trees (Fenwick Trees)

> The two data structures that turn "I need to update AND query ranges efficiently" from O(n) per operation into O(log n).

## Core Idea

Think of a **segment tree** as a tournament bracket — each node stores the "winner" (sum, min, max) of its range, and updating one player only changes O(log n) matches. A **Binary Indexed Tree (BIT / Fenwick Tree)** is a cleverer, more compact structure that exploits binary representations to answer prefix queries in O(log n), but it can't do everything a segment tree can.

Both solve the same core problem: you have an array, and you need to **update elements** and **query ranges** repeatedly. A plain prefix sum array handles queries in O(1) but updates cost O(n). These structures give you O(log n) for both.

## What You Need to Know

### When to Use What

| Structure | Update | Query | Build | Space | Use When |
|-----------|--------|-------|-------|-------|----------|
| Prefix Sum Array | O(n) | O(1) | O(n) | O(n) | Static array, many queries, no updates |
| BIT (Fenwick Tree) | O(log n) point | O(log n) prefix | O(n log n) | O(n) | Need point updates + prefix/range sums |
| Segment Tree | O(log n) point | O(log n) range | O(n) | O(2n) | Need range queries (min/max/sum) + updates |
| Segment Tree + Lazy | O(log n) range | O(log n) range | O(n) | O(4n) | Need **range updates** + range queries |

**Rule of thumb:** Start simple. Prefix sum → BIT → Segment tree → Lazy propagation. Only escalate when the simpler tool can't handle the operation.

### Segment Tree — Array-Based Implementation

The array-based segment tree is the cleanest approach for interviews. For an array of size `n`, you store the tree in an array of size `2n`. The leaves sit at indices `n` to `2n-1`, and internal nodes at `1` to `n-1`. Index `0` is unused.

**Why array-based?** No node objects, no pointers, no recursion needed for basic operations. Just index math:
- Parent of `i`: `i // 2`
- Children of `i`: `2*i` and `2*i + 1`
- Leaf for `nums[i]`: index `i + n` in the tree array

### Binary Indexed Tree (Fenwick Tree)

A BIT stores partial sums in a flat array where each index "covers" a range determined by its **lowest set bit**. The magic operation `i & (-i)` isolates that lowest set bit, telling you how far to jump.

**Why it works:** In two's complement, `-i` flips all bits then adds 1, so `i & (-i)` gives you just the rightmost `1` bit. For index `6` (binary `110`), `6 & (-6) = 2` (binary `10`) — so index 6 covers 2 elements.

- **Query prefix sum** `[0..i]`: walk from `i` toward `0`, subtracting the lowest set bit each step.
- **Point update** at `i`: walk from `i` toward `n`, adding the lowest set bit each step.

**Critical: BITs are 1-indexed.** Index 0 is a dead zone (`0 & (-0) = 0` → infinite loop). Always shift your array indices by +1.

## Key Patterns & Templates

### 1. Array-Based Segment Tree (Range Sum)

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # Build: place leaves, then fill parents bottom-up
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, val):
        """Point update: set nums[i] = val."""
        i += self.n  # shift to leaf position
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left, right):
        """Range sum query over [left, right] inclusive."""
        res = 0
        left += self.n
        right += self.n + 1  # make right exclusive
        while left < right:
            if left & 1:       # left is a right child → include it, move right
                res += self.tree[left]
                left += 1
            if right & 1:      # right is a right child → include its sibling
                right -= 1
                res += self.tree[right]
            left //= 2
            right //= 2
        return res
```

**Complexity:** Build O(n), query O(log n), update O(log n), space O(2n).

**Adapting to min/max:** Replace `+` with `min()` or `max()`, and initialize unused slots to `float('inf')` or `float('-inf')`.

### 2. Segment Tree with Lazy Propagation (Range Update + Range Query)

Use this when you need to update an entire range, not just one element. Without lazy propagation, a range update would touch every leaf — O(n). Lazy stores pending updates at internal nodes and pushes them down only when needed.

```python
class LazySegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self._build(nums, 2 * node, start, mid)
        self._build(nums, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push_down(self, node, start, end):
        """Propagate lazy value to children."""
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            self._apply(2 * node, start, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, end, self.lazy[node])
            self.lazy[node] = 0

    def _apply(self, node, start, end, val):
        """Apply a pending add-val to a node's range."""
        self.tree[node] += val * (end - start + 1)
        self.lazy[node] += val

    def update_range(self, node, start, end, l, r, val):
        """Add val to every element in [l, r]."""
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self._apply(node, start, end, val)
            return
        self._push_down(node, start, end)
        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, l, r, val)
        self.update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        """Sum of elements in [l, r]."""
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        self._push_down(node, start, end)
        mid = (start + end) // 2
        return (self.query(2 * node, start, mid, l, r) +
                self.query(2 * node + 1, mid + 1, end, l, r))
```

**Complexity:** Build O(n), range update O(log n), range query O(log n), space O(4n).

### 3. Binary Indexed Tree (Fenwick Tree)

```python
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed!

    def update(self, i, delta):
        """Add delta to index i (0-indexed input, converted to 1-indexed)."""
        i += 1  # shift to 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # move to next responsible ancestor

    def prefix_sum(self, i):
        """Sum of elements [0..i] (0-indexed input)."""
        i += 1  # shift to 1-indexed
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)  # strip lowest set bit
        return s

    def range_sum(self, left, right):
        """Sum of elements [left..right] inclusive."""
        res = self.prefix_sum(right)
        if left > 0:
            res -= self.prefix_sum(left - 1)
        return res

    @classmethod
    def from_array(cls, nums):
        """Build BIT from existing array in O(n)."""
        bit = cls(len(nums))
        for i, val in enumerate(nums):
            bit.update(i, val)
        return bit
```

**Complexity:** Build O(n log n), point update O(log n), prefix query O(log n), space O(n).

**BIT for counting inversions** — a classic pattern:

```python
def count_inversions(nums):
    """Count pairs (i, j) where i < j and nums[i] > nums[j]."""
    # Coordinate compress to [0, n)
    sorted_unique = sorted(set(nums))
    rank = {v: i for i, v in enumerate(sorted_unique)}

    bit = BIT(len(sorted_unique))
    inversions = 0
    for num in reversed(nums):
        # Count elements already inserted that are smaller
        r = rank[num]
        if r > 0:
            inversions += bit.prefix_sum(r - 1)
        bit.update(r, 1)
    return inversions
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Range Sum Query - Mutable | [307](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Direct application of segment tree or BIT — the gateway problem |
| Range Sum Query 2D - Mutable | [308](https://leetcode.com/problems/range-sum-query-2d-mutable/) | Hard | 2D BIT: nest two BIT update/query loops |
| Count of Smaller Numbers After Self | [315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | Traverse right-to-left, BIT tracks frequencies by rank |
| Count of Range Sum | [327](https://leetcode.com/problems/count-of-range-sum/) | Hard | Convert to prefix sums, then count pairs with BIT or merge sort |
| The Skyline Problem | [218](https://leetcode.com/problems/the-skyline-problem/) | Hard | Sweep line + max-heap is standard; segment tree is the brute-force-proof approach |
| My Calendar I / II / III | [729](https://leetcode.com/problems/my-calendar-i/) / [731](https://leetcode.com/problems/my-calendar-ii/) / [732](https://leetcode.com/problems/my-calendar-iii/) | Med-Hard | Calendar III is a perfect lazy segment tree problem |
| Reverse Pairs | [493](https://leetcode.com/problems/reverse-pairs/) | Hard | Similar to inversions — BIT with coordinate compression, count `nums[i] > 2 * nums[j]` |

## Common Mistakes

- **Off-by-one in segment tree ranges.** The iterative query uses half-open `[left, right)` internally but you likely want closed `[left, right]`. Pick one convention and stick to it. The template above converts at the API boundary.
- **Forgetting lazy propagation push-down.** Every query and update must push pending lazy values to children *before* recursing. Miss one `_push_down` call and you get stale data silently — the hardest kind of bug to find.
- **BIT is 1-indexed, always.** `i & (-i)` at index 0 gives 0 → infinite loop. The template handles this with `i += 1` at the API boundary so callers use natural 0-indexed inputs.
- **Reaching for segment tree when you don't need it.** If the array is static (no updates), prefix sums solve range sum in O(1). If you only need min/max on a static array, sparse table gives O(1) queries. Only use segment tree/BIT when updates exist.
- **Not coordinate-compressing before using BIT for counting.** If values range up to 10⁹ but you only have 10⁵ elements, compress ranks to `[0, 10⁵)` first — otherwise your BIT array won't fit in memory.

## Interview Questions

1. **Conceptual:** Explain how a segment tree answers range sum queries in O(log n). Why is the tree height log n?
2. **Conceptual:** What's the difference between a segment tree and a BIT? When would you choose one over the other?
3. **Conceptual:** What is lazy propagation and why is it necessary? What goes wrong without it?
4. **Problem:** Given a mutable array, support `update(i, val)` and `sumRange(l, r)` — implement both operations in O(log n). *(LC 307)*
5. **Problem:** Count the number of inversions in an array. *(Classic, variant of LC 315)*
6. **Problem:** Given a stream of intervals for calendar bookings, return the maximum number of overlapping events at any point. *(LC 732)*
7. **Problem:** Count the number of range sums that lie in `[lower, upper]`. *(LC 327)*
8. **Follow-up:** You implemented a segment tree for range sum. How would you modify it for range minimum query? What changes in the merge step?
9. **Follow-up:** Your segment tree supports point updates. The interviewer now wants range updates (add `val` to all elements in `[l, r]`). Walk through how lazy propagation works.
10. **Design:** Design a system that tracks user activity counts per minute and supports queries like "total activity in the last k minutes" with real-time updates. What data structure do you use and why?

## Quick Reference

```
Segment Tree (array-based, size 2n):
  Leaf for nums[i]  →  tree[i + n]
  Parent of i        →  i // 2
  Children of i      →  2*i, 2*i + 1
  Build: O(n)  |  Query: O(log n)  |  Update: O(log n)  |  Space: O(2n)

Segment Tree + Lazy (recursive, size 4n):
  Range update: O(log n)  |  Range query: O(log n)
  Key rule: always push_down before recursing into children

BIT / Fenwick Tree (size n+1, 1-indexed):
  Move to parent (query):  i -= i & (-i)   # strip lowest set bit
  Move to next (update):   i += i & (-i)   # add lowest set bit
  Build: O(n log n)  |  Query: O(log n)  |  Update: O(log n)  |  Space: O(n)

Decision flowchart:
  Static array, range sum?          → Prefix sum array (O(1) query)
  Static array, range min/max?      → Sparse table (O(1) query, O(n log n) build)
  Point updates + prefix/range sum? → BIT (simpler, less code)
  Point updates + range min/max?    → Segment tree
  Range updates + range queries?    → Segment tree + lazy propagation
```
