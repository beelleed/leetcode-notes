# 🌟 LeetCode 78 - Subsets 子集問題
🔗 [題目連結](https://leetcode.com/problems/subsets/)

---

## 📘 題目說明 | Problem Description
### 中文：
給定一個整數陣列 nums，其中元素互不相同，請返回該陣列所有可能的子集（即冪集）。解集不能包含重複的子集，且子集的順序可以任意。

### English:
Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

### Examples
- Example 1:

    - Input: nums = [1,2,3]
    - Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
- Example 2:

    - Input: nums = [0]
    - Output: [[],[0]]

---

## 🧠 解題思路 | Solution Strategy
✅ 核心想法：
- 每個元素都有兩種選擇：包含或不包含。

- 因此，對於長度為 n 的陣列，總共有 2^n 種子集。

- 我們可以透過：

    - 🔁 回溯法（Backtracking） 逐步嘗試所有選擇。

    - ⚙️ 位元操作（Bit Manipulation） 使用二進位表示選與不選的組合。


✅ Core Idea:
- Each element has two options: include or not include.

- Therefore, for an array of length n, there are 2^n possible subsets.

- We can generate all subsets using:

    - 🔁 Backtracking: recursively explore inclusion/exclusion of each element.

    - ⚙️ Bit Manipulation: use binary representation to simulate choices (e.g., 1 for include, 0 for exclude).

---

## 💻 Python 程式碼 | Python Code
### 方法一：回溯法（Backtracking）
```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
```
#### 📘 完整程式碼與詳細說明
```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 用來儲存所有的子集結果

        def backtrack(start: int, path: List[int]):
            res.append(path[:])  # 每一次進入遞迴，就加入當前 path 的副本為一個子集
```
- 這裡的 path[:] 是淺拷貝，表示保留目前子集內容，避免後面遞迴改變 path 時影響之前結果。
```python
for i in range(start, len(nums)):
    path.append(nums[i])         # 選擇這個元素
    backtrack(i + 1, path)       # 從下一個位置開始繼續遞迴
    path.pop()                   # 回溯：移除最後一個加入的元素，繼續嘗試別的組合

```
- 🔁 解釋 for 迴圈：
    - 從 start 開始遍歷，確保產生的是不重複且遞增的子集。
        - 如果不用 start，會發生什麼事？
            - 你會從頭遍歷 nums，導致像 [1,2] 和 [2,1] 都出現，這違反了「子集」的定義（順序不影響，但不能重複排列組合）。

    - 每層選一個元素加入 path，然後向下遞迴。

    - 回來時用 pop() 移除剛剛加入的，準備試別的元素（回溯核心步驟）。
```python
backtrack(0, [])  # 從 index 0 開始，初始 path 為空集合 []
return res        # 回傳所有子集
```
#### 🔍 以 [1, 2, 3] 為例，回溯展開步驟：
```css
[]
├── [1]
│   ├── [1,2]
│   │   └── [1,2,3]
│   └── [1,3]
├── [2]
│   └── [2,3]
└── [3]
```
🔹 Step 1: 呼叫 backtrack(0, [])
- res = [[]]（初始空子集）

- start = 0，i = 0

🔹 Step 2: 加入 1 → path = [1]，呼叫 backtrack(1, [1])
- res = [[], [1]]

- start = 1，i = 1

🔹 Step 3: 加入 2 → path = [1, 2]，呼叫 backtrack(2, [1, 2])
- res = [[], [1], [1, 2]]

- start = 2，i = 2

🔹 Step 4: 加入 3 → path = [1, 2, 3]，呼叫 backtrack(3, [1, 2, 3])
- res = [[], [1], [1, 2], [1, 2, 3]]

- start = 3，超出範圍，返回

- 🔹 回溯：移除 3 → 回到 path = [1, 2]
    - i = 2 完畢 → 返回上一層

- 🔹 回溯：移除 2 → 回到 path = [1]
    - 現在 i = 2

🔹 Step 5: 加入 3 → path = [1, 3]，呼叫 backtrack(3, [1, 3])
- res = [[], [1], [1, 2], [1, 2, 3], [1, 3]]

- 超出邊界，返回

- 🔹 回溯：移除 3 → 回到 path = [1]
    - i = 2 完畢 → 返回上一層

- 🔹 回溯：移除 1 → 回到 path = []
    - 現在 i = 1

🔹 Step 6: 加入 2 → path = [2]，呼叫 backtrack(2, [2])
- res = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]

