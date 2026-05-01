# Singly Linked List

> The most common linked list interview topic — reversal, merging, and pointer manipulation show up everywhere.

## Core Idea

A singly linked list is a chain of **nodes** where each node holds a value and a pointer to the next node. Unlike arrays, there's no random access — you must walk from the head. The tradeoff: O(1) insertions/deletions at known positions (no shifting), but O(n) search because you can't index.

## What You Need to Know

### Node Structure

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Operations & Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access by index | O(n) | O(1) | Must traverse from head |
| Search | O(n) | O(1) | Linear scan |
| Insert at head | O(1) | O(1) | Just rewire one pointer |
| Insert at tail (no tail pointer) | O(n) | O(1) | Must walk to end first |
| Insert at tail (with tail pointer) | O(1) | O(1) | Maintain a `tail` reference |
| Insert at middle (given prev node) | O(1) | O(1) | Rewire prev → new → old_next |
| Insert at position k | O(k) | O(1) | Walk k steps, then O(1) rewire |
| Delete at head | O(1) | O(1) | `head = head.next` |
| Delete at tail | O(n) | O(1) | Must find second-to-last |
| Delete node (given prev) | O(1) | O(1) | `prev.next = prev.next.next` |

### The Dummy/Sentinel Node Technique

When your operation might modify the head (insert before head, delete head), use a **dummy node** to avoid special-casing:

```python
dummy = ListNode(0)
dummy.next = head
# ... do your work using dummy as the anchor ...
return dummy.next  # new head
```

Why this works: every real node now has a predecessor. No more "is the list empty?" or "am I deleting the head?" checks. Use this by default in interview problems — it's free safety.

### Traversal

```python
curr = head
while curr:
    # process curr.val
    curr = curr.next
```

### Insert & Delete

```python
# Insert new_node after prev_node
new_node.next = prev_node.next
prev_node.next = new_node

# Delete the node after prev_node
prev_node.next = prev_node.next.next
```

### Reversal Techniques

**Iterative reversal** — the bread and butter. Three pointers: `prev`, `curr`, `next`.

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next   # save next before we overwrite it
        curr.next = prev   # reverse the link
        prev = curr        # advance prev
        curr = nxt         # advance curr
    return prev            # prev is the new head
# Time: O(n), Space: O(1)
```

Think of it as: at each step, you detach `curr` from the forward chain and attach it to the reversed chain anchored at `prev`.

**Reverse a sub-list** (positions m to n) — same logic, but you need to stitch the reversed portion back into the surrounding list.

```python
def reverseBetween(head, left, right):
    dummy = ListNode(0, head)
    prev = dummy

    # Move prev to the node just before position `left`
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    # Reverse (right - left) links
    for _ in range(right - left):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next
# Time: O(n), Space: O(1)
```

**Recursive reversal** — elegant but uses O(n) stack space. Understand how the call stack unwinds:

```python
def reverseRecursive(head):
    if not head or not head.next:
        return head
    new_head = reverseRecursive(head.next)  # recurse to end
    head.next.next = head  # the node after me should point back to me
    head.next = None       # I no longer point forward
    return new_head        # propagate the new head (original tail)
# Time: O(n), Space: O(n) due to call stack
```

The recursion hits the last node first (base case), then as each call returns, it reverses one link. The original tail becomes `new_head` and gets passed all the way back up.

### Merge Two Sorted Lists

A foundational pattern — also the merge step in merge sort on linked lists.

```python
def mergeTwoLists(l1, l2):
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

    curr.next = l1 or l2  # attach whichever list remains
    return dummy.next
# Time: O(n + m), Space: O(1) — just rewiring existing nodes
```

The **dummy head** eliminates all "is the result list empty?" checks. You always have `curr` to append to.

### Deep Copy with Random Pointer

Each node has `.next` and `.random` (points to any node or None). Two approaches:

**Hash map approach** — straightforward, O(n) space:

```python
def copyRandomList(head):
    if not head:
        return None

    old_to_new = {}

    # Pass 1: create cloned nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Pass 2: wire next and random pointers
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]
# Time: O(n), Space: O(n)
```

**Interweaving approach** — O(1) extra space by embedding clones between originals:

```python
def copyRandomList(head):
    if not head:
        return None

    # Step 1: Interleave — A → A' → B → B' → C → C'
    curr = head
    while curr:
        clone = Node(curr.val, curr.next)
        curr.next = clone
        curr = clone.next

    # Step 2: Set random pointers on clones
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the two lists
    dummy = Node(0)
    copy_curr = dummy
    curr = head
    while curr:
        copy_curr.next = curr.next
        curr.next = curr.next.next
        copy_curr = copy_curr.next
        curr = curr.next

    return dummy.next
