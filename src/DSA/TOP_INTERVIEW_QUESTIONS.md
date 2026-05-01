# 🎯 The Definitive DSA Interview Question Bank

> Curated from real interview loops at Google, Microsoft, and Amazon.
> Every question here is a **gateway problem** — master it, and you unlock 5–10 variants.

---

## 1. Arrays & Strings (Two Pointers, Sliding Window, Prefix Sums)

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Two Sum** | 1 | Easy | Hash Map Lookup |
| 2 | **Best Time to Buy and Sell Stock** | 121 | Easy | Kadane's / Running Min |
| 3 | **Product of Array Except Self** | 238 | Medium | Prefix & Suffix Products |
| 4 | **Container With Most Water** | 11 | Medium | Two Pointers (Greedy Shrink) |
| 5 | **Longest Substring Without Repeating Characters** | 3 | Medium | Sliding Window |
| 6 | **Minimum Window Substring** | 76 | Hard | Sliding Window + Hash Map |
| 7 | **Subarray Sum Equals K** | 560 | Medium | Prefix Sum + Hash Map |
| 8 | **Trapping Rain Water** | 42 | Hard | Two Pointers / Monotonic Stack |

### Why These Matter & The "Aha" Insights

**LC 1 – Two Sum**
- **Why:** The #1 most-asked question in phone screens. Tests if you can think "complement lookup" instead of brute-force.
- **Aha:** Don't search for pairs — for each element, ask: *"Have I already seen my complement (target - num)?"* Store what you've seen in a hash map. This `complement = target - current` pattern recurs in dozens of problems.

**LC 121 – Best Time to Buy and Sell Stock**
- **Why:** Tests greedy/single-pass thinking. Amazon asks this in every batch of OAs.
- **Aha:** Track `min_price_so_far` as you iterate. At each price, the best profit is `price - min_so_far`. You never need to look backward — the answer builds forward. This is baby Kadane's algorithm.

**LC 238 – Product of Array Except Self**
- **Why:** Tests prefix/suffix decomposition WITHOUT division. Google loves the follow-up: "do it in O(1) extra space."
- **Aha:** Any "all except current" problem decomposes into `left_product[i] * right_product[i]`. Build left-to-right pass, then right-to-left pass. The O(1) space trick: reuse the output array for left products, then sweep right with a running variable.

**LC 11 – Container With Most Water**
- **Why:** THE gateway two-pointer problem. If you understand *why* it's correct, you understand two-pointer proofs.
- **Aha:** Start pointers at both ends. Move the **shorter** pointer inward. Why? The shorter line is the bottleneck — moving the taller one can only decrease width without increasing height. You're never skipping a potential answer.

**LC 3 – Longest Substring Without Repeating Characters**
- **Why:** The canonical sliding window problem. Amazon/Microsoft phone screens.
- **Aha:** Maintain a window `[left, right]` with a set of characters. When you see a duplicate, shrink from the left until the window is valid again. Optimization: use a hash map storing last-seen index and jump `left` directly to `last_seen[char] + 1`.

**LC 76 – Minimum Window Substring**
- **Why:** The hardest standard sliding window. If you can solve this, you can solve any sliding window problem.
- **Aha:** Use two hash maps: `need` (required char counts) and `have` (current window counts). Track a `formed` counter for how many unique chars meet their required count. Expand `right` to find a valid window, then shrink `left` to minimize it. The template: **expand → validate → shrink → record**.

**LC 560 – Subarray Sum Equals K**
- **Why:** The prefix sum + hash map combo is tested at Google constantly. It's the bridge between arrays and hashing.
- **Aha:** If `prefix[j] - prefix[i] = k`, then subarray `(i, j]` sums to k. So at each index, ask: *"How many times have I seen `prefix_sum - k` before?"* This is Two Sum, but for prefix sums.

**LC 42 – Trapping Rain Water**
- **Why:** Google's favorite "hard" array problem. Tests whether you can see the structure in the problem.
- **Aha:** Water at position `i` = `min(max_left[i], max_right[i]) - height[i]`. Two-pointer version: maintain `left_max` and `right_max`. Process from the side with the smaller max — you know the water level there is determined by YOUR side's max.

---

## 2. Hashing

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Group Anagrams** | 49 | Medium | Custom Key Design |
| 2 | **Top K Frequent Elements** | 347 | Medium | Counting + Bucket Sort |
| 3 | **Longest Consecutive Sequence** | 128 | Medium | Set + Sequence Start |
| 4 | **Valid Anagram** | 242 | Easy | Frequency Count |
| 5 | **LRU Cache** | 146 | Medium | Hash Map + Doubly Linked List |
| 6 | **Encode and Decode Strings** | 271 | Medium | Delimiter Design |

### Why These Matter & The "Aha" Insights

**LC 49 – Group Anagrams**
- **Why:** Tests your ability to design a hash key. This pattern appears in clustering, dedup, and grouping problems.
- **Aha:** Two strings are anagrams iff they have the same sorted characters (or the same character frequency tuple). Use `sorted(word)` or `tuple(count[0..25])` as the dictionary key. The real lesson: **when you need to group, design the right equivalence key**.

**LC 347 – Top K Frequent Elements**
- **Why:** Amazon asks this constantly. Tests counting + selection.
- **Aha:** Count frequencies with a hash map, then use **bucket sort**: create array of size `n+1` where index = frequency, value = list of elements with that frequency. Walk buckets from right to left to get top K. This avoids O(n log n) sorting. Alternative: use a min-heap of size K.

