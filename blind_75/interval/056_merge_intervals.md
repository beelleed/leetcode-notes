# 🔢 LeetCode 56. Merge Intervals | 合併區間

[Leetcode 56](https://leetcode.com/problems/merge-intervals/)

---

## 📘 題目描述 | Problem Description
### 中文
給定一組區間，每個區間為 `[start, end]`，請合併所有重疊的區間，並返回一個**不重疊且按起始時間排序**的新區間列表。

### English
Given an array of intervals where each interval is `[start, end]`, merge all overlapping intervals and return an array of the non-overlapping intervals sorted by their start times.

### Examples

- Example 1:

    - Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    - Output: [[1,6],[8,10],[15,18]]
    - Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

- Example 2:

    - Input: intervals = [[1,4],[4,5]]
    - Output: [[1,5]]
    - Explanation: Intervals [1,4] and [4,5] are considered overlapping.

- Example 3:

    - Input: intervals = [[4,7],[1,4]]
    - Output: [[1,7]]
    - Explanation: Intervals [1,4] and [4,7] are considered overlapping.

---

## 💡 解題思路 | Solution Approach

### 🧠 中文解法邏輯：
1. 先將所有區間依據「起始時間」排序。
2. 建立一個 `merged` 陣列放入第一個區間。
3. 依序遍歷剩下的區間：
   - 若目前區間的起始點 `current[0]` 小於等於上個區間的結束點 `last[1]`，代表有重疊 → 合併成一個新區間。
   - 否則，無重疊 → 直接加入 `merged`。
4. 回傳 `merged` 陣列。

### 💡 English Explanation:
1. Sort the intervals based on their start times.
2. Initialize a `merged` list with the first interval.
3. Iterate through the remaining intervals:
   - If `current[0] <= last[1]`, it overlaps → merge them by setting `last[1] = max(last[1], current[1])`.
   - Else, add `current` to the result.
4. Return the merged list.

---

## ✅ Python 程式碼 | Code

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  # 按起始時間排序
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # 合併
            else:
                merged.append(current)  # 無重疊，直接加入

        return merged
```
```python
class Solution:
    def merge(self, intervals: List[List[int]]):
```
🔹 定義類別和方法，接收 intervals（一個區間列表）並返回合併後的區間列表。
```python
if not intervals:
    return []
```
✅ 如果輸入是空的，就直接回傳空陣列。
```python
intervals.sort(key=lambda x: x[0])
```
🧠 核心邏輯第一步：排序！

- 把所有區間按照它們的「起始值」從小到大排序。

- 這樣做的目的是讓我們可以依序比較每個區間和前一個區間有沒有重疊。

| 部分               | 意思                                         |
| ---------------- | ------------------------------------------ |
| `intervals`      | 一個列表（裡面每個元素可能是 `[start, end]` 的子清單或 tuple） |
| `.sort()`        | Python 的原地排序函式（直接改變原本列表順序）                 |
| `key=`           | 告訴 sort()：「我要依照什麼條件排序」                     |
| `lambda x: x[0]` | 一個匿名函式：輸入 `x`（也就是每個子清單），回傳 `x[0]`（第一個元素）   |

```python
merged = [intervals[0]]
```
📦 初始化合併結果 merged，先放入第一個區間作為基礎。
```python
for current in intervals[1:]:
```
🔁 從第二個區間開始依序檢查每一個區間。
```python
last = merged[-1]
```
📌 拿出目前 merged 裡的最後一個區間（也就是上一個合併結果），用來做比較。
```python
if current[0] <= last[1]:
```
🧩 判斷重疊條件：

- 如果「目前區間的起點」小於等於「前一個的終點」→ 表示兩個區間重疊。
```python
last[1] = max(last[1], current[1])
```
🔁 更新上個區間的結束值為「兩個結尾中較大的那個」，等於把它們合併起來了。
```python
else:
    merged.append(current)
```
🧱 否則代表「沒有重疊」，就直接把新的區間加入到 merged 結果中。
```python
return merged
```
✅ 回傳合併完的結果。

- 也可以寫成
    ```python
    class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last = merged[-1]
            curr = intervals[i]   # ← 正確取出區間

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)

        return merged
    ```

---

## 🧪 範例

輸入：[[1,3],[2,6],[8,10],[15,18]]

### 🔹 Step 1: 排序
```python
intervals.sort(key=lambda x: x[0])
```
排序後的 intervals：
```python
[[1,3], [2,6], [8,10], [15,18]]
```
### 🔹 Step 2: 初始化 merged
```python
merged = [intervals[0]]
```
現在：
```lua
merged = [[1,3]]
```
### 🔹 Step 3: 開始迴圈
- current = [2,6]

    - last = merged[-1] = [1,3]

    - 檢查是否重疊：current[0] (2) <= last[1] (3) ✅ 有重疊

    - 合併：更新 last → [1, max(3,6)] = [1,6]

🔁 merged 現在變成：
```lua
[[1,6]]
```
- current = [8,10]

    - last = [1,6]

    - 檢查：8 <= 6 ❌ 不重疊

    - 加入新區間

🔁 merged 現在變成：
```lua
[[1,6], [8,10]]
```
- current = [15,18]

    - last = [8,10]

    - 檢查：15 <= 10 ❌ 不重疊

    - 加入新區間

🔁 merged 現在變成：
```lua
[[1,6], [8,10], [15,18]]
```
### ✅ 最終輸出
```python
[[1,6],[8,10],[15,18]]
```

---

## ⏱️ 時間與空間複雜度 | Time & Space Complexity

- 時間複雜度 Time: O(n log n)（排序）

- 空間複雜度 Space: O(n)（儲存結果）

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- 合併區間問題的第一步永遠是「先排序」，才能保證比較的是鄰近的區間。

- 要用「是否重疊」來決定是否合併：只要目前的起始點 ≤ 前一個的結束點就表示有重疊。

- 熟悉 Python 的排序語法和 list 操作可以大大簡化程式碼邏輯。

### English:

- The key to merging intervals is sorting them first by start time.

- Merging happens only when current.start <= last.end.

- Practicing lambda functions for sorting and understanding list manipulation helps a lot in interval-related problems.