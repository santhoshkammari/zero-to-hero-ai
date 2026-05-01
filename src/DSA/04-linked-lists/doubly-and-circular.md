# Doubly & Circular Linked Lists

> Doubly linked lists unlock O(1) deletion by node reference — that's why they're the backbone of LRU Cache, one of the most common system design interview questions.

## Core Idea

A **doubly linked list (DLL)** adds a `prev` pointer to each node, enabling bidirectional traversal. The killer advantage: if you have a reference to a node, you can delete it in O(1) without knowing its predecessor. A **circular linked list** connects the tail back to the head, forming a ring — useful for round-robin problems and cycle detection.

## What You Need to Know

### Doubly Linked List Node

```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
```

### Operations Comparison

| Operation | Singly | Doubly | Why the difference |
|-----------|--------|--------|--------------------|
| Insert at head | O(1) | O(1) | Both just rewire head |
| Insert at tail (with tail ptr) | O(1) | O(1) | Both just rewire tail |
| Delete given node reference | O(n) | **O(1)** | Singly must find prev by traversal; doubly has `node.prev` |
| Delete at tail | O(n) | O(1) | Singly must find second-to-last; doubly uses `tail.prev` |
| Traverse forward | O(n) | O(n) | Same |
| Traverse backward | ✗ | O(n) | Only doubly can go backward |
| Space per node | 1 pointer | 2 pointers | Extra `prev` pointer |

### DLL Insert & Delete

```python
# Insert new_node after prev_node
def insert_after(prev_node, new_node):
    new_node.prev = prev_node
    new_node.next = prev_node.next
    if prev_node.next:
        prev_node.next.prev = new_node
    prev_node.next = new_node

# Delete a node (given direct reference)
def delete_node(node):
    node.prev.next = node.next
    node.next.prev = node.prev
# O(1) — no traversal needed because we have both prev and next
```

### Sentinel Nodes in DLL

Use **two sentinel nodes** (dummy head and dummy tail) to eliminate all null checks:

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = DLLNode()  # sentinel head
        self.tail = DLLNode()  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_back(self):
        """Remove and return the node just before tail sentinel."""
        node = self.tail.prev
        if node == self.head:
            return None
        self.remove(node)
        return node
```

Why sentinels: `remove()` never needs to check if `node.prev` or `node.next` is None. The sentinels are always there, so every real node has both neighbors.

### LRU Cache = Hash Map + DLL

This is the classic DLL application. The insight: you need O(1) for both lookup (hash map) and recency tracking (DLL).

```python
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}           # key → DLLNode
        self.dll = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.dll.remove(node)     # O(1) remove from current position
        self.dll.add_to_front(node)  # O(1) move to front (most recent)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self.dll.remove(self.cache[key])
        node = DLLNode(key, value)
        self.cache[key] = node
        self.dll.add_to_front(node)
        if len(self.cache) > self.cap:
            evicted = self.dll.pop_back()  # least recently used
            del self.cache[evicted.key]    # need key stored in node for this
# get: O(1), put: O(1)
```

Why store `key` in the node: when you evict from the tail, you need to also delete from the hash map. Without the key in the node, you'd need a reverse lookup.

### Circular Linked List

The **last node's `next` points to the head** instead of `None`.

```python
# Traversal — must stop when we return to start
def traverse_circular(head):
    if not head:
        return
    curr = head
    while True:
        # process curr.val
        curr = curr.next
        if curr == head:
            break
```

Circular lists naturally model anything cyclical: round-robin scheduling, circular buffers, the Josephus problem.

### When to Use What

| Scenario | Use | Reason |
|----------|-----|--------|
| Simple traversal, reversal problems | Singly | Less overhead, simpler code |
| Need O(1) delete by node reference | Doubly | `prev` pointer avoids traversal |
| LRU/LFU cache | Doubly + Hash Map | O(1) access and O(1) eviction |
| Browser back/forward | Doubly | Bidirectional navigation |
| Round-robin, cyclic iteration | Circular | Natural ring structure |
| Cycle detection | Singly + Floyd's | Don't need doubly for this |

## Key Patterns & Templates

### LRU Cache Template

```python
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # key → node
        # Sentinel head (MRU side) and tail (LRU side)
        self.head, self.tail = DLLNode(), DLLNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, value)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