**LC 128 – Longest Consecutive Sequence**
- **Why:** Tests O(n) thinking with sets. Google interview classic.
- **Aha:** Put everything in a set. Only start counting from **sequence beginnings** — a number `x` is a start if `x-1` is NOT in the set. Then count `x, x+1, x+2...` This is O(n) because each element is visited at most twice (once in outer loop, once in inner expansion).

**LC 242 – Valid Anagram**
- **Why:** Warm-up that validates you understand frequency counting — the backbone of many string problems.
- **Aha:** Count characters in both strings using an array of size 26 (or a hash map). Increment for string1, decrement for string2. If all counts are 0, they're anagrams. The single-array trick is the insight.

**LC 146 – LRU Cache**
- **Why:** THE design question. Asked at all three companies. Tests data structure composition.
- **Aha:** You need O(1) get AND O(1) put. Hash map gives O(1) lookup; doubly linked list gives O(1) removal/insertion. Combine them: map stores `key → node`, list maintains recency order. On access, move node to front. On eviction, remove from tail. **This "hash map + ordered structure" combo is a design pattern you'll reuse.**

**LC 271 – Encode and Decode Strings**
- **Why:** Tests protocol/serialization thinking. Common at Google.
- **Aha:** You can't use a simple delimiter because the strings might contain it. Use **length-prefix encoding**: `"4#word5#hello"`. Each string is encoded as `len + "#" + string`. This is how real network protocols work.

---

## 3. Linked Lists

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Reverse Linked List** | 206 | Easy | Iterative Pointer Rewiring |
| 2 | **Linked List Cycle (+ II)** | 141/142 | Easy/Med | Floyd's Cycle Detection |
| 3 | **Merge Two Sorted Lists** | 21 | Easy | Dummy Head + Merge |
| 4 | **Merge K Sorted Lists** | 23 | Hard | Divide & Conquer / Min-Heap |
| 5 | **Reorder List** | 143 | Medium | Find Middle + Reverse + Merge |
| 6 | **Copy List with Random Pointer** | 138 | Medium | Hash Map Clone / Interleave |

### Why These Matter & The "Aha" Insights

**LC 206 – Reverse Linked List**
- **Why:** The fundamental linked list operation. Used as a subroutine in 10+ other problems (reverse k-group, palindrome list, reorder list).
- **Aha:** Three pointers: `prev`, `curr`, `next`. At each step: save next, point curr to prev, advance prev and curr. The key: **you must save `curr.next` before you overwrite it**. Recursive version: `reverse(head.next)` returns new head; then `head.next.next = head; head.next = null`.

**LC 141/142 – Linked List Cycle**
- **Why:** Floyd's algorithm is one of those "either you know it or you don't" concepts. Amazon loves it.
- **Aha (141):** Slow pointer moves 1 step, fast moves 2. If they meet, there's a cycle. **(142 — finding the start):** After they meet, put one pointer back at head. Move both at speed 1. They meet at the cycle start. **Mathematical proof:** if the non-cycle part has length `a` and the meeting point is `b` steps into the cycle of length `c`, then `a = c - b`. This same technique detects duplicates in LC 287.

**LC 21 – Merge Two Sorted Lists**
- **Why:** Subroutine for merge sort and merge-K problems. Tests clean pointer manipulation.
- **Aha:** Use a **dummy head** node to avoid edge cases with the first element. Compare heads of both lists, attach the smaller one, advance that pointer. At the end, attach whatever remains. The dummy head trick eliminates all "is the result list empty?" checks.

**LC 23 – Merge K Sorted Lists**
- **Why:** The jump from "merge 2" to "merge K" tests algorithmic thinking. Google/Amazon favorite.
- **Aha:** **Divide and conquer:** pair up lists and merge each pair, reducing K lists to K/2, then K/4, etc. This is O(N log K). Alternative: min-heap of size K holding the head of each list. Pop min, push its next. Both are O(N log K) but D&C has better constants.

**LC 143 – Reorder List**
- **Why:** Combines three fundamental techniques in one problem. Common at Amazon.
- **Aha:** Three steps: (1) Find middle using slow/fast pointers, (2) Reverse the second half, (3) Merge the two halves by alternating. Each step is a standalone pattern — this problem tests whether you can compose them.

**LC 138 – Copy List with Random Pointer**
- **Why:** Tests deep copy logic with non-trivial references. Microsoft/Amazon.
- **Aha:** **Hash map approach:** First pass creates a map `original_node → cloned_node`. Second pass wires up `next` and `random` using the map. **O(1) space trick:** Interleave cloned nodes (`A → A' → B → B' → ...`), set random pointers using `node.next.random = node.random.next`, then separate the lists. The hash map approach is cleaner and preferred in interviews.

---

## 4. Stacks & Queues (Including Monotonic Stack)

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Valid Parentheses** | 20 | Easy | Stack Matching |
| 2 | **Min Stack** | 155 | Medium | Auxiliary State Stack |
| 3 | **Daily Temperatures** | 739 | Medium | Monotonic Decreasing Stack |
| 4 | **Next Greater Element I** | 496 | Easy | Monotonic Stack + Hash Map |
| 5 | **Largest Rectangle in Histogram** | 84 | Hard | Monotonic Stack (Classic) |
| 6 | **Evaluate Reverse Polish Notation** | 150 | Medium | Operand Stack |
| 7 | **Sliding Window Maximum** | 239 | Hard | Monotonic Deque |

### Why These Matter & The "Aha" Insights

**LC 20 – Valid Parentheses**
- **Why:** The definitive "use a stack" warm-up. Every company asks this or a variant.
- **Aha:** Push opening brackets. On a closing bracket, check if the top of stack is its match. If not, invalid. If stack is non-empty at the end, invalid. The general pattern: **stacks are for matching nested structures**.

