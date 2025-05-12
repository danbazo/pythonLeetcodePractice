82. Remove Duplicates from Sorted List II
Solved
Medium
Topics
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:

![image](https://github.com/user-attachments/assets/cd3ce386-6cc9-44f1-b167-ed9ca784dbea)

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:

![image](https://github.com/user-attachments/assets/f68c029f-c51f-4148-b995-310e8e39617f)


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Solution:
Use a dummy node (fakeHead) before the actual head to simplify handling of head removals.

Iterate through the list using two pointers:

prevNode: the last confirmed non-duplicate node.

currentNode: the node currently being evaluated.

Track duplicates using a boolean flag duplicated.

If a duplicate sequence is detected, skip all its elements.

If duplicated is still True at the end, remove the last duplicate group manually.


Time Complexity:
O(n)
Space Complexity:
O(1)
