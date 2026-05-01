# Trie (Prefix Tree)

> When hash maps fail at prefix queries and you need to search through thousands of words simultaneously, the trie is your weapon of choice.

## Core Idea

A **trie** (pronounced "try") is a tree where each path from root to a node represents a prefix. Unlike hash maps which store complete keys, a trie **distributes the key across the path** — each edge represents one character. This makes prefix operations (autocomplete, spell check, "starts with") blazing fast at O(m) where m is the word length, regardless of how many words are stored. The key insight: **shared prefixes share nodes**, making tries memory-efficient for similar strings.

## What You Need to Know

### Trie vs Hash Set/Map

| Operation | Hash Set | Trie |
|-----------|----------|------|
| Search exact word | O(m) avg | O(m) |
| Search prefix | O(m × n) scan all | **O(m)** ← trie wins |
| Autocomplete | Not possible efficiently | O(m + results) via DFS |
| Longest common prefix | O(n × m) | O(m) single walk |
| Memory | Each word stored separately | Shared prefixes share nodes |

**Use a trie when**: You need prefix matching, autocomplete, or searching multiple patterns simultaneously.

### TrieNode Structure

Two implementation choices:

```python
# Option 1: Dictionary-based (flexible, any alphabet)
class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False

# Option 2: Array-based (faster for lowercase English, fixed 26 slots)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
```

**Dictionary** is preferred in interviews — cleaner code, handles any character set. **Array** is faster for fixed alphabets but wastes memory when sparse.

### Implement Trie (LC 208) — The Foundation

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):                # O(m)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):                # O(m)
        node = self._find_prefix(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):          # O(m)
        return self._find_prefix(prefix) is not None
    
    def _find_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

**Critical detail**: `search` checks `is_end` — the word must have been explicitly inserted. `startsWith` doesn't check `is_end` — any prefix of an inserted word matches. Confusing these is a top interview mistake.

### Add and Search Words with Wildcards (LC 211) — O(26^d) worst case

When you hit a `.` wildcard, branch to **all** children:

```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            char = word[i]
            if char == '.':
                # Wildcard: try ALL children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)
```

### Word Search II (LC 212) — The Hard One

Build a trie from the word list, then DFS from every grid cell while walking the trie simultaneously. The trie prunes dead-end paths.

```python
def find_words(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # store complete word at terminal node
    
    result = []
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return
        
        child = node.children[char]
        if hasattr(child, 'word'):
            result.append(child.word)
            del child.word  # avoid duplicates
        
        board[r][c] = '#'  # mark visited
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, child)
        board[r][c] = char  # restore
        
        # Optimization: prune empty trie branches
        if not child.children:
            del node.children[char]
    
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    
    return result
```

**Why the trie prune?** After finding a word, removing its leaf node prevents re-visiting dead paths. Without this optimization, you get TLE on large inputs.

### Replace Words (LC 648) — O(n × m)

Find the shortest prefix in a dictionary for each word:

```python
def replace_words(dictionary, sentence):
    trie = Trie()
    for root_word in dictionary:
        trie.insert(root_word)
    
    def find_root(word):
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word  # no prefix found
            node = node.children[char]
            if node.is_end:
                return word[:i + 1]  # shortest prefix
        return word
    
    return ' '.join(find_root(w) for w in sentence.split())
```

### Search Suggestions System (LC 1268)

Build trie, then at each prefix, DFS to find lexicographically smallest matches:

```python
def suggested_products(products, search_word):
    root = TrieNode()
    for product in products:
        node = root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def dfs_collect(node, prefix, results):
        if len(results) >= 3:
            return
        if node.is_end:
            results.append(prefix)
        for char in sorted(node.children):  # sorted for lexicographic order
            dfs_collect(node.children[char], prefix + char, results)
    
    result = []
    node = root
    prefix = ""
    for char in search_word:
        prefix += char
        if node and char in node.children:
            node = node.children[char]
            matches = []
            dfs_collect(node, prefix, matches)
            result.append(matches)
        else:
            node = None
            result.append([])
    
    return result
```

## Key Patterns & Templates

### Pattern Recognition

