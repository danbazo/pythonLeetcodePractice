# Copy List with Random Pointer (LeetCode #138)
**Difficulty: Medium**

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

### Example 1:

![image](https://github.com/user-attachments/assets/8668c089-50ea-42ed-8305-87a8c0bac1fb)


**Input:** head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

**Output**: [[7,null],[13,0],[11,4],[10,2],[1,0]]
### Example 2:

![image](https://github.com/user-attachments/assets/c61afdbf-94b2-4a04-beec-3b4967036672)


**Input:** head = [[1,1],[2,1]]

**Output:** [[1,1],[2,1]]

### Example 3:

![image](https://github.com/user-attachments/assets/611cc961-ec44-4e44-8489-efec2dc536e0)


**Input:** head = [[3,null],[3,0],[3,null]]

**Output:** [[3,null],[3,0],[3,null]]
 

### Constraints:

0 <= n <= 1000

-104 <= Node.val <= 104

Node.random is null or is pointing to some node in the linked list.

## Solution:
- First pass
  - Traverse the original list.
  - For each original node, create a copy with the same value.
  - Store the mapping: original_node -> copy_node.
  - Set the .next of the copied nodes (optional to delay until second pass, but it's often done here).
- Second pass
  - Traverse the original list again.
  - For each node, get the random node from the originally list and assign its correspondent one in the mapping to the new list
## Time Complexity:
- O(n) as we iterate over the original list twice
## Space Complexity:
- O(n) as we create a dictionary mapping all the nodes from the new list to the original one
