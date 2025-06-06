# Candy (LeetCode #35)

**Difficulty: Hard**

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
- Return the minimum number of candies you need to have to distribute the candies to the children.

 

### Example 1:

**Input:** ratings = [1,0,2]

**Output:** 5

**Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
### Example 2:

**Input:** ratings = [1,2,2]

**Output:** 4

**Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

### Constraints:

n == ratings.length

1 <= n <= 2 * 104

0 <= ratings[i] <= 2 * 104

## Solution:
- Traverse the ratings list once from left to right, comparing each element with the previous.
- Track increases, decreases, and equal values in order to assign candies according to the problem's rules:
- Children with higher ratings than the previous get more candies.
- For descending sequences, adjust candies to ensure each child gets at least one and the rule still holds.
- Keep a running total of candies, adjusting for over- or under-allocation in descending streaks.
- Handle the last child separately outside the loop to complete the evaluation.

## Time Complexity:
- O(n)
## Space Complexity:
- O(1)