### Flatten Multilevel DLL Template

```python
def flatten(head):
    """Flatten child pointers into a single-level DLL using a stack."""
    if not head:
        return None
    dummy = DLLNode(0)
    dummy.next = head
    prev = dummy
    stack = [head]

    while stack:
        curr = stack.pop()
        prev.next = curr
        curr.prev = prev
        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr

    head.prev = None
    return dummy.next
# Time: O(n), Space: O(n) for stack
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| LRU Cache | 146 | Medium | Hash map (key→node) + DLL (recency order). On access: move to front. On eviction: remove from tail. Store key in node so you can delete from map during eviction. |
| Flatten a Multilevel Doubly Linked List | 430 | Medium | Use a stack: push `next` first, then `child`. Pop gives child-first DFS order. Rewire prev/next as you go, clear child pointers. |
| Convert BST to Sorted Doubly Linked List | 426 | Medium | In-order traversal gives sorted order. Maintain a `prev` pointer — at each node, set `prev.right = curr`, `curr.left = prev`. After traversal, connect head and tail to make it circular. |
| Design Linked List | 707 | Medium | Good practice for implementing DLL with sentinel nodes from scratch. Tests insert/delete at arbitrary index. |
| All O'one Data Structure | 432 | Hard | DLL of frequency buckets + hash map. Similar pattern to LRU — DLL maintains ordering, hash map provides O(1) access. |

## Common Mistakes

- **Forgetting to update both `prev` and `next` pointers** — In DLL, every insert or delete must update pointers in both directions. Missing one creates a broken list.
- **Not storing the key inside the DLL node for LRU** — Without it, you can't find which hash map entry to delete on eviction.
- **Null-checking when you should use sentinels** — If your DLL insert/delete code is full of `if node.prev is not None` checks, add sentinel nodes instead. Cleaner and less error-prone.
- **Confusing circular termination** — In a circular list, `while curr.next` never terminates. You need `while curr.next != head` or a `do-while` equivalent (use `while True` + `break`).
- **Memory leaks from dangling pointers** — In Python, garbage collection handles this, but in interviews you should mention that removed nodes' pointers should be cleared in languages like C++/Java.

## Interview Questions

1. **Implement an LRU Cache with O(1) get and put.** What data structures do you combine and why? *(LC 146)*
2. **Why can't you build an O(1) LRU cache with just a hash map?** What does the DLL give you that the hash map doesn't?
3. **Given a reference to a node in a DLL, delete it in O(1).** Why can't you do this with a singly linked list?
4. **Flatten a multilevel doubly linked list.** Walk through your approach — recursive vs iterative? *(LC 430)*
5. **Convert a BST to a sorted circular doubly linked list in-place.** What traversal order do you use? *(LC 426)*
6. **When would you choose a doubly linked list over an array-based deque?** Discuss the tradeoffs in terms of cache locality, memory, and operation complexity.
7. **How would you detect a cycle in a circular linked list vs an unintentional cycle in a singly linked list?**

## Quick Reference

```
DLL Decision Flowchart:

Need O(1) delete by node reference?
  └─ YES → Doubly linked list

Need O(1) get + O(1) put with eviction?
  └─ LRU Cache → Hash Map + DLL with sentinels

Need to flatten nested/multilevel structure?
  └─ Stack-based DFS + rewire pointers

Need sorted circular from BST?
  └─ In-order traversal + link prev ↔ curr + connect head ↔ tail
```

| Pattern | Time | Space | Key Data Structures |
|---------|------|-------|---------------------|
| LRU Cache (get/put) | O(1) | O(capacity) | Hash map + DLL |
| Flatten multilevel DLL | O(n) | O(n) | Stack |
| BST → sorted circular DLL | O(n) | O(h) | Recursion stack |
| DLL insert/delete at known node | O(1) | O(1) | Just pointer rewiring |
