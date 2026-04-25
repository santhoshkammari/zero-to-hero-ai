# Stack Fundamentals

> Stacks are the go-to structure for anything with nesting or matching — parentheses, function calls, undo systems, and expression evaluation.

## Core Idea

A **stack** is a Last-In-First-Out (LIFO) container: the most recent item added is the first one removed. Think of it like a stack of plates — you always grab from the top. This makes stacks perfect for tracking *nested* or *recursive* structures because the most recently opened context is always the one you need to close first.

## What You Need to Know

### Stack Operations

| Operation | What It Does | Time | Space |
|-----------|-------------|------|-------|
| `push(x)` | Add `x` to the top | O(1) | O(1) |
| `pop()` | Remove and return top element | O(1) | O(1) |
| `peek()` / `top()` | View top element without removing | O(1) | O(1) |
| `is_empty()` | Check if stack has no elements | O(1) | O(1) |

In Python, just use a `list` — `append()` is push, `pop()` is pop, `[-1]` is peek. No need for a special class.

### Where Stacks Show Up

- **Matching nested structures**: parentheses, HTML tags, nested function calls
- **Expression evaluation**: converting and evaluating mathematical expressions
- **DFS traversal**: explicit stack replaces recursion's call stack
- **Undo/redo**: each action pushed; undo = pop
- **Backtracking**: try a path, pop when it fails

### The Core Pattern: Stacks Are for Matching Nested Structures

Every time you see a problem involving *pairs* that can nest inside each other, reach for a stack. The opening element goes on the stack; when you hit a closing element, pop and check if it matches.

### Parentheses Problems

**Valid Parentheses (LC 20)** — The classic stack warm-up.

The insight: push opening brackets, and on every closing bracket, the stack top *must* be the matching opener. If it's not (or the stack is empty), it's invalid.

```python
def is_valid(s: str) -> bool:
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack  # must be empty — all openers matched
```

**Minimum Remove to Make Valid Parentheses (LC 1249)** — Track *indices* of unmatched parens, then rebuild the string without them.

```python
def min_remove_to_make_valid(s: str) -> str:
    stack = []  # indices of unmatched '('
    remove = set()
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)  # unmatched ')'
    remove.update(stack)  # remaining unmatched '('
    return ''.join(ch for i, ch in enumerate(s) if i not in remove)
```

Time: O(n) | Space: O(n)

**Longest Valid Parentheses (LC 32)** — Stack stores *indices*. Push index of last unmatched position as a boundary marker.

```python
def longest_valid_parentheses(s: str) -> int:
    stack = [-1]  # boundary marker
    max_len = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # new boundary
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

Time: O(n) | Space: O(n)

### Expression Evaluation

**Evaluate Reverse Polish Notation (LC 150)** — Numbers go on the stack. When you hit an operator, pop two operands, compute, push the result back.

Critical detail: the *second* popped value is the left operand. `[3, 4, -]` means `3 - 4`, not `4 - 3`.

```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),  # truncate toward zero
    }
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()  # b is right, a is left
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]
```

Time: O(n) | Space: O(n)

**Basic Calculator II (LC 227)** — Handle `+`, `-`, `*`, `/` with correct precedence using a stack.

The trick: delay all additions/subtractions by pushing to the stack. Execute `*` and `/` immediately because they bind tighter.

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    op = '+'  # previous operator
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))
            op = ch
            num = 0
    return sum(stack)
```

Time: O(n) | Space: O(n)

**Basic Calculator (LC 224)** — Handles `+`, `-`, parentheses, and unary minus. Use the stack to save/restore state when entering/leaving parentheses.

```python
def calculate(s: str) -> int:
    stack = []
    result = 0
    num = 0
    sign = 1
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            result += sign * num
            num = 0
            sign = 1
        elif ch == '-':
            result += sign * num
            num = 0
            sign = -1
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # sign before paren
            result += stack.pop()  # result before paren
    result += sign * num
    return result
```

Time: O(n) | Space: O(n)

### Infix to Postfix (Shunting-Yard Algorithm)

This is the algorithm behind how calculators handle precedence. Operators sit on a stack ordered by precedence; higher-precedence operators get output first.

