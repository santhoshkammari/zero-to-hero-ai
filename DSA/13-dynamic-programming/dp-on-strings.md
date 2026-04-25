# DP on Strings

> Two-string DP problems are among the most-asked DP questions at Google/Amazon/Microsoft — master the 2D table and you unlock a dozen problems.

## Core Idea

Most string DP problems boil down to: **"compare two strings character by character and fill a 2D table."** The cell `dp[i][j]` represents the answer for `text1[:i]` and `text2[:j]`. At each cell, you ask: do the current characters match? If yes, take the diagonal. If no, try skipping a character from one or both strings and pick the best option.

Think of it like a spreadsheet: rows are characters of one string, columns are the other. You fill it cell-by-cell, and the answer sits at the bottom-right corner.

## What You Need to Know

### The 2D String DP Framework

Every problem in this family shares the same skeleton:

1. **Define state**: `dp[i][j]` = answer considering `s1[:i]` and `s2[:j]`
2. **Base cases**: empty string vs anything (row 0 and column 0)
3. **Transition**: depends on whether `s1[i-1] == s2[j-1]` (note the 1-index offset!)
4. **Answer**: usually `dp[m][n]` (bottom-right cell)

### Why 1-indexed DP with 0-indexed strings?

The DP table has dimensions `(m+1) x (n+1)` to accommodate the empty-string base cases. Row 0 means "empty prefix of s1", column 0 means "empty prefix of s2". So `dp[i][j]` talks about `s1[:i]` and `s2[:j]`, and when you check the current characters, you compare `s1[i-1]` and `s2[j-1]`.

---

### Longest Common Subsequence (LC 1143)

The foundational 2D string DP. Everything else is a variation.

