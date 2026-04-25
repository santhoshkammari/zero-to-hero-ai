# Bit Manipulation

> Half of FAANG "easy" problems are bit tricks — know them cold and you'll solve in 2 minutes what others struggle with for 20.

## Core Idea

Every integer is a sequence of bits. **Bit manipulation** exploits this representation to solve problems in O(1) space and often O(n) or O(log n) time — no extra data structures needed. Think of each bit position as an independent yes/no switch. Most bit tricks work because flipping specific switches (bits) follows predictable algebraic rules, especially with XOR.

## What You Need to Know

### Bitwise Operators

| Operator | Symbol | What It Does | Example (`a=5` → `101`, `b=3` → `011`) |
|----------|--------|-------------|----------------------------------------|
| **AND** | `&` | 1 only if both bits are 1 | `5 & 3` → `001` → `1` |
| **OR** | `\|` | 1 if either bit is 1 | `5 \| 3` → `111` → `7` |
| **XOR** | `^` | 1 if bits differ | `5 ^ 3` → `110` → `6` |
| **NOT** | `~` | Flip all bits | `~5` → `...11111010` → `-6` in Python (two's complement, infinite precision) |
| **Left Shift** | `<<` | Shift bits left, fill with 0s | `5 << 1` → `1010` → `10` (multiply by 2) |
| **Right Shift** | `>>` | Shift bits right | `5 >> 1` → `10` → `2` (floor divide by 2) |

**Why does `~5 = -6`?** Python integers have arbitrary precision and use two's complement. `~n` is always `-(n+1)`. This matters — you'll need a **32-bit mask** (`0xFFFFFFFF`) when problems expect fixed-width integers.

### Essential Bit Tricks

| Trick | Code | Why It Works | Use Case |
|-------|------|-------------|----------|
| Clear lowest set bit | `n & (n - 1)` | `n-1` flips all bits from the lowest set bit rightward. AND zeros out that bit and everything below it. | Counting set bits, power-of-2 check |
| Isolate lowest set bit | `n & (-n)` | `-n` is `~n + 1` in two's complement. Only the lowest set bit survives the AND. | Fenwick Tree (Binary Indexed Tree) |
| XOR cancellation | `n ^ n = 0` | XOR with itself always cancels. `n ^ 0 = n` preserves. | Finding unique elements |
| Check kth bit | `(n >> k) & 1` | Shift the kth bit to position 0, then mask. | Bit-level inspection |
| Set kth bit | `n \| (1 << k)` | OR with a 1 at position k forces that bit on. | Building bitmasks |
| Clear kth bit | `n & ~(1 << k)` | AND with a 0 at position k forces that bit off. | Clearing flags |
| Toggle kth bit | `n ^ (1 << k)` | XOR flips the target bit, leaves others unchanged. | Toggling states |
| Check power of 2 | `n > 0 and (n & (n - 1)) == 0` | Powers of 2 have exactly one set bit. Clearing it gives 0. | Validation |
| Get all 1s mask (k bits) | `(1 << k) - 1` | `1 << k` is `100...0` (k zeros). Subtract 1 → `011...1` (k ones). | Masking to k bits |
| Swap without temp | `a ^= b; b ^= a; a ^= b` | XOR is its own inverse. Three rounds fully swap. | Interview parlor trick |

### XOR — The Star of Bit Problems

**XOR properties** you must internalize:
- **Self-inverse**: `a ^ a = 0`
- **Identity**: `a ^ 0 = a`
- **Commutative & associative**: order doesn't matter — `a ^ b ^ c = c ^ a ^ b`
- **No overflow**: unlike addition, XOR never overflows — preferred for "missing number" problems

### Brian Kernighan's Algorithm — Counting Set Bits

The insight: `n & (n - 1)` drops exactly one set bit per iteration. So loop until `n = 0` and count iterations.

```python
def count_bits(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # drop lowest set bit
        count += 1
    return count
# Time: O(k) where k = number of set bits — faster than O(32) bit-by-bit
```

### Python-Specific Gotcha: Negative Numbers & 32-Bit Masking

Python integers are arbitrary-precision — there's no natural 32-bit boundary. When a problem says "32-bit integer," you must mask explicitly:

```python
MASK = 0xFFFFFFFF  # 32 ones
MAX_INT = 0x7FFFFFFF  # max positive 32-bit signed int

def to_32bit(n: int) -> int:
    """Convert Python int to 32-bit signed representation."""
    n &= MASK
    # If the sign bit (bit 31) is set, it's negative in 32-bit world
    return n if n <= MAX_INT else n - (MASK + 1)
```

## Key Patterns & Templates

### Pattern 1: Single Number (XOR All)

When every element appears twice except one — XOR everything. Pairs cancel to 0, leaving the unique one.

```python
def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result
# Time: O(n), Space: O(1)
```

### Pattern 2: Missing Number (XOR with Indices)

XOR all values with all indices `0..n`. Each index-value pair cancels except the missing one.

```python
def missing_number(nums: list[int]) -> int:
    xor = len(nums)  # start with n (index n has no pair)
    for i, num in enumerate(nums):
        xor ^= i ^ num
    return xor
# Time: O(n), Space: O(1) — no overflow risk unlike sum approach
```

### Pattern 3: Single Number III (Two Unique Numbers)

XOR all → gives `a ^ b`. Find any differing bit (use lowest set bit), split numbers into two groups. Each group contains exactly one unique number.

```python
def single_number_iii(nums: list[int]) -> list[int]:
    xor_all = 0
    for n in nums:
        xor_all ^= n

    # Isolate lowest set bit — this bit differs between a and b
    diff_bit = xor_all & (-xor_all)

    a = 0
    for n in nums:
        if n & diff_bit:
            a ^= n  # group where this bit is set
    b = xor_all ^ a  # the other unique number
    return [a, b]
# Time: O(n), Space: O(1)
```

### Pattern 4: Count Bits for Every Number 0..n (DP + Bits)

```python
def counting_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
        # i >> 1 removes last bit; (i & 1) checks if last bit was 1
    return dp
# Time: O(n), Space: O(n)
```

### Pattern 5: Reverse Bits

```python
def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)  # shift result left, append last bit of n
        n >>= 1
    return result
# Time: O(32) = O(1), Space: O(1)
```

### Pattern 6: Sum Without + Operator

XOR gives the sum ignoring carries. AND then left-shift gives the carries. Repeat until no carries remain — this is literally how a **hardware adder** works.

```python
def get_sum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    while b & MASK:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    # If b is 0, a is the answer. Handle negative results in 32-bit.
    return a & MASK if b > 0 else a
# Time: O(32) worst case = O(1), Space: O(1)
```

### Pattern 7: Enumerate All Subsets via Bitmask

Each number from `0` to `2^n - 1` represents a subset. Bit `i` being set means "include element i."

```python
def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    return result
# Time: O(n * 2^n), Space: O(n * 2^n) for output
```

**Iterate submasks of a given mask** (useful in bitmask DP):

```python
def iterate_submasks(mask: int):
    sub = mask
    while sub:
        # process sub
        sub = (sub - 1) & mask  # next smaller submask
    # don't forget to process sub = 0 (empty set) if needed
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Single Number | 136 | Easy | XOR everything — pairs cancel, unique survives |
| Single Number II | 137 | Medium | Count each bit position mod 3; surviving bits form the answer |
| Single Number III | 260 | Medium | XOR all → split by lowest differing bit → two independent XOR groups |
| Missing Number | 268 | Easy | XOR indices with values; prefer over sum to avoid overflow |
| Number of 1 Bits | 191 | Easy | Brian Kernighan: `n &= n - 1` loop, count iterations |
| Counting Bits | 338 | Easy | DP: `dp[i] = dp[i >> 1] + (i & 1)` — right-shift reuses previous work |
| Reverse Bits | 190 | Easy | Build result bit-by-bit: shift left, OR with last bit of input |
| Sum of Two Integers | 371 | Medium | XOR = sum without carry, `(a & b) << 1` = carry; loop until no carry |
| Subsets | 78 | Medium | Bitmask `0` to `2^n - 1`; bit `i` set → include `nums[i]` |

## Common Mistakes

- **Ignoring Python's infinite-precision integers.** There's no natural 32-bit wraparound. When problems say "32-bit integer," you must `& 0xFFFFFFFF` to simulate overflow and handle the sign bit manually.
- **Confusing bitwise with logical operators.** `&` is bitwise AND (operates on bits), `and` is logical AND (short-circuit boolean). `3 & 1 = 1`, but `3 and 1 = 1` for totally different reasons. Same for `|` vs `or`.
- **Forgetting XOR is commutative + associative.** Order doesn't matter. If your solution depends on processing order, you're overcomplicating it.
- **Bitmask DP with n > 20.** `2^20` ≈ 1 million states is borderline. `2^25` is ~33 million — likely TLE. If `n > 20`, reconsider whether bitmask DP is the right approach.
- **Off-by-one with bit positions.** Bits are 0-indexed from the right. The "1st bit" in a problem might mean index 0 or index 1 — always clarify.

## Interview Questions

1. **How would you determine if a number is a power of 2 in O(1)?** (Use `n > 0 and (n & (n-1)) == 0`)
2. **Given an array where every element appears twice except one, find the unique element in O(n) time and O(1) space.** (LC 136 — XOR all)
3. **Same as above, but two elements are unique.** How do you separate them? (LC 260 — XOR all, split by differing bit)
4. **What if every element appears three times except one?** (LC 137 — count bits mod 3)
5. **Find the missing number in `[0, 1, ..., n]` with one missing, without using extra space.** Why prefer XOR over sum? (LC 268 — no overflow)
6. **Add two integers without using `+` or `-`.** Walk through the carry logic. (LC 371)
7. **How does Brian Kernighan's algorithm work, and why is it faster than checking all 32 bits?** (It skips zero bits — O(k) where k = set bits)
8. **Reverse the bits of a 32-bit unsigned integer.** (LC 190)
9. **Generate all subsets of a set using bit manipulation.** What's the time complexity? (LC 78 — O(n × 2^n))
10. **In Python, what does `~5` evaluate to, and why?** (−6, because Python uses arbitrary-precision two's complement: `~n = -(n+1)`)

## Quick Reference

### Bit Tricks Cheat Sheet

| Operation | Code | Time |
|-----------|------|------|
| Check if even | `n & 1 == 0` | O(1) |
| Check if odd | `n & 1 == 1` | O(1) |
| Multiply by 2^k | `n << k` | O(1) |
| Divide by 2^k (floor) | `n >> k` | O(1) |
| Check kth bit set | `(n >> k) & 1` | O(1) |
| Set kth bit | `n \| (1 << k)` | O(1) |
| Clear kth bit | `n & ~(1 << k)` | O(1) |
| Toggle kth bit | `n ^ (1 << k)` | O(1) |
| Clear lowest set bit | `n & (n - 1)` | O(1) |
| Isolate lowest set bit | `n & (-n)` | O(1) |
| Check power of 2 | `n > 0 and n & (n-1) == 0` | O(1) |
| Count set bits | Brian Kernighan loop | O(k) |
| Mask to k bits | `n & ((1 << k) - 1)` | O(1) |
| All subsets of n items | `for mask in range(1 << n)` | O(2^n) |
| Submasks of mask | `sub = (sub-1) & mask` loop | O(2^k) |
| Two's complement negate | `~n + 1` or `-n` | O(1) |

### Complexity at a Glance

| Problem Pattern | Time | Space |
|----------------|------|-------|
| XOR scan (single number, missing number) | O(n) | O(1) |
| Brian Kernighan (count bits) | O(k), k = set bits | O(1) |
| Counting bits 0..n (DP) | O(n) | O(n) |
| Reverse bits | O(32) = O(1) | O(1) |
| Enumerate all subsets | O(n × 2^n) | O(2^n) |
| Bitmask DP | O(2^n × f(n)) | O(2^n) |

### Decision Flowchart

```
"Find unique / missing element"
  → Can elements cancel in pairs? → XOR scan
  → Elements repeat k times?     → Count bits mod k

"Check property of a number"
  → Power of 2?        → n & (n-1) == 0
  → Count set bits?    → Brian Kernighan
  → Specific bit set?  → (n >> k) & 1

"Generate combinations / subsets"
  → n ≤ 20?  → Bitmask enumeration
  → n > 20?  → Backtracking instead

"Arithmetic without operators"
  → XOR = sum without carry
  → (a & b) << 1 = carry
  → Loop until carry = 0
```
