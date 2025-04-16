# Longest Consecutive Sequence (leetCode #128)

**Difficulty: Medium**


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

### Example 1:

**Input:** nums = [100,4,200,1,3,2]
**Output:** 4
**Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
### Example 2:

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]
**Output:** 9
### Example 3:

**Input:** nums = [1,0,1,2]
**Output:** 3
 

### Constraints:

0 <= nums.length <= 105

-109 <= nums[i] <= 109

## Solution:
- Convert input list to a set for O(1) lookups.
- For each number, only start a new sequence if it's the beginning (i.e., `num - 1` not in the set).
- Count the length of that sequence by checking consecutive numbers.
- Keep track of the longest sequence found.
  
## Time Complexity:
- O(n), every number is only visited once

## Previous attempts:
- First approach used a dictionary to keep track of starting an ending numbers in a sequence so far. Complexity was still O(n), but was a bit more complex and memory heavy
