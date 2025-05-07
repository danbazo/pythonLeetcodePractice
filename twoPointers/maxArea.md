# Container With Most Water (LeetCode #11)

**Difficulty: Medium**


You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

### Example 1:

![image](https://github.com/user-attachments/assets/d5ec994d-9bac-4b30-8d54-ac6e3d3dffe3)


**Input:** height = [1,8,6,2,5,4,8,3,7]

**Output:** 49

**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:

**Input:** height = [1,1]

**Output:** 1
 

### Constraints:

- n == height.length

- 2 <= n <= 105

- 0 <= height[i] <= 104

## Solution:
- Use a **two-pointer** approach:
  - Initialize two pointers, `lower` at the start and `upper` at the end of the list.
  - Calculate the area between the lines at `lower` and `upper`.
  - Move the pointer pointing to the **shorter height**, since that limits the water volume.
  - Continue until the pointers meet.
- Track the maximum area found throughout the process.

## Time Complexity:
- **O(n)** — where `n` is the number of elements in the `height` list.  
  Each index is visited at most once as the pointers move toward each other.
## Space Complexity:
- **O(1)** — constant extra space is used.
