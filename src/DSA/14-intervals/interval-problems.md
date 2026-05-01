# Interval Problems

> Intervals show up in ~15% of Google/Amazon coding rounds. Master the sort-then-scan pattern and you can solve nearly all of them.

## Core Idea

An interval `[start, end]` represents a range. Almost every interval problem starts the same way: **sort the intervals**, then scan left to right making greedy decisions. Think of intervals as events on a timeline — sorting puts them in chronological order so you only need one pass to find overlaps, gaps, or conflicts.

## What You Need to Know

### The Golden Rule

**Always sort intervals first.** The only question is: sort by start or by end?

| Sort By | When | Why |
|---------|------|-----|
| **Start time** | Merging, inserting, intersection | You process intervals left-to-right; sorting by start guarantees you see the earliest interval first |
| **End time** | Removing minimum overlapping intervals, activity selection | Choosing the earliest-ending interval leaves the most room for future intervals (greedy exchange argument) |

### Overlap Detection

Two intervals `[a, b]` and `[c, d]` (sorted so `a ≤ c`) overlap when:

```python
a <= c <= b  # c starts before b ends
```

They do **not** overlap when:

```python
b < c  # gap between them
```

⚠️ **Edge case**: Do `[1, 5]` and `[5, 10]` overlap? Depends on the problem — **always clarify with your interviewer** whether endpoints touching counts as overlap.

### Three Core Techniques

**1. Sort + Linear Scan** — Merge Intervals, Meeting Rooms I

Sort by start, iterate once, compare each interval to the previous/result.

- Time: O(n log n) for sort + O(n) scan = **O(n log n)**
- Space: O(n) for result (or O(1) if modifying in-place, ignoring sort space)

**2. Sweep Line** — Meeting Rooms II, Max Overlapping, Skyline

Convert each interval into two **events**: `+1` at start (someone arrives) and `-1` at end (someone leaves). Sort all events, scan left to right tracking a running count.

Think of it like a nightclub bouncer with a clicker — click up when someone enters, click down when they leave. The max count at any point = max simultaneous occupancy.

- Time: **O(n log n)** for sorting events
- Space: **O(n)** for the event list

**3. Min-Heap** — Meeting Rooms II, Employee Free Time

Maintain a heap of end times. For each new interval, if it starts after the earliest end time, reuse that resource (pop). Otherwise, allocate a new one (push).

- Time: **O(n log n)**
- Space: **O(n)** for the heap

## Key Patterns & Templates

### Merge Intervals (LC 56)

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:       # overlaps with last merged
            merged[-1][1] = max(merged[-1][1], end)  # extend
        else:
            merged.append([start, end])  # no overlap, new group

    return merged
# Time: O(n log n) | Space: O(n)
```

The merge condition is just: `current.start <= result[-1].end`. That's it.

### Insert Interval (LC 57)

Three phases — before overlap, during overlap, after overlap:

```python
def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Phase 1: intervals entirely before new (no overlap)
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # Phase 2: merge all overlapping intervals into new
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    result.append(new)

    # Phase 3: intervals entirely after new
    result.extend(intervals[i:])
    return result
# Time: O(n) | Space: O(n)
```

### Sweep Line Template

```python
def max_overlapping(intervals: list[list[int]]) -> int:
    events = []
    for start, end in intervals:
        events.append((start, 1))   # +1 = interval begins
        events.append((end, -1))    # -1 = interval ends

    events.sort()  # sort by time, then by type (-1 before +1 at same time)

    max_count = curr = 0
    for _, delta in events:
        curr += delta
        max_count = max(max_count, curr)

    return max_count
# Time: O(n log n) | Space: O(n)
```

**Same-timestamp ordering matters.** If `[1,5]` and `[5,8]` should NOT be counted as overlapping, sort so that `-1` events come before `+1` at the same timestamp (the default tuple sort handles this since `-1 < 1`).

### Min-Heap for Meeting Rooms II (LC 253)

```python
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    heap = []  # stores end times of active meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # reuse room — earliest meeting ended
        heapq.heappush(heap, end)

    return len(heap)  # heap size = rooms in use
# Time: O(n log n) | Space: O(n)
```

**Alternative — two-pointer on sorted starts/ends** (no heap, same complexity):

```python
def min_meeting_rooms_two_ptr(intervals: list[list[int]]) -> int:
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    rooms = end_ptr = 0
    for s in starts:
        if s < ends[end_ptr]:
            rooms += 1          # need a new room
        else:
            end_ptr += 1        # free up a room
    return rooms
# Time: O(n log n) | Space: O(n)
```

### Interval Intersection (LC 986)

Two pointers, each advancing through its own sorted list:

```python
def interval_intersection(
    A: list[list[int]], B: list[list[int]]
) -> list[list[int]]:
    i = j = 0
    result = []

    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])

        if lo <= hi:
            result.append([lo, hi])

        # advance the pointer with the smaller end time
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return result
# Time: O(n + m) | Space: O(n + m) for result
```

### Non-overlapping Intervals (LC 435)

Sort by **end** time. Greedily keep the interval that ends earliest:

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])  # sort by END
    removals = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end     # keep this interval
        else:
            removals += 1     # overlaps — remove it

    return removals
# Time: O(n log n) | Space: O(1)
```

