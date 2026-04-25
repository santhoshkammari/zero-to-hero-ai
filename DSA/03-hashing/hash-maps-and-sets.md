# Hash Maps and Sets

> Hash maps are your Swiss Army knife. O(1) lookup transforms brute force into elegance. ~25% of interview problems use hashing.

## Core Idea

A hash map maps keys → values with **O(1) average** insert/lookup/delete by converting keys to array indices via a hash function. A hash set is a hash map without values — just membership testing.

The catch: **O(n) worst case** with bad hash functions or pathological inputs, but interviewers almost always accept O(1) average.

```
key → hash(key) → index → bucket → value
         ↓
  deterministic integer that distributes evenly across buckets
```

---

## What You Need to Know

### Python `dict` and `set` Internals

`dict` is a hash table. `set` is the same structure but stores keys only.

```python
d = {}
d["key"] = "value"    # O(1) avg insert
d["key"]              # O(1) avg lookup
"key" in d            # O(1) avg membership
del d["key"]          # O(1) avg delete

s = set()
s.add(5)              # O(1)
5 in s                # O(1)
s.remove(5)           # O(1), raises KeyError if missing
s.discard(5)          # O(1), no error if missing

# Set operations — all O(min(len(a), len(b)))
a | b   # union
a & b   # intersection
a - b   # difference
a ^ b   # symmetric difference
```

### Hash Function Basics

- **Deterministic**: same input → same output, always.
- **Uniform distribution**: minimize collisions by spreading keys across buckets.
- Python's `hash()` handles built-in types. For custom keys, use **tuples** (hashable), not lists (mutable → unhashable).

```python
hash("hello")       # works — strings are immutable
hash((1, 2, 3))     # works — tuples of hashables are hashable
hash([1, 2, 3])     # TypeError — lists are mutable
hash(frozenset({1})) # works — frozenset is the hashable version of set
```

### Collision Resolution

Two keys hash to the same index. Two strategies:

**Chaining** — each bucket holds a linked list of colliding entries:
```
bucket[3] → ("cat", 5) → ("dog", 7) → None
```

**Open addressing (probing)** — find the next empty slot. Python uses a variant of this:
```
hash(key) → index 3 (occupied) → probe index 7 → probe index 12 (empty) → insert
```

**Load factor** = n_elements / n_buckets. Python resizes the table when load factor hits ~2/3, roughly doubling capacity. This keeps average chain length short → O(1) amortized.

### `Counter` (collections)

Frequency counting in one line:

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

freq.most_common(2)          # [('apple', 3), ('banana', 2)]
freq["apple"]                # 3
freq["missing"]              # 0 (not KeyError)

# Merge counters
Counter("aab") + Counter("bcc")  # Counter({'b': 2, 'a': 2, 'c': 2})
Counter("aab") - Counter("ab")   # Counter({'a': 1}) — drops zero/negative

# Iteration over elements (with repeats)
list(freq.elements())  # ['apple', 'apple', 'apple', 'banana', 'banana', 'cherry']
```

### `defaultdict`

Auto-initializes missing keys with a factory function:

```python
from collections import defaultdict

# Grouping pattern
groups = defaultdict(list)
for word in ["eat", "tea", "tan", "ate", "nat", "bat"]:
    key = tuple(sorted(word))
    groups[key].append(word)
# {('a','e','t'): ['eat','tea','ate'], ('a','n','t'): ['tan','nat'], ('a','b','t'): ['bat']}

# Counting pattern
counts = defaultdict(int)
for ch in "abracadabra":
    counts[ch] += 1
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Nested default — adjacency list
graph = defaultdict(set)
graph["A"].add("B")
graph["A"].add("C")
```

### `OrderedDict`

`dict` preserves insertion order in Python 3.7+, but `OrderedDict` adds `move_to_end()` — critical for LRU cache:

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

od.move_to_end("a")         # moves "a" to end (most recent)
od.move_to_end("c", last=False)  # moves "c" to front (least recent)
od.popitem(last=False)       # pops from front → ("c", 3) — evict LRU
```

