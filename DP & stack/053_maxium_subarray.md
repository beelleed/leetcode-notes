# 📘 Leetcode 53 – Maximum Subarray（最大子陣列和）
🔗 題目連結：[https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

---

## 📄 題目說明 | Problem Description

- **中文：**
  給定一個整數陣列 `nums`，找出一個**連續子陣列**，使其總和最大，並回傳其總和。
  例：`nums = [-2,1,-3,4,-1,2,1,-5,4]` → 最大子陣列為 `[4,-1,2,1]`，總和為 `6`。

- **English:**
  Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) with the largest sum, and return its sum.

### Examples
- Example 1:

    - Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    - Output: 6
    - Explanation: The subarray [4,-1,2,1] has the largest sum 6.

- Example 2:

    - Input: nums = [1]
    - Output: 1
    - Explanation: The subarray [1] has the largest sum 1.

- Example 3:

    - Input: nums = [5,4,-1,7,8]
    - Output: 23
    - Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

---

## 🧠 解法邏輯 | Solution Approach

使用 Kadane’s Algorithm（卡登演算法），在每個位置動態計算包含當前元素的最大和。

- `current_max = max(x, current_max + x)`
- `global_max = max(global_max, current_max)`

此算法可理解為動態規劃，也可視為貪心策略，選擇“延續先前區段”或“重啟新區段”。

---

## 💻 程式碼 | Code

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = global_max = nums[0]

        for x in nums[1:]:
            current_max = max(x, current_max + x)
            global_max = max(global_max, current_max)

        return global_max
```
```python
current_max = global_max = nums[0]
```
- 初始化兩個變數：

    - current_max: 目前以第 i 個元素結尾的最大子陣列和。

    - global_max: 整體出現過的最大子陣列和。

- 兩者都初始為 nums[0]，表示從第一個元素開始。
```python
for x in nums[1:]:
```
🔁 遍歷列表中從第 1 個元素（索引 1）開始的所有元素，逐個處理。
```python
current_max = max(x, current_max + x)
```
🔁 關鍵邏輯：

- 決定要「繼續加到之前的區段」還是「重新開始新的子陣列」：

    - current_max + x: 把當前數字加到前面子陣列。

    - x: 直接從這個數字重新開始。

👆 兩者取最大值，更新 current_max。
```python
global_max = max(global_max, current_max)
```
🔁 每次更新完 current_max，都檢查是否比目前的 global_max 更大，如果是，就更新它。
```python
return global_max
```
✅ 回傳全局最大子陣列和，也就是我們的答案。

### 🧠 精華總結：

- 這是典型的 DP 優化版本，只使用兩個變數就能完成。

- 核心：要嘛繼續累加，要嘛重啟子陣列。

- 透過線性遍歷即可完成，效率非常高。

---

## 🧪 範例 | Example Walkthrough
輸入：nums = [-2,1,-3,4,-1,2,1,-5,4]
| i | nums\[i] | current\_max 計算   | current\_max | global\_max |
| - | -------- | ----------------- | ------------ | ----------- |
| 0 | -2       | 初始化               | -2           | -2          |
| 1 | 1        | max(1, -2+1) = 1  | 1            | 1           |
| 2 | -3       | max(-3, 1-3) = -2 | -2           | 1           |
| 3 | 4        | max(4, -2+4) = 4  | 4            | 4           |
| 4 | -1       | max(-1, 4-1) = 3  | 3            | 4           |
| 5 | 2        | max(2, 3+2) = 5   | 5            | 5           |
| 6 | 1        | max(1, 5+1) = 6   | 6            | 6           |
| 7 | -5       | max(-5, 6-5) = 1  | 1            | 6           |
| 8 | 4        | max(4, 1+4) = 5   | 5            | 6           |

✅ 最後回傳 global_max = 6

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity

- 時間複雜度 Time Complexity: O(n)

- 空間複雜度 Space Complexity: O(1)

---

## 📝 我學到了什麼 | What I Learned

- Kadane’s Algorithm 可以在線性時間內找出最大連續子陣列。

- 只需要維護兩個變數：current_max 與 global_max，就能解決問題。

- 若出現負數，也能自動在之後找到更佳解。