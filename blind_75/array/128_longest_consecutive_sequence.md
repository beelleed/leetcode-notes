# 🔢 LeetCode 128 – Longest Consecutive Sequence
🔗 題目連結：[https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## 📄 題目說明 | Problem Description

**中文**：

給定一個未排序的整數陣列 `nums`，要找出陣列中能構成的最長連續整數序列（consecutive sequence）的長度。序列裡的數字要是連續的整數，但在原陣列中不一定是連續出現的。  

**English**: 

Given an unsorted array of integers `nums`, return the length of the longest sequence of consecutive integers. The numbers in the array can be in any order, but the sequence you count must be of consecutive values (like `4,5,6,7` etc.).

### Examples
- Example 1:

    - Input: nums = [100,4,200,1,3,2]
    - Output: 4
    - Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

- Example 2:

    - Input: nums = [0,3,7,2,5,8,4,6,0,1]
    - Output: 9

- Example 3:

    - Input: nums = [1,0,1,2]
    - Output: 3

---

## 🧠 解題思路 | Solution Idea

要達到 **O(n)** 時間複雜度，常見且有效的方法是使用 **集合（Set）**：

1. 將整個陣列 `nums` 放進一個 set，使查找某個數是否存在成為 O(1) 的操作。  
2. 初始化一個變數 `longest = 0`，用來存目前找到的最長連續序列長度。  
3. 遍歷 set 中的每一個數字 `num`：  
   - 若 `num - 1` 不在 set 中 → 表示 `num` 是某段連續序列的 *開頭*。  
   - 如果是開頭，就從這個 `num` 開始往上數，檢查 `num + 1`, `num + 2`... 是否也在 set 中。  
   - 計算這段序列的長度（從開頭 `num` 開始連續到某個中斷的點）。  
   - 更新 `longest = max(longest, current_length)`。

這樣做可以確保每段連續序列只從它的開頭算一次，避免重複計算。

---

## 💻 程式碼實作 | Code

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 只有當 num 是某條序列的開頭才開始往後數
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
```
### 檢查空陣列
```python
if not nums:
    return 0
```
- 如果 nums 是空的（沒有元素），直接回傳 0，因為沒有連續序列。

- 這是邊界條件（edge case）的處理。
### 轉成 Set + 初始化變數
```python
num_set = set(nums)
longest = 0
```
- 把 nums 放進一個 set，叫 num_set。這樣做可以讓「查某個元素是否存在」是 O(1) 的時間複雜度。
    - 在 Python 中，set 的底層其實是用 哈希表（hash table） 實作的。
    - 也就是說，所有放進去的元素，都會被轉換成一個「哈希值（hash value）」→ 然後根據這個哈希值，存進特定的「桶（bucket）」裡。  
    - 因為「透過哈希值直接定位」→ 不需要線性搜尋。  
        - 舉例：
            - 假設你放入：
            ```python
            num_set = {5, 10, 13}
            ```
            - Python 背後會做的事 roughly 是這樣：
            
            |  元素 | hash(元素) | 存放的位置 (bucket index) |
            | :-: | :------: | :------------------: |
            |  5  |   12345  |          45          |
            |  10 |   56789  |          89          |
            |  13 |   91234  |          34          |
            - 這樣當你要查「10 是否存在」時，
            - Python 會先算出 hash(10)，再直接跳到那個位置去找。
            - 不需要一個一個比對所有元素。


- longest 用來儲存目前找到的最長連續序列的長度。
### 遍歷集合中的每一個數字
```python
for num in num_set:
    if num - 1 not in num_set:
```
- 遍歷 set 中的每個 num。

- if num - 1 not in num_set: 這行非常關鍵：只對那些 沒有前一個連續數字 的 num 執行「往後數」的動作，這樣可以確保每條連續序列只「從頭」被計算一次，避免重複。
    - 不能寫成for num in nums 因為nums 可能有 重複元素
        - 例如: nums = [1,2,2,3] 會造成重複檢查


### 從這個起點往後數（計算連續序列的長度）
```python
current_num = num
current_streak = 1

while current_num + 1 in num_set:
    current_num += 1
    current_streak += 1
```
- current_num 從 num 開始，表示序列中的當前數字。

- current_streak 表示從這個起始點到目前為止的連續長度（至少 1，因為起點自己算一個）。

- while current_num + 1 in num_set: 這個迴圈一直往後檢查 current_num+1, current_num+2, ... 是否存在於 set。

- 每次存在就把 current_num 加 1，current_streak 加 1。

### 更新最長紀錄
```python
longest = max(longest, current_streak)
```
- 用 max 比較目前這條連續序列的長度 (current_streak) 與過去紀錄的 longest，更新 longest 為較大值。

### 最後回傳答案
```python
return longest
```
- 當所有可能的起點都計算過後，longest 就是整個陣列中可以形成的最長連續序列的長度。

---

## 🧪 範例流程

假設輸入：
```python
nums = [100, 4, 200, 1, 3, 2]
```
1. nums 不空 → 繼續

2. num_set = {100, 4, 200, 1, 3, 2}，longest = 0

3. 遍歷 num_set 中的元素（順序可以是任意，但結果一樣）：

    - 比如先看 num = 1：檢查 0 是否存在？不存在 → 表示序列從 1 開始往後檢查 2,3,4,5... → 2 存在 → current_streak = 2 → 3 存在 → 3；4 存在 → 4；5 不存在 → 停；更新 longest = max(0,4) = 4

    - 接著看 num = 2：但 1 存在 → 所以跳過，不做從 2 開始計算的動作（因為這條序列已經從 1 被算過）

    - 看 num = 100：99 不存在 → 從 100 開始序列長度至少 1，往後檢查 101（不存在）→ current_streak = 1，更新 longest = max(4,1) = 4

    - 看 num = 200：同樣從 200 開始 → current_streak = 1 → longest 仍然 4

4. 所有元素都檢查完 → 回傳 4

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類        | 複雜度                                                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **時間複雜度** | **O(n)**，n 是 `nums` 的長度。原因是：把所有元素放 set 是 O(n)，然後遍歷每個元素。對每個元素，只有當它是序列開頭時才進一步做 while 往後檢查，整體每個元素最多被 `while current_num + 1 in num_set` 檢查一次。 |
| **空間複雜度** | **O(n)**，因為要存 `num_set`，裡面可能存所有元素。還有一些變數佔用空間也為 O(1)，但總體是 O(n)。                                                                             |

---

## ✍️ 我學到了什麼 | What I Learned

- 利用 set 的查詢 O(1) 的特性，可以避免排序並維持時間複雜度為 O(n)。

- 關鍵點在要「只在一個序列的開頭」時才展開往後檢查，避免重複計算。

- 特殊情況要注意：空陣列、全部元素相同、很大範圍但不連續的數字。

- 面試中講這題要強調為什麼能做到 O(n)：因為沒排序、每個元素檢查次數有限。