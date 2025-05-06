# Trapping Rain Water (LeetCode #42)

**Difficulty: Hard**

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 

### Example 1:

![image](https://github.com/user-attachments/assets/a7496f45-5457-435e-8a0a-4d3ab85bbbd6)


**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]

**Output:** 6

**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


### Example 2:

**Input:** height = [4,2,0,3,2,5]

**Output:** 9
 

### Constraints:

n == height.length

1 <= n <= 2 * 104

0 <= height[i] <= 105

## Solution:
 Perform **three passes** over the elevation map:
  1. **First pass:** Identify local maxima (peaks) where the height decreases after increasing. These are potential water boundaries.
  2. **Second pass:** Refine the list of local maxima by removing those that are "overshadowed" by taller peaks—only keep the necessary ones to trap water effectively.
  3. **Third pass:** For each pair of remaining peaks, calculate how much water can be trapped in between them by comparing the height of the bars to the smaller of the two peaks.

- Use two auxiliary lists:
  - `maxHeight`: stores the values of local maxima.
  - `maxHeightIndex`: stores the corresponding indices of these maxima.

- Water trapped between two peaks is calculated using the formula:  
  `water += min(left_peak, right_peak) - height[i]`,  
  for each `i` between the peaks.
## Time Complexity:
- **Worst case: O(n²)**  
  - First pass: O(n) – scans the elevation list once.
  - Second pass: Can be up to O(n²) due to nested deletions while refining the peak list.
  - Third pass: O(n) – sums trapped water by iterating between peaks.
## Space Complexity:
- **O(n)**  
  - Used to store local maxima and their indices (`maxHeight`, `maxHeightIndex`).
  - No extra space required for the final result; water is accumulated incrementally.
