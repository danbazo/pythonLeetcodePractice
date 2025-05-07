# Trapping Rain Water (LeetCode #42)

**Difficulty: Hard**

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 

### Example 1:

![image](https://github.com/user-attachments/assets/a7496f45-5457-435e-8a0a-4d3ab85bbbd6)


**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]

**Output:** 6

**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


### Example 2:

**Input:** height = [4,2,0,3,2,5]

**Output:** 9
 

### Constraints:

n == height.length

1 <= n <= 2 * 104

0 <= height[i] <= 105

## Solution:
- Uses a two-pointer approach to traverse the elevation map from both ends.
- Maintains two variables, left_max and right_max, to keep track of the maximum height seen so far from the left and right.
- At each step, determines water trapped at the current position based on the minimum of the two maximums.
- Efficiently calculates the trapped water in a single pass.
## Time Complexity:
- O(n)
## Space Complexity:
- O(1)
