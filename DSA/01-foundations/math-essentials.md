# Math Essentials for Interviews

> You won't be asked to prove theorems, but modular arithmetic, GCD, and bit tricks show up more than you'd expect.

## Core Idea

A handful of math tools unlock dozens of interview problems: modular arithmetic for large numbers, GCD/LCM for number theory, prime sieves for optimization, and combinatorics for counting problems. Python handles big integers natively, but these patterns appear in DP state transitions, string problems, and bit manipulation.

## What You Need to Know

### Modular Arithmetic

Properties that let you take mod at each step (preventing overflow in other languages, required by many LC problems):

```python
MOD = 10**9 + 7

# Additive: (a + b) % m = ((a % m) + (b % m)) % m
# Multiplicative: (a * b) % m = ((a % m) * (b % m)) % m
# Subtraction: (a - b) % m = ((a % m) - (b % m) + m) % m  (add m to avoid negative)
# Division: NOT (a/b) % m — use modular inverse instead

# Example: count paths in DP grid mod 10^9+7
def count_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    return dp[m-1][n-1]
```

**Why 10^9 + 7?** It's prime (needed for modular inverse), large enough to avoid collisions, and fits in 32-bit when squared (barely — actually needs 64-bit for intermediate `a*b`).

### GCD / LCM

```python
import math

# Built-in (Python 3.5+)
math.gcd(12, 8)  # 4
math.lcm(12, 8)  # 24 (Python 3.9+)

# Manual Euclidean algorithm — O(log min(a, b))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM from GCD
def lcm(a, b):
    return a * b // gcd(a, b)

# Extended Euclidean: find x, y such that ax + by = gcd(a, b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
```

**Key facts:**
- `gcd(0, n) = n` (not 0!)
- `gcd(a, b) = gcd(b, a % b)` — each step reduces by at least half → O(log min(a,b))
- GCD of strings: `gcd("ABCABC", "ABC") = "ABC"` — check if `s1 + s2 == s2 + s1` first

### Primes

```python
# Trial division — O(√n)
def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # all primes > 3 are of form 6k ± 1
    return True

# Sieve of Eratosthenes — O(n log log n)
def sieve(n):
    """Return list of all primes <= n."""
    if n < 2: return []
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_p[p]:
            # Start from p² — smaller multiples already marked
            for mult in range(p * p, n + 1, p):
                is_p[mult] = False
    return [i for i, v in enumerate(is_p) if v]
```

**Why start from p²?** All multiples of p less than p² have a smaller prime factor and were already marked. E.g., for p=5: 10=2×5 (marked by 2), 15=3×5 (marked by 3), 20=4×5 (marked by 2). Start at 25.

### Fast Exponentiation

```python
# Recursive — O(log n) time, O(log n) space
def fast_pow(x, n):
    if n == 0: return 1
    if n < 0: return 1 / fast_pow(x, -n)
    half = fast_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x

# Iterative — O(log n) time, O(1) space
def fast_pow_iter(x, n):
    if n < 0:
        x, n = 1 / x, -n
    result = 1
    while n > 0:
        if n & 1:  # n is odd
            result *= x
        x *= x
        n >>= 1
    return result

# Modular exponentiation — for large number problems
def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        exp >>= 1
        base = base * base % mod
    return result
# Python built-in: pow(base, exp, mod) does this!
```

### Combinatorics

```python
# nCr — basic (fine for small values)
from math import comb  # Python 3.8+
comb(10, 3)  # 120

# Pascal's triangle — precompute for multiple queries
def build_pascal(n):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C
# C[n][r] gives nCr in O(1) after O(n²) precomputation

# nCr mod p — using Fermat's little theorem (p must be prime)
# a^(-1) mod p = a^(p-2) mod p
MOD = 10**9 + 7

def precompute_factorials(n, mod=MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % mod
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], mod - 2, mod)  # Fermat's little theorem
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def ncr_mod(n, r, fact, inv_fact, mod=MOD):
    if r < 0 or r > n: return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod
```

### Power of 2 Tricks

```python
# Check if n is power of 2 — O(1)
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
# Why: power of 2 = single bit set. n-1 flips all lower bits.
# 8 = 1000, 7 = 0111, 8 & 7 = 0000 → True

# Count number of times n can be halved (floor of log2)
n.bit_length() - 1  # equivalent to floor(log2(n)) for n > 0

# Next power of 2 >= n
def next_power_of_2(n):
    return 1 << (n - 1).bit_length()
```

### Integer Overflow

Python handles arbitrary precision integers natively — no overflow. But:
- Java/C++: `int` overflows at 2^31. Use `long` or take mod.
- In DP problems, when answer says "return result mod 10^9 + 7", take mod at **every** addition/multiplication step.
- Intermediate products can overflow even with mod: compute `(a * b) % m` carefully in other languages.

## Key Patterns & Templates

### 1. GCD — Euclidean Algorithm

