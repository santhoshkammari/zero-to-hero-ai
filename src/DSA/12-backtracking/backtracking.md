# Backtracking

> Backtracking = controlled brute force. It builds solutions incrementally, abandoning paths that can't lead to valid answers. When the problem says "find ALL" — this is your tool.

## Core Idea

**Backtracking** systematically explores all potential solutions using a **choose → explore → unchoose** framework. It's recursion with cleanup: make a choice, recurse, then *undo* that choice before trying the next option. The power comes from **pruning** — skipping entire branches of the recursion tree when you know they can't lead to valid solutions.

## What You Need to Know

### When Backtracking vs DP

| | Backtracking | DP |
|---|---|---|
| Goal | Find **all** valid solutions | Find **count** or **optimal** solution |
| Approach | Enumerate explicitly | Compute from subproblems |
| Output | List of solutions | Single number or sequence |
| Pruning | Key optimization | N/A (memoization instead) |
| Example | Generate all permutations | Count permutations |

### The Universal Template

Every backtracking problem fits this skeleton:

```python
def backtrack(start, path, ...):
    if is_goal(path):                        # base case
        result.append(path[:])               # copy! path is mutable
        return
    
    for i in range(start, len(choices)):
        if not is_valid(choices[i]):         # prune
            continue
        
        path.append(choices[i])              # choose
        backtrack(i_or_i_plus_1, path, ...)  # explore
        path.pop()                           # un-choose
```

**Three key decisions** for each problem:
1. **What's the start index?** `i` for reuse allowed, `i+1` for no reuse
2. **When do I stop?** (base case — target reached, length met, etc.)
3. **How do I prune?** (skip duplicates, bail early on invalid state)

### Subsets vs Permutations vs Combinations

| Problem Type | Loop Start | Key Difference |
|-------------|-----------|----------------|
| **Subsets** | `i = start` → `i+1` | Every node in recursion tree is a valid subset |
| **Combinations** | `i = start` → `i+1` | Only collect when size/sum meets target |
| **Permutations** | `i = 0` (with `used[]`) | Use all elements; order matters |

## Key Patterns & Templates

### Subsets (LC 78)

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # every node is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

**Time: O(n · 2ⁿ)** — 2ⁿ subsets, each takes O(n) to copy.

### Subsets II — With Duplicates (LC 90)

Sort first, then skip adjacent duplicates at the same recursion level.

```python
def subsetsWithDup(nums):
    nums.sort()
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # skip duplicate at same level
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

**The `i > start` condition is crucial** — the first occurrence at each recursion level is allowed, but subsequent duplicates are skipped.

### Permutations (LC 46)

```python
def permute(nums):
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    
    backtrack([])
    return result
```

**Key difference from subsets:** always start loop at 0, use `used[]` array instead of `start` index. Time: O(n · n!).

### Permutations II — With Duplicates (LC 47)

```python
def permuteUnique(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicate: same value as previous, and previous wasn't used at this level
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    
    backtrack([])
    return result
```

### Combination Sum (LC 39) — Reuse Allowed

```python
def combinationSum(candidates, target):
    result = []
    candidates.sort()
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:  # prune: sorted, so all future too large
                break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse)
            path.pop()
    
    backtrack(0, [], target)
    return result
```

### Combination Sum II (LC 40) — No Reuse, With Duplicates

```python
def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:  # skip duplicates
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result
```

### Word Search (LC 79) — Grid Backtracking

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'  # mark visited
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            if backtrack(r + dr, c + dc, idx + 1):
                return True
        
        board[r][c] = temp  # un-mark (backtrack)
        return False
    
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False
```

### Palindrome Partitioning (LC 131)

```python
def partition(s):
    result = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    backtrack(0, [])
    return result
```

### N-Queens (LC 51)

