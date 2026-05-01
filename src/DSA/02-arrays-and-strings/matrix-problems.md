# Matrix Problems

> Matrix problems are array problems in 2D. The key skill: mapping row/col to the right traversal pattern.

## Core Idea

A matrix is a 2D array. Most matrix problems involve traversal patterns (spiral, diagonal), search (treat as 1D or staircase), transformation (rotate, transpose), or grid-based DFS/BFS. The trick is always about **index manipulation**.

---

## What You Need to Know

- **Matrix traversal**: row-major, column-major, spiral order, diagonal traversal.
- **Rotation**: 90° clockwise = transpose + reverse each row. 90° counter-clockwise = transpose + reverse each column (or reverse rows then transpose).
- **Transpose**: swap `matrix[i][j]` with `matrix[j][i]` for `i < j`.
- **Search in sorted matrix**:
  - Rows sorted, first elem > last of prev row → treat as 1D sorted array, binary search. Index `k` maps to `matrix[k // cols][k % cols]`.
  - Rows sorted AND columns sorted → staircase search from top-right or bottom-left. O(m+n).
- **Grid DFS/BFS**: Number of islands pattern. 4-directional movement. Mark visited.
- **2D prefix sums**: for region sum queries (covered in [prefix-sums.md](prefix-sums.md)).

---

## Key Patterns & Templates

### 1. Spiral Order Traversal (LC 54)

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # traverse right across top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # traverse down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # traverse left across bottom row (if rows remain)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # traverse up along left column (if columns remain)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

# [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]
# The if-checks after top/right updates prevent duplicates in non-square matrices
```

### 2. Rotate Matrix 90° In-Place (LC 48)

```python
def rotate(matrix: list[list[int]]) -> None:
    """90° clockwise = transpose + reverse each row. Modifies in-place."""
    n = len(matrix)

    # Step 1: transpose — swap matrix[i][j] with matrix[j][i]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row
    for row in matrix:
        row.reverse()

# [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]
# 90° CCW: transpose + reverse each column (or reverse all rows, then transpose)
```

### 3. Search in Sorted Matrix — Binary Search as 1D (LC 74)

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Each row sorted, first element > last of previous row → treat as 1D."""
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]  # map 1D index to 2D
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False

# O(log(m*n)) — same as binary search on a flat sorted array
```

### 4. Staircase Search in Row-Col Sorted Matrix (LC 240)

```python
def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    """Rows sorted left→right, columns sorted top→bottom. Start top-right."""
    if not matrix:
        return False

    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1  # too big, move left
        else:
            row += 1  # too small, move down

    return False

# O(m + n) — each step eliminates a full row or column
# Can also start from bottom-left (symmetric logic)
```

### 5. Grid DFS Template (Island Counting — LC 200)

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '#'  # mark visited BEFORE recursing to prevent infinite loops
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count

# Mark visited BEFORE recursive calls, not after — otherwise you revisit and stack overflow
# Modifying grid in-place avoids a separate visited set
```

---

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Spiral Matrix | 54 | Medium | Track boundaries: top, bottom, left, right. Shrink after each direction. |
| Rotate Image | 48 | Medium | 90° CW = transpose + reverse each row. In-place, O(1) space. |
| Search a 2D Matrix | 74 | Medium | Treat as 1D sorted array: `mid → matrix[mid//n][mid%n]`. Standard binary search. |
| Set Matrix Zeroes | 73 | Medium | Use first row/col as markers. Separate flag for first row/col themselves. |
| Valid Sudoku | 36 | Medium | Track seen in `rows[9]`, `cols[9]`, `boxes[9]` sets. Box index = `(r//3)*3 + c//3`. |
| Game of Life | 289 | Medium | Encode transitions in-place: use 2 (was 1→0) and 3 (was 0→1). Decode with `% 2` and `> 1`. |

---

## Common Mistakes

- **Spiral traversal**: not checking `top <= bottom` and `left <= right` after each direction change — causes duplicates for non-square matrices.
- **Rotate**: confusing in-place (transpose + reverse) with creating a new matrix. Interviewers want in-place.
- **Search 2D matrix**: using staircase search O(m+n) when full sorted guarantees O(log(m×n)) binary search. Know which problem you're solving — LC 74 vs LC 240.
- **Set Matrix Zeroes**: zeroing as you scan → cascading zeros. Must record all zero positions first, *then* zero out.
- **Grid problems**: forgetting to mark visited **BEFORE** recursion, not after — causes infinite loops and stack overflow.
- **Index mapping**: `matrix[k // n][k % n]` uses `n` (number of columns), not `m`. Getting this wrong silently produces wrong results.

---

## Interview Questions

- **"Traverse a matrix in spiral order."**
  - Use four boundary variables. After traversing each direction, shrink the corresponding boundary. Check bounds before the 3rd and 4th directions.
- **"Rotate a matrix 90° clockwise in-place — what's the trick?"**
  - Transpose (swap across diagonal) + reverse each row. Two simple passes, O(1) extra space.
- **"Search a sorted matrix — which approach and when?"**
  - Fully sorted (LC 74): binary search as 1D, O(log(m×n)). Row+col sorted (LC 240): staircase from top-right, O(m+n).
- **"Set Matrix Zeroes with O(1) extra space — how?"**
  - Use the first row and first column as markers. Process inner matrix first, then handle first row/col using saved flags.
- **"How do you compute the box index for a Sudoku cell?"**
  - `box_index = (row // 3) * 3 + col // 3`. Maps each 3×3 box to indices 0–8.
- **"Implement Game of Life in-place — how do you avoid overwriting needed state?"**
  - Encode transitions: 2 means "was alive, now dead", 3 means "was dead, now alive". Original state = `val % 2`. New state = `val > 1`.

---

## Quick Reference

| Problem Type | Key Technique | Time |
|---|---|---|
| Spiral traversal | Four boundaries, shrink | O(m×n) |
| Rotation 90° CW | Transpose + reverse rows | O(m×n) |
| Binary search (full sort) | Treat as 1D, `k → [k//n][k%n]` | O(log(m×n)) |
| Staircase search | Start top-right | O(m+n) |
| Grid DFS/BFS | Mark visited, 4 directions | O(m×n) |
