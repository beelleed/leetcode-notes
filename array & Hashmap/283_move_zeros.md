# 🔄 LeetCode 283 — Move Zeroes / 移動零
🔗 [題目連結](https://leetcode.com/problems/move-zeroes/)


---

## 📄 題目說明 | Problem Description

**中文**  
給定一個整數陣列 `nums`，請你 **就地（in‑place）** 將所有 `0` 移到陣列的末尾，同時保持其他非零元素的相對順序不變。你必須做到不使用額外的陣列（空間複雜度 O(1)）。

**English**  
Given an integer array `nums`, move all `0`s to the end of the array in-place while maintaining the relative order of the non-zero elements. Do not use extra space for another array (i.e. space complexity must be O(1)).

**Examples**
- Example 1:

    - Input: nums = [0,1,0,3,12]
    - Output: [1,3,12,0,0]

- Example 2:

    - Input: nums = [0]
    - Output: [0]

---

## 🧠 解法思路 | Solution Idea

這題是非常典型的 **雙指標（two pointers）** 技巧：

- 使用 `left` 指向目前“要放下個非零元素”的位置。
- 使用 `right` 從 0 遍歷整個陣列。
- 每當你遇到 `nums[right] != 0` 時，你就把它交換到 `nums[left]`（可能是它自己或一個之前的 0 的位置），並 `left += 1`。
- 最後所有非零元素已被向前移動，剩餘的位置自然都是 0（因為交換過程中把零慢慢往後移）。

這種方法只要遍歷一次就可以完成，且是就地操作。

---

## 💻 程式碼

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        # 函式沒有 return，因為是原地修改 nums
```
```python
left = 0
```
- left 指向下一個應該被填入非零元素的位置。

```python
for right in range(len(nums)):
```
- right 走訪整個陣列索引。

```python
if nums[right] != 0:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
```
- 當 nums[right] 是非零元素時：

    1. 交換 nums[right] 和 nums[left] 的值，把這個非零元素往前移到 left 的位置。

    2. left += 1，準備下一個非零值應該被放的位置。

（若 right == left，交換其實不會改變陣列，這樣也涵蓋在同樣的邏輯中。）

- 如果 nums[right] == 0，就跳過，繼續往右。

```python
# 函式沒有 return，因為是原地修改 nums
```
- 此題是 in-place，函式不需回傳值，直接修改 nums 即可。

---

## 🧪 範例演算
- 假設：
    - nums = [0,1,0,3,12]

        - 初始：left = 0

        - right = 0 → nums[0] = 0 → 跳過

        - right = 1 → nums[1] = 1 != 0 → 交換 nums[0] 和 nums[1] → → [1,0,0,3,12] → left = 1

        - right = 2 → nums[2] = 0 → 跳過

        - right = 3 → nums[3] = 3 != 0 → 交換 nums[1] 與 nums[3] → → [1,3,0,0,12] → left = 2

        - right = 4 → nums[4] = 12 != 0 → 交換 nums[2] 與 nums[4] → → [1,3,12,0,0] → left = 3

- 最終結果：[1,3,12,0,0]，非零元素保持順序，零被移至最後。

---

## ⏱ 複雜度分析
- 時間複雜度：O(n)，只遍歷一次陣列

- 空間複雜度：O(1)，只用常數個指標變數

---

## ✍ 我學到了什麼 / What I Learned
- 雙指標交換法是許多 in-place 陣列操作題的通用技巧。

- 即使遇到零很多的情況，這種方法也能穩定地把非零往前移，不需要後續額外填充。

- 要注意如果 right == left 的時候交換其實就是原地交換，不會破壞原本的數字。

- 題目要求「保持非零元素順序」這一點是用交換法可以自然滿足的。