**Recurrence:**
- If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1` (match — extend the subsequence)
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (skip one char from either string, keep the better)

**Why it works:** A common subsequence either includes the current pair of matching characters, or it doesn't include at least one of them. The recurrence covers all cases.

| | "" | a | b | c | d | e |
|---|---|---|---|---|---|---|
| **""** | 0 | 0 | 0 | 0 | 0 | 0 |
| **a** | 0 | 1 | 1 | 1 | 1 | 1 |
| **c** | 0 | 1 | 1 | 2 | 2 | 2 |
| **e** | 0 | 1 | 1 | 2 | 2 | 3 |

| Aspect | Value |
|--------|-------|
| Time | O(m × n) |
| Space | O(m × n), optimizable to O(min(m, n)) |

---

### Edit Distance (LC 72)

The single most important 2D string DP problem. Used in spell checkers, `git diff`, DNA alignment. Interviewers love it because the transitions test whether you truly understand DP.

**Recurrence** — each cell asks "what's the cheapest last operation?":
- **Replace** (or match): `dp[i-1][j-1] + (0 if s1[i-1] == s2[j-1] else 1)`
- **Delete** from s1: `dp[i-1][j] + 1` (shrink s1 by one char)
- **Insert** into s1: `dp[i][j-1] + 1` (equivalent to advancing in s2)

`dp[i][j] = min(replace, delete, insert)`

**Why delete = go up, insert = go left?** Deleting a char from `s1` means we now need to convert `s1[:i-1]` to `s2[:j]` — that's one row up. Inserting a char into `s1` to match `s2[j-1]` means we still have `s1[:i]` left but now only need to match `s2[:j-1]` — that's one column left.

**Base cases:**
- `dp[i][0] = i` (delete all chars from s1)
- `dp[0][j] = j` (insert all chars of s2)

| Aspect | Value |
|--------|-------|
| Time | O(m × n) |
| Space | O(m × n), optimizable to O(n) with rolling row |

---

### Longest Palindromic Subsequence (LC 516)

**Key insight:** The longest palindromic subsequence of `s` is just the LCS of `s` and `reversed(s)`. That's it. One reduction, full reuse of LCS code.

**Why?** A palindromic subsequence reads the same forwards and backwards. Any common subsequence between `s` and `reverse(s)` is, by definition, a palindrome.

| Aspect | Value |
|--------|-------|
| Time | O(n²) |
| Space | O(n²), optimizable to O(n) |

You can also solve it directly with interval DP: `dp[i][j]` = longest palindromic subsequence in `s[i..j]`.

---

### Longest Palindromic Substring (LC 5)

Unlike the subsequence version, here we need **contiguous** characters.

**Approach 1: Expand Around Center** — For each possible center (2n − 1 centers: n single chars + n−1 gaps), expand outward while characters match. Simple and efficient.

**Approach 2: DP** — `dp[i][j] = True` if `s[i..j]` is a palindrome. Fill diagonally: length 1, length 2, then length 3+.

| Approach | Time | Space |
|----------|------|-------|
| Expand around center | O(n²) | O(1) |
| DP table | O(n²) | O(n²) |
| Manacher's (bonus) | O(n) | O(n) |

Interviewers almost always expect expand-around-center. Know the DP version for follow-ups.

---

### Regular Expression Matching (LC 10)

Hard but classic. Pattern can contain `.` (any single char) and `*` (zero or more of preceding char).

**State:** `dp[i][j]` = does `s[:i]` match `p[:j]`?

**Transitions:**
- `p[j-1]` is a normal char or `.`: match if current chars match and `dp[i-1][j-1]`
- `p[j-1]` is `*`: two choices:
  - **Zero occurrences** of preceding char: `dp[i][j-2]` (skip the `x*` pattern entirely)
  - **One+ occurrences**: `dp[i-1][j]` if `s[i-1]` matches `p[j-2]` (consume one char from s, keep `*` active)

| Aspect | Value |
|--------|-------|
| Time | O(m × n) |
| Space | O(m × n) |

---

### Wildcard Matching (LC 44)

Similar to regex but simpler: `?` matches any single char, `*` matches any sequence (including empty).

**Key difference from LC 10:** Here `*` is standalone (not tied to a preceding character), so the transition is simpler:
- `*`: `dp[i-1][j]` (match one more char) OR `dp[i][j-1]` (match empty)
- `?` or char match: `dp[i-1][j-1]`

| Aspect | Value |
|--------|-------|
| Time | O(m × n) |
| Space | O(m × n) |

---

### Space Optimization

All 2D string DPs can be optimized from O(m × n) to O(min(m, n)) because each row only depends on the current and previous row.

**The trick:** Use a 1D array and update it left-to-right, keeping a `prev_diagonal` variable to hold the value that would have been overwritten.

```python
# Space-optimized LCS: O(min(m, n)) space
def lcs_optimized(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1  # s2 is the shorter one
    m, n = len(s1), len(s2)
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0  # dp[i-1][0]
        for j in range(1, n + 1):
            temp = dp[j]  # save before overwrite
            if s1[i-1] == s2[j-1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev = temp
    return dp[n]
```

## Key Patterns & Templates

### Template 1: Longest Common Subsequence (LC 1143)

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # match: extend from diagonal
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # skip one char

    return dp[m][n]
```

### Template 2: Edit Distance (LC 72)

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i  # delete all from word1
    for j in range(n + 1):
        dp[0][j] = j  # insert all of word2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]        # no edit needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],  # replace
                    dp[i-1][j],    # delete from word1
                    dp[i][j-1],    # insert into word1
                )

    return dp[m][n]
```

### Template 3: Longest Palindromic Subsequence (LC 516)

```python
def longestPalindromeSubseq(s: str) -> int:
    # Reduce to LCS(s, reverse(s))
    return longestCommonSubsequence(s, s[::-1])
```

Or the direct interval DP approach:

```python
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # single char is a palindrome

    for length in range(2, n + 1):           # substring length
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
```

### Template 4: Longest Palindromic Substring — Expand Around Center (LC 5)

```python
def longestPalindrome(s: str) -> str:
    start, max_len = 0, 1

    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)      # odd-length palindromes
        expand(i, i + 1)  # even-length palindromes

    return s[start:start + max_len]
```

### Template 5: Regular Expression Matching (LC 10)

```python
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # patterns like a*, a*b*, a*b*c* can match empty string
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # zero occurrences of preceding element
                dp[i][j] = dp[i][j-2]
                # one+ occurrences (if current char matches preceding pattern char)
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Longest Common Subsequence | 1143 | Medium | The foundational 2D string DP — match → diagonal+1, no match → max(up, left) |
| Edit Distance | 72 | Medium | Three operations map to three adjacent cells; base cases are deletions/insertions of full string |
| Longest Palindromic Subsequence | 516 | Medium | Reduce to LCS(s, reverse(s)) — the "aha" that saves you from reinventing the wheel |
| Longest Palindromic Substring | 5 | Medium | Expand around center is simpler and O(1) space — 2n−1 centers, not n |
| Regular Expression Matching | 10 | Hard | `*` means "zero or more of preceding" — handle zero case (skip 2 cols) and one+ case separately |
| Wildcard Matching | 44 | Hard | `*` is standalone (unlike LC 10) — simpler transitions: match one more char OR match empty |
| Distinct Subsequences | 115 | Hard | Count ways: match → `dp[i-1][j-1] + dp[i-1][j]`, no match → `dp[i-1][j]` (always can skip) |
| Shortest Common Supersequence | 1092 | Hard | Find LCS first, then reconstruct by weaving in non-LCS characters |

