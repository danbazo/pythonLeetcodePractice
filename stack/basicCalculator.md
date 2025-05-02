# Basic Calculator (LeetCode #224)
**Difficulty: Hard**

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

### Example 1:

**Input:** s = "1 + 1"

**Output:** 2
### Example 2:

**Input:** s = " 2-1 + 2 "

**Output:** 3
### Example 3:

**Input:** s = "(1+(4+5+2)-3)+(6+8)"

**Output:** 23
 

### Constraints:

- 1 <= s.length <= 3 * 105
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Solution:
- Use a stack to keep track of partial results and signs when dealing with parentheses.
- Maintain a num string to build multi-digit numbers and a sign variable to apply the correct operation.
- Iterate over the string character by character:
  - If it's a digit, build the current number.
  - If it's an operator (+ or -), apply the previous number and update the sign.
  - If it's '(', push the current sign and a new subtotal (0) onto the stack, and reset the sign to '+'.
  - If it's ')', compute the value inside the parentheses:
    - Pop the subtotal and its associated sign.
    - Apply the operation to the previous level’s result.
- At the end, if there's a pending number, apply it.
- The final result is at the top of the stack.
## Time Complexity:
- O(n) the string is iterated over once
