# Set Matrix Zeroes (LeetCode #073)
difficulty: Medium


Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

![image](https://github.com/user-attachments/assets/92bf2740-1da7-4695-a595-064771e81002)


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:

![image](https://github.com/user-attachments/assets/40ec55e8-35fb-4c14-bce7-91f97b88587d)


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length

n == matrix[0].length

1 <= m, n <= 200

-231 <= matrix[i][j] <= 231 - 1
