# Stack & Queue Design Problems

> Design problems test whether you can combine data structures to achieve seemingly impossible time complexities — like O(1) getMin or O(1) LRU cache operations.

## Core Idea

Every design problem in this category follows the same meta-pattern: **combine two data structures so each one covers the other's weakness**. A hash map gives O(1) lookup but no ordering; a linked list gives O(1) insert/delete but no lookup. Put them together and you get O(1) for everything. The interviewer is testing whether you can see *which* combination and *why*.

## What You Need to Know

### Min Stack (LC 155)

**Goal**: A stack that supports `push`, `pop`, `top`, and `getMin` — all in O(1).

**The trick**: Each stack entry remembers the minimum *at that point in time*. When you pop, the previous minimum is automatically restored because it's stored in the entry below.

Think of it as taking a snapshot of the minimum at each level. No backtracking needed.

```python
class MinStack:
    def __init__(self):
        self.stack = []  # stores (value, current_min) pairs

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

All operations: O(1) time, O(n) space

**Alternative — auxiliary min stack**: Keep a separate stack that only pushes when a new minimum is seen. Slightly less space in practice, but same worst-case.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # only tracks minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### LRU Cache (LC 146) — The Canonical Design Problem

**Goal**: `get(key)` and `put(key, value)` both in O(1), with least-recently-used eviction when capacity is exceeded.

**The combination**: **Hash map** (O(1) key lookup) + **doubly linked list** (O(1) move-to-front and remove-from-tail).

The hash map stores `key → node`, where each node lives in the doubly linked list ordered by recency. Most recent at head, least recent at tail.

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node
        # Sentinel nodes avoid null checks
        self.head = Node()  # dummy head (most recent side)
        self.tail = Node()  # dummy tail (least recent side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)  # mark as recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                self._evict()
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def _evict(self):
        lru = self.tail.prev  # least recently used
        self._remove(lru)
        del self.cache[lru.key]  # need key stored in node for this
```

All operations: O(1) time, O(capacity) space

**Why sentinel nodes?** They eliminate edge cases for empty list, single element, etc. You never have to check for `None` — the head and tail always exist.

**Why store the key in the node?** When evicting the tail node, you need to delete it from the hash map too. Without the key in the node, you'd have no way to find the hash map entry.

### Python Shortcut: `OrderedDict`

Python's `collections.OrderedDict` is literally a hash map + doubly linked list. In a real interview, implement it manually to show understanding, but know the shortcut exists.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove oldest
```

### LFU Cache (LC 460)

**Goal**: Like LRU, but evict the **least frequently used** item. On frequency ties, evict the least recently used among those.

**The combination**: Two hash maps + a hash map of doubly linked lists:
- `key_map`: key → (value, frequency)
- `freq_map`: frequency → OrderedDict of keys (ordered by recency)
- Track `min_freq` to know which frequency bucket to evict from

```python
from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}  # key → (value, freq)
        self.freq_map = defaultdict(OrderedDict)  # freq → OrderedDict of key→None
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        val, freq = self.key_map[key]
        self._increase_freq(key, val, freq)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            _, freq = self.key_map[key]
            self._increase_freq(key, value, freq)
        else:
            if len(self.key_map) >= self.capacity:
                # Evict least frequent, least recent
                evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
                del self.key_map[evict_key]
            self.key_map[key] = (value, 1)
            self.freq_map[1][key] = None
            self.min_freq = 1

    def _increase_freq(self, key, value, freq):
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_map[key] = (value, freq + 1)
        self.freq_map[freq + 1][key] = None
```

All operations: O(1) time, O(capacity) space

### Queue Using Two Stacks (LC 232)

Already covered in [queue-and-deque.md](queue-and-deque.md), but the key design insight: the `in_stack` reverses order on push; transferring to `out_stack` reverses again, restoring FIFO order. Two reversals = original order.

**Amortized O(1)**: Each element is moved between stacks at most once, so across `n` operations, total work is O(n).

### Stack Using Two Queues (LC 225)

Push is O(n): after adding the new element, rotate all existing elements behind it. This makes the front of the queue always the "top" of the stack.

### Design Circular Queue (LC 622)

Covered in [queue-and-deque.md](queue-and-deque.md). The core design decision: use a `size` counter to distinguish full from empty, avoiding the classic `front == rear` ambiguity.

## Key Patterns & Templates

### Pattern 1: Snapshot State at Each Level

```python
# Min Stack pattern: each entry stores its own context
# Generalizes to: MaxStack, MinQueue, etc.
class SnapshotStack:
    def __init__(self):
        self.stack = []  # (value, derived_state)

    def push(self, val):
        derived = compute(val, self.stack[-1][1] if self.stack else default)
        self.stack.append((val, derived))

    def query(self):
        return self.stack[-1][1]  # O(1) access to derived state
