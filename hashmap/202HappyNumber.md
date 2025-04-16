# Happy Number (LeetCode #202)
**Difficulty: Easy**

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

### Example 1:

**Input:** n = 19
**Output:** true
**Explanation:**
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
### Example 2:

**Input:** n = 2
**Output:** false
 

### Constraints:

1 <= n <= 231 - 1

## Solution:
- Uses a `set` to keep track of seen numbers to detect cycles.
- Calculates square sum of digits in each iteration.
- Returns `True` if 1 is reached, otherwise `False` if a cycle is found.

## Time Complexity:
- O(log n) per iteration (since we're summing squares of digits), with a small number of unique sums.
