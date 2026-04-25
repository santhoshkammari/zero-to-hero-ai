# Math, Geometry & Advanced String Matching

> These topics feel "random" until you're staring at one in a Google on-site. A handful of patterns cover 90% of what gets asked.

## Core Idea

Most math/geometry interview problems aren't about knowing obscure theorems — they're about recognizing that a **mathematical shortcut** turns brute-force into something elegant. The interviewer wants to see if you can spot that structure. Geometry problems almost always reduce to a few linear algebra tricks (cross products, matrix transforms). Advanced string matching tests whether you understand **amortized analysis** and **preprocessing**.

## What You Need to Know

### 1. GCD / LCM — Euclidean Algorithm

**GCD** (Greatest Common Divisor) uses the fact that `gcd(a, b) = gcd(b, a % b)`. Terminates because `a % b` strictly decreases toward 0.

**LCM** follows directly: `lcm(a, b) = a * b // gcd(a, b)`. Compute GCD first to avoid overflow.

```python
import math
# Python 3.9+ has math.gcd and math.lcm built-in
math.gcd(12, 8)     # 4
math.lcm(12, 8)     # 24

# Manual (interview-safe):
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

| Operation | Time Complexity | Note |
|-----------|----------------|------|
| `gcd(a, b)` | O(log min(a, b)) | Fibonacci numbers are worst case |
| `lcm(a, b)` | O(log min(a, b)) | Multiply before dividing risks overflow in other languages |

### 2. Modular Arithmetic

When problems say "return answer mod 10⁹+7," they're preventing overflow and hinting at DP or combinatorics.

Key properties:
- `(a + b) % m = ((a % m) + (b % m)) % m`
- `(a * b) % m = ((a % m) * (b % m)) % m`
- Division requires **modular inverse**: `a / b mod m = a * pow(b, m-2, m) mod m` (when m is prime, by Fermat's little theorem)

```python
MOD = 10**9 + 7

# Modular inverse (m must be prime)
def mod_inverse(b, m=MOD):
    return pow(b, m - 2, m)

# Safe division under mod
def mod_divide(a, b, m=MOD):
    return (a % m) * mod_inverse(b, m) % m
```

### 3. Sieve of Eratosthenes — Finding Primes

The idea: start with all numbers marked as prime, then for each prime p, mark all its multiples starting from p² (smaller multiples already handled by smaller primes).

**Time:** O(n log log n) — nearly linear.  
**Space:** O(n)

### 4. Fast Exponentiation (Binary Exponentiation)

Computing `x^n` naively is O(n). By squaring and halving, we get O(log n). The trick: `x^10 = (x^5)^2`, and `x^5 = x * (x^2)^2`.

### 5. Weighted Random Pick (LC 528)

You have weights `[1, 3, 2]`. You want index 0 with probability 1/6, index 1 with probability 3/6, index 2 with probability 2/6.

The pattern: build a **prefix sum** `[1, 4, 6]`, pick a random number in `[1, 6]`, then **binary search** for where it lands. The prefix sum converts weights into non-overlapping ranges.

### 6. Reservoir Sampling

Problem: pick k items uniformly at random from a stream of unknown length. You can't store the whole stream.

Algorithm for k=1: keep the first item. For the i-th item (1-indexed), replace current pick with probability 1/i. Every element ends up with equal probability 1/n — provable by induction.

```python
import random

