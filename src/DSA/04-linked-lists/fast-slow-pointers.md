# Fast & Slow Pointers (Floyd's Tortoise and Hare)

> This one technique solves cycle detection, finding middles, and kth-from-end problems — all O(1) space. Interviewers love it because it tests pointer intuition.

## Core Idea

Use two pointers moving at different speeds through a linked list. **Slow** moves 1 step, **fast** moves 2 steps. Because fast covers ground at 2× the rate, their relative positions encode useful information: if fast reaches the end, slow is at the middle; if they meet, there's a cycle. One technique, multiple applications.

## What You Need to Know

### Floyd's Cycle Detection

**Phase 1 — Detect the cycle:** Slow moves 1 step, fast moves 2 steps. If there's a cycle, they *must* meet (fast closes the gap by 1 each step). If fast reaches `None`, no cycle.

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# Time: O(n), Space: O(1)
```

**Phase 2 — Find cycle start:** After slow and fast meet inside the cycle, reset one pointer to head. Move both at speed 1. They meet at the cycle's entry point.

```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Phase 2: find entry point
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle start
    return None
# Time: O(n), Space: O(1)
```

### The Math Behind It

This is worth understanding because interviewers sometimes ask *why* Phase 2 works.

```
Let:
  a = distance from head to cycle start
  b = distance from cycle start to meeting point
  c = cycle length

When they meet:
  slow traveled: a + b
  fast traveled: a + b + k·c  (for some integer k ≥ 1)

Since fast moves 2× speed:
  2(a + b) = a + b + k·c
  a + b = k·c
  a = k·c - b
  a = (k-1)·c + (c - b)
