# Monotonic Stack

> When a problem asks "for each element, find the next greater/smaller element," a monotonic stack solves it in O(n) instead of the brute-force O(n²).

## Core Idea

A **monotonic stack** maintains elements in sorted order (either all increasing or all decreasing from bottom to top). As you iterate through an array, you pop elements that *violate* the monotonic property — and the act of popping is when you discover the answer for those elements. It's like a waiting line where people leave as soon as someone taller (or shorter) shows up behind them.

## What You Need to Know

### Which Direction to Use

| Stack Type | Property (bottom → top) | What It Finds | Pop When |
|------------|------------------------|---------------|----------|
| **Monotonic decreasing** | Values decrease toward top | **Next greater** element | New element is *greater* than top |
| **Monotonic increasing** | Values increase toward top | **Next smaller** element | New element is *smaller* than top |

Why does this work? Because the element that *causes* a pop is exactly the "next greater" (or "next smaller") element for whatever got popped. Every element is pushed and popped at most once, giving O(n) total.

### Store Indices, Not Values

Almost always store **indices** on the stack, not values. You can always look up the value from the index, but you can't recover the index from the value. Indices let you compute distances, widths, and positions.

### The Template

```python
# Next Greater Element (monotonic decreasing stack)
def next_greater(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices; values at these indices are decreasing
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]  # nums[i] is the next greater for nums[idx]
        stack.append(i)
    return result

# Next Smaller Element (monotonic increasing stack)
def next_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices; values at these indices are increasing
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

Time: O(n) — each element pushed and popped at most once
Space: O(n)

### Daily Temperatures (LC 739) — The Gateway Problem

"For each day, how many days until a warmer temperature?" This is literally "find next greater element, return the distance."

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # indices, decreasing by temperature
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev = stack.pop()
            result[prev] = i - prev  # distance, not value
        stack.append(i)
    return result
```

### Next Greater Element I (LC 496)

Two arrays: `nums1` is a subset of `nums2`. For each element in `nums1`, find the next greater element in `nums2`.

Process `nums2` with a monotonic stack, store results in a hash map, then look up `nums1`.

```python
def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(num, -1) for num in nums1]
```

### Largest Rectangle in Histogram (LC 84) — The Boss Fight

For each bar, you need the nearest shorter bar on both sides to determine how far it can extend. A **monotonic increasing** stack (by height) gives you exactly this.

When a shorter bar arrives and you pop a taller bar, the popped bar's rectangle extends from the new stack top to the current index.

```python
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # indices, increasing by height
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx  # this bar can extend back to popped bar's position
        stack.append((start, h))
    # remaining bars extend to the end
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area
```

Time: O(n) | Space: O(n)

### Trapping Rain Water (LC 42) — Monotonic Stack Approach

While there's a two-pointer solution, the stack approach processes bars left-to-right. When you find a bar taller than the stack top, water is trapped between the current bar and the bar below the top.

```python
def trap(height: list[int]) -> int:
    stack = []  # indices, decreasing by height
    water = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            width = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[bottom]
            water += width * bounded_height
        stack.append(i)
    return water
```

Time: O(n) | Space: O(n)

### Next Greater Element II (LC 503) — Circular Array

For circular arrays, iterate through the array *twice* (indices `0` to `2n-1`), using `i % n` to wrap around. Only push indices from the first pass.

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)
    return result
