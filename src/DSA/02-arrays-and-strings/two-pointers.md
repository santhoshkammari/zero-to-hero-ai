# Two Pointers

> Two pointers transform O(n²) brute force into O(n) elegance. The most versatile pattern for array/string problems.

## Core Idea

Place two pointers at strategic positions (both ends, same start, or different arrays) and move them based on conditions. This eliminates the need for nested loops by using structure (usually sorted order) to skip unnecessary comparisons.

## What You Need to Know

**Opposite-direction pointers**: start from both ends, move inward. Works when the array is sorted or the structure is symmetric (palindromes). Move the pointer that can improve the answer.

**Same-direction pointers (fast/slow)**: both start at the beginning. Fast pointer explores, slow pointer marks the "valid" position. Used for removing duplicates, partitioning, moving zeros. The slow pointer always lags behind or equals the fast pointer.

**Three pointers**: extension for 3Sum. Sort the array, fix one element with an outer loop, run two-pointer on the remainder. The hard part is **duplicate skipping** — skip at all levels.

**When two pointers work**: array is sorted (or you can sort it without affecting the answer), or you're comparing from both ends of a symmetric structure.

**When two pointers DON'T work**: subarray sum problems with negative numbers — sorted order doesn't help because adding an element can decrease the sum. Use prefix sum + hash map instead.

| Variant | Start Positions | Movement Rule | Typical Use |
|---|---|---|---|
| Opposite direction | `left=0`, `right=n-1` | Move based on sum/comparison | Sorted pair search, palindrome, container |
| Same direction (fast/slow) | Both at `0` | Fast scans, slow marks valid | Remove duplicates, partition, move zeros |
| Three pointers | Fix one, two-point rest | Outer loop + inner two-pointer | 3Sum, 3Sum Closest |

## Key Patterns & Templates

### 1. Two Sum on Sorted Array (Opposite Direction)

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Container With Most Water (Opposite Direction, Greedy Shrink)

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        best = max(best, w * h)
        # move the shorter side — it's the bottleneck
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

### 3. Remove Duplicates from Sorted Array (Same Direction)

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### 4. 3Sum (Fix One + Two Pointer)

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate for first element
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # skip duplicates for second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result
```

### 5. Move Zeros (Same Direction, Partition)

```python
def move_zeroes(nums: list[int]) -> None:
    slow = 0  # insertion point for non-zeros
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

## Must-Do Problems

| Problem | LC# | Difficulty | Key Insight |
|---------|-----|-----------|-------------|
| Two Sum II (Sorted) | 167 | Medium | Left + right pointers: sum too big → move right left, too small → move left right |
| Container With Most Water | 11 | Medium | Move the SHORTER line inward — it's the bottleneck. Never skip a potential answer. |
| 3Sum | 15 | Medium | Sort + fix one + two pointer. Skip duplicates at ALL levels to avoid duplicate triplets. |
| Trapping Rain Water | 42 | Hard | Two pointers with `left_max` and `right_max`. Process from side with smaller max. O(1) space. |
| Valid Palindrome | 125 | Easy | Two pointers from ends, skip non-alphanumeric, compare lowercase. |
| Remove Duplicates from Sorted Array | 26 | Easy | Slow pointer marks last unique, fast pointer scans ahead. |

## Common Mistakes

- **Using two pointers on unsorted array** for problems that require sorted order — sort first or use a hash map instead
- **3Sum duplicate handling** — must skip duplicates at all three levels: the fixed element AND both pointers after finding a triplet
- **Trapping Rain Water pointer movement** — move the pointer with the smaller `max`, not the smaller `height` (they're correlated but the logic is about the max)
- **Off-by-one in remove duplicates** — return `slow + 1` (length), not `slow` (last index)
- **Container With Most Water proof** — moving the shorter pointer works because the shorter side is the bottleneck; moving the taller side can only decrease or maintain area, never increase it

## Interview Questions

- "Solve Two Sum on a sorted array in O(n) time O(1) space."
- "Why does moving the shorter pointer work in Container With Most Water?"
- "Solve 3Sum — how do you handle duplicates?"
- "Trapping Rain Water with O(1) space — explain the two-pointer approach."
- "When can you NOT use two pointers?" (unsorted + subarray sum with negatives)
- "Remove duplicates from sorted array in-place."
- "How would you extend 3Sum to 4Sum?" (add another outer loop, same skip logic, O(n³))

## Quick Reference

| Variant | Start Positions | Movement Rule | Typical Use |
|---|---|---|---|
| Opposite direction | `left=0`, `right=n-1` | Move based on comparison | Sorted pair search, palindrome |
| Same direction (fast/slow) | Both at `0` | Fast scans, slow marks valid | Remove duplicates, partition |
| Three pointers | Fix one, two-point rest | Outer loop + two-pointer | 3Sum, Sort Colors |