```python
def solveNQueens(n):
    result = []
    cols = set()
    diag = set()       # row - col is constant on each diagonal
    anti_diag = set()  # row + col is constant on each anti-diagonal
    board = [['.' ] * n for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag or (row + col) in anti_diag:
                continue
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)
            board[row][col] = 'Q'
            
            backtrack(row + 1)
            
            board[row][col] = '.'
            cols.remove(col)
            diag.remove(row - col)
            anti_diag.remove(row + col)
    
    backtrack(0)
    return result
```

**The diagonal trick:** cells on the same diagonal share the same `row - col` value; cells on the same anti-diagonal share the same `row + col` value. This makes conflict checking O(1).

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Subsets | 78 | Medium | Every recursion node = valid subset |
| Permutations | 46 | Medium | Start from 0 with `used[]` array |
| Combination Sum | 39 | Medium | Pass `i` (not `i+1`) for reuse |
| Combination Sum II | 40 | Medium | Sort + skip `i > start and nums[i] == nums[i-1]` |
| Word Search | 79 | Medium | Grid backtracking: mark/unmark visited cells |
| Palindrome Partitioning | 131 | Medium | Try all cuts where substring is palindrome |
| N-Queens | 51 | Hard | Row-by-row placement; O(1) diagonal check via `row±col` |
| Sudoku Solver | 37 | Hard | Constraint propagation + backtracking |

## Common Mistakes

- **Not undoing changes (the "un-choose" step)** — corrupts state for sibling branches. Every `append` needs a `pop`, every `add` needs a `remove`, every mark needs an unmark.
- **Forgetting to sort before skipping duplicates** — the `nums[i] == nums[i-1]` trick only works on sorted arrays
- **Using `start` index for permutations** — permutations use `used[]` array starting from 0. Using `start` gives combinations, not permutations.
- **Not copying `path` before appending to result** — `result.append(path)` stores a reference. When `path` changes, so does the result. Always use `path[:]` or `list(path)`.
- **Not pruning early** — generating all 2ⁿ or n! possibilities when most are invalid. Sort + break early when remaining candidates are too large.
- **Word Search: not restoring the cell** — modifying the board permanently instead of restoring after backtrack

## Interview Questions

- "Generate all subsets of a set." (LC 78 — the starting point for all backtracking)
- "Generate all permutations. Now handle duplicates." (LC 46/47)
- "Find all combinations that sum to a target. Each number used once." (LC 40 — how do you handle duplicates?)
- "Find a word in a grid by moving to adjacent cells." (LC 79 — Amazon/Microsoft)
- "Partition a string so every part is a palindrome." (LC 131)
- "Place N queens on an N×N board so no two attack each other." (LC 51 — classic)
- "What's the time complexity of generating all subsets? All permutations?"
- "How is backtracking different from brute force?" (Pruning! Backtracking cuts branches, brute force explores everything.)
- "When would you use backtracking vs DP?" (All solutions → backtracking; count/optimal → DP)
- "Solve a Sudoku puzzle." (LC 37 — constraint satisfaction)

## Quick Reference

```
Backtracking = choose → explore → un-choose

                  Subsets       Combinations    Permutations
Loop start:       start → i+1  start → i+1     0 → n (with used[])
Collect result:   every node    when target met  when len == n
Duplicates:       sort + skip   sort + skip      sort + skip (used[i-1])
Time:             O(n · 2ⁿ)    varies           O(n · n!)

Duplicate handling recipe:
  1. Sort the input
  2. Skip if nums[i] == nums[i-1] AND i > start (combinations)
     OR if nums[i] == nums[i-1] AND not used[i-1] (permutations)

Pruning checklist:
  ✓ Sort to enable early termination (break when too large)
  ✓ Skip invalid choices before recursing
  ✓ Track constraints in sets for O(1) lookup (N-Queens)
  ✓ Grid: mark visited, check bounds, check character match

Key problems by category:
  Selection:  Subsets (78), Subsets II (90)
  Counting:   Combination Sum (39, 40)
  Ordering:   Permutations (46, 47)
  Grid:       Word Search (79), N-Queens (51)
  Partition:  Palindrome Partition (131), Restore IP (93)
```
