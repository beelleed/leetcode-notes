# LeetCode 55 - Jump Game | 跳躍遊戲

🔗 [題目連結](https://leetcode.com/problems/jump-game/)

---

## 📘 題目說明 | Problem Description
### 中文：
給定一個整數陣列 nums，其中每個元素代表你在該位置最多可以跳幾步。你最初站在陣列的第一個位置，請判斷是否能跳到最後一個位置。

### English:
Given an array of non-negative integers nums, where each element represents your maximum jump length at that position. Determine if you can reach the last index starting from the first index.

### 🔍 範例 | Examples
```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 with no way to jump to the last index.
```

---

## 🧠 解題思路 | Solution Strategy
✅ 核心想法：
- 使用貪婪法（Greedy）。

- 我們維護一個 maxReach，表示目前為止能跳到的最遠距離。

- 如果某個索引 i 超出 maxReach，表示跳不到，直接回傳 False。

- 如果遍歷整個陣列都沒有違規，就能跳到最後。

✅ Core Idea:
- Use a Greedy approach.

- Maintain a variable maxReach to store the farthest index you can reach so far.

- If at any index i, i > maxReach, then you can't reach that point → return False.

- If you finish the loop, then return True.

---

## 💻 程式碼 | Python Code
```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, jump in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + jump)
        return True
```

### 🧾 程式碼解釋 | Code Explanation
- maxReach = 0：初始化為你一開始能跳到的位置（索引 0）。

- for i, jump in enumerate(nums)：遍歷每個位置與它的最大跳躍距離。

- if i > maxReach：如果這個位置你跳不到，就代表無法完成任務。

- maxReach = max(maxReach, i + jump)：更新能跳到的最遠位置。

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 Time Complexity: O(n)

- 空間複雜度 Space Complexity: O(1)

---

## 📌 學到什麼 | What I Learned
- 「跳躍遊戲」是一道貪婪策略的經典題。

- 記得：我們不需要實際模擬跳的過程，只要看「能不能跳到」。

- 如果一個位置你永遠跳不到，就整題失敗。

- 這種「範圍更新」或「最遠可到達」的技巧，常見於區間問題或跳躍類題型。