### When NOT to Use Hashing

| Use Case | Better Alternative |
|---|---|
| Need sorted/ordered traversal | BST (`SortedList` from sortedcontainers) |
| Guaranteed worst-case O(1) | Arrays with direct indexing |
| Keys aren't hashable | Convert to hashable form or use other structures |
| Need range queries (all keys in [a, b]) | BST or sorted array + binary search |
| Memory-critical (hash tables waste ~30-50% space) | Sorted array |

---

## Key Patterns & Templates

### 1. Two Sum — Hash Map Complement Lookup

**Pattern**: for each element, check if `target - num` is already in the map.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Why store-as-you-go works: we only need ONE pair, and checking before
# storing avoids using the same element twice.

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
```

**Time**: O(n) — single pass. **Space**: O(n).

---

### 2. Frequency Counting

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Manual version — useful when you need more control
def is_anagram_manual(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = [0] * 26
    for a, b in zip(s, t):
        freq[ord(a) - ord('a')] += 1
        freq[ord(b) - ord('a')] -= 1
    return all(f == 0 for f in freq)

# Top K Frequent — bucket sort approach O(n)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    # Bucket sort: index = frequency, value = list of nums with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result

assert top_k_frequent([1,1,1,2,2,3], 2) == [1, 2]
```

---

### 3. Group Anagrams — Custom Key Design

**Pattern**: design a key that maps equivalent items to the same bucket.

```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        # Option A: sorted string as key — O(k log k) per word
        # key = tuple(sorted(s))

        # Option B: frequency tuple as key — O(k) per word
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)

        groups[key].append(s)
    return list(groups.values())

assert sorted([sorted(g) for g in group_anagrams(["eat","tea","tan","ate","nat","bat"])]) == \
       sorted([sorted(g) for g in [["eat","tea","ate"],["tan","nat"],["bat"]]])
```

**Key design is the creative part**. Other examples:
- Grouping by digit frequency: `tuple(sorted(str(n)))` for nums with same digits
- Grouping by word pattern: `"abb" → (0,1,1)` mapping each char to first-seen index

---

### 4. Longest Consecutive Sequence — Set + Start Detection

```python
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0
    for n in num_set:
        # Only start counting from sequence START
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best

# Why O(n): each number is visited at most twice —
# once in the outer loop, once in a while loop from its sequence start.
# The "if n-1 not in num_set" ensures we only enter the while loop
# for sequence starts, so the total inner iterations across all
# outer iterations is O(n).

assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1,2,3,4]
assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
```

---

### 5. LRU Cache ⭐

**THE design question at FAANG.** Two implementations — know both.

#### Version A: Using `OrderedDict` (clean, Pythonic)

```python
from collections import OrderedDict

class LRUCache:
    """
    Least Recently Used Cache.
    - get(key): return value if exists, mark as most recently used
    - put(key, value): insert/update, evict LRU if over capacity
    Both operations O(1).
    """
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
            self.cache.move_to_end(key)  # update position
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict LRU (front of order)

# Test
lru = LRUCache(2)
lru.put(1, 1)       # cache: {1=1}
lru.put(2, 2)       # cache: {1=1, 2=2}
assert lru.get(1) == 1   # cache: {2=2, 1=1} — 1 moved to end
lru.put(3, 3)       # evicts key 2 → cache: {1=1, 3=3}
assert lru.get(2) == -1  # 2 was evicted
lru.put(4, 4)       # evicts key 1 → cache: {3=3, 4=4}
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4
```

#### Version B: Hash Map + Doubly Linked List (what interviewers really want)

This is the from-scratch implementation. You need to understand this cold.

**Data structures**:
- **Doubly linked list**: maintains access order. Head = LRU, Tail = MRU.
- **Hash map**: `key → node` for O(1) node lookup (so we can remove/move nodes in O(1)).

```
HEAD ↔ [LRU node] ↔ [node] ↔ ... ↔ [MRU node] ↔ TAIL
         ↑                              ↑
     evict this                   most recent

HashMap: { key1: node1, key2: node2, ... }
```

