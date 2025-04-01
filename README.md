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
   ```
   
2. Navigate to the desired category:

   ``` bash
   cd arrays
   ```

3. Run a Python script:

   ```bash
   
   python two_sum.py
   ```

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

|# |	Problem	|Category	|Difficulty	|Explaination|Solution|
|-----------|-----------|-----------|--------|-------|------|
|12 |Integer to Roman	|Arrays	|🔵 Medium	|[012IntegerToRoman.md](Arrays/012IntegerToRoman.md)|[012IntegerToRoman.py](Arrays/012IntegerToRoman.py)|
|13 |Roman to Integer	|Arrays	|🟢 Easy	|[013RomanToInteger.md](Arrays/013RomanToInteger.md)|[013RomanToInteger.py](Arrays/013RomanToInteger.py)|
|42 |Trapping Rain Water	|Arrays	|🔴 Hard	|[42TrappingRainWater.md](Arrays/42TrappingRainWater.md)|[42TrappingRainWater.py](Arrays/42TrappingRainWater.py)|
|135	|Candy	|Arrays	|🔴 Hard	|[135Candy.md](Arrays/135Candy.md)|[135Candy.py](Arrays/135Candy.py)|









