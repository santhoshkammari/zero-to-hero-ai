# Custom Sorting

> Half of sorting problems don't ask you to implement a sort — they ask you to *choose the right sort key*. Recognizing "this is a sorting problem" is the real skill.

## Core Idea

Most interview sorting problems boil down to: define the right ordering, sort with it, then process the sorted result. Python's `key=` parameter handles 90% of cases. For the remaining 10% where you need to compare two elements directly (like "is ab > ba?"), use `functools.cmp_to_key`. The hardest part is usually recognizing that sorting is the right first step.

---

## What You Need to Know

### Python's Sorting API

| Approach | Syntax | When to Use |
|----------|--------|-------------|
| `key=` function | `sorted(arr, key=lambda x: x[0])` | When each element maps to a sortable value |
| Multi-key sort | `sorted(arr, key=lambda x: (x[0], -x[1]))` | Sort by first key ascending, break ties by second key descending |
| `cmp_to_key` | `sorted(arr, key=cmp_to_key(cmp_func))` | When ordering depends on comparing *pairs* of elements, not mapping each to a key |
| `reverse=True` | `sorted(arr, reverse=True)` | Descending order |

### `key=` — The Default Tool

Python's `sorted()` and `list.sort()` accept a `key` function that transforms each element into a comparable value. The sort compares these transformed values.

```python
# Sort strings by length
sorted(["banana", "fig", "apple"], key=len)
# → ["fig", "apple", "banana"]

# Sort intervals by start time
sorted(intervals, key=lambda x: x[0])

# Sort by multiple criteria: ascending by start, descending by end
sorted(intervals, key=lambda x: (x[0], -x[1]))
```

**Why tuples work for multi-key:** Python compares tuples lexicographically — first element first, then second on tie, etc. Negate a value to reverse that key's order.

**Gotcha with negation:** `-x` only works for numbers. For strings, you'd need `cmp_to_key` or a wrapper.

### `cmp_to_key` — When `key=` Isn't Enough

Sometimes the ordering isn't about mapping each element to a value — it's about comparing *two elements directly*. Classic example: LC 179 Largest Number.

```python
from functools import cmp_to_key

def compare(a, b):
    """Return negative if a should come first, positive if b should come first, 0 if equal."""
    if a + b > b + a:
        return -1   # a before b
    elif a + b < b + a:
        return 1    # b before a
    return 0

# "9" vs "34": "934" > "349", so "9" comes first
sorted(["3", "34", "9"], key=cmp_to_key(compare))
# → ["9", "34", "3"] → "9343"
```

**Comparison function contract:**
- Return **negative** → first argument comes first
- Return **positive** → second argument comes first  
- Return **0** → equal
- Must be **transitive**: if a < b and b < c, then a < c. Violating this → undefined behavior.

### The "Sort First, Then Process" Pattern

Many problems follow this structure:

```
1. Sort the input by some criterion
2. Linear scan the sorted result, making greedy decisions
```

This works because sorting brings related elements together or establishes an ordering that makes greedy choices locally optimal.

### Intervals Pattern

Interval problems almost always start with sorting:

```python
# Merge Intervals: sort by start time
intervals.sort(key=lambda x: x[0])

# Meeting Rooms II: sort events by time (need to process starts and ends)
events = []
for start, end in intervals:
    events.append((start, 1))   # +1 for meeting starting
    events.append((end, -1))    # -1 for meeting ending
events.sort()  # sort by time; ties broken by -1 before +1 (end before start)
```

**Why sort by start?** After sorting, you only need to compare each interval with the previous one. Without sorting, you'd need O(n²) pairwise comparisons.

### Recognizing Hidden Sorting Problems

Not every sorting problem says "sort" in the title. Watch for these signals:

- **"Merge overlapping..."** → sort by start, linear merge
- **"Maximum number of non-overlapping..."** → sort by end (greedy activity selection)
- **"Largest/smallest arrangement..."** → custom comparator (LC 179)
- **"K closest/largest/smallest..."** → partial sort (heap or quick select), but sometimes full sort + slice is fine
- **"Rearrange so that..."** → often sort + interleave

---

