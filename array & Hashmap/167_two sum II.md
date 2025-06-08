# Leetcode 167 - Two Sum II (Input Array Is Sorted)

## 題目說明 | Problem Description
- 中文: 給定一個已排序（遞增）的整數陣列 `numbers`，找出兩個數，使它們的總和為 `target`，回傳這兩個數字的index（從 1 開始）。
- English: Given a sorted (increasing order) array of integers `numbers`, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-based index).
---

## 方法一：Hash Map 解法（O(n) 時間，O(n) 空間）

### 思路：
- 中文: 利用 Hash Map 儲存數字和對應的 index。每當遇到一個數字 `num`，就檢查 `target - num` 是否已存在於 map 中。
- English: Use a hash map to store the number and its index. For each number, check if target - num exists in the map. 

### 程式碼：
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement] + 1, i + 1]  # 回傳 1-indexed
            hashmap[num] = i
```
## 注意
- return numbers[left] + 1, numbers[right] + 1 回傳的是「值 + 1」，不是「索引 + 1」

- 題目要的是 1-indexed 的索引值

- 如果回傳 a, b，回傳的是 tuple，應改為 return [a, b] 才是 List[int]

特點：
- 適合任意陣列（不一定排序）

- 額外空間需求為 O(n)
---
## 方法二：雙指標解法（最佳解，O(n) 時間，O(1) 空間）
## 思路：
- 由於輸入已排序，可以使用兩個指標 left 與 right：
  Since the array is sorted, use two pointers left and right:

    1. 若兩數之和 < target，左指標右移
       If sum < target → move left right

    2. 若兩數之和 > target，右指標左移
       If sum > target → move right left

    3. 若兩數之和 = target，回傳索引
       If equal → return indices
       
```python

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 回傳 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1
```
## 雙指標（Two Pointers）解法的核心
left, right = 0, len(numbers) - 1

🔍 詳解：
| 變數      | 設定值              | 意思                             |
| ------- | ---------------- | ------------------------------ |
| `left`  | `0`              | 從陣列「最左邊」開始（第一個數）               |
| `right` | `len(numbers)-1` | 從陣列「最右邊」開始（最後一個數，因為 index 從 0） |

特點：
- 完全不需要額外空間

- 利用「已排序」這個特性 → 空間最優解

---

## 比較總結：
| 方法 / Method       | 時間複雜度 / Time | 空間複雜度 / Space | 是否利用排序 / Uses Sorting | 回傳正確性 / Return Type |
| ----------------- | ------------ | ------------- | --------------------- | ------------------- |
| Hash Map          | O(n)         | O(n)          | ❌                     | ✅                   |
| 雙指標 / Two-Pointer | O(n)         | O(1) ✅        | ✅                     | ✅（最佳 / Best）        |


--- 

## ✅ Leetcode 1 & 167 這兩題的共同點：

- 都是找「兩個數字的和等於 target」

- 回傳的是那兩個數的索引（題目通常要求從 1 開始算）

- 本質上都是要解一個「兩數和」問題

🚨 核心差別：

| 比較項目                | Leetcode 1：Two Sum | Leetcode 167：Two Sum II |
| ------------------- | ------------------ | ----------------------- |
| **輸入是否排序？**         | ❌ 無排序              | ✅ 已排序（遞增）               |
| **是否可以用 hash map？** | ✅ 適合用 hash map     | ✅ 可以，但不是最佳方法            |
| **最佳解法**            | hash map（O(n)）     | 雙指標 two pointers（O(n)）  |
| **可否用雙指標？**         | ❌ 不行（因為沒排序）        | ✅ 可以（因為有序）              |
| **空間複雜度**           | O(n)               | O(1)（用雙指標就不需要額外空間）      |

## 🧠 總結：
- Leetcode 1：無排序，用 hash map

- Leetcode 167：有排序，用雙指標更好