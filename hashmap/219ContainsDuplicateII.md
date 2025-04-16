# Contains Duplicate II (LeetCode #219)
**Difficulty: Easy**

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

 

### Example 1:

**Input:** nums = [1,2,3,1], k = 3
**Output:** true
### Example 2:

**Input:** nums = [1,0,1,1], k = 1
**Output:** true
### Example 3:

**Input:** nums = [1,2,3,1,2,3], k = 2
**Output:** false
 

### Constraints:

1 <= nums.length <= 105

-109 <= nums[i] <= 109

0 <= k <= 105

## Solution:
- Uses a dictionary to keep track of numbers and the last index they were found
- Check in a loop if each number has been found before, and checks if the indexes are close enough according to `k`
- Returns `true` if a match is found, `false` if all the loops are done and no answer is found

## Time Complexity:
- O(n) as we make only a loop over the list of numbers, using a dictionary to look matches

