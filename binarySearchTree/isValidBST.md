98. Validate Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

![tree1](https://github.com/user-attachments/assets/a5f45d99-8b93-4a94-b514-00e7d3384860)

Input: root = [2,1,3]
Output: true
Example 2:

![tree2](https://github.com/user-attachments/assets/260df295-0738-4b69-9974-0f56b16dbf89)

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
