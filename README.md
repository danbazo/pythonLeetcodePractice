#  LeetCode Python Practice Solutions

This repository contains my solutions to various **LeetCode** problems, categorized by topic.  
Each solution includes explanations, optimized approaches, and test cases.  

## 📖 Table of Contents
- [🔥 Arrays](Arrays/)
- [🔗 Linked Lists](linked_lists/)
- [🔁 Dynamic Programming](dynamic_programming/)
- [🧮 Math](math/)
- [🧩 Recursion & Backtracking](recursion/)
- [📊 Sorting & Searching](sorting_searching/)
- [🔑 Hashing](hashing/)
- [📡 Graphs & Trees](graphs_trees/)

---

## ✅ How to Use This Repository
1. Clone the repository:  
   ```bash
   git clone https://github.com/danbazo/pythonLeetcodePractice
Navigate to the desired category:


cd arrays
Run a Python script:

bash

python two_sum.py

# 📌 Example Problem: Two Sum (LeetCode #1)
Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

🔹 Approach: Hash Map for O(n) time complexity.
🔹 Solution Code: two_sum.py
``` python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]
```

# 🔥 Progress Tracker

|# |	Problem	|Category	|Difficulty	|Solution|
|-----------|-----------|-----------|--------|-------|
|135	|Candy	|Arrays	|🔴 Hard	|(Arrays/135Candy.py)|
|42 |Trapping Rain Water	|Arrays	|🔴 Hard	|Arrays/42TrappingRainWater.py|