```python
def infix_to_postfix(tokens: list[str]) -> list[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    ops = []
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()  # discard '('
        else:
            while ops and ops[-1] != '(' and precedence.get(ops[-1], 0) >= precedence[token]:
                output.append(ops.pop())
            ops.append(token)
    while ops:
        output.append(ops.pop())
    return output
```

## Key Patterns & Templates

### Pattern 1: Bracket Matching Template

```python
def bracket_match(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```

### Pattern 2: Expression Evaluation Template

```python
def evaluate_with_precedence(s: str) -> int:
    """Handles +, -, *, / with correct precedence."""
    stack = []
    num, op = 0, '+'
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1:
            if op == '+':   stack.append(num)
            elif op == '-': stack.append(-num)
            elif op == '*': stack.append(stack.pop() * num)
            elif op == '/': stack.append(int(stack.pop() / num))
            op, num = ch, 0
    return sum(stack)
```

### Pattern 3: Stack-Based DFS (Iterative)

```python
def iterative_dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()       # process when POPPING
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Valid Parentheses | 20 | Easy | Push openers, pop on closers — stack enforces nesting order |
| Evaluate Reverse Polish Notation | 150 | Medium | Second popped = left operand; `int(a/b)` truncates toward zero |
| Basic Calculator II | 227 | Medium | Delay `+`/`-` on stack, execute `*`/`/` immediately for precedence |
| Basic Calculator | 224 | Hard | Stack saves (result, sign) before `(`; restore on `)` |
| Longest Valid Parentheses | 32 | Hard | Stack of indices with boundary marker at `-1` |
| Minimum Remove to Make Valid Parentheses | 1249 | Medium | Track indices of unmatched parens in stack + set |
| Decode String | 394 | Medium | Stack of (current_string, repeat_count) for nested `k[encoded]` |
| Remove All Adjacent Duplicates in String II | 1209 | Medium | Stack of (char, count) — pop when count hits `k` |

## Common Mistakes

- **Processing on push instead of pop in DFS**: In stack-based DFS, process the node when you *pop* it, not when you push. Pushing just means "visit later." Processing on push gives wrong traversal order.
- **Not checking for empty stack before `pop()` or `[-1]`**: Always guard with `if stack:` or `len(stack) > 0`. An empty stack pop in an interview = instant red flag.
- **Forgetting unary minus in calculator problems**: The `-` in `(-3 + 2)` isn't subtraction — it's negation. Handle it by tracking whether `-` appears after `(` or at the start.
- **Wrong operand order in RPN**: `a b -` means `a - b`, so after popping `b` then `a`, compute `a - b`, not `b - a`.
- **Using `//` instead of `int(a/b)` for division**: Python's `//` floors toward negative infinity (`-7 // 2 = -4`), but most problems want truncation toward zero (`int(-7/2) = -3`).

## Interview Questions

1. **Conceptual**: Why is a stack the right data structure for matching parentheses? Could you use a queue instead?
2. **Conceptual**: Explain how the call stack in recursion relates to an explicit stack in iterative DFS.
3. **Problem**: Given a string of parentheses, find the minimum number of additions (not removals) to make it valid.
4. **Problem**: Evaluate the expression `"3 + 2 * (4 - 1)"` — walk through how you'd use two stacks (operands + operators).
5. **Problem**: How would you extend Basic Calculator II to handle parentheses? What changes?
6. **Design**: How would you implement an undo/redo system using stacks?
7. **Follow-up**: Can you solve Valid Parentheses without a stack? What's the trade-off?
8. **Problem**: How would you handle multiple types of brackets that can nest in any order, like `[{()}]`?
9. **Conceptual**: What's the time complexity of checking if a string of `n` characters has valid parentheses? Can you do better than O(n)?

## Quick Reference

```
Stack = LIFO → push/pop/peek all O(1)

Python: use list
  push  → append(x)
  pop   → pop()
  peek  → [-1]
  empty → not stack

When to use a stack:
  ├─ Matching nested structures (parens, tags)
  ├─ Expression evaluation (RPN, infix→postfix)
  ├─ DFS (iterative)
  ├─ Undo/redo
  └─ Backtracking

Calculator precedence trick:
  + and - → push to stack (delay)
  * and / → execute immediately (higher precedence)
  ( and ) → save/restore state on stack

Parentheses checklist:
  ✓ Push index or char for openers
  ✓ Pop and match for closers
  ✓ After loop: stack must be empty for valid
```