```

### Pattern 2: Hash Map + Ordered Container

```python
# LRU/LFU pattern: hash map for O(1) lookup + ordered structure for O(1) eviction
# Hash map: key → node/metadata
# Ordered structure: maintains ordering (recency, frequency, etc.)
# On every access: update BOTH structures
```

### Pattern 3: Sentinel Nodes for Linked Lists

```python
# Always use dummy head and tail to eliminate edge cases
head = Node()
tail = Node()
head.next = tail
tail.prev = head
# Now insert/remove never needs null checks
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Min Stack | 155 | Medium | Store `(value, current_min)` pairs — each entry snapshots the min at that point |
| LRU Cache | 146 | Medium | Hash map + doubly linked list; sentinel nodes eliminate edge cases |
| LFU Cache | 460 | Hard | Two hash maps + freq buckets; track `min_freq` for O(1) eviction |
| Implement Queue using Stacks | 232 | Easy | Two stacks; transfer only when out_stack empty → amortized O(1) |
| Implement Stack using Queues | 225 | Easy | One queue; rotate after push to maintain LIFO at front |
| Design Circular Queue | 622 | Medium | Array + front/size pointers; `size` counter resolves full-vs-empty ambiguity |
| Max Stack | 716 | Hard | Two stacks or sorted container + doubly linked list for O(log n) popMax |
| Design Hit Counter | 362 | Medium | Queue of timestamps; dequeue expired hits; count = queue length |

## Common Mistakes

- **LRU Cache — forgetting to update position on `get()`**: Both `get` *and* `put` should move the node to the front. A common bug is only moving on `put`, which means frequently read items still get evicted.
- **LRU Cache — not storing the key in the node**: When evicting the tail, you need the key to delete from the hash map. Without it, you'd need an O(n) search.
- **Min Stack — using a single variable for min**: When you pop the current minimum, you have no way to know the *previous* minimum. You need history, not a single value. That's why each stack entry stores its own min.
- **Circular queue — full vs empty confusion**: Both `front == rear` states look identical without a `size` counter. Some solutions waste one slot (`full` when `(rear + 1) % cap == front`), but tracking `size` is cleaner.
- **LFU Cache — not updating `min_freq` correctly**: When you increment an element's frequency and its old frequency bucket becomes empty, check if that was `min_freq`. If so, `min_freq` must increment. Missing this causes wrong evictions.

## Interview Questions

1. **Design**: Implement a Min Stack. Can you do it with O(1) extra space? (Hint: store encoded differences.)
2. **Design**: Walk me through how an LRU cache handles `put(1,1), put(2,2), get(1), put(3,3)` with capacity 2.
3. **Conceptual**: Why does LRU cache need a *doubly* linked list? Why not singly linked?
4. **Follow-up**: How would you make an LRU cache thread-safe?
5. **Design**: Explain the difference between LRU and LFU eviction. When would you prefer one over the other?
6. **Problem**: Design a MaxStack that supports `push`, `pop`, `top`, `peekMax`, and `popMax`. What's the time complexity of `popMax`?
7. **Follow-up on LRU**: What if you need to support TTL (time-to-live) for each entry? How does the design change?
8. **Conceptual**: The two-stack queue has amortized O(1) per operation. Is any single operation ever O(n)? When?
9. **Design**: How would you implement an LRU cache with O(1) operations without using a doubly linked list? (Hint: Python's `OrderedDict`.)

## Quick Reference

```
Design Problem Cheat Sheet
══════════════════════════

Min Stack:
  Store (value, current_min) pairs
  getMin = stack[-1][1]  → O(1)

LRU Cache:
  Hash map: key → DLL node       → O(1) lookup
  Doubly linked list: recency    → O(1) move/evict
  get:  lookup + move to front
  put:  insert at front, evict tail if full
  ⚠️  Don't forget: get() also updates recency!

LFU Cache:
  key_map:  key → (value, freq)
  freq_map: freq → OrderedDict
  min_freq: tracks which bucket to evict from
  Every access: increase freq, move between buckets

Two-Stack Queue:
  in_stack ←push    pop→ out_stack
  Transfer in→out only when out is empty
  Amortized O(1)

Sentinel Nodes:
  head ↔ [node1] ↔ [node2] ↔ tail
  No null checks needed for insert/remove

Data Structure Combinations:
  O(1) lookup + O(1) ordered ops = hash map + linked list
  O(1) min/max + O(1) push/pop  = auxiliary stack
```