```python
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# For multiple numbers
from functools import reduce
def gcd_of_list(nums):
    return reduce(math.gcd, nums)
```

### 2. Sieve of Eratosthenes

```python
def sieve(n):
    if n < 2: return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p::p] = [False] * len(is_prime[p*p::p])
    return [i for i, v in enumerate(is_prime) if v]
```

### 3. Fast Power (Modular Exponentiation)

```python
def mod_pow(base, exp, mod):
    """Compute base^exp % mod in O(log exp)."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        exp >>= 1
        base = base * base % mod
    return result

# Or just use: pow(base, exp, mod)
```

### 4. nCr with Modular Inverse

```python
MOD = 10**9 + 7

def setup(n):
    """Precompute factorials and inverse factorials up to n."""
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    return fact, inv

def ncr(n, r, fact, inv):
    if r < 0 or r > n: return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD

# Usage:
# fact, inv = setup(10**5)
# print(ncr(10, 3, fact, inv))  # 120
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Count Primes | 204 | Medium | Sieve of Eratosthenes; start marking from p², only odd numbers |
| Pow(x, n) | 50 | Medium | Recursive squaring; handle n < 0 as `1/pow(x, -n)`, edge case n = -2^31 |
| Greatest Common Divisor of Strings | 1071 | Easy | GCD of lengths; check if `str1 + str2 == str2 + str1` first |
| Plus One | 66 | Easy | Handle carry propagation; edge case: all 9s → prepend 1 |
| Excel Sheet Column Number | 171 | Easy | Base-26 conversion; `result = result * 26 + (ord(c) - ord('A') + 1)` |

## Common Mistakes

- **Off-by-one in sieve** — `range(2, int(n**0.5) + 1)` needs the `+1`. Forgetting it misses perfect squares.
- **Overflow in intermediate calculations** — take mod at **each** step: `(a * b) % mod`, not `(a * b) % mod` after a*b overflows (matters in Java/C++, not Python).
- **Negative exponent edge case** — `pow(x, n)` when `n = -2^31`: negating gives 2^31 which overflows 32-bit int. Handle by converting to float division: `1.0 / pow(x, -(n+1)) / x`.
- **Floating point for combinatorics** — `factorial(20)` = 2.4×10^18, fine as int, but `20! / (10! * 10!)` as floats loses precision. Always use integer arithmetic or `math.comb()`.
- **GCD with zero** — `gcd(0, n) = n`, not 0. `gcd(0, 0)` is undefined (or 0 by convention).

## Interview Questions

- **"Implement Pow(x, n) — what's the time complexity? Handle edge cases."** — O(log n) via repeated squaring. Edge cases: n=0 → 1, n<0 → 1/pow(x,-n), x=0 and n<0 → undefined, n=-2^31 overflow.
- **"How does the Sieve of Eratosthenes work? Why start from p²?"** — Mark all multiples of each prime. Start from p² because smaller multiples (2p, 3p, ..., (p-1)p) have smaller prime factors and are already marked.
- **"What's the time complexity of Euclidean GCD and why?"** — O(log min(a,b)). Each step, the remainder is at most half the divisor (by the division algorithm), so the numbers shrink exponentially.
- **"How would you compute nCr for large numbers without overflow?"** — Use modular arithmetic: precompute factorials and inverse factorials mod p (prime). Inverse via Fermat's little theorem: `a^(-1) ≡ a^(p-2) mod p`.
- **"Why do we use 10^9 + 7 as the modulus?"** — It's prime (needed for modular inverse via Fermat's little theorem), large enough that `(mod-1)^2` fits in a 64-bit integer, and a standard convention in competitive programming.
- **"Check if a number is a power of 2 in O(1)."** — `n > 0 and (n & (n-1)) == 0`. A power of 2 has exactly one set bit; `n-1` flips all bits below it; AND gives 0.

## Quick Reference

| Operation | Algorithm | Time Complexity |
|---|---|---|
| GCD | Euclidean | O(log min(a,b)) |
| Primality test | Trial division | O(√n) |
| Find all primes ≤ n | Sieve of Eratosthenes | O(n log log n) |
| x^n | Fast exponentiation | O(log n) |
| nCr | Pascal's triangle (precompute) | O(n²) build, O(1) query |
| nCr mod p | Fermat's little theorem | O(n) precompute factorials |
| Is power of 2? | Bit trick: n & (n-1) | O(1) |
| Integer factorization | Trial division | O(√n) |
| Modular inverse | Fermat's little theorem | O(log p) |

**Useful Python built-ins:**
```python
import math
math.gcd(a, b)           # GCD
math.lcm(a, b)           # LCM (3.9+)
math.comb(n, r)           # nCr (3.8+)
math.isqrt(n)             # integer sqrt (3.8+)
pow(base, exp, mod)       # modular exponentiation (built-in, not math.pow)
n.bit_length()            # number of bits needed
bin(n).count('1')         # popcount
```
