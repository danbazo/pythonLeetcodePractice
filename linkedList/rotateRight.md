61. Rotate List
Solved
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
![image](https://github.com/user-attachments/assets/bb322585-e3d9-4c32-9acf-1685ab1588c7)


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
![image](https://github.com/user-attachments/assets/9b7b2505-4719-414e-bb53-765377128789)


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

Solution:

Use a dictionary to map indices to nodes during a single traversal.

Calculate the length of the list.

Use modulo operation to reduce unnecessary rotations (k % length).

Identify the new head and tail using the mapped indices.

Reassign pointers:

Disconnect the new tail (length - kNew - 1) from the rest of the list.

Point the old tail to the original head.

Return the new head (length - kNew).

Time Complexity: O(n) – one pass to store nodes.

Space Complexity: O(n) – due to the dictionary storing all nodes by index.
