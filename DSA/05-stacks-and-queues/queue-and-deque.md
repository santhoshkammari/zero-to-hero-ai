# Queue and Deque

> Queues power BFS and level-order processing; deques give you O(1) access to both ends — the backbone of sliding window problems.

## Core Idea

A **queue** is a First-In-First-Out (FIFO) container: elements leave in the same order they arrived, like a line at a coffee shop. A **deque** (double-ended queue) allows O(1) insert and remove from *both* ends. In Python, always use `collections.deque` — never use `list` as a queue because `list.pop(0)` is O(n) (it shifts every element).

## What You Need to Know

### Queue vs Deque Operations

| Operation | Queue (FIFO) | Deque | `collections.deque` |
|-----------|-------------|-------|-------------------|
| Add to back | `enqueue(x)` — O(1) | `push_back(x)` — O(1) | `append(x)` |
| Remove from front | `dequeue()` — O(1) | `pop_front()` — O(1) | `popleft()` |
| Add to front | ✗ | `push_front(x)` — O(1) | `appendleft(x)` |
| Remove from back | ✗ | `pop_back()` — O(1) | `pop()` |
| Peek front | O(1) | O(1) | `deque[0]` |
| Peek back | ✗ | O(1) | `deque[-1]` |

### Why `collections.deque` and Not `list`

| Operation | `list` | `collections.deque` |
|-----------|--------|-------------------|
| `append(x)` (add to end) | O(1) amortized | O(1) |
| `pop()` (remove from end) | O(1) | O(1) |
| `pop(0)` / `popleft()` (remove from front) | **O(n)** — shifts all elements | **O(1)** — doubly linked list |
| `insert(0, x)` / `appendleft(x)` | **O(n)** | **O(1)** |
| Random access `[i]` | O(1) | **O(n)** |

`deque` is implemented as a doubly-linked list of fixed-size blocks, so front/back operations are O(1) but random access is O(n). That trade-off is almost always worth it for queue use cases.

```python
from collections import deque

q = deque()
q.append(1)       # enqueue: [1]
q.append(2)       # enqueue: [1, 2]
q.popleft()       # dequeue: returns 1, queue is [2]
q.appendleft(0)   # add to front: [0, 2]

# Fixed-size deque (automatically drops oldest)
recent = deque(maxlen=3)
recent.append(1)  # [1]
recent.append(2)  # [1, 2]
recent.append(3)  # [1, 2, 3]
recent.append(4)  # [2, 3, 4] — 1 was dropped
```

### BFS Level-Order Pattern

The single most important queue pattern. The trick to processing one level at a time is snapshotting the queue size at the start of each level:

```python
from collections import deque

def bfs_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)  # snapshot: nodes in THIS level
        level = []
        for _ in range(level_size):  # process exactly one level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

Why `for _ in range(len(queue))`? Because the queue grows as you add children, but `level_size` was captured *before* any children were added. This guarantees you process exactly the nodes from one level before moving to the next.

### Implement Stack Using Queues (LC 225)

Use one queue. Make `push` expensive: after appending, rotate all previous elements behind the new one.

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):  # rotate older elements behind new
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
```

Push: O(n) | Pop: O(1)

### Implement Queue Using Stacks (LC 232)

Two stacks: `in_stack` for pushes, `out_stack` for pops. Only transfer when `out_stack` is empty — this gives **amortized O(1)** per operation because each element moves at most twice.

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        if not self.out_stack:  # only transfer when empty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

### Design Circular Queue (LC 622)