## Key Patterns & Templates

### Merge Intervals

```python
def merge(intervals):
    """LC 56: Sort by start, merge overlapping intervals."""
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # overlaps with last merged interval
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged
```

**The merge condition:** `current.start <= result[-1].end`. If this holds, extend the last interval's end to `max(result[-1].end, current.end)`. The `max` is important — the new interval might be entirely contained within the previous one.

### Largest Number (Custom Comparator)

```python
from functools import cmp_to_key

def largest_number(nums):
    """LC 179: Arrange numbers to form the largest possible number."""
    strs = [str(n) for n in nums]
    
    # Compare by concatenation: "9" + "34" = "934" vs "34" + "9" = "349"
    strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
    
    result = "".join(strs)
    return "0" if result[0] == "0" else result  # edge case: all zeros
```

### Meeting Rooms I (Can Attend All?)

```python
def can_attend_meetings(intervals):
    """LC 252: Check if any meetings overlap."""
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # starts before previous ends
            return False
    return True
```

### Meeting Rooms II (Min Rooms Needed)

```python
import heapq

def min_meeting_rooms(intervals):
    """LC 253: Minimum conference rooms needed."""
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])  # sort by start time
    
    # Min-heap of end times = rooms currently in use
    heap = [intervals[0][1]]
    
    for start, end in intervals[1:]:
        if start >= heap[0]:  # earliest-ending room is free
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    
    return len(heap)
```

**Alternative — sweep line approach:**

```python
def min_meeting_rooms_sweep(intervals):
    """Event-based approach: +1 at start, -1 at end, track peak."""
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort()  # ties: end (-1) before start (+1) at same time
    
    rooms = max_rooms = 0
    for _, delta in events:
        rooms += delta
        max_rooms = max(max_rooms, rooms)
    return max_rooms
```

### K Closest Points to Origin

```python
def k_closest(points, k):
    """LC 973: Sort by distance, take first k."""
    # No need for sqrt — comparing squared distances preserves ordering
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:k]
    
    # For O(n) average: use Quick Select on distances
    # For O(n log k): use max-heap of size k
```

### Sort Array by Increasing Frequency

```python
from collections import Counter

def frequency_sort(nums):
    """LC 1636: Sort by frequency ascending; ties broken by value descending."""
    freq = Counter(nums)
    # Primary: frequency ascending. Secondary: value descending (for ties).
    return sorted(nums, key=lambda x: (freq[x], -x))
```

### Custom Sort String

