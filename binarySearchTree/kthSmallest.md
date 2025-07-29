230. Kth Smallest Element in a BST
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:

![kthtree1](https://github.com/user-attachments/assets/3f010c12-5c39-47af-a8dc-bed68cc39210)

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

![kthtree2](https://github.com/user-attachments/assets/1d4bd7d9-afa8-458a-a758-8ae4fb2e6b3b)

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
