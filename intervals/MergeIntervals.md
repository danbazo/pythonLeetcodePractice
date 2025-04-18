# Merge Intervals (LeetCode #56)
**Difficulty: Medium**

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

### Example 1:

**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]

**Output:** [[1,6],[8,10],[15,18]]

**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
### Example 2:

**Input:** intervals = [[1,4],[4,5]]

**Output:** [[1,5]]

**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.
 

### Constraints:

1 <= intervals.length <= 104


intervals[i].length == 2


0 <= starti <= endi <= 104

## Solution:
- Sort the intervals by their start value.
- Initialize `start` and `end` with the first interval's start and end.
- Iterate through the remaining intervals:
  - If the current interval starts before or when the previous one ends, there's overlap. Update `newEnd`.
  - If there's no overlap, add the current merged interval to the result and reset `newStart` and `newEnd`.
- After the loop, add the last interval.
  
## Time Complexity:
- O(nlogn) as we first sorted the input list, and then iterate over it once
