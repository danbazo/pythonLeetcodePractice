637. Average of Levels in Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

![avg1-tree](https://github.com/user-attachments/assets/42d02c47-311a-4ddd-92d2-373ba1dcfe9e)

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:

![avg2-tree](https://github.com/user-attachments/assets/66c27af8-7316-47f2-a701-a72b1f3ca0d1)

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
