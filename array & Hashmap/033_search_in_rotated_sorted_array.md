# 🔍 LeetCode 33 – Search in Rotated Sorted Array

## 📘 題目說明 | Problem Description

### 中文：
給定一個原本升序排列但經過旋轉的整數陣列 `nums`（元素互不相同），以及一個目標值 `target`，請你在 `nums` 中找出目標值的索引，若不存在則回傳 `-1`。

要求：時間複雜度為 `O(log n)`。

### English:
You are given an integer array `nums` sorted in ascending order, but rotated at an unknown pivot. Given a target value, return its index if found in `nums`, otherwise return `-1`.  
Must run in `O(log n)` time.

---

## 💡 解題思路 | Solution Idea

- 雖然整個陣列是旋轉過的，但它仍然**部分有序**。
- 可透過 **二分搜尋 (Binary Search)** 方式，在「有序的那一半」繼續搜尋。
- 每次計算中間點 `mid`：
  - 如果 `nums[mid]` 剛好是 `target`，直接回傳。
  - 否則根據左半或右半是否有序，決定下一步搜尋哪一段。

---

## 🧾 程式碼 | Python Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 左半邊是有序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左半邊繼續找
                else:
                    left = mid + 1   # 在右半邊找
            # 右半邊是有序的
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右半邊找
                else:
                    right = mid - 1  # 在左半邊找

        return -1
```

### 🔍 程式逐行解析 | Step-by-Step Explanation
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 初始化左右指標
```
- Set left and right pointers to the beginning and end of the array.
```python
while left <= right:
    mid = (left + right) // 2
```
- Loop while left ≤ right, calculating mid each iteration.
```python
if nums[mid] == target:
    return mid
```
- If nums[mid] equals target, return immediately.
```python
if nums[left] <= target < nums[mid]:
    right = mid - 1
else:
    left = mid + 1
```
- If the left segment (nums[left] → nums[mid]) is sorted:

    - And if target lies between those endpoints, search left half.

    - Else, search right half.
```python
else:
    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```
- Otherwise, the right segment (nums[mid] → nums[right]) must be sorted:

    - If target lies there, search right; else search left.
```python
return -1
```
- If the loop ends, target isn't in the array.

---

## 🔍 範例解析 | Example
```python
nums = [4,5,6,7,0,1,2]
target = 5
```
初始化：
```python
left = 0, right = 6 → mid = 3 → nums[mid] = 7
```
- 左半段 nums[0:4] = [4,5,6,7] 是有序的

- target = 5 確實在這段內（4 ≤ 5 < 7）

👉 所以接下來只要搜尋 [4,5,6]

那就設定：
```python
right = mid - 1 = 2
```
下一輪範圍是 left = 0, right = 2，mid = 1 → 找到 5！

✅ 小總結：
| 如果發現...           | 搜尋方向              | 為什麼               |
| ----------------- | ----------------- | ----------------- |
| `target` 在左半段（有序） | `right = mid - 1` | 去掉 `mid` 與右側，往左邊找 |
| `target` 在右半段（有序） | `left = mid + 1`  | 去掉 `mid` 與左側，往右邊找 |

這就是標準 二分搜尋的區間更新方式。

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 項目    | 複雜度        |
| ----- | ---------- |
| 時間複雜度 | `O(log n)` |
| 空間複雜度 | `O(1)`     |

---

## 📚 我學到了什麼 | What I Learned

- 即使資料不是完全有序，仍能透過「局部有序判斷」來進行二分搜尋。

- 旋轉排序陣列是許多進階搜尋題目的核心技巧。

- 要善用條件 nums[left] <= nums[mid] 來判斷哪一段是有序的。