```python
def custom_sort_string(order, s):
    """LC 791: Sort s so chars appear in the order given by 'order'."""
    # Build priority map: chars in 'order' get their index, others get infinity
    priority = {c: i for i, c in enumerate(order)}
    return "".join(sorted(s, key=lambda c: priority.get(c, len(order))))
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Merge Intervals | 56 | Medium | Sort by start, linear merge. Merge condition: `current.start <= result[-1].end`. Always extend with `max` of ends |
| Largest Number | 179 | Medium | Custom comparator: compare `a+b` vs `b+a` as strings. Requires `cmp_to_key` because the ordering depends on pairs, not individual values |
| Meeting Rooms | 252 | Easy | Sort by start, check if any `intervals[i].start < intervals[i-1].end` |
| Meeting Rooms II | 253 | Medium | Sort by start + min-heap of end times. Heap size = rooms in use. Pop when earliest room is free |
| K Closest Points to Origin | 973 | Medium | Sort by squared distance (skip sqrt). For follow-up: Quick Select for O(n) or max-heap for O(n log k) |
| Sort Array by Increasing Frequency | 1636 | Easy | `key=lambda x: (freq[x], -x)` — tuple sorting with negation for tie-breaking |
| Custom Sort String | 791 | Medium | Map each char to its priority index in the custom order, sort by that. Chars not in order go to the end |
| Valid Anagram | 242 | Easy | Sort both strings, compare — or use Counter. Sorting approach is O(n log n), Counter is O(n) |

---

## Common Mistakes

- **Inconsistent comparator** — if your `cmp_to_key` function says a < b and b < c but a > c, the sort produces undefined results. Always ensure **transitivity**.
- **Forgetting the `max` in merge intervals** — `merged[-1][1] = end` is wrong when the previous interval's end is *larger* than the current one (the current interval is fully contained). Must use `max(merged[-1][1], end)`.
- **Not recognizing a sorting problem** — if you're doing O(n²) pairwise comparisons on intervals, distances, or orderings, ask yourself: "would sorting make this linear?"
- **Using `cmp_to_key` when `key=` suffices** — `key=` is cleaner and faster. Only reach for `cmp_to_key` when the comparison genuinely depends on *two* elements together (like string concatenation in LC 179).
- **Sorting strings by negation** — you can't do `-"abc"` in Python. For reverse string sorting, use `cmp_to_key` or sort twice (sort by secondary key first, then stable-sort by primary key).

---

## Interview Questions

1. **"Merge overlapping intervals."** — Sort by start time. Linear scan, merge when `current.start <= result[-1].end`. Follow-up: what if intervals are streaming in? (Use a balanced BST / sorted container.)
2. **"Given a list of numbers, form the largest possible number."** — Convert to strings, sort with custom comparator `a+b > b+a`. Edge case: all zeros → return "0". Explain why `key=` alone can't solve this.
3. **"What's the minimum number of meeting rooms needed?"** — Sort by start time, use min-heap of end times. Or: sweep line with +1/-1 events. Both are O(n log n).
4. **"How does Python's `key=` parameter work internally?"** — It calls the key function once per element, caches the result, and compares cached values. This is called the **decorate-sort-undecorate** pattern (Schwartzian transform).
5. **"Sort points by distance to origin. Can you do better than O(n log n)?"** — Quick Select for kth closest in O(n) average, then return all points with distance ≤ kth. Or max-heap of size k for O(n log k).
6. **"When would you use `cmp_to_key` instead of `key=`?"** — When the comparison between two elements depends on both simultaneously (e.g., string concatenation order). If you can map each element independently to a sortable value, `key=` is better.
7. **"Insert an interval into a sorted list of non-overlapping intervals."** (LC 57) — Binary search for position, merge with overlapping neighbors. Or: linear scan collecting left part, merged part, right part.
8. **"How do you sort by multiple criteria?"** — Return a tuple from the `key` function. Python sorts tuples lexicographically. Negate numeric values to reverse that key. For non-numeric reverse, sort is stable so you can sort twice: secondary key first, then primary.
9. **"Given tasks with deadlines and profits, maximize profit."** — Sort by deadline (or profit), greedy selection. This is "sorting as preprocessing for greedy" — a recurring pattern.

---

## Quick Reference

### Python Sorting Cheat Sheet

```python
# Basic sort (ascending)
sorted(arr)
arr.sort()                          # in-place

# Descending
sorted(arr, reverse=True)

# By key function
sorted(arr, key=len)                # by length
sorted(arr, key=lambda x: x[1])    # by second element
sorted(arr, key=lambda x: (x[0], -x[1]))  # multi-key

# Custom comparator
from functools import cmp_to_key
sorted(arr, key=cmp_to_key(my_cmp))

# Python's sorted() is STABLE — equal elements keep original order
# This means you can sort twice for complex orderings:
arr.sort(key=lambda x: x[1], reverse=True)  # secondary key first
arr.sort(key=lambda x: x[0])                # primary key second (stable!)
```

### Interval Problem Decision Tree

```
Interval problem?
├── Merge overlapping → sort by start, linear merge
├── Can attend all? → sort by start, check adjacent overlap
├── Min resources needed → sort by start + min-heap of ends (or sweep line)
├── Max non-overlapping → sort by END, greedy pick earliest-ending
├── Insert into sorted intervals → find overlap range, merge
└── Interval intersection → two pointers after sorting both lists
```

### Sorting Complexity Reminder

- Python's `sorted()` / `.sort()`: **O(n log n)** time, **O(n)** space (Timsort)
- Timsort is **stable** — this is guaranteed by the language spec
- `key` function is called **once per element**, not once per comparison
- `cmp_to_key` wraps your comparator so it's called **once per comparison** — slightly slower than `key=`
