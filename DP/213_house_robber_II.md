# 🏠 LeetCode 213 — House Robber II / 打家劫舍 II
🔗 [題目連結](https://leetcode.com/problems/house-robber-ii/)

---

## 📄 題目說明 | Problem Description

- **中文**：有一排屋子排成一個圓圈，每個屋子裡有一定數量的金錢（`nums[i]`）。如果你偷相鄰的兩個房子就會觸動警報。因為是圓形排列，第一個和最後一個房子互為鄰居。求在不觸警報的情況下，能偷到的最大金額。

- **English**: Houses are arranged in a circle, each house has some money. You cannot rob two adjacent houses or else the alarm triggers. Because it's a circle, the first and last house are adjacent. Return the maximum money you can rob without alerting the police.

- **Examples**
    - Example 1:

        - Input: nums = [2,3,2]
        - Output: 3
        - Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    - Example 2:

        - Input: nums = [1,2,3,1]
        - Output: 4
        - Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

    - Example 3:

        - Input: nums = [1,2,3]
        - Output: 3

---

## 🧠 解題思路 | Solution Idea

### 方法一

這題是 “House Robber I（198 題）” 的延伸版本，差異在於圓圈的結構使得第一家和最後一家不能同時被偷。核心想法是：

1. **拆成兩個線性問題 (linear cases)**  
   - 不偷第 1 個房子：考慮區間 `nums[1:]`  
   - 不偷最後一個房子：考慮區間 `nums[:-1]`  
   這樣就不會同時觸及第一與最後的邊界問題。

2. 每個線性子問題就可以用與 House Robber I 同樣的 DP 方法求解。

3. 最後取這兩個結果的最大值，就是原本圓形排列的答案。

用這樣拆解後，複雜度仍是 O(n)，空間可以優化到 O(1)。

### 方法二

- 房子排成一圈，因此第一間和最後一間不能同時被偷。
- 不能偷相鄰的房子。
- 求在這些限制下可以偷到的最大金額。

為了解決「環狀」這個限制，我們把問題拆成兩個線性版本：  
1. 不偷最後一間 → 偷 `nums[0 .. n-2]`  
2. 不偷第一間 → 偷 `nums[1 .. n-1]`  
最後取得兩個結果的最大值即為答案。  

---

## 💻 程式碼實作 | Code (Python) - linear

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # 線性版本的 rob 函式（從 start 到 end 包含）
        def rob_linear(houses: List[int]) -> int:
            prev1, prev2 = 0, 0
            # prev1 = 前一個位置偷或不偷的最大值
            # prev2 = 前兩個位置的最大值
            for x in houses:
                # 新的 prev1 是不要偷這間：max(prev1, prev2 + x?) 其實是 max(prev1, prev2 + x) 但這邊用 prev2 + x
                new_val = max(prev1, prev2 + x)
                prev2 = prev1
                prev1 = new_val
            return prev1

        # 不偷最後一棟 → rob_linear(nums[0 : n-1])
        case1 = rob_linear(nums[:-1])
        # 不偷第一棟 → rob_linear(nums[1 : n])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
```
```python
n = len(nums)
if n == 0:
    return 0
if n == 1:
    return nums[0]
```
- 先處理邊界情況：

    - 如果 nums 是空的，沒有房子可偷，回傳 0。

    - 如果只有一個房子，答案就是這個房子的金額。
```python
def rob_linear(houses: List[int]) -> int:
    prev1, prev2 = 0, 0
    for x in houses:
        new_val = max(prev1, prev2 + x)
        prev2 = prev1
        prev1 = new_val
    return prev1
```
- 這是 線性版本的打家劫舍（與 LeetCode 198 題相同）：

    - prev1 表示「到目前位置（包括前一房子）能偷到的最大金額」

    - prev2 表示「到前前一個位置能偷到的最大金額」

    - 當我們考慮偷或不偷當前房子 x 時，

        - 不偷的話能拿到 prev1

        - 偷的話就是 prev2 + x

    - 所以 new_val = max(prev1, prev2 + x)

    - 更新變數：把 prev1 給 prev2，然後新的值給 prev1

    - 最後回傳 prev1（代表整個線性段的最優解）

```python
case1 = rob_linear(nums[:-1])
case2 = rob_linear(nums[1:])
return max(case1, case2)
```
- 因為原題是圓形排列，第一間與最後一間是鄰居，不能同時偷。

- 所以拆成兩種情況計算：

    1. 不偷最後一間 → nums[:-1]（從第 0 到倒數第 2 間房子）

    2. 不偷第一間 → nums[1:]（從第 1 間到最後一間房子）

- 分別對這兩條線性情況呼叫 rob_linear，然後取兩者的最大值做為最終答案。

---

## 🧪 範例
```python
nums = [2, 3, 2]
```
### 運算 case1 = rob_linear(nums[:-1])

- nums[:-1] 是 [2, 3]（不偷最後一間）

- 呼叫 rob_linear([2, 3])

- 在 rob_linear 中：

    - 初始化 prev1 = 0, prev2 = 0

    - 第一間房子 x = 2

        - new_val = max(prev1 (=0), prev2 + x = 0 + 2) = 2

        - 更新：prev2 = prev1 (0), prev1 = new_val (2) → 現在 prev1=2, prev2=0

    - 第二間房子 x = 3

        - new_val = max(prev1 (=2), prev2 + x = 0 + 3) = 3

        - 更新：prev2 = prev1 (2), prev1 = new_val (3) → 最終 prev1 = 3

    - 返回 3

- 所以 case1 = 3

### 運算 case2 = rob_linear(nums[1:])

- nums[1:] 是 [3, 2]（不偷第一間）

- 呼叫 rob_linear([3, 2])

- 在 rob_linear 中：

    - 初始化 prev1 = 0, prev2 = 0

    - x = 3

        - new_val = max(0, 0 + 3) = 3

        - 更新：prev2 = 0, prev1 = 3

    - x = 2

        - new_val = max(prev1 = 3, prev2 + x = 0 + 2) = 3

        - 更新：prev2 = 3, prev1 = 3

    - 返回 3

- 所以 case2 = 3

### 最終答案

- max(case1, case2) = max(3, 3) = 3

- 所以 rob([2,3,2]) = 3

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度：O(n) — 我們對 nums[:-1] 和 nums[1:] 各掃描一遍

- 空間複雜度：O(1) — rob_linear 用常數額外空間，除了輸入切片（如果算切片那部分的額外空間）

---

## 💻 程式碼實作 | Code (Python) - DP
```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 邊界處理
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # 線性版本的打家劫舍，用完整 dp 陣列寫法
        def rob_linear_dp(houses: List[int]) -> int:
            m = len(houses)
            if m == 0:
                return 0
            if m == 1:
                return houses[0]
            # dp[i] 表示偷到 houses[i]（考慮到第 i 間）時的最大金額
            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            # 從第三間 (index=2) 開始
            for i in range(2, m):
                # 偷這間：dp[i-2] + houses[i]
                # 不偷這間：dp[i-1]
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]


        # 情況一：不偷最後一間
        case1 = rob_linear_dp(nums[:-1])
        # 情況二：不偷第一間
        case2 = rob_linear_dp(nums[1:])

        return max(case1, case2)
