# DSA Interview Course Blueprint — FAANG Focus

> Built from 500+ Google/Amazon interview loops. Every topic, problem, and pitfall listed here reflects what actually gets asked and what actually separates hire from no-hire.

---

## Module 1: Foundations

### Key Concepts
- **Big-O, Big-Ω, Big-Θ** — formal definitions, how to derive for loops/recursion; amortized analysis (dynamic array resize, union-find with path compression)
- **Space complexity** — auxiliary vs total; stack frames in recursion count; understanding when O(1) extra space is possible vs not
- **Recurrence relations** — Master Theorem (T(n)=aT(n/b)+O(n^d)), recursion tree method, substitution method
- **Recursion fundamentals** — base case / recursive case, call stack mechanics, stack overflow risks, tail recursion
- **Recursion to iteration** — converting any recursion to explicit stack; why interviewers ask this
- **Math essentials for interviews:**
  - Modular arithmetic (mod properties, modular exponentiation for large numbers)
  - GCD/LCM (Euclidean algorithm, O(log min(a,b)))
  - Prime numbers (Sieve of Eratosthenes O(n log log n), primality check O(√n))
  - Combinatorics basics (nCr, nPr, Pascal's triangle for DP)
  - Power of 2 tricks, logarithm intuition (why binary search is O(log n))
  - Integer overflow awareness — when to use long, modular arithmetic in DP

### Top Interview Problems
1. **Pow(x, n)** — fast exponentiation, handle negative n, overflow edge cases
2. **Count Primes (Sieve of Eratosthenes)** — optimization: only mark from p²
3. **Climbing Stairs** — recursion → memoization → DP transition (foundation for DP module)
4. **Fibonacci Number** — matrix exponentiation for O(log n) solution; compare all approaches

### Common Mistakes
- Saying O(n) when the inner loop makes it O(n²) — not analyzing nested dependencies
- Forgetting recursion uses O(depth) stack space
- Confusing average case with worst case (e.g., quicksort)
- Not recognizing amortized O(1) for dynamic arrays
- Off-by-one errors in modular arithmetic

---

## Module 2: Arrays & Strings

### Key Concepts
- **Array fundamentals** — contiguous memory, O(1) access, O(n) insert/delete; dynamic arrays and amortized doubling
- **In-place operations** — overwrite from end, swap-based rearrangement, two-pass vs one-pass
- **String manipulation** — immutability (in Java/Python), StringBuilder, character frequency arrays vs hash maps
- **Two Pointers pattern:**
  - Same-direction (fast/slow for removing duplicates, partition)
  - Opposite-direction (sorted two-sum, container with most water, valid palindrome)
  - Three pointers (3Sum — sort + two pointer, skip duplicates)
- **Sliding Window pattern:**
  - Fixed-size window (max sum subarray of size k)
  - Variable-size window (longest substring without repeating characters, minimum window substring)
  - Template: expand right, shrink left while condition violated, track answer
  - When to use hash map inside window vs frequency array
- **Prefix Sum / Difference Array:**
  - 1D prefix sum: range sum query O(1) after O(n) precompute
  - Prefix sum + hash map: subarray sum equals K (count of prefix[j]-prefix[i]=k)
  - 2D prefix sum for matrix region queries
  - Difference array for range update operations O(1) per update
- **Kadane's Algorithm** — max subarray sum, O(n) time O(1) space; handle all-negative arrays
- **Dutch National Flag** — 3-way partition in single pass O(n), used in sort colors

### Top Interview Problems
1. **Minimum Window Substring** — sliding window + frequency map, shrink from left greedily
2. **3Sum** — sort + two pointers, duplicate skipping logic is the hard part
3. **Trapping Rain Water** — two pointer O(1) space approach; also stack-based and prefix max approaches
4. **Subarray Sum Equals K** — prefix sum + hash map, O(n); tricky: doesn't work with two pointers because of negatives
5. **Longest Substring Without Repeating Characters** — sliding window with hash map/set

### Common Mistakes
- Sliding window: forgetting to shrink the window (infinite loop) or shrinking too aggressively
- Two pointers on unsorted array when problem requires sorted input
- Prefix sum: off-by-one on index (prefix[0]=0 sentinel)
- Not handling duplicate skipping in 3Sum/4Sum → TLE or duplicate triplets
- Using O(n) string concatenation in a loop instead of StringBuilder → O(n²)

---

## Module 3: Hashing

### Key Concepts
- **Hash Map operations** — O(1) average insert/lookup/delete; O(n) worst case with bad hash
- **Hash Set** — membership testing, deduplication
- **Collision resolution:**
  - Chaining (linked list per bucket) — most common in interviews
  - Open addressing (linear probing, quadratic probing, double hashing)
  - Load factor and rehashing — when/why resize happens
- **Designing a good hash function** — distribution, determinism; rolling hash for string matching (Rabin-Karp)
- **Frequency counting pattern** — character frequency, word frequency, anagram grouping
- **Two-sum pattern** — complement lookup; generalization to k-sum
- **Hash map + linked list** — ordered hash map (LinkedHashMap), LRU Cache design
- **When NOT to use hashing** — when order matters, when worst-case O(1) is needed (use balanced BST)

### Top Interview Problems
1. **Two Sum** — hash map complement lookup; follow-up: sorted input (two pointers), duplicates, streaming
2. **Group Anagrams** — sorted string as key OR frequency tuple as key
3. **Longest Consecutive Sequence** — hash set, only start counting from sequence start (O(n))
4. **LRU Cache** — hash map + doubly linked list; O(1) get and put (also in Stacks & Queues)
5. **Subarray Sum Equals K** — prefix sum stored in hash map (crossover with Arrays)

### Common Mistakes
- Assuming hash map is always O(1) — pathological inputs can cause O(n) per operation
- Using mutable objects as hash keys (lists in Python)
- Not considering hash collisions in custom hash functions
- Forgetting that hash map iteration order is not guaranteed (unless using ordered variant)
- In "longest consecutive sequence" — iterating from every element instead of only sequence starts → O(n²)

---

## Module 4: Linked Lists

### Key Concepts
- **Singly linked list** — node structure, insert/delete at head/tail/middle O(1)/O(n), traversal
- **Doubly linked list** — bidirectional traversal, O(1) delete when node reference is given; used in LRU cache
- **Circular linked list** — last node points to head; cycle detection
- **Dummy/sentinel node technique** — simplifies edge cases for insert/delete at head
- **Fast & slow pointers (Floyd's):**
  - Cycle detection — slow moves 1, fast moves 2; meeting proves cycle; find cycle start (reset one to head)
  - Find middle node — when fast reaches end, slow is at middle
  - Find kth from end — advance fast k steps, then move both
- **Reversal techniques:**
  - Iterative reversal (3 pointers: prev, curr, next) — O(n) time O(1) space
  - Reverse a sub-list (reverse between positions m and n)
  - Recursive reversal — understand the call stack unwinding
- **Merge two sorted lists** — foundational for merge sort on linked lists
- **Deep copy with random pointer** — hash map approach O(n) space; interweaving approach O(1) space

### Top Interview Problems
1. **Reverse Linked List** — iterative AND recursive; must be instant in interview
2. **Merge Two Sorted Lists** — recursive and iterative; foundation for merge k lists
3. **Linked List Cycle II** — find the START of the cycle, not just detect; math proof matters
4. **Copy List with Random Pointer** — interweaving nodes trick for O(1) space
5. **Reorder List** — find middle + reverse second half + merge alternating (combines 3 patterns)

### Common Mistakes
- Losing reference to head (not using dummy node)
- Null pointer exceptions — not checking `node != null` before `node.next`
- Off-by-one in "kth from end" — clarify if k is 0-indexed or 1-indexed
- Forgetting to disconnect old pointers when reversing (creates cycles)
- Not handling single-node or two-node edge cases

---

## Module 5: Stacks & Queues

### Key Concepts
- **Stack fundamentals** — LIFO, push/pop/peek O(1); use cases: undo, DFS, expression eval
- **Queue fundamentals** — FIFO, enqueue/dequeue O(1); use cases: BFS, scheduling
- **Monotonic stack:**
  - Monotonically increasing stack — find next smaller element
  - Monotonically decreasing stack — find next greater element
  - Template: pop while top violates monotonic property, push current
  - Applications: daily temperatures, largest rectangle in histogram, trapping rain water
- **Monotonic deque** — sliding window maximum/minimum in O(n); deque maintains indices of candidates
- **Stack for expression evaluation:**
  - Infix to postfix conversion (Shunting-yard)
  - Evaluate postfix/RPN
  - Basic calculator (handle +, -, *, /, parentheses, unary minus)
- **Stack for parentheses:** valid parentheses, minimum remove to make valid, longest valid parentheses
- **Design problems:**
  - Min Stack — O(1) getMin using auxiliary stack or encoded values
  - LRU Cache — doubly linked list + hash map
  - LFU Cache — multiple linked lists + two hash maps
  - Queue using two stacks / Stack using two queues
  - Design circular queue / deque
- **Deque (double-ended queue)** — insert/remove from both ends O(1)

### Top Interview Problems
1. **Largest Rectangle in Histogram** — monotonic stack, O(n); foundation for maximal rectangle in matrix
2. **Basic Calculator II** — handle operator precedence with stack; extend to Basic Calculator I/III
3. **LRU Cache** — hash map + doubly linked list; clean API design matters
4. **Valid Parentheses** — classic stack; extend to wildcard version (LC 678)
5. **Sliding Window Maximum** — monotonic deque maintaining decreasing order of values

### Common Mistakes
- Monotonic stack: confusing when to use increasing vs decreasing; not tracking indices vs values
- LRU Cache: forgetting to update position on `get` (not just `put`)
- Stack-based DFS: processing node when pushing instead of when popping (wrong order)
- Not handling empty stack before peek/pop
- Circular queue: confusing full vs empty condition (both have front==rear)

---

## Module 6: Sorting

### Key Concepts
- **Comparison-based sorts:**
  - **Merge Sort** — divide & conquer, O(n log n) time, O(n) space, STABLE; preferred when stability needed or for linked lists (O(1) extra space on LL); count inversions using merge sort
  - **Quick Sort** — partition (Lomuto vs Hoare), O(n log n) average, O(n²) worst; randomized pivot avoids worst case; NOT stable; in-place O(log n) stack space; Quick Select for kth element O(n) average
  - **Heap Sort** — O(n log n) guaranteed, O(1) extra space, NOT stable; rarely best choice but useful to know
  - **Insertion Sort** — O(n²) but O(n) on nearly sorted; stable; used as base case in hybrid sorts (Timsort)
- **Non-comparison sorts (O(n) when applicable):**
  - **Counting Sort** — O(n+k) where k is range; only for integers in known range
  - **Radix Sort** — O(d*(n+k)) where d is digits; sort by least significant digit first
  - **Bucket Sort** — O(n) average for uniform distribution; used in Maximum Gap problem
- **Custom sorting:**
  - Custom comparator — sorting objects by multiple keys
  - Lambda comparators in Python/Java
  - Meeting rooms (sort by start), merge intervals (sort by start), task scheduler
- **Stability** — why it matters; which sorts are stable (merge, insertion, counting) vs unstable (quick, heap)
- **Quick Select** — O(n) average kth smallest; partition-based; randomized for practical O(n)

### Top Interview Problems
1. **Kth Largest Element** — Quick Select O(n) average; alternatively heap O(n log k); know BOTH
2. **Merge Intervals** — sort by start, linear scan merge; foundation for interval problems
3. **Sort Colors (Dutch National Flag)** — 3-way partition, one pass O(n) O(1)
4. **Maximum Gap** — bucket sort / pigeonhole principle to get O(n); tricky insight
5. **Count of Smaller Numbers After Self** — merge sort counting inversions variant

### Common Mistakes
- Using O(n²) sort when O(n log n) is needed — know when each applies
- Quicksort: always picking first/last element as pivot → O(n²) on sorted input
- Forgetting merge sort needs O(n) extra space (interviewers will ask)
- Custom comparator: inconsistent comparison function (not transitive) → undefined behavior
- Not recognizing when a problem is really a sorting problem in disguise

---

## Module 7: Binary Search

### Key Concepts
- **Fundamentals:**
  - Standard binary search — find target in sorted array; left <= right vs left < right template
  - Find first/last occurrence of target (lower_bound / upper_bound)
  - Off-by-one prevention: be deliberate about `left = mid + 1` vs `left = mid`; know which template avoids infinite loops
- **Binary search on rotated/modified arrays:**
  - Search in rotated sorted array — determine which half is sorted, then decide direction
  - Find minimum in rotated sorted array — with and without duplicates
  - Search in nearly sorted array (element may be ±1 position)
- **Search on answer (binary search on result space):**
  - Pattern: if answer `x` is feasible, then all answers > x (or < x) are also feasible → monotonic predicate
  - Koko eating bananas — binary search on speed, check feasibility
  - Split array largest sum — binary search on answer, greedy check
  - Capacity to ship packages — binary search on weight, greedy validation
  - Aggressive cows / magnetic balls — binary search on minimum distance
- **Binary search on 2D:**
  - Search in sorted matrix (rows sorted, first element > last of prev row) — treat as 1D array
  - Search in row-sorted and column-sorted matrix — staircase search O(m+n) (not binary search but related)
- **Advanced patterns:**
  - Median of two sorted arrays — binary search on partition, O(log(min(m,n)))
  - Find peak element — binary search on unsorted array using slope
  - Minimize maximum / maximize minimum pattern

### Top Interview Problems
1. **Median of Two Sorted Arrays** — binary search on shorter array partition; hardest binary search problem
2. **Search in Rotated Sorted Array** — handle duplicates as follow-up
3. **Koko Eating Bananas** — binary search on answer, classic pattern
4. **Split Array Largest Sum** — binary search + greedy feasibility check
5. **Find Peak Element** — binary search without sorted array; slope-based reasoning

### Common Mistakes
- Infinite loop: `left = mid` without using `left + (right-left+1)/2` for mid calculation
- Not handling even/odd length arrays differently for median problems
- Binary search on answer: wrong bounds (too tight initial range) or wrong feasibility check direction
- Search in rotated array: not handling duplicates (`nums[left]==nums[mid]`) — worst case becomes O(n)
- Integer overflow: `(left + right) / 2` → use `left + (right - left) / 2`

---

## Module 8: Trees

### Key Concepts
- **Binary tree fundamentals** — node structure, height, depth, balanced vs complete vs full vs perfect
- **Traversals (MUST know all):**
  - Inorder (left-root-right) — gives sorted order for BST
  - Preorder (root-left-right) — serialize tree, copy tree
  - Postorder (left-right-root) — delete tree, evaluate expression tree
  - Level-order (BFS) — queue-based, level grouping with size tracking
  - **Morris Traversal** — O(1) space inorder/preorder using threaded tree (advanced but asked at Google)
  - Iterative versions of all traversals using explicit stack
- **Binary tree DFS patterns:**
  - Top-down (passing info from parent → child): max depth, path sum
  - Bottom-up (returning info from child → parent): height, diameter, balanced check
  - Path problems: root-to-leaf, any-node-to-any-node (need global variable for max)
- **Binary Search Tree (BST):**
  - Property: left < root < right (all nodes in subtree, not just immediate children)
  - Search, insert, delete (3 cases: leaf, one child, two children — replace with inorder successor/predecessor)
  - Validate BST — pass min/max bounds, not just compare with parent
  - BST iterator (inorder using stack — O(h) space, O(1) amortized next())
  - Convert sorted array/list to balanced BST
- **Lowest Common Ancestor (LCA):**
  - LCA in binary tree — recursive: if both sides return non-null, current is LCA
  - LCA in BST — use BST property, O(h)
- **Heap / Priority Queue:**
  - Binary heap — array representation, parent at i/2, children at 2i, 2i+1
  - Heapify: sift-up (insert), sift-down (extract); build heap O(n) not O(n log n)
  - Min-heap vs max-heap; top-k problems
  - Merge K sorted lists using min-heap — O(n log k)
  - Two heaps pattern: find median from data stream (max-heap for left, min-heap for right)
- **Serialization/deserialization** — preorder with null markers; level-order approach

### Top Interview Problems
1. **Lowest Common Ancestor** — binary tree version (not BST); follow-up: with parent pointers
2. **Binary Tree Maximum Path Sum** — any-to-any path; track global max, return single-side max
3. **Serialize and Deserialize Binary Tree** — preorder + null markers; also level-order approach
4. **Validate BST** — min/max bound passing; inorder traversal approach
5. **Merge K Sorted Lists** — min-heap approach O(n log k); also divide-and-conquer merge

### Common Mistakes
- Validate BST: only comparing node with direct parent, not maintaining global min/max range
- LCA: not handling case where one node is ancestor of the other
- Max path sum: returning two-sided path from recursion instead of single-sided (can't go both ways then up)
- Heap: forgetting build-heap is O(n) not O(n log n) — interviewers specifically ask this
- Level-order: not capturing level size at start of each level → mixed levels

---

## Module 9: Tries

### Key Concepts
- **Trie (prefix tree) structure:**
  - Node has children map/array (26 for lowercase English), `isEnd` boolean
  - Insert O(m), search O(m), startsWith O(m) where m = word length
- **Implementation choices:**
  - Array-based children (fixed alphabet, faster) vs hash map children (flexible alphabet)
  - Memory optimization: compressed trie (Patricia/radix tree) — merge single-child chains
- **Applications:**
  - Autocomplete / prefix matching — DFS from prefix node
  - Word search in grid (Backtracking + Trie for pruning) — much faster than individual DFS per word
  - Longest common prefix
  - Spell checker / word dictionary
- **Bitwise trie** — for XOR problems: maximum XOR of two numbers (store binary representations)

### Top Interview Problems
1. **Word Search II** — backtracking on grid + trie for pruning; remove words from trie after finding (optimization)
2. **Implement Trie** — insert, search, startsWith; clean OOP design
3. **Design Add and Search Words (Wildcard)** — trie + DFS for '.' wildcard matching
4. **Maximum XOR of Two Numbers** — bitwise trie, greedy bit selection from MSB
5. **Replace Words** — find shortest prefix in dictionary for each word using trie

### Common Mistakes
- Not marking `isEnd` properly — "app" found when only "apple" was inserted
- Word Search II: not pruning trie (removing found words) → TLE on large inputs
- Memory: creating 26-element arrays for every node even when sparse → excessive memory
- Forgetting that trie search returns false for prefix of inserted word if `isEnd` not set
- Not handling empty string edge case

---

## Module 10: Graphs

### Key Concepts
- **Representations** — adjacency list (sparse, O(V+E) space) vs adjacency matrix (dense, O(V²) space); edge list
- **BFS:**
  - Level-order traversal of graph; shortest path in UNWEIGHTED graph
  - Multi-source BFS (01 matrix, rotting oranges — start from all sources simultaneously)
  - Bidirectional BFS for optimization (word ladder)
- **DFS:**
  - Recursive and iterative (with stack)
  - Connected components, cycle detection
  - DFS on grid (flood fill, island counting, island perimeter)
  - DFS states: white/gray/black for directed cycle detection
- **Topological Sort:**
  - Kahn's algorithm (BFS-based, uses in-degree) — also detects cycles in DAG
  - DFS-based (post-order reverse) — add to result when all descendants processed
  - Applications: course schedule, build order, alien dictionary
- **Shortest Path:**
  - Dijkstra's — O((V+E) log V) with min-heap; NON-NEGATIVE weights only
  - Bellman-Ford — O(VE); handles negative weights; detects negative cycles
  - Floyd-Warshall — O(V³); all-pairs shortest path; detect negative cycles
  - 0-1 BFS — deque-based, when weights are only 0 or 1
- **Union-Find (Disjoint Set Union):**
  - Operations: find (with path compression), union (by rank/size)
  - O(α(n)) ≈ O(1) amortized per operation
  - Applications: connected components, detect cycle in undirected graph, accounts merge, number of islands II (online)
- **Minimum Spanning Tree:**
  - Kruskal's (sort edges + union-find) — O(E log E)
  - Prim's (min-heap, grow from vertex) — O(E log V)
  - When to use which: Kruskal for sparse, Prim for dense
- **Advanced patterns:**
  - Bipartite check (2-color BFS/DFS)
  - Clone graph (DFS/BFS + hash map)
  - Graph with state (shortest path with constraints — BFS with (node, state) tuple)

### Top Interview Problems
1. **Course Schedule / Course Schedule II** — topological sort; Kahn's BFS preferred; cycle = impossible
2. **Number of Islands** — DFS/BFS on grid; follow-up: Number of Islands II (union-find, online)
3. **Word Ladder** — BFS shortest path; bidirectional BFS optimization; build adjacency with wildcard patterns
4. **Clone Graph** — DFS + hash map to track visited/cloned nodes
5. **Network Delay Time** — Dijkstra's from source; covers shortest path pattern

### Common Mistakes
- BFS: not marking visited BEFORE enqueuing (causes duplicates in queue, TLE or wrong answer)
- Dijkstra: using with negative weights (doesn't work — need Bellman-Ford)
- Topological sort: not checking if all nodes are processed (miss cycle detection)
- Union-find: forgetting path compression or union by rank → O(n) per operation
- Grid DFS: forgetting to mark cell as visited before recursion → infinite loop

---

## Module 11: Backtracking

### Key Concepts
- **Framework:** choose → explore → unchoose; recursion tree visualization
- **Permutations** — with/without duplicates; `used[]` array vs swap-based
- **Combinations** — use start index to avoid duplicates; combination sum (reuse allowed vs not)
- **Subsets** — power set generation; with duplicates (sort + skip adjacent duplicates)
- **Pruning** — early termination when partial solution can't lead to valid result; sorting to enable pruning
- **Constraint satisfaction:**
  - N-Queens — row/column/diagonal constraints; O(1) diagonal check using (row-col) and (row+col)
  - Sudoku solver — constraint propagation + backtracking
  - Word search in grid — visited matrix, 4-directional DFS
- **String partitioning** — palindrome partitioning, restore IP addresses
- **When backtracking vs DP** — backtracking when you need ALL solutions; DP when you need count/optimal

### Top Interview Problems
1. **N-Queens** — classic backtracking; O(1) validity check using sets for columns/diagonals
2. **Permutations II (with duplicates)** — sort + skip same element at same level
3. **Combination Sum II** — sort + skip duplicates + start index; distinct from Combination Sum I
4. **Word Search** — DFS + backtracking on grid; mark/unmark visited
5. **Palindrome Partitioning** — backtracking to generate all partitions; precompute palindrome checks with DP

### Common Mistakes
- Not undoing changes (unchoose step) — corrupts state for sibling branches
- Duplicate handling: not sorting before skipping adjacent duplicates
- Permutations: using start index instead of used array (or vice versa for combinations)
- Not pruning early — generates all 2^n subsets when most are invalid
- Word search: modifying board permanently instead of restoring cell after backtrack

---

## Module 12: Dynamic Programming

### Key Concepts
- **Fundamentals:**
  - Optimal substructure + overlapping subproblems — the TWO requirements for DP
  - Top-down (memoization) vs bottom-up (tabulation) — trade-offs
  - State definition — the HARDEST part; what information uniquely defines a subproblem?
  - Transition/recurrence relation — how to build solution from smaller subproblems
  - Base cases — initial values; getting these wrong breaks everything
  - Space optimization — rolling array (reduce 2D to 1D, 1D to O(1))
- **1D DP:**
  - Climbing stairs, house robber (skip adjacent), decode ways
  - Coin change (min coins), coin change II (count ways — order of loops matters!)
  - Longest Increasing Subsequence — O(n²) DP, O(n log n) with patience sorting / binary search
  - Word break — DP + trie/set for dictionary lookup
- **2D DP:**
  - Grid paths (unique paths, minimum path sum)
  - 0/1 Knapsack — take or skip; weight/value; space optimize to 1D (iterate backwards!)
  - Unbounded Knapsack — iterate forwards
  - Edit distance (Levenshtein) — insert/delete/replace transitions
  - Interleaving string
- **String DP:**
  - Longest Common Subsequence (LCS) — O(mn) classic; space optimize to O(min(m,n))
  - Longest Palindromic Subsequence — reduce to LCS with reversed string
  - Longest Palindromic Substring — expand around center O(n²) or DP; Manacher's O(n) for bonus
  - Regular expression matching / wildcard matching
- **Subsequence / Partition DP:**
  - Partition equal subset sum (reduce to 0/1 knapsack with sum/2 target)
  - Target sum (reduce to subset sum with offset)
  - Burst balloons — interval DP, think about what's popped LAST
  - Matrix chain multiplication — interval DP
- **State machine DP:**
  - Best time to buy and sell stock (I through IV) — states: hold, not-hold, cooldown, transactions remaining
- **Bitmask DP** — when state includes a subset of items (TSP, assign tasks)

### Top Interview Problems
1. **Longest Increasing Subsequence** — O(n²) DP AND O(n log n) binary search approach; follow-up: count of LIS
2. **Edit Distance** — classic 2D DP; explain each transition clearly
3. **Coin Change** — min coins (BFS also works); Coin Change II for counting (loop order matters!)
4. **Word Break** — DP with set lookup; follow-up: Word Break II (backtracking to find all sentences)
5. **Best Time to Buy and Sell Stock III/IV** — state machine DP with k transactions

### Common Mistakes
- Coin Change II: wrong loop order (iterating coins in inner loop counts permutations, not combinations)
- 0/1 Knapsack space optimization: iterating forwards instead of backwards → items reused
- LIS: not knowing O(n log n) approach; interviewers expect it
- Edit distance: confusing 0-indexed string with 1-indexed DP table
- Not identifying the state properly — too many dimensions = TLE, too few = wrong answer

---

## Module 13: Greedy

### Key Concepts
- **Greedy choice property** — locally optimal choice leads to globally optimal; must PROVE or argue correctness
- **When greedy works vs DP** — greedy: no future decision undoes past optimality; DP: need to consider all options
- **Activity/interval selection** — sort by end time, pick non-overlapping greedily
- **Huffman coding** — greedy for optimal prefix codes; priority queue based
- **Jump game problems** — track farthest reachable; greedy forward scan
- **Task scheduling** — assign tasks by deadline/penalty; CPU task scheduler with cooldown
- **Fractional knapsack** — sort by value/weight ratio (greedy works; 0/1 knapsack doesn't)
- **Gas station** — circular route; single pass, track deficit
- **Common greedy patterns:**
  - Sort then greedily assign
  - Two pointers greedily
  - Priority queue + greedy (merge k sorted, task scheduler, reorganize string)

### Top Interview Problems
1. **Jump Game / Jump Game II** — can reach end (greedy bool) / min jumps (greedy BFS-like)
2. **Task Scheduler** — greedy: count of most frequent task determines minimum; formula or simulation with heap
3. **Gas Station** — single pass O(n); if total gas ≥ total cost, solution exists; find unique start
4. **Non-overlapping Intervals** — sort by end, count overlaps to remove (equivalent to activity selection)
5. **Partition Labels** — last occurrence map + greedy extension of current partition

### Common Mistakes
- Applying greedy when DP is needed (can't prove greedy choice property)
- Not sorting by the right key (e.g., intervals by start vs end makes different algorithms)
- Jump Game II: not using BFS-level approach, trying DP → O(n²) instead of O(n) greedy
- Confusing "can I reach" (boolean) with "minimum steps" (count) in jump problems
- Not handling edge cases: empty array, single element, all same values

---

## Module 14: Bit Manipulation

### Key Concepts
- **Bitwise operators:** AND (&), OR (|), XOR (^), NOT (~), left shift (<<), right shift (>>)
- **Essential tricks:**
  - `n & (n-1)` — clear lowest set bit (used in counting bits, power of 2 check)
  - `n & (-n)` — isolate lowest set bit (used in Binary Indexed Tree / Fenwick Tree)
  - `n ^ n = 0`, `n ^ 0 = n` — XOR for cancellation (single number problems)
  - `n >> k & 1` — check if kth bit is set
  - `n | (1 << k)` — set kth bit; `n & ~(1 << k)` — clear kth bit
- **XOR problems:**
  - Single Number — XOR all elements, result is the unique one
  - Single Number II — count bits mod 3 (generalized: mod k)
  - Single Number III — XOR all, then split into two groups by a differing bit
  - Missing number — XOR with indices
- **Bit counting:** Brian Kernighan's algorithm (n & (n-1) loop); Hamming distance
- **Power of 2** — `n > 0 && (n & (n-1)) == 0`
- **Bitmask for subsets** — enumerate all subsets of n elements (2^n); iterate submasks of a mask
- **Bit manipulation in DP** — bitmask DP for TSP, task assignment

### Top Interview Problems
1. **Single Number** — XOR all; follow-up: two unique numbers (Single Number III)
2. **Counting Bits** — DP using `dp[n] = dp[n & (n-1)] + 1` or `dp[n] = dp[n >> 1] + (n & 1)`
3. **Reverse Bits** — bit-by-bit reversal; O(1) with divide-and-conquer swap
4. **Subsets via bitmask** — enumerate 0 to 2^n-1, include element i if bit i is set
5. **Missing Number** — XOR approach or math (sum formula); handle overflow with XOR

### Common Mistakes
- Signed vs unsigned right shift (>> vs >>> in Java) — sign extension issues
- Not considering integer overflow with left shift
- XOR: forgetting that order doesn't matter (associative + commutative)
- Bitmask DP: using int when n > 30 (need long) or n > 62 (need different approach)
- Confusing bitwise AND/OR with logical AND/OR (& vs && in Java)

---

## Module 15: Intervals

### Key Concepts
- **Interval representation** — [start, end]; open vs closed; clarify in interview
- **Merge intervals** — sort by start, extend end if overlapping; O(n log n)
- **Insert interval** — find position, merge with overlapping, O(n)
- **Interval intersection** — two pointers on two sorted interval lists
- **Non-overlapping intervals** — sort by end, count min removals (activity selection / greedy)
- **Meeting rooms:**
  - Can attend all? — sort by start, check no overlap
  - Minimum rooms needed — sort start/end separately OR min-heap of end times; sweep line
- **Sweep line technique:**
  - Convert intervals to events (+1 at start, -1 at end), sort, scan
  - Applications: max overlapping intervals, minimum platforms, sky line problem

### Top Interview Problems
1. **Merge Intervals** — sort + linear merge; the fundamental interval problem
2. **Insert Interval** — handle 3 phases: before, overlapping, after; O(n)
3. **Meeting Rooms II** — min-heap approach or sweep line; equivalent to "minimum platforms"
4. **Non-overlapping Intervals** — greedy: sort by end, count conflicts to remove
5. **Employee Free Time** — merge k sorted interval lists using min-heap; find gaps

### Common Mistakes
- Not sorting by start time first (or sorting by wrong key)
- Off-by-one: `[1,5], [5,10]` — do these overlap? Clarify with interviewer
- Meeting rooms: not realizing sort-starts + sort-ends separately gives O(n log n) without heap
- Sweep line: handling events at same timestamp in wrong order (end before start vs start before end)
- Forgetting to handle empty interval list

---

## Module 16: Advanced

### Key Concepts
- **Segment Tree:**
  - Range query + point update in O(log n); build O(n)
  - Range query + range update with lazy propagation
  - Applications: range sum, range min/max, count of elements in range
  - Implementation: array-based (2*n size) or node-based
- **Binary Indexed Tree (Fenwick Tree):**
  - Prefix sum query + point update in O(log n)
  - Simpler than segment tree but limited to prefix operations
  - `i & (-i)` to navigate tree
  - Applications: count inversions, range sum queries
- **Math & Geometry:**
  - Line sweep for computational geometry
  - Convex hull (Graham scan, Andrew's monotone chain)
  - Detecting collinear points (cross product = 0)
  - Rectangle overlap / area of union of rectangles
  - Random pick with weight (prefix sum + binary search)
  - Reservoir sampling (random selection from stream)
- **String algorithms (advanced):**
  - KMP pattern matching — O(n+m); failure function construction
  - Rabin-Karp — rolling hash; O(n) average for pattern matching
  - Z-algorithm — pattern matching alternative to KMP
- **Miscellaneous advanced:**
  - LRU/LFU cache (already covered but design depth)
  - Skip list
  - Bloom filter concept
  - Sqrt decomposition

### Top Interview Problems
1. **Range Sum Query - Mutable** — segment tree or BIT; immutable version uses prefix sum
2. **Count of Range Sum** — merge sort or BIT; count prefix sums in range
3. **The Skyline Problem** — sweep line + max-heap or segment tree
4. **Rectangle Area II** — coordinate compression + sweep line
5. **Random Pick with Weight** — prefix sum + binary search; uniform random to weighted

### Common Mistakes
- Segment tree: off-by-one in build/query ranges; forgetting to propagate lazy updates
- BIT: 1-indexed (not 0-indexed); forgetting this causes silent bugs
- KMP: building failure function incorrectly; not understanding why it's O(n+m)
- Geometry: floating point precision issues; use cross product (integer) over angle (float) when possible
- Over-engineering: reaching for segment tree when a simpler prefix sum or monotonic stack suffices

---

## Cross-Module: Meta-Skills for FAANG Interviews

### Pattern Recognition Cheat Sheet
| If you see... | Think... |
|---|---|
| "Subarray sum" | Prefix sum + hash map |
| "Longest/shortest substring with condition" | Sliding window |
| "Top K / Kth largest" | Heap or Quick Select |
| "Sorted array + search" | Binary search |
| "Tree path problem" | DFS recursion, track path |
| "Shortest path unweighted" | BFS |
| "Shortest path weighted" | Dijkstra / Bellman-Ford |
| "Build order / dependencies" | Topological sort |
| "Generate ALL solutions" | Backtracking |
| "Count ways / optimize" | DP |
| "Connected components / grouping" | Union-Find or DFS |
| "Overlapping intervals" | Sort + sweep/merge |
| "Find unique / missing" | XOR / bit manipulation |

### Universal Interview Mistakes
1. **Jumping to code** — always clarify inputs, constraints, and edge cases FIRST
2. **Not stating complexity** — time AND space for every approach
3. **Ignoring edge cases** — empty input, single element, all same, overflow, negative numbers
4. **Not testing** — walk through 1-2 examples on your solution before saying "done"
5. **Optimizing prematurely** — start with brute force, then optimize; interviewers want to see the journey
