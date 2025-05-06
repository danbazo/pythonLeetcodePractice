# Text Justification (LeetCode #68)

**Difficulty: Hard**


Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

### Example 1:

**Input:** words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

**Output:**
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
### Example 2:

**Input:** words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

**Output:**
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

**Explanation:** Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
### Example 3:

**Input:** words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20

**Output:**
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

### Constraints:

1 <= words.length <= 300

1 <= words[i].length <= 20

words[i] consists of only English letters and symbols.

1 <= maxWidth <= 100

words[i].length <= maxWidth

## Solution:
- Use a greedy algorithm to pack as many words as possible into each line without exceeding `maxWidth`.
- For each line (except the last):
  - If the line has only one word, it is left-justified and padded with spaces on the right.
  - If the line has multiple words, distribute the remaining space evenly between words.
  - Distribute any extra spaces one by one from left to right.
- The last line is left-justified with a single space between words, and extra spaces at the end.
## Time Complexity:
- **O(n)** where `n` is the total number of characters across all words.
  - Each word is processed once, and space distribution is done line-by-line.
## Space Complexity:
- **O(1)** extra space (excluding the output list).

The solution builds the result incrementally without using any additional data structures beyond a few variables and the result list.
