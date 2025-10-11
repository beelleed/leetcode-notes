# 🔢 LeetCode 26 — Remove Duplicates from Sorted Array / 刪除排序陣列中的重複項目
🔗 [題目連結](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 📄 題目說明 | Problem Description

**中文**：給定一個排序過的整數陣列 `nums`，請「**就地（in-place）**」刪除重複項，使得每個元素只出現一次，並回傳新的陣列長度 `k`。你**不得使用額外陣列空間**。  
最終，前 `k` 個元素會是刪除重複項後的結果。

**English**: Given a sorted array `nums`, remove the duplicates **in-place** such that each element appears only once and return the new length `k`. Do not allocate extra space for another array. You must do this with O(1) extra memory.

**Examples**
- Example 1:

    - Input: nums = [1,1,2]
    - Output: 2, nums = [1,2,_]
    - Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).


- Example 2:

    - Input: nums = [0,0,1,1,1,2,2,3,3,4]
    - Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    - Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
 

---

## 🧠 解題思路 | Solution Idea

由於陣列已經「**排序**」，我們只需確保：
- 每當遇到 **不同的數字** 時，就放到 `nums` 陣列的下一個位置。

### 👣 使用雙指標 Two Pointers
- 使用兩個指標：
  - `left` 指向目前有效序列的尾端
  - `right` 從第 1 個元素開始掃描整個陣列

- 若 `nums[right] != nums[left]`，表示是新元素：
  - 將 `nums[right]` 放到 `left+1` 的位置
  - 更新 `left += 1`

- 結束時，`left + 1` 就是有效的長度。

---

## 💻 程式碼

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1
```
```python
if not nums:
    return 0
```

- 如果陣列是空的，直接回傳 0。
```python
left = 0
```

- 初始化指標 left，指向目前不重複序列的尾端。
```python
for right in range(1, len(nums)):
```

- 用 right 從第 1 個元素開始遍歷陣列。
```python
    if nums[left] != nums[right]:
        left += 1
        nums[left] = nums[right]
```

- 若遇到不同的數字，就把它寫入下一個有效位置 left + 1，並更新 left。
```python
return left + 1
```

- 回傳不重複元素的數量（索引從 0 開始，所以要加 1）。

---

## 🧪 根據程式碼的範例
- Input：
```python
nums = [0,0,1,1,1,2,2,3,3,4]
```
- 執行過程：

    - 初始：left = 0

    - right=1：nums[1] = 0 == nums[0] → 跳過

    - right=2：nums[2] = 1 != nums[0] → left = 1, nums[1] = 1

    - right=3：nums[3] = 1 == nums[1] → 跳過

    - right=5：nums[5] = 2 != nums[2] → left = 2, nums[2] = 2

    - 依此類推

- 最終結果：

    - nums[:5] = [0, 1, 2, 3, 4]

    - 回傳 5

---

## ⏱ 複雜度分析

- 時間複雜度：O(n)，只掃描一次陣列

- 空間複雜度：O(1)，只用了常數個變數

---

## ✍️ 我學到的東西 | What I Learned

- 排序陣列的特性（重複元素會集中）減少了搜尋成本

- 雙指標技巧 (two pointers) 很適合做 in-place 的資料壓縮 / 重組

- 題目要求 “in-place” 是常見面試點，要注意不要創造新陣列

- 寫程式時要嚴謹處理邊界（空陣列、全重複、無重複等狀況）