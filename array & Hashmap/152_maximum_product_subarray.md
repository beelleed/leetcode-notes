# 📘 LeetCode 152 — Maximum Product Subarray / 最大乘積子陣列
🔗 [題目連結](https://leetcode.com/problems/maximum-product-subarray)

---

## 🧩 題目說明 | Problem Description
### 中文
給你一個整數陣列 nums，找出其中一個連續非空子陣列，使得這個子陣列所有元素乘起來的值最大，返回這個最大值。

### English
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return that product.

### Examples
- Example 1:

    - Input: nums = [2,3,-2,4]
    - Output: 6
    - Explanation: [2,3] has the largest product 6.

- Example 2:

    - Input: nums = [-2,0,-1]
    - Output: 0
    - Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

---

## 🧠 解題思路 | Solution Idea 
- 我們維護兩個變數：max_ending_here 表示到目前為止（以第 i 個元素作結尾的子陣列）能取到的最大乘積；min_ending_here 表示以第 i 元素作結尾的最小乘積（因為最小乘積乘上一個負數有可能變成最大）。

- 初始：max_ending_here = min_ending_here = nums[0]，全局答案 ans = nums[0]。

- 對於每個 nums[i]，我們有三種可能性：

    1. 單獨用 nums[i] 新開始一個子陣列

    2. 延續前一個最大乘積 * nums[i]

    3. 延續前一個最小乘積 * nums[i]（因為前一最小可能為負，乘上負 nums[i] 變正）

- 因此新的 max_ending_here = max(nums[i], max_ending_here * nums[i], min_ending_here * nums[i])

- 新的 min_ending_here = min(nums[i], max_old * nums[i], min_ending_here * nums[i])

- 更新 ans = max(ans, max_ending_here)

- 最後回傳 ans

這樣能在一次掃描中處理正負與 0 的情況。

---

## 💻 程式碼範例（Python）
```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化：以第一個元素為起點
        max_ending = nums[0]
        min_ending = nums[0]
        ans = nums[0]

        # 從第二個元素開始遍歷
        for i in range(1, len(nums)):
            x = nums[i]
            # 暫存上一輪的 max_ending（因為更新 min_ending 時會用到它）
            prev_max = max_ending
            prev_min = min_ending

            # 更新 max_ending、min_ending
            max_ending = max(x, prev_max * x, prev_min * x)
            min_ending = min(x, prev_max * x, prev_min * x)

            # 更新全域答案
            ans = max(ans, max_ending)

        return ans
```
### 🔹 第 1 段：初始化變數
```python
max_ending = nums[0]
min_ending = nums[0]
ans = nums[0]
```
- max_ending: 到目前為止，以 nums[i] 結尾的最大乘積

- min_ending: 到目前為止，以 nums[i] 結尾的最小乘積

    - 因為負數乘負數會變正，所以也要保留最小值

- ans: 用來記錄全域最大乘積

### 🔹 第 2 段：開始遍歷陣列（從第 2 個元素開始）
```python
for i in range(1, len(nums)):
    x = nums[i]
```
- 對每個 nums[i] 進行考慮

- 為什麼從 index 1 開始？因為 index 0 在初始化時已經處理過了

### 🔹 第 3 段：先儲存舊值，避免更新後互相影響
```python
prev_max = max_ending
prev_min = min_ending
```
- 接下來 max_ending 和 min_ending 要同時更新

- 需要先把之前的值保留，才能分別代入 max 和 min 的公式中

### 🔹 第 4 段：更新目前位置結尾的最大/最小乘積
```python
max_ending = max(x, prev_max * x, prev_min * x)
min_ending = min(x, prev_max * x, prev_min * x)
```
- 有三種情況需要考慮：

    1. 單獨取 x 當作新的開始

    2. 把 x 接在前一個最大乘積之後（可能仍然是正數）

    3. 把 x 接在前一個最小乘積之後（可能是負數 * 負數 → 正）

這段是整個演算法的核心邏輯。

### 🔹 第 5 段：更新最終答案
```python
ans = max(ans, max_ending)
```
- 每次更新目前的 max_ending 後，就檢查是否需要更新整體最大乘積
### 🔹 第 6 段：回傳最終結果
```python
return ans
```
### 🔍 補充小結
| 變數           | 意義                     |
| ------------ | ---------------------- |
| `max_ending` | 以 `nums[i]` 結尾的最大乘積子陣列 |
| `min_ending` | 以 `nums[i]` 結尾的最小乘積子陣列 |
| `ans`        | 全陣列中所有子陣列中的最大乘積        |

---

## 🧪 範例 | Example：nums = [2, 3, -2, 4]
### ✅ 初始狀態
```python
max_ending = 2
min_ending = 2
ans = 2
```
### 🔁 i = 1 → x = 3
```python
prev_max = 2
prev_min = 2
max_ending = max(3, 2*3, 2*3) = max(3, 6, 6) = 6
min_ending = min(3, 2*3, 2*3) = min(3, 6, 6) = 3
ans = max(2, 6) = 6
```
### 🔁 i = 2 → x = -2
```python
prev_max = 6
prev_min = 3
max_ending = max(-2, 6*(-2), 3*(-2)) = max(-2, -12, -6) = -2
min_ending = min(-2, 6*(-2), 3*(-2)) = min(-2, -12, -6) = -12
ans = max(6, -2) = 6
```
### 🔁 i = 3 → x = 4
```python
prev_max = -2
prev_min = -12
max_ending = max(4, -2*4, -12*4) = max(4, -8, -48) = 4
min_ending = min(4, -2*4, -12*4) = min(4, -8, -48) = -48
ans = max(6, 4) = 6
```
### ✅ 最終輸出
```python
return ans = 6
```

最大乘積子陣列是 [2, 3]，乘積為 6。

---

## 📊 複雜度分析 | Complexity

- 時間複雜度：O(n)，只掃描一次陣列

- 空間複雜度：O(1)，只使用常數個變數（不額外開陣列）

---

## ✅ 我學到什麼 / What I Learned

- 在處理乘積這樣含有負數的情況時，不能只追蹤最大，需要同時追蹤最小，因為負 × 負可能變正。

- 更新時的順序要小心：用原先的 max/min 去算新的值，不能互相覆蓋。

- 這題是經典「在一次掃描中維持多種狀態」的例子，型態與 Kadane 演算法類似，但多了一層負數翻轉的挑戰。