```
When to use a trie:
─────────────────────
✓ "Find all words with prefix X"           → Trie + DFS from prefix node
✓ "Search with wildcards (.)"              → Trie + DFS branching at wildcards
✓ "Find multiple words in a grid"          → Trie + backtracking (prune with trie)
✓ "Replace words with shortest prefix"     → Trie, stop at first is_end
✓ "Autocomplete suggestions"              → Trie + DFS for top-k from prefix
✗ "Find exact word in set"                → Hash set is simpler, same complexity
✗ "Count word frequency"                  → Hash map, no trie needed
```

### Trie + Backtracking Template

For grid/string problems where you search multiple patterns:

```python
def solve_with_trie(patterns, search_space):
    # 1. Build trie from patterns
    root = build_trie(patterns)
    
    # 2. Search the space, walking trie simultaneously
    def backtrack(position, trie_node):
        if trie_node has match:
            record_answer()
        for next_position in neighbors(position):
            char = get_char(next_position)
            if char in trie_node.children:
                mark_visited(next_position)
                backtrack(next_position, trie_node.children[char])
                unmark_visited(next_position)
    
    # 3. Start search from all valid starting points
    for start in all_starts:
        backtrack(start, root)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Implement Trie | 208 | Medium | Foundation — `search` checks `is_end`, `startsWith` doesn't |
| Design Add and Search Words | 211 | Medium | `.` wildcard → DFS all children at that position |
| Word Search II | 212 | Hard | Trie prunes grid DFS; remove found words to avoid TLE |
| Replace Words | 648 | Medium | Walk trie, return at first `is_end` for shortest prefix |
| Search Suggestions System | 1268 | Medium | DFS from prefix node, sorted children for lexicographic order |
| Longest Common Prefix | 14 | Easy | Walk trie until a node has >1 child or is_end |
| Maximum XOR of Two Numbers | 421 | Medium | Bitwise trie — greedily pick opposite bit at each level |

## Common Mistakes

- **Not marking `is_end` properly**: Insert "apple" but `search("app")` returns True because you forgot `is_end` must be `True` at the terminal node of the inserted word, not at every prefix.
- **Word Search II without pruning**: Not removing trie leaves after finding words → revisiting dead branches → TLE. The optimization `if not child.children: del node.children[char]` is essential.
- **Using 26-element arrays for every node when input is sparse**: If words use few distinct characters, dictionary children use less memory. Mention this tradeoff in interviews.
- **Forgetting `is_end` for `search` vs `startsWith`**: `search("app")` is False when only "apple" exists. `startsWith("app")` is True. Mixing these up is the #1 trie bug.
- **Not handling empty string**: Insert empty string? What should `search("")` return? The root node's `is_end` should be True.

## Interview Questions

1. **"Implement a trie with insert, search, and startsWith. What's the time complexity?"** (Amazon/Google)
2. **"Design a word dictionary that supports wildcard search with `.` characters."** (Meta)
3. **"Given a board of characters and a list of words, find all words that can be formed. Optimize for large word lists."** (Google — LC 212)
4. **"What are the tradeoffs between a trie and a hash set for string lookups?"**
5. **"How would you implement autocomplete? What data structure and what's the time complexity per keystroke?"**
6. **"Find the longest common prefix among a list of strings using a trie."**
7. **"How would you find the maximum XOR of two numbers in an array using a trie?"** (Advanced)
8. **"When would you use an array-based trie vs a hash-map-based trie?"**
9. **"How much memory does a trie use compared to a hash set of the same strings?"**
10. **"Your trie-based solution is getting TLE. What optimizations can you apply?"** (Pruning, compressed trie)

## Quick Reference

```
Trie Operations:
─────────────────
Insert:     O(m)  — m = word length
Search:     O(m)  — check is_end at terminal
StartsWith: O(m)  — don't check is_end
Delete:     O(m)  — walk to end, unmark is_end, prune empty branches

Memory:
  Worst case: O(alphabet_size × total_chars)
  Dictionary children: proportional to actual chars used
  Array children (26): fixed per node, faster but wastes space when sparse

Trie vs Hash Set:
  Exact match only?            → Hash set (simpler)
  Prefix queries?              → Trie (unbeatable)
  Wildcard search?             → Trie + DFS
  Multiple pattern search?     → Trie + backtracking

Common Trie Variants:
  Standard trie         → Dict/array children, is_end flag
  Compressed trie       → Merge single-child chains (Patricia/Radix tree)
  Bitwise trie          → Binary trie for XOR problems (0/1 children)
  Suffix trie/tree      → All suffixes of a string (advanced, rarely in interviews)
```