def reservoir_sample(stream, k=1):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir
```

### 7. Geometry Essentials

| Concept | Formula / Method | When to Use |
|---------|-----------------|-------------|
| **Cross product** (2D) | `(b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)` | Collinearity (= 0), left/right turn |
| **Collinear check** | Cross product == 0 | Max Points on a Line (LC 149) |
| **Rectangle overlap** | `x_overlap = max(0, min(r1.x2, r2.x2) - max(r1.x1, r2.x1))` | Rectangle Area (LC 223), Overlap (LC 836) |
| **Rotate image** | Transpose → reverse each row | Rotate Image (LC 48) |
| **Spiral traversal** | Shrink boundaries: top, bottom, left, right | Spiral Matrix (LC 54) |

**Golden rule:** use **cross products** (integers) instead of angles (floats) wherever possible. Floating point kills you silently.

### 8. KMP Pattern Matching

Brute-force string matching is O(n·m). **KMP** preprocesses the pattern into a **failure function** (also called LPS — Longest Proper Prefix which is also Suffix) so that on mismatch, you skip ahead intelligently instead of restarting.

Why it's O(n + m): the text pointer never moves backward. The failure function ensures at most 2n comparisons total.

### 9. Rabin-Karp — Rolling Hash

Instead of comparing characters one-by-one, hash the window and compare hashes. On match, verify characters to handle collisions.

**Rolling hash update:** remove leftmost character's contribution, shift, add new character. This makes sliding the window O(1) per step, O(n) total on average.

```python
def rabin_karp(text, pattern, base=256, mod=10**9 + 7):
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    # Precompute base^(m-1) % mod
    h = pow(base, m - 1, mod)
    p_hash = t_hash = 0

    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod

    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            return i
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * base + ord(text[i + m])) % mod
    return -1
```

## Key Patterns & Templates

### Sieve of Eratosthenes

```python
def sieve(n):
    """Returns list of all primes < n."""
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Start from i*i — smaller multiples already crossed off
            for j in range(i * i, n, i):
                is_prime[j] = False
    return [i for i in range(n) if is_prime[i]]
```

### Fast Exponentiation

```python
def power(x, n):
    """Compute x^n in O(log n). Handles negative exponents."""
    if n < 0:
        x, n = 1 / x, -n
    result = 1
    while n:
        if n & 1:          # n is odd — take one x out
            result *= x
        x *= x             # square the base
        n >>= 1            # halve the exponent
    return result

# With modular arithmetic:
# pow(x, n, mod) is built into Python and uses this internally
```

### Binary Search on Prefix Sums (Weighted Random)

```python
import bisect
import random

class WeightedRandom:
    def __init__(self, weights):
        self.prefix = []
        running = 0
        for w in weights:
            running += w
            self.prefix.append(running)

    def pick(self):
        target = random.randint(1, self.prefix[-1])
        # bisect_left finds first index where prefix[i] >= target
        return bisect.bisect_left(self.prefix, target)
```

### KMP Pattern Matching

```python
def kmp_search(text, pattern):
    """Returns all start indices where pattern occurs in text."""
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    # Build failure function (LPS array)
    lps = [0] * m
    length = 0   # length of previous longest prefix-suffix
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            # Don't increment i — try shorter prefix
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search
    results = []
    j = 0  # pointer in pattern
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = lps[j - 1]   # fall back using failure function
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            results.append(i - m + 1)
            j = lps[j - 1]   # continue searching for overlapping matches
    return results
```

### Rotate Image (In-Place 90° Clockwise)

```python
def rotate(matrix):
    """Transpose then reverse each row. O(n²) time, O(1) space."""
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
```

### Spiral Matrix Traversal

```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):       # →
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):        # ↓
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1): # ←
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):  # ↑
                result.append(matrix[row][left])
            left += 1
    return result
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Count Primes | 204 | Medium | Sieve of Eratosthenes; start marking from p², not 2p |
| Pow(x, n) | 50 | Medium | Binary exponentiation; handle n < 0 and n = -2³¹ edge case |
| Random Pick with Weight | 528 | Medium | Prefix sum + `bisect_left`; converting weights to ranges |
| Rotate Image | 48 | Medium | Transpose + reverse rows = 90° clockwise. No extra matrix needed |
| Spiral Matrix | 54 | Medium | Shrinking boundaries; check `top <= bottom` and `left <= right` after direction changes |
| The Skyline Problem | 218 | Hard | Sweep line + max-heap; process events (building start/end) left to right |
| Rectangle Area II | 850 | Hard | Coordinate compression + sweep line; track active intervals |
| Rectangle Overlap | 836 | Easy | Overlap exists iff projections on both axes overlap; negate the no-overlap conditions |

