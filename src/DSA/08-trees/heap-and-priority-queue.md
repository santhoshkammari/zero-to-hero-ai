# Heap & Priority Queue

> Anytime you see "top K," "kth largest," "merge K sorted," or "median from stream" — your first thought should be heap.

## Core Idea

A **heap** is a complete binary tree stored as an array where each parent is ≤ its children (**min-heap**) or ≥ its children (**max-heap**). It gives you O(1) access to the min/max and O(log n) insertion and extraction. Python's `heapq` module implements a min-heap. The key interviewer-tested fact: **building a heap from n elements is O(n), not O(n log n)** — and you should know why.

## What You Need to Know

### Heap Operations & Complexity

| Operation | Time | How |
|-----------|------|-----|
| `heappush` | O(log n) | Add to end, **sift up** |
| `heappop` | O(log n) | Remove root, move last to root, **sift down** |
| Peek min | O(1) | `heap[0]` |
| `heapify` (build) | **O(n)** | Bottom-up sift-down — NOT n × O(log n) |
| `heappushpop` | O(log n) | Push then pop in one operation (faster than separate calls) |

### Why Build Heap is O(n)

Most nodes are near the bottom and barely sift down. Roughly n/2 nodes are leaves (0 work), n/4 sift down 1 level, n/8 sift down 2 levels... The sum converges to O(n). Interviewers specifically ask this.

### Python `heapq` — Min-Heap Only

```python
import heapq

nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)             # O(n) — in-place

heapq.heappush(nums, 4)         # O(log n)
smallest = heapq.heappop(nums)  # O(log n) — returns 1

# Peek without removing
top = nums[0]

# Top-k smallest
k_smallest = heapq.nsmallest(3, nums)  # O(n log k)

# Top-k largest
k_largest = heapq.nlargest(3, nums)    # O(n log k)
```

### Max-Heap Trick in Python

Python only has min-heap. **Negate values** to simulate max-heap:

```python
max_heap = []
heapq.heappush(max_heap, -val)    # insert negated
max_val = -heapq.heappop(max_heap) # negate on pop
```

### Custom Comparators

For tuples, Python compares element by element. Use `(priority, tiebreaker, item)`:

```python
# Priority queue with custom ordering
heap = []
heapq.heappush(heap, (distance, node_id))  # sorts by distance first
heapq.heappush(heap, (freq, -index, word))  # freq asc, then index desc
```

### Top-K Elements (LC 347 — Top K Frequent) — O(n log k)

Maintain a **min-heap of size k**. This keeps the k largest elements — the root is the smallest of those k, which you can evict.

```python
def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Manual approach (more interview-friendly):
def top_k_frequent_manual(nums, k):
    from collections import Counter
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)  # evict least frequent
    return [num for freq, num in heap]
```

**Why min-heap of size k, not max-heap of size n?** Space is O(k) instead of O(n), and time is O(n log k) instead of O(n log n).

### Merge K Sorted Lists (LC 23) — O(N log k)

Push the head of each list into a min-heap. Pop the smallest, push its next node.

```python
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = curr = ListNode(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

**Why the index `i`?** ListNode objects aren't comparable. The index acts as a tiebreaker when values are equal, avoiding `TypeError`.

### Find Median from Data Stream (LC 295) — O(log n) per add, O(1) for median

The **two-heap pattern**: split numbers into a lower half (max-heap) and upper half (min-heap). The median is at the tops.

```python
class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negated) — stores smaller half
        self.hi = []  # min-heap — stores larger half
    
    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        # Move largest of lo to hi
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Balance: lo can have at most 1 more element than hi
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

**Why two heaps?** You need O(1) access to the middle. A single sorted structure gives O(n) insertion. Two heaps give O(log n) insertion and O(1) median — each heap's top is adjacent to the median.

### Kth Largest Element (LC 215)

Three approaches, know all:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort | O(n log n) | O(1) | Simple but slow |
| Min-heap of size k | O(n log k) | O(k) | Good for streaming |
| Quickselect | **O(n)** average | O(1) | Best, but O(n²) worst |

```python
# Min-heap approach
def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)  # pushpop in one step
    return heap[0]
```

### Task Scheduler (LC 621) — O(n)

Use max-heap to always pick the most frequent task. Cool-down managed with a queue.

