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

        def rob_range(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end + 1):
                new = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, new
            return prev1
        return max(rob_range(0, n - 2), rob_range(1, n - 1))
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
def rob_range(start, end):
    prev1, prev2 = 0, 0
    for i in range(start, end + 1):
        new = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, new
    return prev1
```
- 這是 線性版本的打家劫舍（與 LeetCode 198 題相同）：

    - prev1 表示「到目前位置（包括前一房子）能偷到的最大金額」

    - prev2 表示「到前前一個位置能偷到的最大金額」

    - 當我們考慮偷或不偷當前房子 x 時，

        - 不偷的話能拿到 prev1

        - 偷的話就是 prev2 + nums[i]

    - 所以 new = max(prev1, prev2 + nums[i])

    - 更新變數：把 prev1 給 prev2，然後新的值給 prev1

    - 最後回傳 prev1（代表整個線性段的最優解）

```python
return max(rob_range(0, n - 2), rob_range(1, n - 1))
```
- 把兩種情況下的最大收益取最大值即可

- 因為不能同時搶第一間和最後一間

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
        def rob_range(start: int, end: int) -> int:
            m = end - start + 1
            dp = [0] * (m + 1)
            dp[1] = nums[start]
            for i in range(2, m + 1):
                # nums[start + i - 1] 是第 i 間房子的實際值（因為 nums 是 0-based）
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i - 1])
            return dp[m]

        return max(rob_range(0, n - 2), rob_range(1, n - 1))
```
### 🧱 Step 1 - Edge Case 處理
```python
n = len(nums)
# 邊界處理
if n == 0:
    return 0
if n == 1:
    return nums[0]
```
- 如果 nums 是空的，就不能搶，回傳 0。

- 如果只有一間房子，就只能搶這一間。

### 🧱 Step 2 - 定義 rob_range() 子函式
```python
def rob_range(start: int, end: int) -> int:
    m = end - start + 1
    dp = [0] * (m + 1)
    dp[1] = nums[start]
```
- 這個函式負責處理一段連續的房子（不包含環狀限制）。

- 使用 1-based index 的 dp 陣列：dp[i] 表示搶到「第 i 間（相對位置）房子」的最大金額。

- dp[1] = nums[start]：第一間房子只能搶它自己。
### 🧱 Step 3 - 動態規劃遞推關係
```python
for i in range(2, m + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i - 1])
```
- 這是標準的 House Robber transition：

    - dp[i - 1]: 不搶當前房子，保留前面最大值。

    - dp[i - 2] + nums[start + i - 1]: 搶這一間，就不能搶上一間。

- 注意 nums[start + i - 1]：因為 nums 是 0-based，而 dp 是 1-based。

    - 在函式 rob_range(start, end) 中，我們定義一段從 nums[start] 到 nums[end] 的子區間，並建立一個新的 dp 陣列，長度為這段區間的長度 + 1，用來存放動態規劃的結果。

    - 💡 dp[i] 的含義是：表示搶到 第 i 間房子（從 start 開始算） 為止的最大金額。

    - 🔢 舉例說明：

        假設：

        ```python
        nums = [2, 3, 2]
        start = 1  # 對應房子是 3（index 1）
        end = 2    # 對應房子是 2（index 2）
        ```
        - 在 rob_range(1, 2) 中，我們會建立：
        ```python
        dp = [0, nums[1], ...]
        ```
        - 在第 i = 2 次迴圈中，我們要處理「實際上的第幾間房子」？

        - 因為 dp 是從 1 開始記錄（不是從 0），所以：
            ```python
            nums[start + i - 1]
            = nums[1 + 2 - 1]
            = nums[2]
            ```
        - ✔️ 正確對應到「實際上的第 i 間房子」。


### 🧱 Step 4 - 回傳最大值
```python
return dp[m]
```
- 最後一間（第 m 間）房子的 dp 值，就是這一段的最大獲利。

### 🧱 Step 5 - 主邏輯：比較兩種情況
```python
return max(rob_range(0, n - 2), rob_range(1, n - 1))
```
- 不能同時搶第一和最後一間，所以分兩種情況：

    1. 把第一間包含進來，最後一間不能搶 → rob_range(0, n - 2)

    2. 把最後一間包含進來，第一間不能搶 → rob_range(1, n - 1)

- 取兩者最大值為最終解。

---

## 🧪 範例

- nums = [2, 3, 2]

### 📘 1. rob_range(0, 1) → 處理 [2, 3]

- 對應房子：第 1 間、第 2 間（不能搶最後一間）

    - 初始化：
        - m = 2（範圍大小）
        - dp = [0, 2, 0] → dp[1] = nums[0] = 2

- 迴圈：

    - i = 2

        - dp[2] = max(dp[1], dp[0] + nums[1]) = max(2, 0 + 3) = 3

- 結果：dp = [0, 2, 3] → 回傳 dp[2] = 3

### 📘 2. rob_range(1, 2) → 處理 [3, 2]

- 對應房子：第 2 間、第 3 間（不能搶第一間）

    - 初始化：
        - m = 2
        - dp = [0, 3, 0] → dp[1] = nums[1] = 3

- 迴圈：

    - i = 2

        - dp[2] = max(dp[1], dp[0] + nums[2]) = max(3, 0 + 2) = 3

- 結果：dp = [0, 3, 3] → 回傳 dp[2] = 3

### ✅ 最終結果：
```python
max(rob_range(0, 1), rob_range(1, 2)) = max(3, 3) = 3
```
所以答案是 3。

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