```python
class Node:
    __slots__ = ('key', 'val', 'prev', 'next')

    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node

        # Sentinel nodes — eliminates edge cases for empty list
        self.head = Node()  # dummy head (LRU side)
        self.tail = Node()  # dummy tail (MRU side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove node from its current position in the DLL."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node: Node) -> None:
        """Add node right before tail (MRU position)."""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move to MRU position
        self._remove(node)
        self._add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing: remove old position, will re-add at end
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_end(node)

        if len(self.cache) > self.capacity:
            # Evict LRU: node right after head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]  # need key stored in node for this!

# Test — same sequence as above
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
assert lru.get(1) == 1
lru.put(3, 3)
assert lru.get(2) == -1
lru.put(4, 4)
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4
```

**Why store `key` in the Node?** When evicting LRU, we need the key to delete it from the hash map. The node alone doesn't tell us the key unless we store it.

**Why sentinel nodes?** Without them, `_remove` and `_add_to_end` need null checks for head/tail. Sentinels make every real node have valid `prev` and `next`.

**Complexity**: O(1) for both `get` and `put` — hash map lookup + constant DLL pointer operations.

---

### 6. Subarray Sum Equals K — Prefix Sum + Hash Map

**The crossover pattern** — combines prefix sums with Two Sum logic.

**Insight**: `sum(nums[i:j]) == k` iff `prefix[j] - prefix[i] == k` iff `prefix[i] == prefix[j] - k`.

```python
def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    # How many times each prefix sum has occurred
    prefix_count = {0: 1}  # ← critical: empty prefix (subarray starting at index 0)

    for num in nums:
        prefix += num
        # How many previous prefixes equal (prefix - k)?
        # Each one represents a subarray summing to k
        count += prefix_count.get(prefix - k, 0)
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    return count

assert subarray_sum([1, 1, 1], 2) == 2       # [1,1] at index 0-1 and 1-2
assert subarray_sum([1, 2, 3], 3) == 2        # [1,2] and [3]
assert subarray_sum([1, -1, 0], 0) == 3       # [1,-1], [-1,0], [1,-1,0]
```

**Why `{0: 1}`?** If `prefix` itself equals `k`, then `prefix - k = 0`, and we need to count that. The `0: 1` entry represents the empty prefix before index 0.

**This pattern generalizes**: divisible by k (use prefix % k), subarray sum in range, etc.

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Two Sum | 1 | Easy | Complement lookup: check if `target - num` in map. Store as you go. O(n). |
| Group Anagrams | 49 | Medium | Hash key = `sorted(word)` or `tuple` of char frequencies. Groups by equivalence. |
| Longest Consecutive Sequence | 128 | Medium | Put all in set. Only count from sequence START (`x-1` not in set). O(n) despite inner loop. |
| Top K Frequent Elements | 347 | Medium | Count freq + bucket sort by frequency. O(n). Or min-heap of size k: O(n log k). |
| LRU Cache | 146 | Medium | Hash map + doubly linked list. O(1) get and put. Move to front on access, evict from tail. |
| Subarray Sum Equals K | 560 | Medium | Prefix sum + hash map. At each index: count of `(prefix - k)` seen before. Two Sum on prefix sums. |
| Valid Anagram | 242 | Easy | Single frequency array: increment for s, decrement for t. All zeros = anagram. |
| Encode and Decode Strings | 271 | Medium | Length-prefix encoding: `"4#word"` — delimiter alone fails because strings may contain any character. |

### Encode and Decode Strings (LC 271)

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        # "4#word3#abc" — length prefix makes any content safe
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)           # find the # delimiter
            length = int(s[i:j])          # extract the length
            result.append(s[j + 1:j + 1 + length])  # extract the string
            i = j + 1 + length
        return result