## Common Mistakes

- **Confusing 0-indexed strings with 1-indexed DP table.** The DP table is `(m+1) × (n+1)`. When you're at `dp[i][j]`, the current characters are `s1[i-1]` and `s2[j-1]`, not `s1[i]` and `s2[j]`. Off-by-one here = wrong answer that's brutally hard to debug.

- **Forgetting space optimization for LCS/edit distance.** Interviewers expect you to mention it, even if you code the 2D version first. The key: each row depends only on the previous row → use a 1D array with a `prev_diagonal` variable.

- **Getting edit distance operations backwards.** Remember: delete = look up (`dp[i-1][j]`), insert = look left (`dp[i][j-1]`), replace = look diagonal (`dp[i-1][j-1]`). Mixing these up changes the meaning entirely.

- **Regex matching: not initializing `dp[0][j]` for `*` patterns.** Patterns like `a*b*` can match an empty string. You need to initialize the first row by checking: if `p[j-1] == '*'`, then `dp[0][j] = dp[0][j-2]`.

- **Expand-around-center: forgetting even-length palindromes.** There are `2n − 1` centers, not `n`. You must expand from both `(i, i)` and `(i, i+1)` for each position.

## Interview Questions

1. **"Walk me through how you'd compute the LCS of two strings."** — Fill the 2D table, explain match vs. no-match transitions. Mention space optimization.

2. **"Given two words, find the minimum number of operations to convert one to the other."** — Edit Distance (LC 72). Clearly explain all three operations and their cell mappings.

3. **"How would you find the longest palindromic subsequence?"** — Reduce to LCS with reversed string. Bonus: explain the interval DP approach.

4. **"Find the longest palindromic substring."** — Expand around center. Explain why 2n−1 centers, not n.

5. **"Implement regex matching with `.` and `*`."** — LC 10. The `*` transition is the crux: zero occurrences vs. one-or-more.

6. **"Can you optimize the space complexity of your LCS solution?"** — Yes, from O(mn) to O(min(m,n)) using a single row + prev_diagonal variable. Be ready to code it.

7. **"What's the difference between wildcard matching and regex matching?"** — In wildcard (LC 44), `*` matches any sequence independently. In regex (LC 10), `*` modifies the preceding character. This changes the transitions.

8. **"How would you find the shortest common supersequence of two strings?"** — Compute LCS first, then reconstruct by interleaving non-LCS characters (LC 1092).

9. **"Count the number of distinct subsequences of `s` that equal `t`."** — LC 115. Match → sum of using and skipping the match. No match → must skip.

10. **"How is edit distance used in real-world systems?"** — Spell check suggestions, `git diff` / `diff` tools, DNA/protein sequence alignment (bioinformatics), fuzzy search.

## Quick Reference

### Decision Flowchart

```
String DP Problem?
├── Two strings, compare them?
│   ├── Longest common something → LCS pattern (LC 1143)
│   ├── Transform one into another → Edit Distance pattern (LC 72)
│   ├── Pattern matching (., *) → Regex/Wildcard DP (LC 10, 44)
│   └── Count subsequences → Distinct Subsequences (LC 115)
└── Single string, palindrome?
    ├── Subsequence → LCS(s, reverse(s)) (LC 516)
    └── Substring → Expand around center (LC 5)
```

### Complexity Table

| Problem | Time | Space | Space (Optimized) |
|---------|------|-------|--------------------|
| LCS (LC 1143) | O(mn) | O(mn) | O(min(m,n)) |
| Edit Distance (LC 72) | O(mn) | O(mn) | O(n) |
| Palindromic Subseq (LC 516) | O(n²) | O(n²) | O(n) |
| Palindromic Substr (LC 5) | O(n²) | O(1)* | — |
| Regex Matching (LC 10) | O(mn) | O(mn) | O(n) |
| Wildcard Matching (LC 44) | O(mn) | O(mn) | O(n) |
| Distinct Subseq (LC 115) | O(mn) | O(mn) | O(n) |
| Shortest Superseq (LC 1092) | O(mn) | O(mn) | — |

\* Expand-around-center approach

### Core Recurrence Cheat Sheet

```
LCS:     match → diag + 1       | no match → max(up, left)
Edit:    match → diag            | no match → 1 + min(diag, up, left)
Distinct Subseq: match → diag + up | no match → up
```
