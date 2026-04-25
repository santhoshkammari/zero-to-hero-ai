# String Manipulation

> Strings are immutable in Python — every concatenation creates a new string. Understanding this changes how you approach problems.

## Core Idea

Strings in Python are immutable sequences of characters. Any "modification" creates a new string, making naive concatenation in a loop O(n²). Use lists for building strings, join at the end. Many string problems reduce to frequency counting, two-pointer techniques, or sliding windows.

## What You Need to Know

**Immutability**: `s[0] = 'x'` raises `TypeError`. Convert to list for mutations, then rejoin:

```python
chars = list(s)
chars[0] = 'x'
s = ''.join(chars)
```

**Building strings efficiently**: `''.join(parts)` is O(n) total. The naive `s += char` loop copies the entire string on every iteration → O(n²).

**Character frequency**: use `Counter` for convenience or a size-26 array for speed with lowercase-only constraints:

```python
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1
```

Frequency arrays avoid hash overhead — measurably faster on large inputs.

**Anagram detection**: two strings are anagrams iff they have identical character frequencies. `Counter(s) == Counter(t)` works but `sorted(s) == sorted(t)` is O(n log n) vs O(n).

**Palindrome checking**: two pointers from both ends moving inward. For "valid palindrome" problems, skip non-alphanumeric chars with `isalnum()`.

**String comparison and ordering**: Python compares strings lexicographically. `ord('a')` = 97, `chr(97)` = 'a'. Useful for character arithmetic: `ord(c) - ord('a')` gives 0–25 index.

**Common Python string methods**: `split()`, `join()`, `strip()`, `find()` (returns -1 if not found), `replace()`, `isalpha()`, `isdigit()`, `lower()`, `startswith()`, `endswith()`.

**Encoding/decoding**: length-prefix encoding handles arbitrary characters. Format: `"len#string"` — e.g., `"4#word3#cat"`. Can't use a simple delimiter because the strings themselves may contain it.

## Key Patterns & Templates

### 1. Build String Efficiently with List + Join

```python
def build_string(parts: list[str]) -> str:
    result = []
    for p in parts:
        result.append(p.upper())  # any transformation
    return ''.join(result)
```

### 2. Frequency Count — Counter vs Array

```python
from collections import Counter

# Counter approach
def freq_counter(s: str) -> dict:
    return Counter(s)

# Array approach (lowercase only — faster)
def freq_array(s: str) -> list[int]:
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    return freq
```

### 3. Check Palindrome (Two Pointers)

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### 4. Check Anagram

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = [0] * 26
    for a, b in zip(s, t):
        freq[ord(a) - ord('a')] += 1
        freq[ord(b) - ord('a')] -= 1
    return all(f == 0 for f in freq)
```

### 5. Encode/Decode Strings (Length-Prefix)

```python
def encode(strs: list[str]) -> str:
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s: str) -> list[str]:
    result, i = [], 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        result.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return result
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Valid Anagram | 242 | Easy | Frequency count with single array: increment for `s`, decrement for `t` |
| Valid Palindrome | 125 | Easy | Two pointers, skip non-alphanumeric, compare lowercase |
| Group Anagrams | 49 | Medium | Use `tuple(sorted(word))` or `tuple(freq_count)` as hash key |
| Longest Common Prefix | 14 | Easy | Compare char by char across all strings; stop at first mismatch |
| String to Integer (atoi) | 8 | Medium | Handle whitespace, sign, overflow, non-digit characters in order |
| Encode and Decode Strings | 271 | Medium | Length-prefix: `"4#word"` — can't use simple delimiter because strings may contain it |

## Common Mistakes

- **String concatenation in loop** — `s += char` is O(n²) total. Use `parts = []; parts.append(char); ''.join(parts)`
- **Not handling edge cases** — empty strings, single characters, all-whitespace input
- **Case sensitivity** — forgetting to normalize with `.lower()` before comparison
- **atoi overflow** — clamp to `[-2^31, 2^31 - 1]` before returning
- **Anagram: using sorted** — O(n log n) when frequency count gives O(n)
- **Rotation check** — `s2` is a rotation of `s1` iff `len(s1) == len(s2)` and `s2 in s1 + s1`

## Interview Questions

- "Why is string concatenation in a loop O(n²) in Python?"
- "Design an encode/decode scheme for a list of strings that handles any character."
- "Group anagrams — what's the best choice for hash key and why?"
- "Check if a string is a palindrome, ignoring non-alphanumeric characters."
- "What's the difference between using `Counter` vs a size-26 array for frequency counting?"
- "How would you implement atoi handling all edge cases?"
- "Given two strings, check if one is a rotation of the other." (hint: `s2 in s1 + s1`)

## Quick Reference

| Task | Approach | Time |
|---|---|---|
| Build string | list + `''.join()` | O(n) |
| Check anagram | Frequency array / Counter | O(n) |
| Check palindrome | Two pointers | O(n) |
| Find substring | `str.find()` or KMP | O(n·m) / O(n+m) |
| Group by equivalence | Custom hash key + dict | O(n·k) |
