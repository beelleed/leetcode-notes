# 🧩 LeetCode 34 — Find First and Last Position of Element in Sorted Array  

🔗 [題目連結](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

## 📘 Problem Description | 題目描述

### English
Given an **ascending sorted** array of integers `nums` and a target value `target`,  
return the **starting and ending positions** of `target` in `nums`.

If `target` is not found in the array, return `[-1, -1]`.

### 中文
給定一個**升序排列的整數陣列 `nums`** 和一個整數 `target`，  
找出 `target` 在陣列中出現的「第一個位置」和「最後一個位置」。  
若找不到 `target`，回傳 `[-1, -1]`。

### Examples
- Example 1:
    - Input: nums = [5,7,7,8,8,10], target = 8
    - Output: [3,4]

- Example 2:

    - Input: nums = [5,7,7,8,8,10], target = 6
    - Output: [-1,-1]

- Example 3:

    - Input: nums = [], target = 0
    - Output: [-1,-1]

---

## 🧠 解題思路 | Solution Idea

- 因為陣列是排序過的，可以用 **二分搜尋** 來加速查找。
- 不只是找到一個 `target`，而是要找到最左與最右的位置，因此可以做兩種變體的 binary search：
  1. 找 **第一個出現**（first occurrence, lower bound）：遇到 `nums[mid] == target` 時不返回，而是繼續在左半邊找（把 `right = mid - 1`）。
  2. 找 **最後一個出現**（last occurrence, upper bound）：遇到相等時，把 `left = mid + 1`，繼續往右找。
- 最終把這兩個結果合併成 `[first, last]`。如果第一個為 -1，代表根本不存在 `target`，直接回傳 `[-1, -1]`。

---

## 💻 完整程式碼 | Code (Python)

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst() -> int:
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_pos = mid
                    right = mid - 1  # 繼續向左搜尋
            return first_pos

        def findLast() -> int:
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last_pos = mid
                    left = mid + 1  # 繼續向右搜尋
            return last_pos

        first = findFirst()
        if first == -1:
            return [-1, -1]
        last = findLast()
        return [first, last]
```
### 🔍 找第一個出現的位置（左邊界）
```python
def findFirst() -> int:
    left, right = 0, len(nums) - 1
    first_pos = -1
```
- 初始化二分搜尋範圍 left 和 right。

- first_pos 用來記錄找到的第一個出現位置。

```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        first_pos = mid
        right = mid - 1 # 繼續往左邊找
```
- 如果 nums[mid] == target，先記錄下來，但還不能停，還要繼續找左邊有沒有更早出現的。

- 所以向左縮範圍（right = mid - 1）。
```python
return first_pos
```
- 回傳找到的第一個出現索引（或沒找到就是 -1）。

### 🔍 找最後一個出現的位置（右邊界）
```python
def findLast() -> int:
    left, right = 0, len(nums) - 1
    last_pos = -1
```
- def findLast() -> int:
    left, right = 0, len(nums) - 1
    last_pos = -1

```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        last_pos = mid
        left = mid + 1 # 繼續往右邊找
```
- 如果找到相等，先記錄下來，然後繼續向右搜尋，確認是不是還有更晚的出現。
```python
return last_pos
```
- 回傳最後一個出現的索引（或 -1）

### 🔚 回傳最終結果
```python
first = findFirst()
if first == -1:
    return [-1, -1]
last = findLast()
return [first, last]
```
- 如果第一個出現是 -1，代表整個陣列裡根本沒有 target。

- 否則，就回傳 [first, last]。

---

## 🧪 範例流程 | Example Walkthrough

假設：
```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
```
### 找第一個位置（findFirst）
| left         | right | mid | nums[mid] vs target | 更新                                         |
| ------------ | ----- | --- | ------------------- | ------------------------------------------ |
| 0            | 5     | 2   | nums[2]=7 < 8       | left = mid + 1 = 3                         |
| 3            | 5     | 4   | nums[4]=8 == target | first_pos = 4；繼續搜左半邊 → right = mid - 1 = 3 |
| 3            | 3     | 3   | nums[3]=8 == target | first_pos = 3；right = mid - 1 = 2 → 結束迴圈   |
| 結果：first = 3 |       |     |                     |                                            |

結果：first = 3

### 找最後一個位置（findLast）

| left        | right | mid | nums[mid] vs target | 更新                              |
| ----------- | ----- | --- | ------------------- | ------------------------------- |
| 0           | 5     | 2   | 7 < 8               | left = 3                        |
| 3           | 5     | 4   | 8 == target         | last_pos = 4；left = mid + 1 = 5 |
| 5           | 5     | 5   | nums[5] = 10 > 8    | right = mid - 1 = 4 → 結束        |
| 結果：last = 4 |       |     |                     |                                 |

結果：last = 4				

最終回傳 [3, 4]

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(log n) + O(log n) = O(log n)，因為做兩次 binary search。

- 空間複雜度：O(1)，只使用常數級額外變數。