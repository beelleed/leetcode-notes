# 🔍 LeetCode 217 – Contains Duplicate
🔗 題目連結：[https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

---

## 📄 題目說明 | Problem Description

**中文**：

給定整數陣列 `nums`，如果陣列中有任何值至少出現兩次，就回傳 `true`；如果所有元素都互不相同，回傳 `false`。  

**English**: 

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Examples
- Example 1:

    - Input: nums = [1,2,3,1]

    - Output: true

    - Explanation: The element 1 occurs at the indices 0 and 3.

- Example 2:

    - Input: nums = [1,2,3,4]

    - Output: false

    - Explanation: All elements are distinct.

- Example 3:

    - Input: nums = [1,1,1,3,3,4,3,2,4,2]

    - Output: true

---

## 🧠 解題思路 | Solution Idea

有幾種常見解法：

1. **用 Set（雜湊集合）檢查重複**  
   - 建立一個空 set `seen`。  
   - 遍歷 `nums` 的每個元素 `num`：  
     - 如果 `num` 已經在 `seen` 中 → 有重複 → 回傳 `true`。  
     - 否則把 `num` 加進 `seen`。  
   - 最後如果遍歷完都沒重複 → 回傳 `false`。

2. **比較陣列長度與 set 的長度**（簡潔版本）  
   - 若 `len(nums)` 與 `len(set(nums))` 不相等 → 代表有重複 → 回傳 `true`，否則 `false`。

3. **排序後檢查相鄰元素**  
   - 對 `nums` 排序後，以線性方式檢查每對相鄰的元素是否相同；如果有相同的就回傳 `true`。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```
```python
seen = set()
```
- 初始化一個空集合 seen：用來儲存遍歷過的數字。
```python
for num in nums:
```
- 遍歷 nums 陣列中的每個數字 num。
```python
if num in seen:
    return True
```
- 如果 num 已經在集合 seen 裡，代表這個數字出現過 → 有重複 → 回傳 True。
```python
seen.add(num)
```
- 否則，這是第一次看到這個數字，把它加入 seen 中。
```python
return False
```
- 如果整個陣列都檢查完沒有發現重複，回傳 False。

---

## 🧪 範例示範 | Example 

- 範例 1：
```ini
nums = [1, 2, 3, 1]
```
流程：
| 步驟 | seen 狀態 | 處理元素 `num` | 判斷                              |
| -- | ------- | ---------- | ------------------------------- |
| 初始 | {}      | 1          | 1 不在 seen → 加入 → seen = {1}     |
|    | {1}     | 2          | 2 不在 seen → 加入 → seen = {1,2}   |
|    | {1,2}   | 3          | 3 不在 seen → 加入 → seen = {1,2,3} |
|    | {1,2,3} | 1          | 1 已在 seen → 回傳 `True`           |

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類          | 複雜度                                         |
| ----------- | ------------------------------------------- |
| 時間複雜度 Time  | **O(n)**，其中 n 是陣列長度。每個元素最多進行一次 set 查詢與插入操作。 |
| 空間複雜度 Space | **O(n)**，最壞情況下 set 會存所有不同的元素。               |

---

## ✍️ 我學到了什麼 | What I Learned

- 使用 set 可以有效率地檢查重複，比暴力比較每對元素好很多。

- len(nums) != len(set(nums)) 是一個簡潔寫法，但會消耗額外空間來建立 set。

- 在面試中要注意邊界條件，例如空陣列或只有一個元素的情況，也測試這樣的 case。