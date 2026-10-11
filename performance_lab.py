# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    most_common = numbers[0]

    for number in counts:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because each number must be counted.
- Worst-case: O(n), because the function processes all n elements.
- Average-case: O(n), because dictionary operations are O(1) on average.
- Space complexity: O(n), because the dictionary may store every number
  if all values are unique.
- Why this approach? A dictionary lets us efficiently keep track of how
  many times each number appears.
- Could it be optimized? The time complexity is already O(n), which is
  optimal because every element must be examined at least once. Memory
  usage depends on the number of unique values.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because each element must be checked.
- Worst-case: O(n), because the function processes all n elements.
- Average-case: O(n), because checking and adding values to a set is O(1)
  on average.
- Space complexity: O(n), because the set and result list may contain
  all n elements.
- Why this approach? A set provides fast membership checks while the
  result list preserves the original order.
- Could it be optimized? The time complexity is already O(n), which is
  efficient because every element must be examined. The trade-off is
  using extra memory for the set.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs

# Original slower approach for comparison
def find_pairs_original(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))

    return pairs

"""
Optimization Comparison for Problem 3:

Original approach:
- Uses two nested loops to compare pairs of numbers.
- Time complexity: O(n^2)
- Space complexity: O(n) for the output list.

Optimized approach:
- Uses a set to keep track of numbers that have already been seen.
- Time complexity: O(n) on average.
- Space complexity: O(n) because of the additional set.

Trade-off:
- The optimized version uses additional memory, but it is much faster
  for large input lists.
- The original version uses less auxiliary memory but becomes slower
  as the input size increases.
"""

"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because each number is processed once.
- Worst-case: O(n), because the function loops through all n elements.
- Average-case: O(n), because set lookups and additions are O(1) on average.
- Space complexity: O(n), because the set may store all n elements and
  the output list may also contain pairs.
- Why this approach? A set allows us to quickly check whether the number
  needed to reach the target has already been seen.
- Could it be optimized? This is more efficient than using nested loops,
  which would take O(n^2) time. The trade-off is that this solution uses
  O(n) additional memory.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

        items[size] = i
        size += 1

    return items[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize happens whenever the number of stored
  elements reaches the current capacity. The capacity doubles each time.
- What is the worst-case for a single append? O(n), because during a
  resize all existing elements must be copied to the new list.
- What is the amortized time per append overall? O(1). Most appends take
  constant time, and expensive resizing operations happen infrequently.
- Space complexity: O(n), because the list grows in proportion to the
  number of elements being stored.
- Why does doubling reduce the cost overall? Doubling means resizing
  happens less frequently as the list grows. The cost of the occasional
  resize is spread across many constant-time append operations.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because each element must be processed once.
- Worst-case: O(n), because the function loops through all n elements.
- Average-case: O(n), because every element is added to the running total.
- Space complexity: O(n), because a new list containing n running totals
  is created.
- Why this approach? Keeping a running sum avoids repeatedly adding all
  previous elements for each position.
- Could it be optimized? The time complexity is already O(n), which is
  optimal because every element must be processed. Space could be reduced
  by modifying the original list in place, but that would change the input.
"""
