# LeetCode 46 - Permutations 全排列
🔗 [題目連結](https://leetcode.com/problems/permutations/)

## 📘 Description 題目描述

**English:**

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**中文：**

給定一個不含重複數字的整數陣列 `nums`，請你回傳所有可能的排列（順序不限）。

**Examples:**

- Example 1:

    - Input: nums = [1,2,3]
    - Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
- Example 2:

    - Input: nums = [0,1]
    - Output: [[0,1],[1,0]]
- Example 3:

    - Input: nums = [1]
    - Output: [[1]]

---

## 🧠 Solution 解法思路

這題可以用「**回溯法（Backtracking）**」來解。

### 解法邏輯：
1. 使用一個 `path` 紀錄目前的排列組合。
2. 使用一個 `used` 陣列標記哪些數字已經被使用。
3. 每次嘗試把一個未使用的數字加入 `path`，然後遞迴下去。
4. 當 `path` 的長度等於 `nums`，代表一個完整排列，加入結果中。
5. 遞迴完要回溯，把剛剛加入的數字移除，恢復狀態繼續嘗試其他可能性。

###  Solution Logic:
1. Use a path list to keep track of the current permutation being built.

2. Use a used array to mark which numbers have already been included in the current path.

3. At each step, try adding an unused number to the path, then recurse.

4. When the length of path equals the length of nums, it means a complete permutation has been formed—add it to the result list.

5. After recursion, backtrack by removing the last number added and resetting its used status to try other possibilities.

---

## 💻 Python Code 程式碼

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], used: List[bool]):
            if len(path) == len(nums):
                res.append(path[:])  # 加入一個 path 的副本
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()        # 回溯狀態
                    used[i] = False

        backtrack([], [False] * len(nums))
        return res
```
```python
from typing import List
```
🔹 這行是 type hint 的語法，告訴 Python 編譯器（或開發工具）nums 是一個整數列表，permute 的回傳值也是一個「列表裡面裝著整數列表」。

```python
def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
```
🔹 定義一個方法 permute，參數 nums 是整數列表。

🔹 建立一個空的結果列表 res，用來存所有排列的結果。
```python
def backtrack(path: List[int], used: List[bool]):
```
🔹 內部定義一個遞迴函式 backtrack，這是「回溯法」的核心。

- path：目前遞迴中已經選的數字（暫時的排列結果）。

- used：布林值列表，記錄每個數字是否已被使用過。
```python
if len(path) == len(nums):
    res.append(path[:])
    return
```
🔹 如果 path 長度等於 nums，表示完成一組排列。

🔹 path[:] 是淺複製，否則後續的變動會影響結果。

🔹 把這個排列加入 res，然後返回（結束這層遞迴）。
```python
for i in range(len(nums)):
```
🔹 嘗試走訪每個位置的數字。
```python
if not used[i]:
```
🔹 如果這個數字還沒被用過，才繼續。

```python
used[i] = True
path.append(nums[i])
```
🔹 標記這個數字為已使用，並加入 path。
```python
backtrack(path, used)
```
🔹 遞迴進入下一層，嘗試更多數字加入。
```python
path.pop()
used[i] = False
```
🔹 遞迴結束後，要把這層的選擇「取消」：把剛剛加入的數字移除，並把 used 設回 False。

🔹 這樣可以繼續嘗試其他可能的數字。
```python
backtrack([], [False] * len(nums))
```
🔹 開始遞迴，初始化 path 為空，used 為全部 False（表示都沒用過）。
```python
return res
```
🔹 回傳所有的排列結果。

---

## ⏱ 時間與空間複雜度 | Complexity
Time 時間複雜度：O(n!)，n 為 nums 的長度，全排列總數為 n!

Space 空間複雜度：O(n)，遞迴深度與 path 長度皆為 n

---

## 📌 學習重點 | What I Learned
- 學會了如何用「回溯法（Backtracking）」解排列組合的問題。

- 理解到使用 used 陣列來標記已使用元素，可以有效避免重複。

- 練習了寫遞迴函式，並在每次遞迴結束後回溯狀態（把資料還原）。

- 更加熟悉 Python 中的列表操作，如 append、pop 和切片（list slicing）。

