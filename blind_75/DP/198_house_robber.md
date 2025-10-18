# 💰 198. House Robber

[LeetCode 題目連結](https://leetcode.com/problems/house-robber/)

---

## 📘 題目描述 | Description

你是一名小偷，想從一排房子中偷取金錢，但不能偷「相鄰的兩間房」。  
給定一個整數陣列 `nums` 表示每間房子的金額，請你回傳最多可以偷多少錢。

You are a robber planning to rob houses along a street. You cannot rob two adjacent houses.  
Given an array of non-negative integers, return the maximum amount you can rob.

### Examples
- Example 1:

    - Input: nums = [1,2,3,1]
    - Output: 4
    - Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

- Example 2:

    - Input: nums = [2,7,9,3,1]
    - Output: 12
    - Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

---

## 🧠 解題思路 | Solution Roadmap
### 📘 中文版

1. 題型辨識：

    - 陣列 + 動態規劃（Dynamic Programming）

    - 題目限制：不能搶相鄰的房子 → 子問題＋選擇性

2. 轉換問題思考：

    - 每一間房子有兩種選擇：搶 or 不搶

    - 若搶這間（第 i 間），則不能搶上一間（第 i-1 間）→ 累加 dp[i-2]

    - 若不搶，則維持前一間搶到的最大值 → dp[i-1]

3. 狀態表示（State Definition）：

    - dp[i]：前 i 間房子能搶到的最大金額（i 從 1 開始表示第 0 間房）

4. 狀態轉移方程式（Transition）：
```lua
dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
```
- dp[i-1]：不搶第 i 間

- dp[i-2] + nums[i-1]：搶第 i 間，加上 i-2 間的最大值

5. 初始化條件（Base Cases）：

    - dp[0] = 0：沒有房子

    - dp[1] = nums[0]：只搶第一間房

### 📗 English Version

1. Problem Type:

    - Array + Dynamic Programming

    - Constraint: Cannot rob two adjacent houses → Typical choice problem

2. Reframe the Problem:

    - For each house: two options – rob or skip

    - If rob: add nums[i-1] to dp[i-2]

    - If skip: just take dp[i-1]

3. State Definition:

    - dp[i] represents the max money you can rob from the first i houses

4. Transition Function:
```lua
dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
```
5. Base Cases:

    - dp[0] = 0 → no house

    - dp[1] = nums[0] → only one house to rob

---

## ✅ 解法 | Solution (Dynamic Programming)

### Python 程式碼

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]
```

## 🧠 遞推公式解釋 | DP Formula Explanation
- dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

- 解釋：

    - 不偷第 i 間 ➜ dp[i-1]

    - 偷第 i 間 ➜ dp[i-2] + nums[i-1]

- 取兩者最大值，確保不會偷到相鄰的房子

### 1️⃣ 不偷第 i 間

- 那最大金額跟前一間一樣

- 所以是 dp[i-1]

### 2️⃣ 偷第 i 間

- 因為不能連續偷相鄰的房子，所以前一間（第 i-1 間）一定不能偷。

- 能加的上一個安全的金額就是「偷到第 i-2 間的最大值」。

- 再加上這間房的錢：dp[i-2] + nums[i-1]

## 🧪 範例分析 | Example
```python
nums = [5, 2, 9, 11, 1, 15, 6]
```
| i | 房子金額 nums\[i-1] | dp\[i-1] | dp\[i-2] + nums\[i-1] | dp\[i] 解釋                     | dp\[i] 結果 |
| - | --------------- | -------- | --------------------- | ----------------------------- | --------- |
| 1 | 5               | -        | -                     | 初始化                           | 5         |
| 2 | 2               | 5        | 0 + 2                 | max(5, 2)                     | 5         |
| 3 | 9               | 5        | 5 + 9                 | max(5, 14)                    | 14        |
| 4 | 11              | 14       | 5 + 11                | max(14, 16)                   | 16        |
| 5 | 1               | 16       | 14 + 1                | max(16, 15)                   | 16        |
| 6 | 15              | 16       | 16 + 15            | 應是 dp\[4] + 15 = 16 + 15 = 31 | 31        |
| 7 | 6               | 31       | 16 + 6                | max(31, 22)                   | 31        |

最終答案 ➜ dp[7] = 31

---

## ❓ 常見誤解：為什麼不是 `return dp[i]`？

當你寫：

```python
for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
return dp[n]  # 為什麼不是 dp[i]？
```
- 可能會想說「Loop 結束後，i 已經是最後的值啊…」

- 但其實：

    - i 只是迴圈內的暫時變數，離開迴圈後它的值不該成為最終依據。

    - dp[n] 才是我們想要的「偷到 n 間房子時的最大金額」。
## ✅ 為什麼用 dp[n]
- dp[0], dp[1], …, dp[n] 是我們在迴圈中構建的「完整狀態表」。

- dp[n] 表示「偷完最後一間（第 n 間）房子時的最佳結果」，也就是這題的答案。

---

## ✨ 學到的重點 | Key Takeaways
- 動態規劃不是「貪心偷最大」，而是逐步推最大值

- dp[i] 表示偷前 i 間房的最佳解

- 用 for 逐步構建最佳結果，而非一次判斷

## 📌 學習筆記
| 概念      | 說明                                          |
| ------- | ------------------------------------------- |
| 動態規劃 DP | 這題是典型的「不能選相鄰」問題                             |
| 狀態定義    | `dp[i]`：前 i 間可偷的最大值                         |
| 轉移公式    | `dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])` |
| 陣列初始化   | `dp = [0] * (n + 1)`                        |
| 小心邊界條件  | nums 為空或只有 1 間房子的特例要特別處理                    |


## ⏱ 複雜度分析 | Complexity
- 時間：O(n)

- 空間：O(n)（可優化成 O(1) 用兩個變數）
---
## 🧩 補充筆記：流程圖觀念
每一個 dp[i] 都是從 dp[i-1] 和 dp[i-2] 各自「延伸」出來的結果
這樣你才能確保偷到最多、但不會偷相鄰的房子。
```lua
dp[1] = nums[0]
dp[2] = max(nums[0], nums[1])
dp[3] = max(dp[2], dp[1] + nums[2])
⋯⋯
dp[n] = 最佳解
```