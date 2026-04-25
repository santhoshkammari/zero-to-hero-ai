# 🚀 DSA Interview Prep — Zero to Hero

**For data scientists with Python experience, targeting Google / Amazon / Microsoft interviews.**

You already think in data. You work with NumPy, pandas, and SQL daily. Now it's time to translate that analytical mindset into the language of technical interviews. This course is built specifically for people like you — we skip the "what is a variable" preamble and go straight to the patterns and techniques that show up in real interviews.

The goal isn't to memorize 500 LeetCode solutions. It's to **recognize patterns**, build intuition, and solve problems you've never seen before.

Let's get started.

---

## 📂 Course Structure

```
DSA/
├── 01-foundations/
│   ├── complexity-analysis.md
│   ├── recursion.md
│   └── math-essentials.md
├── 02-arrays-and-strings/
│   ├── arrays-fundamentals.md
│   ├── string-manipulation.md
│   ├── two-pointers.md
│   ├── sliding-window.md
│   ├── prefix-sums.md
│   └── matrix-problems.md
├── 03-hashing/
│   └── hash-maps-and-sets.md
├── 04-linked-lists/
├── 05-stacks-and-queues/
├── 06-sorting/
├── 07-binary-search/
├── 08-trees/
├── 09-tries/
├── 10-graphs/
├── 11-greedy/
├── 12-backtracking/
├── 13-dynamic-programming/
├── 14-intervals/
├── 15-bit-manipulation/
└── 16-advanced/
```

---

## 📖 How to Use This Course

1. **Go in order.** Modules build on each other — foundations first, advanced topics last.
2. **Aim for 1–2 modules per week.** Consistency beats intensity. A steady pace over 8–10 weeks will cover everything.
3. **Focus on pattern recognition, not memorization.** Each module teaches you *when* to apply a technique, not just *how*. If you understand the "why," you can handle problems you've never seen.
4. **Practice after each module.** Read the notes, then immediately solve 3–5 problems. Spaced repetition is your friend.
5. **Revisit the cheat sheets below** whenever you get stuck during practice. They're designed as quick-reference guides.

---

## 🧠 Pattern Recognition Cheat Sheet

The single most valuable skill in interviews is reading a problem and knowing which tool to reach for.

| If you see...                              | Think...                      |
| ------------------------------------------ | ----------------------------- |
| "Subarray sum"                             | Prefix sum + hash map         |
| "Longest/shortest substring with condition"| Sliding window                |
| "Top K / Kth largest"                      | Heap or Quick Select          |
| "Sorted array + search"                    | Binary search                 |
| "Tree path problem"                        | DFS recursion, track path     |
| "Shortest path unweighted"                 | BFS                           |
| "Shortest path weighted"                   | Dijkstra / Bellman-Ford       |
| "Build order / dependencies"               | Topological sort              |
| "Generate ALL solutions"                   | Backtracking                  |
| "Count ways / optimize"                    | DP                            |
| "Connected components / grouping"          | Union-Find or DFS             |
| "Overlapping intervals"                    | Sort + sweep/merge            |
| "Find unique / missing"                    | XOR / bit manipulation        |

---

## ⏱️ Complexity Cheat Sheet

### Data Structures

| Data Structure      | Access   | Search   | Insert   | Delete   |
| ------------------- | -------- | -------- | -------- | -------- |
| Array               | O(1)     | O(n)     | O(n)     | O(n)     |
| Linked List         | O(n)     | O(n)     | O(1)*    | O(1)*    |
| Hash Map            | —        | O(1) avg | O(1) avg | O(1) avg |
| Stack / Queue       | O(n)     | O(n)     | O(1)     | O(1)     |
| Binary Search Tree  | O(log n) | O(log n) | O(log n) | O(log n) |
| Balanced BST        | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap                | —        | O(n)     | O(log n) | O(log n) |
| Trie                | —        | O(m)     | O(m)     | O(m)     |

\* = with reference to node · m = key length

### Sorting Algorithms

| Algorithm      | Best       | Average    | Worst      | Space    | Stable |
| -------------- | ---------- | ---------- | ---------- | -------- | ------ |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
| Counting Sort  | O(n+k)     | O(n+k)     | O(n+k)     | O(k)     | Yes    |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |

---

## 🎯 Study Priority

Focus your energy where it matters most. These estimates reflect frequency across real FAANG-style interviews.

| Priority | Topic                                  | Coverage              |
| -------- | -------------------------------------- | --------------------- |
| 🔴 P0   | Arrays & Hashing                       | ~25% of interviews    |
| 🔴 P0   | Trees & Graphs                         | ~20% of interviews    |
| 🟠 P1   | Dynamic Programming                    | ~15% of interviews    |
| 🟠 P1   | Binary Search                          | ~10% of interviews    |
| 🟡 P2   | Stacks & Sliding Window                | ~10% of interviews    |
| 🟡 P2   | Backtracking                           | ~8% of interviews     |
| 🟢 P3   | Linked Lists, Greedy, Tries, Bits      | ~12% of interviews    |

If you're short on time, nail P0 and P1 first. That alone covers ~70% of what you'll face.

---

Good luck. You've got this. 🎯
