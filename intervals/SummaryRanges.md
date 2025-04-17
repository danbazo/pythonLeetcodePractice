# Summary Ranges (LeetCode #228)
**Difficulty: Easy**

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

### Example 1:

**Input:** nums = [0,1,2,4,5,7]
**Output:** ["0->2","4->5","7"]
**Explanation:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
### Example 2:

**Input:** nums = [0,2,3,4,6,8,9]
**Output:** ["0","2->4","6","8->9"]
**Explanation:** The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

### Constraints:

0 <= nums.length <= 20

-231 <= nums[i] <= 231 - 1

All the values of nums are unique.

nums is sorted in ascending order.

## Solution:
- Traverse the list while keeping track of the start of a range.
- When a gap is found (i.e., current number + 1 != next number), add the range.
- Handle both single-number ranges and start->end formats.
- Finalize the last range outside the loop.

## Time Complexity:
- O(n), a single iteration over the list
