# 🔍 LeetCode 704 – Binary Search

---

## 📄 題目說明 | Problem Description

- **中文**：給你一個按遞增順序排序好的整數陣列 `nums`，還有一個整數 `target`。如果 `target` 存在於陣列中，就回傳它的索引；不在的話回傳 `-1`。要求時間複雜度為 **O(log n)**。  
- **English**: Given a sorted array of integers `nums` (in ascending order) and an integer `target`, return the index of `target` in `nums` if it exists, otherwise return `-1`. The algorithm must run in **O(log n)** time.

---

## 🧠 解題思路 | Solution Idea

這題是一個經典的 **Binary Search（二分搜尋）** 問題。因為陣列已經排好序，所以可以：

1. 設立兩個指標 `left` 和 `right` 指向陣列的兩端（最左／最右位置）。  
2. 每次取中間位置 `mid = (left + right) // 2`。  
3. 若 `nums[mid]` 正好等於 `target` → 找到 → 回傳 `mid`。  
4. 如果 `nums[mid]` 比 `target` 小 → 目標在右半邊，所以把 `left = mid + 1`。  
5. 如果 `nums[mid]` 比 `target` 大 → 目標在左半邊，所以把 `right = mid - 1`。  
6. 重複以上步驟直到 `left > right`，代表走完都沒找到，回傳 `-1`。

這樣每次把搜尋空間砍一半，時間複雜度為 O(log n)。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```
### ✅ 初始化左右指標
```python
left, right = 0, len(nums) - 1
```
- left 是指向陣列開頭的指標（索引 0）。

- right 是指向陣列結尾的指標（索引 len(nums) - 1）。

- 二分搜尋的策略是：「每次查中間的元素，根據它與 target 的關係，決定往哪一半繼續查找」。

### 🔁 開始迴圈搜尋
```python
while left <= right:
```
- 只要 left <= right，代表還有搜尋區間，就繼續執行。

- 如果 left > right，代表已經搜尋完畢，都沒找到 → 跳出迴圈。
### 🧮 計算中間位置
```python
mid = (left + right) // 2
```
- mid 是當前搜尋區間的中間位置。

- 使用整數除法 // 來取整數索引。
### 🎯 判斷中間值與 target 的關係
```python
if nums[mid] == target:
    return mid
```
- 若找到目標數字，直接回傳該索引 mid。
### 📈 若中間值太小 → 查右半邊
```python
elif nums[mid] < target:
    left = mid + 1
```
- nums[mid] < target 表示 target 一定在 mid 的右邊。

- 所以把搜尋區間左界移到 mid + 1。

### 📉 若中間值太大 → 查左半邊
```python
else:
    right = mid - 1
```
- nums[mid] > target 表示 target 一定在 mid 的左邊。

- 所以把搜尋區間右界移到 mid - 1。

### ❌ 最後都沒找到
```python
return -1
```
- 如果跳出 while 迴圈代表搜尋完所有可能位置都沒找到 → 回傳 -1。

---

## 🔍 範例
```ini
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```
| 步驟    | left     | right     | mid                | nums\[mid]   | 判斷                   | 更新 left/right       | 有沒有回傳 |
| ----- | -------- | --------- | ------------------ | ------------ | -------------------- | ------------------- | ----- |
| 初始化   | 0        | 5         | —                  | —            | —                    | left = 0, right = 5 | —     |
| 第一次迴圈 | 0        | 5         | mid = (0+5)//2 = 2 | nums\[2] = 3 | 3 < 9                | left = mid + 1 = 3  | —     |
| 第二次   | left = 3 | right = 5 | mid = (3+5)//2 = 4 | nums\[4] = 9 | nums\[mid] == target | 回傳 mid = 4          | ✅     |

### ✅ 結果

這個範例中程式會回傳 4，因為 nums[4] 是 9。

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類          | 複雜度                                                  |
| ----------- | ---------------------------------------------------- |
| 時間複雜度 Time  | **O(log n)** —— 每一步都把搜尋範圍折半。                         |
| 空間複雜度 Space | **O(1)** —— 用常數個變數 left, right, mid，不用額外隨 n 成長的資料結構。 |

---

## ✍️ 我學到了什麼 | What I Learned

- 排序陣列 + 二分搜尋是很多問題的基礎技巧。當看到 “sorted array” + “查找” 時二分搜索通常是第一選擇。

- 小心邊界條件：left <= right 的判斷、mid 計算、更新 left 或 right 的時候不漏掉 +1 或 −1。

- 如果 target 不在陣列中，一定要回傳 -1。

- 面試中講這題時，可以先講 brute force（O(n)）比較，再講為什麼 binary search 更快（log n）。