**LC 155 – Min Stack**
- **Why:** Tests augmenting a data structure with extra state. Design-oriented.
- **Aha:** Store `(value, current_min)` pairs on the stack. Each entry remembers what the minimum was at that point in the stack's history. When you pop, the previous min is automatically restored. **Lesson:** you can "snapshot" state at each level of a stack.

**LC 739 – Daily Temperatures**
- **Why:** THE gateway to monotonic stacks. Once you get this, you get the entire pattern family.
- **Aha:** Maintain a stack of **indices** (not values) in decreasing temperature order. For each new temperature, pop all stack entries with lower temperatures — those entries just found their "next warmer day." **The monotonic stack pattern: "for each element, find the next greater/smaller element in O(n)."**

**LC 496 – Next Greater Element I**
- **Why:** Simpler variant of the monotonic stack pattern; good for building intuition before LC 739/84.
- **Aha:** Process `nums2` with a monotonic stack to precompute "next greater element" for every value. Store results in a hash map. Then look up answers for `nums1`. The key: precompute the relationship on the full array, then query.

**LC 84 – Largest Rectangle in Histogram**
- **Why:** One of the hardest stack problems. The "boss fight" of monotonic stacks. Google/Amazon.
- **Aha:** For each bar, you need to know how far it can extend left and right (i.e., the nearest shorter bar on each side). Maintain an increasing stack of indices. When a shorter bar arrives, pop and calculate the area for each popped bar. **The popped bar's width extends from the new stack top to the current index.** This same technique solves "Maximal Rectangle" (LC 85).

**LC 150 – Evaluate Reverse Polish Notation**
- **Why:** Classic stack problem. Tests that you understand postfix evaluation.
- **Aha:** Numbers go on the stack. Operators pop two operands, compute, push result. **Order matters for subtraction/division:** second popped element is the left operand. This same pattern applies to expression parsing problems.

**LC 239 – Sliding Window Maximum**
- **Why:** Combines sliding window with monotonic data structure. Hard but extremely common.
- **Aha:** Use a **monotonic decreasing deque** of indices. The front of the deque is always the max of the current window. When adding a new element, pop from the back while the new element is larger (they can never be the max while the new element exists). Remove from front if the index is outside the window. This gives O(n) amortized.

---

## 5. Binary Search

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Binary Search** | 704 | Easy | Classic Template |
| 2 | **Search in Rotated Sorted Array** | 33 | Medium | Modified Binary Search |
| 3 | **Find Minimum in Rotated Sorted Array** | 153 | Medium | Binary Search on Condition |
| 4 | **Koko Eating Bananas** | 875 | Medium | Binary Search on Answer |
| 5 | **Search a 2D Matrix** | 74 | Medium | Flattened Binary Search |
| 6 | **Time Based Key-Value Store** | 981 | Medium | Binary Search on Timestamps |
| 7 | **Median of Two Sorted Arrays** | 4 | Hard | Binary Search on Partition |

### Why These Matter & The "Aha" Insights

**LC 704 – Binary Search**
- **Why:** The template everything else builds on. Get the boundary conditions right here.
- **Aha:** Use `left, right = 0, len-1` and `while left <= right`. Compute `mid = left + (right - left) // 2` to avoid overflow. The three templates (inclusive, exclusive, left-bound) all derive from this. **Master the invariant: what does `left` point to when the loop ends?**

**LC 33 – Search in Rotated Sorted Array**
- **Why:** The #1 binary search interview question. Google/Amazon.
- **Aha:** At each step, one half is always sorted. Check which half is sorted, then check if the target falls in that sorted half. If yes, search there. If no, search the other half. **The key question at each mid: "which half is sorted, and is my target in it?"**