codec = Codec()
original = ["hello", "world", "#tricky", "12#ab", ""]
assert codec.decode(codec.encode(original)) == original
```

---

## Common Mistakes

1. **Assuming hash map is always O(1)** — worst case is O(n) with hash collisions. Interviewers know this; mention it proactively.

2. **Mutable keys** — lists can't be dict keys. Convert to tuples:
   ```python
   d = {}
   d[[1, 2]] = "x"       # TypeError
   d[tuple([1, 2])] = "x" # works
   ```

3. **Longest Consecutive: O(n²) trap** — iterating from every element instead of only sequence starts:
   ```python
   # WRONG — starts counting from every element
   for n in num_set:
       length = 1
       while n + length in num_set:
           length += 1
   
   # RIGHT — skip non-starts
   for n in num_set:
       if n - 1 not in num_set:  # ← this line makes it O(n)
           ...
   ```

4. **Dict iteration order** — guaranteed insertion-order in Python 3.7+. Don't assume this in other languages.

5. **Two Sum: storing all first vs store-as-you-go** — storing all indices upfront fails with duplicates like `[3, 3], target=6` (second 3 overwrites first). Store-as-you-go naturally handles this.

6. **LRU Cache: forgetting to update position on GET** — `get` must move the node to MRU position, not just `put`.

7. **Prefix sum: forgetting `{0: 1}`** — without it, subarrays starting at index 0 are missed:
   ```python
   # nums = [3], k = 3
   # prefix = 3, looking for prefix - k = 0
   # Without {0: 1}, we'd miss this subarray
   ```

---

## Interview Questions

1. **"Solve Two Sum in O(n). What data structure and why?"**
   → Hash map. One pass: for each num, check if complement exists. Hash map gives O(1) lookup.

2. **"Group Anagrams — what do you use as the hash key?"**
   → `tuple(sorted(s))` is simplest — O(k log k). For O(k), use a 26-length tuple of character counts.

3. **"Longest Consecutive in O(n) — why O(n) despite the inner while loop?"**
   → The while loop only runs for sequence starts. Each element is counted exactly once across all while loop iterations. Total work = O(n).

4. **"Design an LRU Cache with O(1) get and put."**
   → Hash map (key → node) + doubly linked list (access order). Get: lookup in map, move node to tail. Put: insert at tail, if over capacity, evict from head. Sentinels simplify edge cases.

5. **"What happens with too many collisions?"**
   → Python uses open addressing with perturbation-based probing. On high load factor (~2/3), it resizes to keep O(1) average. Worst case is O(n) if all keys collide.

6. **"Count subarrays summing to K — explain prefix sum + hash map."**
   → Maintain running prefix sum. At each index, `prefix - k` tells us what earlier prefix would create a valid subarray. Hash map counts occurrences of each prefix sum. Initialize with `{0: 1}`.

7. **"When would you use a set vs a dict?"**
   → Set for membership testing / deduplication. Dict when you need to associate values with keys. Same underlying hash table.

8. **"How would you design a hash function for a custom object?"**
   → Implement `__hash__` using immutable fields. Combine field hashes: `hash((self.x, self.y))`. Must also implement `__eq__`. Objects that compare equal must have the same hash.

9. **"Top K Frequent — better than O(n log n)?"**
   → Bucket sort on frequency: O(n). Create array of size n+1, index = freq, value = list of elements. Walk from end, collect first k.

10. **"Encode/Decode Strings — why not just a comma delimiter?"**
    → Strings can contain commas (or any character). Length-prefix encoding (`"4#word"`) is unambiguous because we know exactly how many characters to read.

---

## Quick Reference

| Pattern | When to Use | Template |
|---|---|---|
| Complement lookup | Two Sum, pair problems | `if target - num in seen: found; seen[num] = i` |
| Frequency count | Anagram, top-k, duplicates | `Counter(iterable)` or `freq[x] += 1` |
| Grouping | Anagrams, equivalence classes | `groups[key(item)].append(item)` |
| Existence check | Consecutive sequence, dedup | `set` for O(1) membership |
| Hash map + linked list | LRU/LFU cache | `OrderedDict` or manual DLL + dict |
| Prefix sum + hash map | Subarray sum problems | `count += seen[prefix - k]; seen[prefix] += 1` |