```
### 邊界處理
```python
n = len(nums)
if n == 0:
    return 0
if n == 1:
    return nums[0]
```
- 若無房子可偷，回傳 0

- 若只有一間房子，偷那間就是最大金額

### 線性版 DP：rob_linear_dp
```python
m = len(houses)
if m == 0:
    return 0
if m == 1:
    return houses[0]
dp = [0] * m
dp[0] = houses[0]
dp[1] = max(houses[0], houses[1])
```
- 若線性子列長度為 0、1，直接處理

- 初始化 dp[0] 和 dp[1]，表示前 1 間或前 2 間偷到的最大金額
```python
for i in range(2, m):
    dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
```
- 對於第 i 間房子，有兩種選擇：

    - 不偷第 i 間：得到 dp[i - 1]

    - 偷第 i 間：得到 dp[i - 2] + houses[i]

    - 選較大的那一個

- 最後 return dp[-1] 把最後一間房子的最大偷盜金額當作線性子問題的答案。

---

## 🧪 範例

- 假設 nums = [2, 7, 9, 3, 1]

### 情況一（排除最後一間） → [2, 7, 9, 3]

- m = 4

- dp 初始化：dp = [2, max(2,7)=7, 0, 0] → dp = [2, 7, 0, 0]

- i = 2 → dp[2] = max(dp[1], dp[0] + 9) = max(7, 2+9=11) = 11

- i = 3 → dp[3] = max(dp[2], dp[1] + 3) = max(11, 7+3=10) = 11
→ case1 = 11

### 情況二（排除第一間） → [7, 9, 3, 1]

- m = 4

- dp 初始化：dp = [7, max(7,9)=9, 0, 0] → dp = [7, 9, 0, 0]

- i = 2 → dp[2] = max(dp[1], dp[0] + 3) = max(9,7+3=10) = 10

- i = 3 → dp[3] = max(dp[2], dp[1] + 1) = max(10,9+1=10) = 10
→ case2 = 10

結果：max(case1, case2) = max(11, 10) = 11

所以 rob([2,7,9,3,1]) = 11

---

## 📈 複雜度分析（DP 方法）| Complexity

### ✅ 時間複雜度：O(n)

- rob_linear_dp() 中的迴圈跑一次長度為 n 的陣列，執行時間為 O(n)

- 分成兩段區間（排除第一個與排除最後一個），總共仍是 O(n)

### ✅ 空間複雜度：

- 若使用 完整 dp 陣列寫法：O(n)

- 若使用 空間優化版（只用兩個變數）：O(1)

---

## ✍️ 我學到的東西 | What I Learned

- 遇圓形／首尾相接問題時，可以拆成多個線性情境來解

- 常數空間優化 DP：用兩個變數代替整個 dp 陣列

- 子問題複用：兩個子情境共用同一段 DP 邏輯

- 特殊情況處理很重要：空陣列、一棟房子的情況要先處理