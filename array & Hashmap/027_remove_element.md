# 🗑️ LeetCode 27 — Remove Element / 移除元素（兩種 in‑place 方法）
🔗 [題目連結](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 📄 題目說明 | Problem Description

**中文**  
給定一個整數陣列 `nums` 和一個整數 `val`，請你 **就地（in‑place）** 移除所有值等於 `val` 的元素，並返回剩下元素的個數 `k`。  
你必須在不使用額外空間的情況下完成，也就是空間複雜度為 \(O(1)\)。剩下的前 `k` 個元素可以是任意順序（題目不要求排序）。

**English**  
Given an integer array `nums` and a value `val`, remove all occurrences of `val` in-place and return the new length `k`. You must do this with \(O(1)\) extra memory. The order of the remaining elements doesn’t matter.

**Examples**
- Example 1:

    - Input: nums = [3,2,2,3], val = 3
    - Output: 2, nums = [2,2,_,_]
    - Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).

- Example 2:

    - Input: nums = [0,1,2,2,3,0,4,2], val = 2
    - Output: 5, nums = [0,1,4,0,3,_,_,_]
    - Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4. Note that the five elements can be returned in any order. It does not matter what you leave beyond the returned k (hence they are underscores).

---

## 🧠 解法思路 | Solution Ideas

這題常見的思路是 **雙指標（two pointers）**，但可以有幾個變體：

### 方法 A：前指標 & 掃描指標 + 交換法

- 用 `left` 表示下一個可以寫入非 `val` 的位置（從 0 開始）  
- 用 `right` 從 0 遍歷整個陣列  
- 每當 `nums[right] != val` 時，代表這是我們要保留的元素，就把 `nums[right]` 和 `nums[left]` 交換，然後 `left += 1`  
- 最後 `left` 就是剩下不為 `val` 的元素數量  

優點是寫法直觀，遍歷一遍就能完成。

### 方法 B：雙指標從兩端逼迫

- 用 `left` 從左開始，`right` 從右開始  
- 當 `nums[left] == val` 時，代表這個位置要移除，就用右邊的 `nums[right]` 值覆蓋它，`right -= 1`（把右側的一個可能的非 `val` 的值換過來）  
- 否則，如果 `nums[left] != val`，就是合法的值，`left += 1`  
- 重複直到 `left > right`  
- 回傳 `left`，代表左側都是合法元素  

這種寫法對於移除的元素比較少的情況會略微快一些，因為少了某些交換操作。

---

## 💻 程式碼與詳細說明

### 方法 A — 交換法

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                # 將合法元素換到左邊的 left 位置
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return left
```
- left：下一個寫入合法元素的位置

- right 遍歷整個陣列

- 若 nums[right] != val，就把它換到左邊 left 的位置（或自己覆蓋，如果 right == left 的話也是覆蓋自己）

- 遞增 left

- 最後 left 就代表不等於 val 的元素個數

### 方法 B — 從兩端逼迫法
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # 用末端的值覆蓋這個位置
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
```
- left 從前端掃描

- right 從末端往前移動

- 當 nums[left] == val 時，把 nums[right] 拿來覆蓋它，然後 right -= 1

- 否則 nums[left] 是合法的，直接 left += 1

- 當 left 超過 right，表示掃描完畢

- 最後 left 就是合法元素個數

---

## ⏱ 複雜度分析 | Complexity
| 方法   | 時間複雜度                          | 空間複雜度  |
| ---- | ------------------------------ | ------ |
| 方法 A | (O(n))（一次遍歷）                   | (O(1)) |
| 方法 B | (O(n)) （worst-case 還是遍歷每個元素一次） | (O(1)) |

---

## 🧪 範例演算（兩種方法比對）

- 假設：
    - nums = [3,2,2,3,4,2], val = 3

### 方法 A：

- 初始： left = 0

| right | nums[right] | 操作         | 結果陣列          | left |
| ----- | ----------- | ---------- | ------------- | ---- |
| 0     | 3 == val    | 跳過         | [3,2,2,3,4,2] | 0    |
| 1     | 2 ≠ val     | 換到 nums[0] | [2,3,2,3,4,2] | 1    |
| 2     | 2 ≠ val     | 換到 nums[1] | [2,2,3,3,4,2] | 2    |
| 3     | 3 == val    | 跳過         | [2,2,3,3,4,2] | 2    |
| 4     | 4 ≠ val     | 換到 nums[2] | [2,2,4,3,3,2] | 3    |
| 5     | 2 ≠ val     | 換到 nums[3] | [2,2,4,2,3,3] | 4    |

- 最後 left = 4 → 前 4 個元素是 [2,2,4,2]（順序不重要）

### 方法 B：

- 初始： left = 0, right = 5

| left | right | nums          | 判斷                 | 操作                       | 結果            | left / right    |
| ---- | ----- | ------------- | ------------------ | ------------------------ | ------------- | --------------- |
| 0    | 5     | [3,2,2,3,4,2] | nums[0] = 3 == val | 覆蓋 nums[0] = nums[5] = 2 | [2,2,2,3,4,2] | left=0, right=4 |
| 0    | 4     | [2,2,2,3,4,2] | nums[0] = 2 ≠ val  | left += 1                | —             | left=1, right=4 |
| 1    | 4     | [2,2,2,3,4,2] | nums[1] = 2 ≠ val  | left += 1                | —             | left=2, right=4 |
| 2    | 4     | [2,2,2,3,4,2] | nums[2] = 2 ≠ val  | left += 1                | —             | left=3, right=4 |
| 3    | 4     | [2,2,2,3,4,2] | nums[3] = 3 == val | 覆蓋 nums[3] = nums[4] = 4 | [2,2,2,4,4,2] | left=3, right=3 |
| 3    | 3     | [2,2,2,4,4,2] | nums[3] = 4 ≠ val  | left += 1                | —             | left=4, right=3 |

- 停止條件 left > right，最終 left = 4 → 前 4 個元素 [2,2,2,4]

---

## ✍ 我學到了什麼 / What I Learned

- in‑place + 雙指標 是很多陣列操作題的典型套路

- 方法 B 在刪除元素比較少的場景下可能更有效率，因為它有可能跳過部分交換

- 要注意 left <= right 的終止條件，以及當覆蓋做法可能把尾部元素拿來覆蓋已經「合法」的位置

- 雖然順序可以改，但前 k 個一定要是合法元素 → 必須正確地更新 left