# 🔍 LeetCode 2187 – Minimum Time to Complete Trips

[題目連結](https://leetcode.com/problems/minimum-time-to-complete-trips/)

## 📘 題目說明 | Problem Description
### 中文：

給定一個整數陣列 time，其中 time[i] 代表第 i 台車完成 一趟 所需的時間。
所有車可以 同時、無限次 地跑。

請你找出完成 至少 totalTrips 趟 所需的 最短時間。

### English:

You are given an array time where time[i] represents the time required for the i-th bus to complete one trip.
Each bus can make multiple trips sequentially.

Return the minimum time required so that the total number of trips completed by all buses is at least totalTrips.

### Examples

- Example 1:

    - Input: time = [1,2,3], totalTrips = 5

    - Output: 3

- Example 2:

    - Input: time = [2], totalTrips = 1

    - Output: 2

## 💡 解題思路 | Solution Idea

- 答案是「時間 t」

- 在時間 t 內：

    - 第 i 台車可以完成 t // time[i] 趟

- 總趟數：
    ```python
    sum(t // time[i])
    ```
### 為什麼可以用 Binary Search？

- 時間 t 越大 → 能完成的總趟數 越多

- 這是一個 單調遞增（Monotonic） 的函數

- 問題變成：

    - 找 最小的 t，使 sum(t // time[i]) >= totalTrips

👉 這就是 Binary Search on Answer

## 🧠 二分搜尋設計 | Binary Search Design
- 搜尋範圍

    - 下界：lo = 1

    - 上界：
    ```python
    hi = min(time) * totalTrips
    ```

    最快的車一直跑，一定能完成

## 🧾 程式碼 | Python Code
```python
from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2

            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    break

            if trips >= totalTrips:
                right = mid   # mid 可行，嘗試更小時間
            else:
                left = mid + 1  # mid 不夠，時間要變大

        return left
```
### 🔍 程式逐行解析 | Step-by-Step Explanation
```python
left, right = 1, min(time) * totalTrips
```

- 搜尋時間範圍

- right 一定足夠完成所有 trips
```python
while left < right:
    mid = (left + right) // 2
```

- 標準 binary search

- mid = 嘗試的完成時間
```python
trips = 0
for t in time:
    trips += mid // t
```

- 計算在 mid 時間內：

    - 每台車能跑幾趟

    - 累加總趟數
```python
if trips >= totalTrips:
    right = mid
```

- mid 時間 已經夠

- 嘗試找更小的時間（往左）
```python
else:
    left = mid + 1
```

- mid 不夠

- 時間一定要變大（往右）
```python
return left
```

- 當 left == right

- 找到 最小可行時間

## 🔍 範例解析 | Example Walkthrough
### Input
```python
time = [1,2,3]
totalTrips = 5
```
### Binary Search 過程
| left | right | mid | trips(mid) | 動作             |
| ---- | ----- | --- | ---------- | -------------- |
| 1    | 5     | 3   | 3+1+1 = 5  | 可行 → right = 3 |
| 1    | 3     | 2   | 2+1+0 = 3  | 不夠 → left = 3  |


➡️ left == right == 3

✅ 最小時間 = 3

## ⏱ 複雜度分析 | Time & Space Complexity
| 項目    | 複雜度                                           |
| ----- | --------------------------------------------- |
| 時間複雜度 | `O(n log M)`
`M = min(time) * totalTrips` |
| 空間複雜度 | `O(1)`                                        |

## 🧠 模板 
1️⃣ 答案是「時間」→ Binary Search on Answer

2️⃣ check(mid): sum(mid // time[i]) >= totalTrips

3️⃣ 可行 → 往左

4️⃣ 不可行 → 往右

5️⃣ hi = min(time) * totalTrips

## 📚 我學到了什麼 | What I Learned

- 這題不是排程題，而是 單調函數 + 二分答案

- 「完成幾趟」是典型的 t // cost