```python
from collections import Counter, deque

def least_interval(tasks, n):
    count = Counter(tasks)
    heap = [-freq for freq in count.values()]
    heapq.heapify(heap)
    
    time = 0
    cooldown = deque()  # (available_time, neg_freq)
    
    while heap or cooldown:
        time += 1
        if heap:
            freq = heapq.heappop(heap) + 1  # complete one instance
            if freq < 0:
                cooldown.append((time + n, freq))
        if cooldown and cooldown[0][0] == time:
            heapq.heappush(heap, cooldown.popleft()[1])
    
    return time
```

## Key Patterns & Templates

### Heap Pattern Selector

```python
# "Find top/bottom K elements"          → Min/max-heap of size k
# "Kth largest/smallest"                → Min-heap of size k (root = answer)
# "Merge K sorted structures"           → Min-heap holding one element from each
# "Continuously find median"            → Two heaps (max-heap left, min-heap right)
# "Process by priority, with cooldown"  → Heap + queue for delayed re-insertion
```

### Lazy Deletion Pattern

Sometimes you need to "remove" elements from a heap but can't efficiently. Mark them and skip on pop:

```python
removed = set()

def lazy_pop(heap):
    while heap and heap[0] in removed:
        removed.discard(heapq.heappop(heap))
    return heapq.heappop(heap) if heap else None
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Kth Largest Element in an Array | 215 | Medium | Min-heap of size k; also know quickselect |
| Top K Frequent Elements | 347 | Medium | Min-heap of size k with frequency as key |
| Merge K Sorted Lists | 23 | Hard | Min-heap of k heads, push next on pop |
| Find Median from Data Stream | 295 | Hard | Two heaps: max-heap (left half), min-heap (right half) |
| Task Scheduler | 621 | Medium | Max-heap for most frequent + cooldown queue |
| K Closest Points to Origin | 973 | Medium | Max-heap of size k with negated distance |
| Reorganize String | 767 | Medium | Max-heap: always place most frequent char, ensure no adjacent duplicates |
| Meeting Rooms II | 253 | Medium | Min-heap tracks earliest ending meeting; push new starts |

## Common Mistakes

- **Forgetting `heapify` is O(n)**: Interviewers will ask. It's not n insertions of O(log n) each — it's bottom-up sift-down, which is O(n).
- **Not using a tiebreaker in tuples**: If two elements have the same priority, Python tries to compare the next element. If that's an uncomparable object, you get a `TypeError`. Always include an index or counter.
- **Max-heap: forgetting to negate on both push AND pop**: Push `-val`, pop gives `-val` which you negate back to `val`. Miss either negation and your logic breaks.
- **Two-heap median: unbalanced heaps**: After every insertion, ensure `len(lo) - len(hi)` is 0 or 1. Not rebalancing gives wrong median.
- **Using a heap when a simpler structure works**: If you just need the overall max/min (not dynamic), a single variable suffices. Heap is for when elements are **added and removed** over time.

## Interview Questions

- "Find the kth largest element. Compare heap vs quickselect. When would you use each?" (Amazon)
- "Design a data structure that supports addNum and findMedian in O(log n) and O(1)." (Google)
- "Merge k sorted linked lists. What's the time complexity and why?" (Meta/Amazon)
- "Why is building a heap O(n) instead of O(n log n)? Prove it."
- "Find the top k most frequent elements. Can you do better than O(n log n)?" (Bucket sort → O(n))
- "Given n meeting intervals, find the minimum number of conference rooms required." (Amazon)
- "Schedule tasks with cooldown. How do you decide which task to run next?"
- "What's the difference between a heap and a balanced BST? When would you choose one over the other?"

## Quick Reference

```
Heap Cheat Sheet:
─────────────────
Python: heapq (MIN-heap only). Negate for max-heap.

Array representation:
  Parent of i:      (i - 1) // 2
  Left child of i:  2 * i + 1
  Right child of i: 2 * i + 2

Complexities:
  Push/Pop:    O(log n)
  Peek:        O(1)
  Build heap:  O(n)  ← interviewers test this!
  Top-k:       O(n log k) with size-k heap

Pattern → Heap Type:
  Top k largest     → Min-heap of size k
  Top k smallest    → Max-heap of size k
  Merge k sorted    → Min-heap of k elements
  Running median    → Two heaps (max-left, min-right)
  Schedule by prio  → Max-heap + cooldown queue

Heap vs Alternatives:
  Just need min/max once?   → Single pass O(n), no heap needed
  Need sorted order?        → Sort, not heap
  Need kth element ONCE?    → Quickselect O(n) avg
  Need kth with STREAMING?  → Heap O(n log k)
```