## Common Mistakes

- **Floating point in geometry** — computing angles with `atan2` when you could use cross products with exact integer arithmetic. Interviewers notice and it costs you.
- **KMP failure function off-by-one** — the `elif length:` branch must NOT increment `i`. This is the #1 bug when writing KMP from scratch.
- **Forgetting edge cases in Pow(x, n)** — `n = -2^31` overflows when negated in languages with fixed-width integers. Python handles big ints, but mention this to show awareness.
- **Over-engineering simple math** — reaching for segment trees or fancy structures when basic modular arithmetic or prefix sums solve the problem. Start simple, optimize if needed.
- **Spiral matrix boundary checks** — after moving right→ and down↓, you must re-check `top <= bottom` before going left←, and `left <= right` before going up↑. Missing this causes duplicate traversal.

## Interview Questions

1. **Conceptual:** Why does `gcd(a, b) = gcd(b, a % b)` always terminate? What's the time complexity and why?
2. **Conceptual:** Explain why the Sieve of Eratosthenes starts crossing off at p² instead of 2p. What does this save?
3. **Problem:** Implement `pow(x, n)` handling negative exponents and edge cases. What's the recurrence? *(LC 50)*
4. **Problem:** Given weights, design a system that picks indices with weighted probability. What data structures do you use and why? *(LC 528)*
5. **Problem:** Prove that reservoir sampling gives each element equal probability. Walk through the induction.
6. **Problem:** Rotate an n×n matrix 90° clockwise in-place. Can you do it in O(1) space? *(LC 48)*
7. **Problem:** Return all elements of an m×n matrix in spiral order. What are the tricky edge cases? *(LC 54)*
8. **Conceptual:** Why is KMP O(n + m)? The inner `while` loop looks like it could make it O(n·m) — why doesn't it?
9. **Problem:** Solve The Skyline Problem. What data structure efficiently tracks the current max height? *(LC 218)*
10. **Conceptual:** When would you choose Rabin-Karp over KMP? What's the trade-off?

## Quick Reference

### Complexity Cheat Sheet

| Algorithm | Time | Space | Key Detail |
|-----------|------|-------|------------|
| Euclidean GCD | O(log min(a,b)) | O(1) | Iterative version avoids stack |
| Sieve of Eratosthenes | O(n log log n) | O(n) | Nearly linear for practical n |
| Fast exponentiation | O(log n) | O(1) | Python's built-in `pow(x, n, mod)` does this |
| Prefix sum + binary search | O(n) build, O(log n) query | O(n) | Weighted random pick |
| Reservoir sampling (k=1) | O(n) single pass | O(1) | No need to know stream length |
| KMP | O(n + m) | O(m) | Failure function is the hard part |
| Rabin-Karp | O(n + m) avg, O(nm) worst | O(1) | Worst case = hash collisions |
| Rotate matrix | O(n²) | O(1) | Transpose + reverse |
| Spiral traversal | O(m·n) | O(1) extra | Boundary shrinking |

### Decision Flowchart

```
Need pattern matching?
├── Single pattern, guaranteed O(n+m)? → KMP
├── Multiple patterns or simplicity? → Rabin-Karp (rolling hash)
└── Short pattern, not performance-critical? → Python's `in` operator

Need random selection?
├── Fixed collection with weights? → Prefix sum + binary search
└── Unknown-length stream? → Reservoir sampling

Matrix manipulation?
├── Rotate 90° CW? → Transpose + reverse rows
├── Rotate 90° CCW? → Reverse rows + transpose (or transpose + reverse columns)
├── Rotate 180°? → Reverse rows, then reverse each row
└── Spiral order? → Boundary shrinking (top/bottom/left/right)

Working with large numbers?
├── "Return answer mod 10⁹+7" → Modular arithmetic throughout
├── Need division under mod? → Fermat's little theorem (modular inverse)
└── Need x^n efficiently? → Binary exponentiation
```
