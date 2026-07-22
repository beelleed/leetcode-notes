# 🧩 LeetCode 57 — Insert Interval 插入區間
🔗 [題目連結](https://leetcode.com/problems/insert-interval/)

---

## 📄 題目說明 | Problem Description

- **中文**：給你一個已排序且互不重疊（non‑overlapping）的區間列表 `intervals`（每個為 `[start, end]`），還有一個新的區間 `newInterval`。將 `newInterval` 插入到 `intervals` 中，使得結果仍然是排序的且沒有重疊的區間，必要時要合併重疊區間，回傳最終的區間列表。

- **English**: You are given a list of non-overlapping intervals `intervals` sorted by start times, and a new interval `newInterval`. Insert the new interval into `intervals` such that the resulting list is still sorted and contains no overlapping intervals. Merge overlapping intervals if necessary, and return the resulting list.

- **Examples**
    - Example 1:

        - Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        - Output: [[1,5],[6,9]]

    - Example 2:

        - Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        - Output: [[1,2],[3,10],[12,16]]
        - Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

---

## 🧠 解題思路 | Solution Idea

因為 `intervals` 原本就是排序且無重疊的，我們可以 **線性掃描（one pass）** 的方式完成插入與合併，時間複雜度為 \(O(n)\)。

我們將整個過程分三個階段：

1. **左側不重疊區間**：將所有結尾早於 `newInterval` 開始的區間直接加入結果中（這些區間與 `newInterval` 無任何重疊關係）。
2. **重疊合併階段**：對剩下的區間，只要有重疊，就不直接加入，而是更新 `newInterval` 的開與結（start = min, end = max），直到不再重疊為止。合併後把整個合併好的 `newInterval` 加入結果。
3. **右側不重疊區間**：將剩餘所有開頭晚於 `newInterval` 結束的區間加入結果中。

這樣能確保最終結果排序且無重疊。這種作法利用了原本 `intervals` 有序與無重疊的特性。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. 左邊完全在 newInterval 前面的區間，無重疊
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. 合併所有與 newInterval 重疊的區間
        #    當 intervals[i][0] <= newInterval[1] 時，有重疊
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 把合併後的 newInterval 加入
        result.append(newInterval)

        # 3. 加入右側所有不重疊區間
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
```

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
```

## 🔍 程式碼解釋
| 區段      | 程式碼                                                                                     | 功能 / 說明                                                                        |
| ------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 初始化     | `result = []`, `i = 0`, `n = len(intervals)`                                            | 用 `result` 儲存答案；`i` 是遍歷索引，`n` 是總區間數                                            |
| 左邊部分    | `while i < n and intervals[i][1] < newInterval[0]: result.append(intervals[i]); i += 1` | 把所有結束時間早於 `newInterval` 開始的區間先放結果，不需合併                                         |
| 合併重疊區間  | `while i < n and intervals[i][0] <= newInterval[1]: ...`                                | 只要 `intervals[i]` 的開始時間不晚於 `newInterval` 的結束，就表示有重疊，要更新 `newInterval` 開始與結束以合併 |
| 加入合併後區間 | `result.append(newInterval)`                                                            | 把合併後（或原本就不重疊的）`newInterval` 加入結果                                               |
| 右邊部分    | `while i < n: result.append(intervals[i]); i += 1`                                      | 加入剩下所有開頭在 `newInterval` 之後的區間                                                  |
| 回傳      | `return result`                                                                         | 最終結果為合併後的區間列表                                                                  |

### [][] 的用法是針對「巢狀 list（list of lists）」的索引。第一個索引取出哪個區間，第二個索引取出區間的起點（[0]）或終點（[1]）。

### 兩個區間什麼時候算重疊？
- 兩個區間：
```text
A = [a_start, a_end]
B = [b_start, b_end]
```
- 它們「沒有重疊」只有兩種可能：

1️⃣ A 在 B 左邊
```text
a_end < b_start
```

2️⃣ A 在 B 右邊
```text
a_start > b_end
```
- 所以「有重疊」就是「不是上面兩種」

- 也就是：
```text
a_end >= b_start  AND  a_start <= b_end
```
- 為什麼這題只要檢查一半？

    - 因為在這題中：

        - intervals[i] 是「下一個要處理的區間」

        - newInterval 是「目前正在合併的區間」

        - 而且 intervals 已經按起點排序

👉 所以一定有：
```python
intervals[i][0] >= newInterval[0]（在進到這個 while 時）
```

因此「重疊判斷」只剩下這一個條件需要檢查：
```python
intervals[i][0] <= newInterval[1]
```

### 為甚麼不能寫成while i < n and intervals[i][0] > newInterval[1]:?
```python
while i < n and intervals[i][0] > newInterval[1]:
    result.append(intervals[i])
    i += 1
```
- 這段的意思變成：只把「起點 > newInterval[1]」的區間加進去

- 但在正確演算法中，第二段合併完以後，剩下的所有區間都一定在右邊，你不需要再判斷 > newInterval[1]，直接全部 append 就好。

- 而且用 and intervals[i][0] > newInterval[1] 會造成：

    - 如果後面剛好沒有滿足（或你合併後 newInterval 改變），你可能會直接停止 while，導致右邊區間被漏掉。


---

## 🧪 範例 | Examples
```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```
### ✅ Step 1：加入左側不重疊的區間

- 條件：intervals[i][1] < newInterval[0]
    newInterval[0] = 4

    - i = 0 → intervals[0][1] = 2 → 2 < 4 ✅ → 加入 [1,2]

    - i = 1 → intervals[1][1] = 5 → 5 < 4 ❌ → 停止

👉 result = [[1, 2]]

### ✅ Step 2：合併所有重疊區間

- 條件：intervals[i][0] <= newInterval[1]
    newInterval = [4,8]

    - i = 1 → intervals[1][0] = 3 → 3 <= 8 ✅
        → 合併：newInterval = [min(4,3), max(8,5)] = [3,8]

    - i = 2 → intervals[2][0] = 6 → 6 <= 8 ✅
        → 合併：newInterval = [min(3,6), max(8,7)] = [3,8]

    - i = 3 → intervals[3][0] = 8 → 8 <= 8 ✅
        → 合併：newInterval = [min(3,8), max(8,10)] = [3,10]

    - i = 4 → intervals[4][0] = 12 → 12 <= 10 ❌ → 停止

👉 合併完成後：result = [[1, 2], [3, 10]]

### ✅ Step 3：加入右側不重疊的區間

- 剩下的 interval：

    - i = 4 → intervals[4] = [12, 16] → 加入

👉 最終 result = [[1, 2], [3, 10], [12, 16]]

### 🟢 回傳結果：
```python
[[1, 2], [3, 10], [12, 16]]
```

---

## ⏱ 複雜度分析 | Complexity Analysis
- 時間複雜度（Time Complexity）

    - O(n)，其中 n 是 intervals 的長度。

        - 我們最多只遍歷 intervals 一次，每個 interval 處理一次。

        - 不論是加入、合併、或右邊區間，都只需 O(1) 操作，整體是線性時間。

- 空間複雜度（Space Complexity）

    - O(n)

        - 使用了額外的 result 陣列來儲存新的合併後結果，最壞情況下大小與 intervals 相同。

        - 除此之外只用了常數額外變數。

---

## ✍️ 我學到的東西 | What I Learned

- 利用已排序與無重疊的特性，可以用線性掃描來插入與合併，而無需整體排序或多次合併。

- 合併區間核心在於比較開始、結束端點：start = min(...), end = max(...)

- 分成三段（左不重疊 + 合併重疊 + 右不重疊）的思維很容易理解又好寫。