# 🟦 LeetCode 435 — Erase Overlap Intervals / 刪除最少重疊區間
🔗 [題目連結](https://leetcode.com/problems/non-overlapping-intervals/)

---

## 📄 題目說明 | Problem Description

**中文**  
給定一組區間 `intervals`（每個區間為 `[start, end)`），找出最少要刪除多少個區間，使剩下的區間互相 **不重疊**。  
若兩個區間的端點重疊（例如 one 的 end = another’s start），通常不算重疊（視題目而定）。

**English**  
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Examples**
- Example 1:

    - Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    - Output: 1
    - Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

- Example 2:

    - Input: intervals = [[1,2],[1,2],[1,2]]
    - Output: 2
    - Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

- Example 3:

    - Input: intervals = [[1,2],[2,3]]
    - Output: 0
    - Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

---

## 🧠 解法思路 | Solution Idea

這題的經典貪心策略是：

1. **先把所有區間按結束時間排序**（`intervals.sort(key = end)`）  
   為什麼？因為如果一個區間結束得早，那麼它留給後面區間的「空間」比較大，衝突機會比較低。

2. 以 `prev_end` 記錄上一次選擇保留的區間的結束時間。

3. 從第二個區間開始遍歷，每次遇到：
   - 若 `start < prev_end`：表示這個區間和上次保留的區間衝突 → 必須刪除這個，`count += 1`
   - 否則：這個區間不衝突 → 我們把它保留下來，更新 `prev_end = end`

最終 `count` 就是要刪掉的最小區間數。

這種思路的核心是：**每次都選一個結束最早、與已選「不衝突」的區間**，以最大化可保留區間數量，從而最小化刪除數量。

---

## 💻 程式碼

```python
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 按區間結束時間排序
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                # 衝突：刪除當前這個區間
                count += 1
            else:
                # 無衝突：保留當前區間，更新 prev_end
                prev_end = end
        
        return count
```
```python
if not intervals:
    return 0
```
- 如果輸入是空列表，沒有區間要處理，回傳 0。

```python
intervals.sort(key=lambda x: x[1])
```
- 將區間按結束時間排序。

- 排序保證我們先考慮結束最早的區間，使後續保留最有空間。

```python
count = 0
prev_end = intervals[0][1]
```
- count 計數要刪掉的區間數。

- prev_end 設為第一個區間的結束時間，作為參考。

```python
for i in range(1, len(intervals)):
    start, end = intervals[i]
    if start < prev_end:
        count += 1
    else:
        prev_end = end
```
- 從第二個區間開始遍歷：

    - 若新的區間 start 小於 prev_end → 與已保留的區間衝突 → 刪掉當前區間（count += 1）

    - 否則 → 無衝突 → 保留當前區間，更新 prev_end = end

```python
return count
```
- 最後回傳要刪除的最小區間數。

---

## 🧪 範例演算
- 假設：

```lua
intervals = [[1,2], [2,3], [1,3]]
```
1. 排序後（按結束時間）：[[1,2], [2,3], [1,3]]

2. 初始化：prev_end = 2，count = 0

3. 遍歷：

    - i = 1 → [2,3]，start = 2 >= prev_end = 2 → 無衝突 → 保留 → prev_end = 3

    - i = 2 → [1,3]，start = 1 < prev_end = 3 → 衝突 → 刪除 → count = 1

4. 回傳 1

- 意味著至少刪掉一個區間（刪掉 [1,3]）就可以使區間不重疊。

- 另一個例子：

```lua
intervals = [[1,2],[2,3],[3,4],[1,3]]
```
- 排序後：按 end → [[1,2],[2,3],[1,3],[3,4]]

- prev_end = 2

- i=1 [2,3] → start=2 ≥ 2 → 保留 → prev_end=3

- i=2 [1,3] → start=1 < 3 → 衝突 → 刪除 → count=1

- i=3 [3,4] → start=3 ≥ prev_end=3 → 保留 → prev_end=4

- 回傳 1

---

## ⏱ 複雜度分析
- 時間複雜度： O(nlogn)，因為排序需要 O(nlogn)，遍歷再比較花 O(n)

- 空間複雜度： O(1) 或 O(n)（取決於排序是否在原地進行，其實 Python 的 sort 是原地的，因此是 O(1) 額外空間）

---

## ✍ 我學到了什麼 / What I Learned
- 排序 + 貪心是區間覆蓋／非重疊類題目的關鍵套路

- 為什麼按「結束時間排序」：因為早結束的區間留下更大空間給後來的區間

- 在遍歷時保留「最後保留的區間結束時間」即可做衝突判斷

- 要刪除最少區間，其實等價於「保留最多不重疊區間」的補集問題