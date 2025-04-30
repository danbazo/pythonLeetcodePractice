# Valid Parentheses (LeetCode #20)
**Difficulty: Easy**

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.
 

### Example 1:

**Input:** s = "()"

**Output:** true

### Example 2:

**Input:** s = "()[]{}"

**Output:** true

### Example 3:

**Input:** s = "(]"

**Output:** false

### Example 4:

**Input:** s = "([])"

**Output:** true

 

### Constraints:

1 <= s.length <= 104

s consists of parentheses only '()[]{}'.

## Solution:
- Use a stack to keep track of opening brackets.
- For each character:
  - If it's a closing bracket, check if it matches the last opened one.
  - If it matches, pop the last opened one from the stack.
  - If it doesn't match or the stack is empty, return `False`.
- After processing, if the stack is not empty, return `False`; otherwise, `True`.

## Time Complexity:
- O(n) as the string is looped through only once
