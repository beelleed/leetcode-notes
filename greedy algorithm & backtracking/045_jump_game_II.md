# 📘 LeetCode 45 - Jump Game II | 跳躍遊戲 II
🔗 [題目連結](https://leetcode.com/problems/jump-game-ii/)

---

## 🧾 題目說明 | Problem Description
### 中文：
給定一個整數陣列 nums，其中每個元素代表你在該位置最多可以跳幾步。你最初站在陣列的第一個位置，請計算到達最後一個位置所需的最小跳躍次數。

### English:
Given an array of non-negative integers nums, where each element represents your maximum jump length at that position. Determine the minimum number of jumps required to reach the last index starting from the first index.

### 🔍 範例 | Examples
```text
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

---

## 🧠 解題思路 | Solution Strategy
✅ 核心想法：
- 使用貪婪法（Greedy）。

- 維護兩個變數：current_end 表示當前跳躍的最遠邊界，farthest 表示在當前跳躍範圍內能到達的最遠位置。

- 當我們走到 current_end 時，表示需要進行一次新的跳躍，並更新 current_end 為 farthest。

✅ Core Idea:
- Use a Greedy approach.

- Maintain two variables: current_end denotes the end of the current jump range, and farthest denotes the farthest index reachable within the current range.

- When reaching current_end, increment the jump count and update current_end to farthest.

---

## 💻 程式碼 | Python Code
```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
```

### 🧾 程式碼解釋 | Code Explanation
- jumps：記錄跳躍次數。

- current_end：當前跳躍的最遠邊界。

- farthest：在當前跳躍範圍內能到達的最遠位置。

- 遍歷陣列，更新 farthest，當到達 current_end 時，進行一次跳躍，並更新 current_end 為 farthest。

### 🔄 圖解流程
- 以 nums = [2, 3, 1, 1, 4] 為例：

1. 初始化變數：

    - jumps = 0：跳躍次數

    - current_end = 0：當前跳躍的最遠邊界

    - farthest = 0：在當前跳躍範圍內能到達的最遠位置

2. 遍歷陣列：

    - 索引 0：

        - nums[0] = 2，可跳至索引 2

        - 更新 farthest = max(0, 0 + 2) = 2

        - 因為 i == current_end，需要跳躍一次

            - jumps = 1

            - 更新 current_end = farthest = 2

    - 索引 1：

        - nums[1] = 3，可跳至索引 4

        - 更新 farthest = max(2, 1 + 3) = 4

    - 索引 2：

        - nums[2] = 1，可跳至索引 3

        - farthest 保持為 4

        - 因為 i == current_end，需要跳躍一次

            - jumps = 2

            - 更新 current_end = farthest = 4

3. 結束條件：

    - 當 current_end 到達或超過最後一個索引時，結束遍歷。

### 📈 流程圖示意
```makefile
索引:     0   1   2   3   4
值:       2   3   1   1   4
          ↑
        起點
跳躍1:    └───►
          ↑
        跳至索引1
跳躍2:        └────────────►
                      ↑
                    跳至索引4（終點）
```
### ✅ 結論
- 最少跳躍次數： 2

- 跳躍路徑： 索引 0 → 索引 1 → 索引 4

這種貪婪策略確保在每次跳躍中走得最遠，從而達到最少的跳躍次數。

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 Time Complexity: O(n)

- 空間複雜度 Space Complexity: O(1)

---

## 📌 學到什麼 | What I Learned
- 這題展示了貪婪策略在解決最小跳躍問題中的應用。

- 透過追蹤當前跳躍範圍內能到達的最遠位置，確保每次跳躍都能覆蓋更多的範圍，從而達到最少的跳躍次數。