Use a fixed-size array with `front` and `rear` pointers that wrap around. The key challenge: distinguishing **full** from **empty** (both have `front == rear` in naive designs). Solution: track `size` separately.

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.data[idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
```

### Design Circular Deque (LC 641)

Same idea as circular queue, but supports front insertion and back removal too.

```python
class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.data[idx] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
```

## Key Patterns & Templates

### Pattern 1: BFS with Level Tracking

```python
from collections import deque

def bfs(start, target):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```

### Pattern 2: Level-by-Level Processing

```python
from collections import deque

def process_by_level(root):
    queue = deque([root])
    depth = 0
    while queue:
        for _ in range(len(queue)):  # exactly one level
            node = queue.popleft()
            # process node at current depth
            for child in node.children:
                queue.append(child)
        depth += 1
```

### Pattern 3: Two-Stack Queue (Amortized O(1))

```python
class AmortizedQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def enqueue(self, val):
        self.push_stack.append(val)

    def dequeue(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Implement Queue using Stacks | 232 | Easy | Two stacks; transfer only when out_stack is empty → amortized O(1) |
| Implement Stack using Queues | 225 | Easy | One queue; rotate after each push to maintain LIFO order |
| Design Circular Queue | 622 | Medium | Fixed array + `front`/`size` pointers; mod arithmetic for wrap-around |
| Design Circular Deque | 641 | Medium | Same as circular queue but `front` moves backward on front insert |
| Number of Recent Calls | 933 | Easy | Queue of timestamps; `popleft` anything older than `t - 3000` |
| Binary Tree Level Order Traversal | 102 | Medium | BFS with `for _ in range(len(queue))` to separate levels |
| Rotting Oranges | 994 | Medium | Multi-source BFS — enqueue all rotten oranges first, then BFS |
| Walls and Gates | 286 | Medium | Multi-source BFS from all gates simultaneously |

## Common Mistakes

- **Using `list.pop(0)` instead of `deque.popleft()`**: This turns your O(n) BFS into O(n²). In interviews, mentioning this shows you understand Python internals.
- **Not snapshotting queue size for level-order**: Writing `for _ in range(len(queue))` works because `range()` evaluates `len(queue)` once. But avoid `while len(queue) > 0` *inside* a level loop — the queue changes as you add children.
- **Circular queue: confusing full vs empty**: If you use only `front` and `rear` pointers without a `size` counter, both full and empty states look the same (`front == rear`). Always track `size` separately.
- **Two-stack queue: transferring every time**: Only transfer from `in_stack` to `out_stack` when `out_stack` is empty. Transferring on every pop breaks amortization and gives O(n) per pop.
- **BFS forgetting to mark visited before enqueuing**: Mark as visited when *adding* to the queue, not when *processing*. Otherwise, you'll add the same node multiple times from different parents.

## Interview Questions

1. **Conceptual**: What's the difference between a queue and a stack? When would you choose one over the other?
2. **Conceptual**: Why is `deque.popleft()` O(1) but `list.pop(0)` O(n) in Python? What's the underlying data structure difference?
3. **Problem**: Implement a queue using two stacks. Prove the amortized time complexity is O(1) per operation.
4. **Problem**: Given a binary tree, return the average value of nodes at each level. (LC 637)
5. **Design**: How would you implement a circular buffer for a streaming data source with fixed memory?
6. **Follow-up**: In the two-stack queue, what happens if pushes and pops are interleaved? Does amortized O(1) still hold?
7. **Problem**: Given a grid with rotten oranges, find the minimum time for all oranges to rot. Why is BFS the right choice here instead of DFS?
8. **Conceptual**: Can you implement a deque using two stacks? What's the complexity?

## Quick Reference

```
Queue = FIFO        Deque = double-ended queue
enqueue → append()  Both ends: append/appendleft, pop/popleft

Python: ALWAYS use collections.deque (not list)
  list.pop(0) is O(n)  ← this alone can TLE your BFS

BFS Level-Order Template:
  queue = deque([root])
  while queue:
      for _ in range(len(queue)):   ← snapshot size
          node = queue.popleft()
          # process node
          queue.append(children)

Two-Stack Queue:
  push → in_stack.append(x)
  pop  → if out_stack empty, transfer all from in_stack
         out_stack.pop()
  Amortized O(1) per operation

Circular Queue:
  rear  = (front + size) % capacity
  full  = (size == capacity)
  empty = (size == 0)
```