Why sort by end? Same logic as the classic activity selection problem — picking the earliest finish maximizes the number of non-overlapping intervals you can keep.

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|------|------------|-------------|
| Merge Intervals | 56 | Medium | Sort by start, extend `end` via `max()`. Foundation for everything else. |
| Insert Interval | 57 | Medium | Three-phase scan: before, overlap, after. No sort needed (already sorted). |
| Non-overlapping Intervals | 435 | Medium | Sort by **end** time. Greedy — earliest end leaves most room. Count removals. |
| Meeting Rooms | 252 | Easy | Sort by start. If any `start < prev_end`, return False. |
| Meeting Rooms II | 253 | Medium | Min-heap of end times OR sweep line OR two-pointer on sorted starts/ends. |
| Interval List Intersections | 986 | Medium | Two pointers. Intersection = `[max(starts), min(ends)]` if valid. Advance smaller end. |
| Employee Free Time | 759 | Hard | Flatten + merge all intervals, then find gaps between merged intervals. |
| Minimum Number of Arrows to Burst Balloons | 452 | Medium | Same idea as LC 435 — sort by end, greedily count non-overlapping groups. |

## Common Mistakes

- **Not sorting first.** Almost every interval problem requires sorting. If you're doing anything more complex than O(n log n) on a basic interval problem, you probably forgot to sort.
- **Sorting by the wrong key.** Merge/insert → sort by start. Activity selection/min removals → sort by end. Mixing these up gives wrong answers on edge cases.
- **Off-by-one on touching intervals.** `[1,5]` and `[5,10]` — overlapping or not? The problem statement decides. Read it carefully, and if it's an interview, **ask**.
- **Wrong event ordering in sweep line.** At the same timestamp, should ends process before starts? If you want `[1,5]` and `[5,8]` to NOT overlap, process `-1` before `+1`. Tuple sort `(time, delta)` handles this naturally since `-1 < 1`.
- **Forgetting empty input.** Always handle `if not intervals: return []` (or `0`, `True`, etc.) before accessing `intervals[0]`.

## Interview Questions

1. **Merge Intervals (LC 56):** Given a list of intervals, merge all overlapping intervals. What's the time complexity and can you do better than O(n log n)?
2. **Insert Interval (LC 57):** Insert a new interval into a sorted non-overlapping list and merge if necessary. Why don't you need to sort?
3. **Meeting Rooms II (LC 253):** What is the minimum number of conference rooms required? Solve it three ways: heap, sweep line, two-pointer. Which uses least space?
4. **Non-overlapping Intervals (LC 435):** What is the minimum number of intervals to remove so the rest don't overlap? Why does sorting by end time work here?
5. **Interval List Intersections (LC 986):** Given two lists of sorted disjoint intervals, find their intersection. Why is the two-pointer approach correct?
6. **Conceptual:** You have n intervals. How do you find the point covered by the most intervals? (Sweep line — events at start/end, find max running sum.)
7. **Employee Free Time (LC 759):** Given schedules of multiple employees (each a list of non-overlapping intervals), find the free time common to all. How does this reduce to merge intervals?
8. **Follow-up:** What if intervals arrive in a stream and you need to maintain the merged set online? (Use a balanced BST or sorted container — O(log n) per insert.)

## Quick Reference

### Decision Flowchart

```
Got an interval problem?
│
├─ Need to combine overlapping? → Sort by START → Merge Intervals pattern
├─ Need max simultaneous overlap? → Sweep Line (+1/-1 events)
├─ Need min rooms / resources? → Min-Heap of end times OR Sweep Line
├─ Need min removals for no overlap? → Sort by END → Greedy keep earliest end
├─ Two sorted interval lists? → Two Pointers
└─ Intervals arriving as stream? → Heap or Balanced BST
```

### Complexity Table

| Problem | Time | Space | Sort Key |
|---------|------|-------|----------|
| Merge Intervals (LC 56) | O(n log n) | O(n) | start |
| Insert Interval (LC 57) | O(n) | O(n) | already sorted |
| Non-overlapping Intervals (LC 435) | O(n log n) | O(1) | **end** |
| Meeting Rooms (LC 252) | O(n log n) | O(1) | start |
| Meeting Rooms II (LC 253) | O(n log n) | O(n) | start (heap) or both |
| Interval Intersection (LC 986) | O(n + m) | O(n + m) | already sorted |
| Employee Free Time (LC 759) | O(n log n) | O(n) | start |
| Min Arrows / Balloons (LC 452) | O(n log n) | O(1) | **end** |

### The Two Sorting Rules

| Sort by **start** | Sort by **end** |
|---|---|
| When you need to **build/merge** intervals left-to-right | When you need to **select/keep** maximum non-overlapping intervals |
| Merge, Insert, Intersection, Meeting Rooms | Activity Selection, Min Removals, Burst Balloons |