# Time: O(n), Space: O(1) extra (excluding output)
```

Why interweaving works: by placing each clone right after its original, `original.random.next` is always the clone of `original.random`. No hash map needed.

## Key Patterns & Templates

### Iterative Reversal Template

```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev
```

### Dummy Node Template

```python
dummy = ListNode(0)
dummy.next = head
# work with dummy as anchor
return dummy.next
```

### Merge Template

```python
dummy = ListNode(0)
curr = dummy
while l1 and l2:
    if l1.val <= l2.val:
        curr.next, l1 = l1, l1.next
    else:
        curr.next, l2 = l2, l2.next
    curr = curr.next
curr.next = l1 or l2
return dummy.next
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Reverse Linked List | 206 | Easy | Three pointers: prev, curr, next. Save `curr.next` before overwriting. Recursive version: `reverse(head.next)` returns new head, then `head.next.next = head; head.next = None`. |
| Merge Two Sorted Lists | 21 | Easy | Dummy head avoids all "is result empty?" checks. Compare heads, attach smaller, advance that pointer. |
| Copy List with Random Pointer | 138 | Medium | Hash map: two passes (create clones, wire pointers). O(1) space: interleave clones between originals, set random via `curr.random.next`, then separate. |
| Reorder List | 143 | Medium | Three steps: find middle (slow/fast), reverse second half, merge alternating. Combines three fundamental patterns into one problem. |
| Reverse Linked List II | 92 | Medium | Reverse a sub-list between positions m and n. Use dummy node, walk to position m−1, then reverse (n−m) links in-place. |
| Reverse Nodes in k-Group | 25 | Hard | Check if k nodes remain, reverse that group, recurse/iterate on the rest. Track the tail of each reversed group to stitch groups together. |
| Palindrome Linked List | 234 | Easy | Find middle → reverse second half → compare with first half. O(1) space but modifies the list (optionally restore it). |

## Common Mistakes

- **Losing the head reference** — If your operation might change the head, use a dummy node. Forgetting this leads to returning the wrong list.
- **Null pointer errors** — Always check `node is not None` before accessing `node.next`. The `while curr and curr.next` pattern prevents this.
- **Creating cycles during reversal** — When reversing, if you forget to set the original head's `.next = None`, you create a cycle. The old head still points forward.
- **Not handling single-node or two-node lists** — Your algorithm works on length 5 but crashes on length 1. Test edge cases explicitly.
- **Mutating the input unintentionally** — Linked list operations are in-place by nature. If the problem expects the original list intact, clone first.

## Interview Questions

1. **Reverse a linked list iteratively and recursively.** Explain the time and space tradeoffs. *(LC 206)*
2. **Merge two sorted linked lists in O(1) space.** Why is a dummy node helpful here? *(LC 21)*
3. **How would you detect if reversing created a cycle?** What invariant must hold after reversal?
4. **Deep copy a linked list with random pointers using O(1) extra space.** Walk through the interweaving technique. *(LC 138)*
5. **Reorder a list as L0 → Ln → L1 → Ln-1 → ...** Which sub-problems does this decompose into? *(LC 143)*
6. **Reverse nodes in groups of k.** How do you handle the case where fewer than k nodes remain? *(LC 25)*
7. **Check if a linked list is a palindrome in O(1) space.** What's the tradeoff vs using a stack? *(LC 234)*
8. **Why are linked lists preferred over arrays for merge sort on external data?** Think about sequential access and merge cost.
9. **Reverse only the sublist from position m to n.** What nodes do you need to track before starting the reversal? *(LC 92)*

## Quick Reference

```
Singly Linked List Decision Flowchart:

Need to modify head?
  └─ YES → Use dummy/sentinel node

Need to reverse?
  ├─ Whole list → 3-pointer iterative (O(n) time, O(1) space)
  ├─ Sub-list m..n → Walk to m-1, reverse (n-m) links
  └─ In groups of k → Check length, reverse group, stitch

Need to merge sorted lists?
  └─ Dummy head + compare-and-attach + append remainder

Need to copy with random pointers?
  ├─ O(n) space okay → Hash map (2 passes)
  └─ O(1) space needed → Interweave → set random → separate
```

| Operation | Time | Space |
|-----------|------|-------|
| Iterative reversal | O(n) | O(1) |
| Recursive reversal | O(n) | O(n) |
| Merge two sorted | O(n+m) | O(1) |
| Copy with random (hash map) | O(n) | O(n) |
| Copy with random (interweave) | O(n) | O(1) |
| Reverse sub-list m..n | O(n) | O(1) |
| Reverse in k-groups | O(n) | O(1) |