```

## Key Patterns & Templates

### Pattern 1: Next Greater/Smaller Element

```python
def monotonic_stack(nums, find_greater=True):
    """
    find_greater=True  → next greater element (decreasing stack)
    find_greater=False → next smaller element (increasing stack)
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and (nums[stack[-1]] < nums[i] if find_greater else nums[stack[-1]] > nums[i]):
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### Pattern 2: Previous Greater/Smaller (Scan Left-to-Right, Answer at Push Time)

Sometimes you need the *previous* greater/smaller element instead of the *next* one. The stack top at the time you push is the answer.

```python
def previous_smaller(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # increasing stack
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]  # answer for i is current top
        stack.append(i)
    return result
```

### Pattern 3: Histogram Width Calculation

```python
# When popping index `idx` from an increasing stack at position `i`:
# Left boundary  = stack[-1] + 1  (or 0 if stack is empty)
# Right boundary = i - 1
# Width = i - stack[-1] - 1       (or i if stack is empty)
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Daily Temperatures | 739 | Medium | Gateway problem — monotonic decreasing stack of indices, result is distance `i - prev` |
| Next Greater Element I | 496 | Easy | Process with stack, store in hash map, look up subset |
| Next Greater Element II | 503 | Medium | Circular → iterate `2n` times with `i % n` |
| Largest Rectangle in Histogram | 84 | Hard | Increasing stack; popped bar's width spans from new top to current index |
| Trapping Rain Water | 42 | Hard | Decreasing stack; trapped water computed layer by layer between boundaries |
| Maximal Rectangle | 85 | Hard | Each row is a histogram — apply LC 84 on each row's heights |
| Sum of Subarray Minimums | 907 | Medium | Increasing stack; each element's contribution = element × left_count × right_count |
| Online Stock Span | 901 | Medium | Decreasing stack; span = days since last higher price |

## Common Mistakes

- **Confusing increasing vs decreasing**: Remember by what you're finding. Finding *next greater*? You pop smaller elements → stack stays *decreasing*. Finding *next smaller*? You pop larger elements → stack stays *increasing*.
- **Storing values instead of indices**: You almost always need indices for distance/width calculations. Store indices, access values via the array.
- **Off-by-one in histogram width**: When the stack is empty after a pop, the width extends all the way to the left (width = `i`, not `i - 1`). This is the most common bug in LC 84.
- **Forgetting to process remaining stack elements**: After the loop, elements still on the stack never found a next greater/smaller. Either set them to `-1` or process them (like in histogram, where remaining bars extend to the end).
- **Not handling duplicates**: Decide whether your stack is *strictly* monotonic or allows equal values. This matters for problems like Sum of Subarray Minimums (LC 907) to avoid double-counting.

## Interview Questions

1. **Conceptual**: Why is the time complexity O(n) even though there's a while loop inside the for loop?
2. **Conceptual**: When would you use a monotonic *increasing* stack vs a *decreasing* one? Give an example of each.
3. **Problem**: Given daily stock prices, compute the "span" for each day — how many consecutive previous days had a price ≤ today's. (LC 901)
4. **Problem**: Find the largest rectangle in a histogram. Walk through your approach on `[2, 1, 5, 6, 2, 3]`. (LC 84)
5. **Follow-up on LC 84**: How does Maximal Rectangle (LC 85) reduce to the histogram problem?
6. **Problem**: In a circular array, find the next greater element for each position. How do you handle the wrap-around? (LC 503)
7. **Design**: How would you modify the monotonic stack template to find the *previous* greater element instead of the *next* greater?
8. **Problem**: Given an array, find for each element the sum of minimums of all subarrays that include it. (LC 907)

## Quick Reference

```
Monotonic Stack Cheat Sheet
═══════════════════════════

Goal                    Stack Order      Pop Condition
─────────────────────────────────────────────────────
Next greater element    Decreasing ↓     new > top
Next smaller element    Increasing ↑     new < top
Prev greater element    Decreasing ↓     answer = top at push time
Prev smaller element    Increasing ↑     answer = top at push time

Template:
  for i in range(n):
      while stack and CONDITION(nums[stack[-1]], nums[i]):
          popped = stack.pop()
          result[popped] = ...  ← answer for popped element
      stack.append(i)

Complexity: O(n) time, O(n) space
  (each element pushed once, popped once)

Histogram width when popping idx at position i:
  width = i - stack[-1] - 1    (if stack not empty)
  width = i                    (if stack empty)

Circular array trick:
  iterate 0..2n-1, use i % n, only push during first n
```