**LC 153 – Find Minimum in Rotated Sorted Array**
- **Why:** Tests binary search on a condition rather than a target value.
- **Aha:** Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]`, the minimum is in the right half. Otherwise, it's in the left half (including mid). **You're binary searching for the "inflection point" — the transition from large to small.**

**LC 875 – Koko Eating Bananas**
- **Why:** THE gateway "binary search on answer" problem. This pattern covers 20+ LeetCode problems.
- **Aha:** You're not searching an array — you're searching the **answer space** `[1, max(piles)]`. For each candidate speed `k`, check if Koko can finish in time (linear scan). If yes, try smaller. If no, try larger. **Template: "binary search on the answer when you can verify a candidate in O(n)."** Same pattern: LC 1011 (ship packages), LC 410 (split array), LC 774 (minimize max distance).

**LC 74 – Search a 2D Matrix**
- **Why:** Tests if you can see a 2D matrix as a 1D sorted array.
- **Aha:** Treat the matrix as a single sorted array of `m*n` elements. Index `k` maps to `matrix[k // n][k % n]`. Then apply standard binary search. **Any time you have a sorted 2D structure, consider flattening it mentally.**

**LC 981 – Time Based Key-Value Store**
- **Why:** Tests binary search in a design context. Google favorite.
- **Aha:** For each key, store a list of `(timestamp, value)` pairs. On `get(key, timestamp)`, binary search for the largest timestamp ≤ the query. Use `bisect_right` and return the element at index `pos - 1`. **This is "upper bound binary search" — finding the rightmost valid element.**

**LC 4 – Median of Two Sorted Arrays**
- **Why:** The hardest binary search problem. Google on-site classic.
- **Aha:** Binary search on the partition position in the smaller array. A valid partition has `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`. You're searching for where to "cut" the smaller array such that left halves of both arrays combined equal the right halves. **Don't binary search values — binary search the partition.**

---

## 6. Trees (Binary Tree, BST, Heap)

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Invert Binary Tree** | 226 | Easy | Recursive Thinking |
| 2 | **Maximum Depth of Binary Tree** | 104 | Easy | DFS Base Pattern |
| 3 | **Lowest Common Ancestor of a Binary Tree** | 236 | Medium | Recursive Post-Order |
| 4 | **Binary Tree Level Order Traversal** | 102 | Medium | BFS with Level Tracking |
| 5 | **Validate Binary Search Tree** | 98 | Medium | Range Constraint Propagation |
| 6 | **Kth Smallest Element in a BST** | 230 | Medium | Inorder Traversal |
| 7 | **Serialize and Deserialize Binary Tree** | 297 | Hard | Preorder + Null Markers |
| 8 | **Binary Tree Maximum Path Sum** | 124 | Hard | Post-Order with Global State |

### Why These Matter & The "Aha" Insights

**LC 226 – Invert Binary Tree**
- **Why:** The simplest recursive tree problem. If you can't invert a tree, you can't do any tree problem.
- **Aha:** At each node, swap left and right children, then recurse. The pattern: **"do something at the current node, then trust recursion to handle the subtrees."** Pre-order, post-order, or in-order — all work here because swap is symmetric.

**LC 104 – Maximum Depth of Binary Tree**
- **Why:** Establishes the DFS return-value pattern used in 20+ tree problems.
- **Aha:** `depth(node) = 1 + max(depth(left), depth(right))`. Base case: `depth(null) = 0`. **This "return a value up from children and combine" pattern is how you solve diameter, balanced tree, max path sum, and many more.**

**LC 236 – Lowest Common Ancestor**
- **Why:** Amazon's most-asked tree problem. Tests post-order reasoning.
- **Aha:** Recurse left and right. If both return non-null, current node is the LCA. If only one returns non-null, propagate it up. Base case: if current node is p or q, return it. **You're asking each subtree: "do you contain p or q?" and combining answers at each level.**

**LC 102 – Binary Tree Level Order Traversal**
- **Why:** The canonical BFS tree problem. Basis for zigzag, right-side view, etc.
- **Aha:** Use a queue. Process nodes level by level: at each level, drain the queue (current size = level size), add all children. **The trick is `for _ in range(len(queue))` to process exactly one level per iteration.**

**LC 98 – Validate Binary Search Tree**
- **Why:** Tests understanding of BST invariants. Microsoft/Google.
- **Aha:** A node isn't just "greater than left child" — it must be within a **range** `(min_val, max_val)`. Pass the valid range down: go left → update upper bound; go right → update lower bound. `validate(node, low=-inf, high=inf)`. **BST problems often require passing constraints downward.**

**LC 230 – Kth Smallest Element in a BST**
- **Why:** Tests the connection between BSTs and inorder traversal.
- **Aha:** Inorder traversal of a BST visits nodes in sorted order. Do inorder traversal, decrement K at each visit, stop when K reaches 0. **"Sorted order in a BST" = inorder traversal.** This insight also solves "BST Iterator" (LC 173).

**LC 297 – Serialize and Deserialize Binary Tree**
- **Why:** The ultimate tree construction problem. Tests traversal + reconstruction.
- **Aha:** Serialize with preorder traversal, using a marker (e.g., `"#"`) for null nodes. Deserialize by reading values sequentially: read value → create node → recurse left → recurse right. **Null markers are what let you unambiguously reconstruct the tree from a single traversal.**

**LC 124 – Binary Tree Maximum Path Sum**
- **Why:** The hardest standard tree problem. Google on-site classic.
- **Aha:** At each node, compute the best "single branch" (node + max(left, right, 0)) to return to the parent, but also check if the "full path through this node" (left + node + right) is the global best. **The trick: what you return to the parent (single path) is different from what you track globally (full path).** Use a global variable for the answer.

---

## 7. Tries

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Implement Trie (Prefix Tree)** | 208 | Medium | Core Trie Structure |
| 2 | **Design Add and Search Words Data Structure** | 211 | Medium | Trie + DFS for Wildcards |
| 3 | **Word Search II** | 212 | Hard | Trie + Backtracking on Grid |
| 4 | **Replace Words** | 648 | Medium | Prefix Matching |
| 5 | **Search Suggestions System** | 1268 | Medium | Trie + DFS for Autocomplete |

### Why These Matter & The "Aha" Insights

**LC 208 – Implement Trie**
- **Why:** You must build it before you can use it. Every trie problem starts here.
- **Aha:** Each node has a `children` dict/array (size 26 for lowercase) and an `is_end` boolean. Insert walks/creates nodes. Search walks nodes and checks `is_end`. StartsWith walks nodes (doesn't check `is_end`). **A trie is a tree where the "key" is distributed across the path from root to node, not stored at the node.**

**LC 211 – Design Add and Search Words**
- **Why:** Extends the basic trie with wildcard handling. Tests DFS on a trie.
- **Aha:** For normal characters, follow the single matching child. For `'.'` (wildcard), **branch out to ALL children** and return True if any branch matches. This is DFS/backtracking on the trie structure. **The trie acts as a search space you prune with each character.**

**LC 212 – Word Search II**
- **Why:** THE hard trie problem. Google/Amazon. Combines trie with grid backtracking.
- **Aha:** Build a trie from the word list. Then DFS from each cell in the grid, walking the trie simultaneously. If the trie path dies, prune that search branch. **The trie prunes your grid DFS: instead of searching for each word separately (O(words × cells)), you search for all words simultaneously.** Optimization: remove trie leaf nodes after finding a word to avoid re-finding it.

**LC 648 – Replace Words**
- **Why:** Clean prefix matching problem. Good for understanding trie's primary use case.
- **Aha:** Build a trie from all roots/prefixes. For each word in the sentence, walk the trie. If you hit an `is_end` node, that prefix replaces the word. If you exhaust the word without hitting `is_end`, keep the original. **Tries excel at "find the shortest prefix match" queries.**

**LC 1268 – Search Suggestions System**
- **Why:** Real-world autocomplete feature. Amazon asks this.
- **Aha:** Build a trie. At each prefix (after each typed character), DFS from that trie node to find the lexicographically smallest 3 words. **Alternative O(n log n) approach:** sort the products, then binary search for the prefix at each step. The trie approach is more educational; the sort+binary-search approach is often simpler to code.

---

## 8. Graphs (BFS, DFS, Shortest Path, Topological Sort, Union-Find)

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Number of Islands** | 200 | Medium | Grid DFS/BFS |
| 2 | **Clone Graph** | 133 | Medium | BFS/DFS + Hash Map |
| 3 | **Course Schedule (I + II)** | 207/210 | Medium | Topological Sort |
| 4 | **Pacific Atlantic Water Flow** | 417 | Medium | Multi-Source DFS |
| 5 | **Number of Connected Components** | 323 | Medium | Union-Find / DFS |
| 6 | **Word Ladder** | 127 | Hard | BFS Shortest Path |
| 7 | **Cheapest Flights Within K Stops** | 787 | Medium | Bellman-Ford / BFS |
| 8 | **Alien Dictionary** | 269 | Hard | Topological Sort from Constraints |

### Why These Matter & The "Aha" Insights

**LC 200 – Number of Islands**
- **Why:** The #1 graph problem in interviews. Amazon asks it every week.
- **Aha:** DFS/BFS from each unvisited `'1'`, marking all connected `'1'`s as visited (sink them to `'0'`). Each DFS launch = one island. **The pattern: "count connected components by counting DFS/BFS launches."** Same pattern: LC 695 (max area), LC 130 (surrounded regions), LC 994 (rotting oranges — BFS).

**LC 133 – Clone Graph**
- **Why:** Tests deep copy with cycles. The same pattern appears in linked list copying, tree cloning, etc.
- **Aha:** Use a hash map `{original_node: cloned_node}` to track already-cloned nodes. BFS or DFS: for each neighbor, if not cloned, clone it and enqueue/recurse. If already cloned, just wire the edge. **The hash map prevents infinite loops in cyclic graphs and acts as both "visited" set and "clone registry."**

**LC 207/210 – Course Schedule**
- **Why:** THE topological sort problem. Amazon and Google love it.
- **Aha:** Build an adjacency list + in-degree array. Start BFS from all nodes with in-degree 0. When processing a node, decrement neighbors' in-degrees; if any reaches 0, enqueue it. If you process all nodes, no cycle (valid schedule). If not, there's a cycle. **(Kahn's algorithm.)** LC 210 just asks you to return the actual order. **DFS alternative:** run DFS, add to result in post-order, reverse at the end. Cycle detection: track "in current recursion stack" state.

**LC 417 – Pacific Atlantic Water Flow**
- **Why:** Tests reverse thinking in graph problems. Google favorite.
- **Aha:** Instead of DFS from every cell to both oceans (expensive), **start from the oceans and work inward.** DFS from Pacific border cells (can reach Pacific), DFS from Atlantic border cells. Answer = intersection of both reachable sets. **"Reverse the direction" — think from destination to source.**

**LC 323 – Number of Connected Components**
- **Why:** The cleanest Union-Find problem. Builds intuition for the data structure.
- **Aha:** Initialize each node as its own parent. For each edge, union the two nodes. Count remaining unique roots. **Union-Find with path compression + union by rank gives near-O(1) per operation.** The `find` function with path compression: `parent[x] = find(parent[x])` — one line that makes it fast.

**LC 127 – Word Ladder**
- **Why:** BFS for shortest path in unweighted graph. Microsoft/Google.
- **Aha:** Each word is a node. Two words are connected if they differ by one letter. BFS from `beginWord` to `endWord`. **The trick for efficiency:** instead of checking all word pairs O(n²), generate all possible one-letter transformations of the current word (`*ot`, `h*t`, `ho*`) and use a pattern-to-word hash map.

**LC 787 – Cheapest Flights Within K Stops**
- **Why:** Shortest path with constraints. Tests Bellman-Ford or modified BFS.
- **Aha:** Bellman-Ford with exactly K+1 relaxation rounds (K stops = K+1 edges). **Key:** use a copy of the distances array for each round to prevent "cascading" updates within the same round. Alternative: BFS with a queue of `(cost, city, stops_remaining)` but avoid classic Dijkstra (it doesn't handle the K-stop constraint correctly without modification).

**LC 269 – Alien Dictionary**
- **Why:** The hardest topological sort application. Google favorite.
- **Aha:** Compare adjacent words to extract ordering constraints: the first differing character gives an edge `(char_a → char_b)`. Build a graph from all adjacent-word pairs, then topological sort. **Edge cases:** if a longer word comes before its prefix (e.g., `"abc"` before `"ab"`), the order is invalid. The graph building is the hard part, not the toposort itself.

---

## 9. Backtracking

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Subsets** | 78 | Medium | Include/Exclude Template |
| 2 | **Permutations** | 46 | Medium | Swap / Used Array |
| 3 | **Combination Sum** | 39 | Medium | Unlimited Picks |
| 4 | **Combination Sum II** | 40 | Medium | Skip Duplicates |
| 5 | **Word Search** | 79 | Medium | Grid Backtracking |
| 6 | **Palindrome Partitioning** | 131 | Medium | Partitioning Template |
| 7 | **N-Queens** | 51 | Hard | Constraint Tracking |

### Why These Matter & The "Aha" Insights

**Universal Backtracking Template:**
```
def backtrack(start, current_state):
    if goal_reached:
        result.append(current_state.copy())
        return
    for i in range(start, len(choices)):
        if not valid(choices[i]): continue  # pruning
        current_state.append(choices[i])     # choose
        backtrack(i or i+1, current_state)   # explore (i = reuse, i+1 = no reuse)
        current_state.pop()                  # un-choose
```

**LC 78 – Subsets**
- **Why:** The purest backtracking problem. Every other backtracking problem is a modification of this.
- **Aha:** At each index, you have two choices: include the element or skip it. Recurse from `index + 1` in both cases. Every leaf of the recursion tree is a valid subset. **Alternative view:** iterate and at each level, choose from `[start, end)`, adding the current state to results at EVERY node (not just leaves).

**LC 46 – Permutations**
- **Why:** Tests "arrangement" vs "selection." The other half of the combinatorics coin.
- **Aha:** Unlike subsets (where you pick a subset), permutations use ALL elements in every arrangement. Track a `used` boolean array. At each position, try every unused element. **Key difference from subsets: start from 0 each time (not from `start`), but skip used elements.** Alternative: swap-based approach — swap `nums[i]` with `nums[start]`, recurse, swap back.

**LC 39 – Combination Sum**
- **Why:** The "unlimited reuse" variant. Tests loop structure in backtracking.
- **Aha:** Same as subsets, but recurse with `i` (not `i+1`) to allow reusing the same element. Stop when sum exceeds target. **Sort the candidates first so you can break early when the remaining candidates are too large.**

**LC 40 – Combination Sum II**
- **Why:** Handling duplicates is the trickiest part of backtracking. This is THE duplicate-handling problem.
- **Aha:** Sort the array. In the loop, skip `candidates[i]` if `candidates[i] == candidates[i-1]` AND `i > start`. Recurse with `i + 1` (each element used once). **The skip condition `i > start` is crucial: the first occurrence at each recursion level is allowed, but duplicates at the same level are skipped.** This same technique applies to Subsets II (LC 90) and Permutations II (LC 47).

**LC 79 – Word Search**
- **Why:** Grid backtracking. Amazon/Microsoft.
- **Aha:** DFS from each cell, trying to match the word character by character. Mark cells as visited (change to `'#'`), recurse in 4 directions, then unmark (backtrack). **The "mark and unmark" is the backtracking.** Pruning: if current cell doesn't match the expected character, return immediately.

**LC 131 – Palindrome Partitioning**
- **Why:** Tests partitioning + validation. The partition template generalizes to many problems.
- **Aha:** At each position, try every possible "cut" where the substring `[start:i+1]` is a palindrome. If it is, recurse from `i+1`. **You're generating all possible ways to partition the string where each part satisfies a condition.** This pattern appears in word break, IP addresses, and other partitioning problems.

**LC 51 – N-Queens**
- **Why:** The classic constraint satisfaction problem. Tests efficient pruning.
- **Aha:** Place queens row by row. Track three sets: `cols`, `diag` (row - col), `anti_diag` (row + col). A queen at `(r, c)` attacks column `c`, diagonal `r-c`, and anti-diagonal `r+c`. Before placing, check all three sets. **The insight: diagonals have constant `row - col` and anti-diagonals have constant `row + col`.** This constraint encoding makes checking O(1).

---

## 10. Dynamic Programming

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Climbing Stairs** | 70 | Easy | 1D DP / Fibonacci |
| 2 | **House Robber** | 198 | Medium | 1D DP with Skip |
| 3 | **Coin Change** | 322 | Medium | Unbounded Knapsack |
| 4 | **Longest Increasing Subsequence** | 300 | Medium | 1D DP / Patience Sort |
| 5 | **Longest Common Subsequence** | 1143 | Medium | 2D String DP |
| 6 | **Word Break** | 139 | Medium | 1D DP + String Matching |
| 7 | **Edit Distance** | 72 | Medium | 2D String DP (Classic) |
| 8 | **Unique Paths** | 62 | Medium | 2D Grid DP |

### Why These Matter & The "Aha" Insights

**The DP Framework (use for every problem):**
1. **Define state:** What does `dp[i]` (or `dp[i][j]`) represent?
2. **Recurrence:** How does `dp[i]` relate to smaller subproblems?
3. **Base case:** What are the trivially known values?
4. **Order:** In what order do you fill the table?
5. **Answer:** Where in the table is your final answer?

**LC 70 – Climbing Stairs**
- **Why:** Baby's first DP. If you can't solve this, you can't do any DP.
- **Aha:** `dp[i] = dp[i-1] + dp[i-2]`. To reach step `i`, you came from step `i-1` (1 step) or step `i-2` (2 steps). **This is literally Fibonacci.** Space optimization: you only need the last 2 values, not the whole array.

**LC 198 – House Robber**
- **Why:** The canonical "take or skip" problem. Amazon.
- **Aha:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. At each house: either skip it (take previous best) or rob it (its value + best from two houses ago). **This "include/exclude" recurrence is the backbone of 1D DP.** House Robber II (LC 213): circular — run twice, once excluding first house, once excluding last.

**LC 322 – Coin Change**
- **Why:** THE unbounded knapsack problem. Foundational for all "minimum ways to make X" problems.
- **Aha:** `dp[amount] = min(dp[amount - coin] + 1)` for each coin. Build bottom-up from `dp[0] = 0`. Initialize everything else to `amount + 1` (impossible). **Each subproblem asks: "What's the fewest coins to make this sub-amount?"** The unbounded part: each coin can be used unlimited times (we iterate coins for each amount).

**LC 300 – Longest Increasing Subsequence**
- **Why:** Subsequence DP is its own category. Google/Amazon love this.
- **Aha:** **O(n²) DP:** `dp[i]` = length of LIS ending at index `i`. For each `j < i` where `nums[j] < nums[i]`: `dp[i] = max(dp[i], dp[j] + 1)`. **O(n log n) Patience Sort:** maintain a `tails` array where `tails[i]` = smallest tail element of all increasing subsequences of length `i+1`. Binary search to find where each new element goes. **The O(n log n) approach is expected at Google.**

**LC 1143 – Longest Common Subsequence**
- **Why:** THE 2D string DP problem. The pattern for comparing two strings/sequences.
- **Aha:** `dp[i][j]` = LCS of `text1[:i]` and `text2[:j]`. If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`. Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. **Match → take diagonal + 1. No match → take the better of "skip one character from either string."** This same structure applies to edit distance, shortest common supersequence, and more.

**LC 139 – Word Break**
- **Why:** Combines DP with string matching. Amazon/Google.
- **Aha:** `dp[i]` = can we segment `s[:i]` using the dictionary? For each `j < i`: if `dp[j]` is True and `s[j:i]` is in the word set, then `dp[i] = True`. **You're checking every possible "last word" in the segmentation.** Use a set for O(1) word lookup. Optimization: only check substrings up to the max word length.

**LC 72 – Edit Distance**
- **Why:** The most important 2D string DP. Used in spell checkers, diff algorithms, bioinformatics.
- **Aha:** `dp[i][j]` = min edits to convert `word1[:i]` to `word2[:j]`. Three operations map to three subproblems:
  - Insert: `dp[i][j-1] + 1`
  - Delete: `dp[i-1][j] + 1`
  - Replace: `dp[i-1][j-1] + (0 if match, 1 if not)`
  
  Take the minimum. **Each cell considers "what's the cheapest last operation?"**

**LC 62 – Unique Paths**
- **Why:** The simplest 2D grid DP. Builds intuition for grid-based DP.
- **Aha:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. You can only come from above or from the left. First row and first column are all 1s (only one way to reach any cell in them). **Space optimization: only need the previous row, so use a 1D array.**

---

## 11. Greedy & Intervals

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Merge Intervals** | 56 | Medium | Sort + Merge |
| 2 | **Non-overlapping Intervals** | 435 | Medium | Sort + Greedy (Earliest End) |
| 3 | **Meeting Rooms II** | 253 | Medium | Sweep Line / Min-Heap |
| 4 | **Jump Game** | 55 | Medium | Greedy Farthest Reach |
| 5 | **Jump Game II** | 45 | Medium | Greedy BFS |
| 6 | **Gas Station** | 134 | Medium | Net Gain Analysis |
| 7 | **Task Scheduler** | 621 | Medium | Greedy Frequency |

### Why These Matter & The "Aha" Insights

**LC 56 – Merge Intervals**
- **Why:** THE interval problem. Foundation for all interval-based questions. Amazon.
- **Aha:** Sort by start time. Iterate: if current interval overlaps with the last merged one (start ≤ previous end), merge by extending the end. Otherwise, start a new interval. **Always sort intervals first.** The merge condition is just comparing `current.start` with `result[-1].end`.

**LC 435 – Non-overlapping Intervals (Minimum Removals)**
- **Why:** The classic "activity selection" problem from CLRS. Greedy proof is important.
- **Aha:** Sort by **end time**. Greedily keep intervals that don't overlap with the last kept one. Count removals. **Why sort by end time? Choosing the earliest-ending interval leaves the most room for future intervals.** This is the canonical greedy proof by exchange argument.

**LC 253 – Meeting Rooms II**
- **Why:** "How many rooms do you need?" = "What's the maximum overlap?" Amazon/Google.
- **Aha:** **Sweep line:** create events `(time, +1 for start, -1 for end)`. Sort by time. Sweep through, tracking current overlap. Max overlap = rooms needed. **Alternative:** Sort starts and ends separately. Two pointers: if `starts[i] < ends[j]`, a new meeting starts before one ends (need another room); otherwise, a room frees up. Both are O(n log n).

**LC 55 – Jump Game**
- **Why:** Greedy thinking distilled to its purest form.
- **Aha:** Track the `farthest` index reachable. At each position `i` (if `i <= farthest`), update `farthest = max(farthest, i + nums[i])`. If `farthest >= last index`, return True. **You don't need to simulate jumps — just track how far you CAN reach.**

**LC 45 – Jump Game II**
- **Why:** Extends LC 55 with a "minimum jumps" requirement. Tests BFS/greedy thinking.
- **Aha:** Think of it as BFS on levels. Each "level" is the range of indices reachable with the current number of jumps. Track `current_end` (end of current BFS level) and `farthest` (farthest reachable from this level). When you pass `current_end`, increment jumps and set `current_end = farthest`. **This is implicit BFS without a queue.**

**LC 134 – Gas Station**
- **Why:** Tests net-gain greedy reasoning. Amazon.
- **Aha:** If total gas ≥ total cost, a solution exists. To find the starting station: track cumulative net gas. Whenever it drops below 0, the starting point must be AFTER the current station (reset cumulative to 0, set start to `i+1`). **If you can't reach station `j` starting from `i`, then no station between `i` and `j` works either** — that's the greedy insight that avoids O(n²).

**LC 621 – Task Scheduler**
- **Why:** Greedy with frequency analysis. Amazon/Microsoft.
- **Aha:** The most frequent task determines the minimum time. Imagine slots: `(max_freq - 1)` groups of `(n + 1)` slots, plus a final group for all tasks with max frequency. Total = `(max_freq - 1) * (n + 1) + count_of_max_freq_tasks`. But also, total ≥ number of tasks (if there's no idle time needed). **Answer = max(formula, total_tasks).**

---

## 12. Bit Manipulation

### Questions

| # | Problem | LC# | Difficulty | Pattern |
|---|---------|-----|-----------|---------|
| 1 | **Single Number** | 136 | Easy | XOR Cancellation |
| 2 | **Number of 1 Bits** | 191 | Easy | Brian Kernighan's Trick |
| 3 | **Counting Bits** | 338 | Easy | DP on Bits |
| 4 | **Reverse Bits** | 190 | Easy | Bit-by-Bit Construction |
| 5 | **Missing Number** | 268 | Easy | XOR or Math |
| 6 | **Sum of Two Integers** | 371 | Medium | Bit-Level Arithmetic |

### Why These Matter & The "Aha" Insights

**LC 136 – Single Number**
- **Why:** The most elegant use of XOR. Tests bit manipulation intuition.
- **Aha:** `a XOR a = 0` and `a XOR 0 = a`. XOR all numbers together — pairs cancel out, leaving the single number. **XOR is your best friend for "find the odd one out" problems.** Extends to "Single Number II" (LC 137 — count bits mod 3) and "Single Number III" (LC 260 — separate two singles by a differing bit).

**LC 191 – Number of 1 Bits (Hamming Weight)**
- **Why:** Foundational bit operation. Used as a subroutine elsewhere.
- **Aha:** **Brian Kernighan's trick:** `n = n & (n - 1)` clears the lowest set bit. Count how many times until `n = 0`. **Why it works:** `n - 1` flips all bits from the lowest set bit rightward. AND-ing with `n` zeros out that lowest set bit. This runs in O(number of set bits), not O(32).

**LC 338 – Counting Bits**
- **Why:** DP meets bit manipulation. Clean and elegant.
- **Aha:** `dp[i] = dp[i >> 1] + (i & 1)`. Number of 1s in `i` = number of 1s in `i/2` (shift right = drop last bit) plus whether the last bit is 1. **Alternative:** `dp[i] = dp[i & (i-1)] + 1` (remove lowest set bit, add 1). Both are O(n) for all values 0 to n.

**LC 190 – Reverse Bits**
- **Why:** Tests bit-level construction.
- **Aha:** Extract bits one by one from the right of `n`, place them from the right of `result`, shifting result left each time. `result = (result << 1) | (n & 1); n >>= 1`. Do this 32 times. **You're building the answer bit by bit, which is a pattern for many bit problems.**

**LC 268 – Missing Number**
- **Why:** Multiple approaches make this great for discussion.
- **Aha:** **XOR approach:** XOR all numbers `0..n` with all array elements. Pairs cancel, leaving the missing one. **Math approach:** `n*(n+1)/2 - sum(array)`. **Bit manipulation approach is preferred because it avoids overflow.** The XOR technique generalizes: "given a complete set with one missing, XOR everything."

**LC 371 – Sum of Two Integers**
- **Why:** Understanding how addition works at the bit level.
- **Aha:** `a XOR b` gives the sum without carries. `(a AND b) << 1` gives the carries. Repeat until there are no carries. **This is literally how a hardware adder works.** In Python, watch out for negative numbers due to arbitrary-precision integers — you may need to mask to 32 bits.

---

## 🗺️ The Big Picture: Pattern Map

```
Problem Solving Flowchart:
─────────────────────────────────────────────────────
"Is it asking for..."

OPTIMIZATION (min/max)?
├── Can I make a greedy choice?     → Greedy
├── Overlapping subproblems?        → DP
└── Search space monotonic?         → Binary Search on Answer

ENUMERATION (all combinations)?    → Backtracking

EXISTENCE/COUNT in a sequence?
├── Contiguous subarray?            → Sliding Window / Prefix Sum
├── Subsequence?                    → DP
└── Pair/triplet?                   → Two Pointers / Hash Map

GRAPH STRUCTURE?
├── Shortest path (unweighted)?     → BFS
├── Connected components?           → DFS / Union-Find
├── Ordering with dependencies?     → Topological Sort
└── Shortest path (weighted)?       → Dijkstra / Bellman-Ford

TREE STRUCTURE?
├── Level-by-level?                 → BFS
├── Path/depth/ancestor?            → DFS (recursion)
└── Sorted property?                → BST + Inorder

STRING SEARCH?
├── Single pattern?                 → Two Pointers / Hashing
├── Multiple patterns?              → Trie
└── Prefix queries?                 → Trie

DESIGN QUESTION?
├── O(1) access + ordering?         → Hash Map + Linked List
├── Prefix lookups?                 → Trie
└── Quick min/max?                  → Heap / Monotonic Stack
─────────────────────────────────────────────────────
```

---

## 📊 Priority Order for Study

If you have **limited time**, study in this order:

| Priority | Topic | # of Interview Questions It Covers |
|----------|-------|-------------------------------------|
| 🔴 P0 | Arrays & Hashing | ~25% of all interviews |
| 🔴 P0 | Trees & Graphs | ~20% of all interviews |
| 🟠 P1 | Dynamic Programming | ~15% of all interviews |
| 🟠 P1 | Binary Search | ~10% of all interviews |
| 🟡 P2 | Stacks & Sliding Window | ~10% of all interviews |
| 🟡 P2 | Backtracking | ~8% of all interviews |
| 🟢 P3 | Linked Lists, Greedy, Tries, Bits | ~12% of all interviews |

---

> **Golden Rule:** For each problem, don't just solve it — identify the **pattern**, then find 2-3 similar problems and verify the pattern transfers. That's how you go from "memorized 200 problems" to "can solve any problem."