```

Meaning: the distance from **head to cycle start** (`a`) equals the distance from **meeting point to cycle start** going forward (`c - b`), plus some full loops. So if you put one pointer at head and one at the meeting point, both moving at speed 1, they converge at the cycle start.

### Find Middle Node

When fast reaches the end, slow is at the middle. For even-length lists, this gives the **second middle node** (which is what most problems want).

```python
def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
# Time: O(n), Space: O(1)
```

For even-length lists, if you need the **first middle** instead (e.g., to split evenly for merge sort), use:

```python
def findFirstMiddle(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
# slow stops at the node just before the second half
```

### Find Kth Node From End

Advance `fast` by k steps first. Then move both at speed 1. When fast reaches the end, slow is at the kth node from the end.

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    # Advance fast by n+1 so slow lands on the node BEFORE the target
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next  # skip the target node
    return dummy.next
# Time: O(n), Space: O(1)
```

Why `n + 1` steps: we want slow to stop at the node *before* the one we're deleting, so we can rewire `slow.next`. Using a dummy node handles the edge case of deleting the head.

### Floyd's on Arrays (Duplicate Detection)

The same algorithm works on arrays where values are in range `[1, n]` — treat each value as a "next pointer." If there's a duplicate, following the pointers creates a cycle, and the cycle entry is the duplicate.

```python
def findDuplicate(nums):
    # Phase 1: detect cycle
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find entry (the duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
# Time: O(n), Space: O(1) — no hash set needed
```

This is the key insight for LC 287: the problem says "don't modify array, O(1) space" — that rules out sorting and hash sets, leaving Floyd's as the only option.

## Key Patterns & Templates

### Cycle Detection Template

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # CYCLE FOUND — slow and fast are inside the cycle
        break
else:
    # NO CYCLE — fast reached the end
    pass
```

### Find Middle Template

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle
```

### Kth From End Template

```python
fast = slow = head
for _ in range(k):
    fast = fast.next
while fast:
    slow = slow.next
    fast = fast.next
# slow is at the kth node from end (1-indexed)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Linked List Cycle | 141 | Easy | Slow+fast meet → cycle exists. The `while fast and fast.next` guard prevents null errors. |
| Linked List Cycle II | 142 | Medium | After meeting, reset one to head, both move speed 1 → they meet at cycle start. Understand the math: `a = c - b`. |
| Find the Duplicate Number | 287 | Medium | Treat array as linked list (index → value → next index). Floyd's detects cycle entry = the duplicate. Only O(1) space approach that doesn't modify the array. |
| Middle of the Linked List | 876 | Easy | When fast reaches end, slow is at middle. For even length, returns second middle. |
| Remove Nth Node From End of List | 19 | Medium | Advance fast by n+1 steps (with dummy node), then move both. Slow ends up right before the target. Dummy handles deleting the head. |
| Palindrome Linked List | 234 | Easy | Find middle → reverse second half → compare element by element. Combines fast/slow with reversal. O(1) space. |
| Reorder List | 143 | Medium | Find middle (fast/slow) → reverse second half → merge alternately. Three techniques in one. |
| Happy Number | 202 | Easy | Not a linked list but same idea — slow applies f once, fast applies f twice. If they meet and it's not 1, the number isn't happy. |

## Common Mistakes

- **Off-by-one in kth from end** — Clarify: is k 0-indexed or 1-indexed? LC 19 uses 1-indexed. If you advance fast by `k` steps and skip the dummy, you'll be off by one. Always use `n+1` with a dummy node for delete operations.
- **Not handling single-node and two-node lists** — `fast.next.next` crashes if the list has one node. The `while fast and fast.next` guard covers this, but be careful if you change the loop condition.
- **Using `==` to compare nodes instead of identity** — In Python, `slow == fast` works for identity checks on objects (since default `__eq__` compares identity), but be explicit: you're comparing *references*, not values.
- **Forgetting Phase 2 exists** — Many people know slow/fast detects cycles but forget how to find the cycle *start*. Phase 2 is the part interviewers actually care about.
- **Not disconnecting when splitting at middle** — If you find the middle to split a list (e.g., for merge sort), you must set `mid.next = None` to actually sever the two halves. Otherwise you still have one list.

## Interview Questions

1. **Detect if a linked list has a cycle, and if so, find where it starts.** Explain why the Phase 2 math works. *(LC 141/142)*
2. **Find the middle of a linked list in one pass.** What happens for even-length lists? *(LC 876)*
3. **Remove the nth node from the end in a single pass.** Why do you need n+1 gap and a dummy node? *(LC 19)*
4. **Find the duplicate number in an array of n+1 integers in range [1,n] without modifying the array and in O(1) space.** Why does Floyd's algorithm apply here? *(LC 287)*
5. **Check if a linked list is a palindrome in O(1) space.** What sub-problems does this decompose into? *(LC 234)*
6. **Reorder a list as L0 → Ln → L1 → Ln-1 → ...** Which step uses fast/slow pointers? *(LC 143)*
7. **If the cycle length is c, the non-cycle part is a, and slow/fast meet b steps into the cycle, prove that a = c − b (mod c).**
8. **Can you use fast/slow pointers to find the start of the last quarter of a linked list?** What speeds would you use?
9. **What's the difference between using a hash set vs Floyd's algorithm for cycle detection?** When would you prefer one over the other?

## Quick Reference

```
Fast/Slow Pointer Applications:

┌─────────────────────────┬────────────────────────────────────┐
│ Problem Type            │ Technique                          │
├─────────────────────────┼────────────────────────────────────┤
│ Has cycle?              │ slow=1, fast=2. Meet → yes.        │
│ Cycle start?            │ After meeting, reset one to head,  │
│                         │ both speed 1. Meet at entry.       │
│ Find middle?            │ slow=1, fast=2. Fast ends → slow   │
│                         │ is at middle.                      │
│ Kth from end?           │ Advance fast by k. Then both at 1. │
│                         │ Fast ends → slow is at target.     │
│ Duplicate in array?     │ Floyd's on index-as-pointer graph. │
└─────────────────────────┴────────────────────────────────────┘
```

| Pattern | Time | Space | Key Condition |
|---------|------|-------|---------------|
| Cycle detection (Phase 1) | O(n) | O(1) | `while fast and fast.next` |
| Cycle start (Phase 2) | O(n) | O(1) | Reset one to head, speed 1 |
| Find middle | O(n) | O(1) | `while fast and fast.next` |
| Kth from end | O(n) | O(1) | Advance fast k steps first |
| Duplicate in array | O(n) | O(1) | Values in [1, n], one dup |
| Palindrome check | O(n) | O(1) | Find middle + reverse + compare |
