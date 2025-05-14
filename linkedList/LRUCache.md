146. LRU Cache
Solved
Medium
Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

## Solution Explanation

To achieve O(1) time for both `get` and `put`, we use two data structures:

- A **dictionary** (`self.cache`) that maps keys to nodes for O(1) access.
- A **doubly linked list** to track the usage order from **least recently used** to **most recently used**.

We maintain two dummy nodes:
- `firstNode` (head): Points to the least recently used item.
- `lastNode` (tail): Points to the most recently used item.

### Operations:

- **_append(node)**: Appends a node right before `lastNode` (marks as most recently used).
- **_remove(node)**: Unlinks a node from its current position.

### `get(key)`
- If the key is in the cache:
  - Move the node to the end (marking it as most recently used).
  - Return its value.
- Else return `-1`.

### `put(key, value)`
- If the key is in the cache:
  - Update its value.
  - Move it to the end (most recently used).
- If the key is new:
  - If at capacity, remove the node right after `firstNode` (least recently used).
  - Insert the new node at the end.
 
Time Complexity
get(key) – O(1)

put(key, value) – O(1)

All operations on the doubly linked list and hash map are constant time.

Space Complexity
O(capacity) – For storing up to capacity nodes and dictionary entries.