🔹 Step 7: 加入 3 → path = [2, 3]，呼叫 backtrack(3, [2, 3])
- res = [..., [2, 3]] → 超出，回溯

- 🔹 回溯：移除 3 → path = [2] → 移除 2 → 回到 []
    - 現在 i = 2

🔹 Step 8: 加入 3 → path = [3]，呼叫 backtrack(3, [3])
- res = [..., [3]]

🔚 結束，最終 res = [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

#### 🕒 時間複雜度（Time Complexity）
- 每個元素都有選或不選兩種選擇

- 所以總共有 2^𝑛 種子集

- 每個子集最長長度為 𝑛 ，複製 path 的成本是 O(n)

總時間複雜度：O(n × 2^n)

---

### 方法二：位元操作法（Bit Manipulation）
```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(1 << n):  # 2^n
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
```
#### 📘 完整程式碼與詳細說明
```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(1 << n):  # 1 << n 相當於 2^n，枚舉所有可能子集的編碼
```
- 🧠 為什麼要 1 << n？
    - 如果有 n 個元素，每個元素都可以「選」或「不選」 → 2 個選項

    - 所以一共有 2^𝑛 種子集

    - 把每種選擇用 二進位 表示，例如 i = 5 → 101 表示第 0 和第 2 個元素被選中
```python
subset = []
for j in range(n):
    if i & (1 << j):
        subset.append(nums[j])
```
- 📘 說明：i & (1 << j)
    - 1 << j：表示第 j 位的位元為 1

    - i & (1 << j)：檢查 i 的第 j 位是不是 1，若是代表 nums[j] 要加入子集

- 例子：nums = [1,2,3]，i = 5（二進位 101）

    - j = 0 → 1 << 0 = 1 → 5 & 1 = 1 → 加入 nums[0] = 1

    - j = 1 → 1 << 1 = 2 → 5 & 2 = 0 → 不加 nums[1]

    - j = 2 → 1 << 2 = 4 → 5 & 4 = 4 → 加入 nums[2] = 3

    - 最終 subset = [1, 3]
```python
    res.append(subset)
return res
```
- 把每次組合出來的 subset 加入結果陣列 res 裡

#### 🔢 結果範例
nums = [1,2,3]，則總共 2^3 = 8 種：
```less
i (binary) | 子集
-----------|------------------
000 (0)    | []
001 (1)    | [1]
010 (2)    | [2]
011 (3)    | [1,2]
100 (4)    | [3]
101 (5)    | [1,3]
110 (6)    | [2,3]
111 (7)    | [1,2,3]
```

#### ⏱ 時間與空間複雜度分析
- 時間複雜度： O(n × 2^n) 每個子集最多長度為 n，共 2^n 個子集。

- 空間複雜度： O(n × 2^n)（輸出空間）

#### 📘 學到的重點
- 使用「位元編碼」技巧產生子集

- 二進位枚舉法適合用於枚舉所有「選或不選」情境

- 1 << n 表示 2^n，i & (1 << j) 是檢查 i 的第 j 位

---

## 📌 學習重點 | What I Learned
- 理解回溯法如何在每一步做出選擇，並在需要時回退，探索所有可能的解。

- 學會使用位元操作來生成所有子集，透過二進位的方式表示每個元素的選擇。

- 掌握如何處理組合問題，特別是在元素不重複的情況下生成所有子集。