# 📘 LeetCode 451: 字元依出現頻率排序 | Sort Characters by Frequency

## 🔗 題目連結 | Problem Link
[LeetCode 451 - Sort Characters by Frequency](https://leetcode.com/problems/sort-characters-by-frequency)

---

## 📖 題目說明 | Problem Description

### 中文
給定一個字串 `s`，請根據每個字元出現的「頻率」由高到低重新排列字元，回傳新的字串。

### English
Given a string `s`, sort it in decreasing order based on the frequency of characters, and return the sorted string.

---

## ✅ 解法一：最大堆（Max Heap）

### 💡 解題想法 | Idea
**中文**
- 使用 `Counter` 統計每個字元出現的次數，然後使用 heap（堆積）來依頻率排序。
- 為了用 `heapq`（預設是 min-heap）做最大堆，我們將頻率設為負值 `(-freq, char)`。
- 每次從 heap 中彈出最常出現的字元，重複它的頻率次數加入結果中。

**English**
- Use `Counter` to count the frequency of each character. Push `(-freq, char)` into the heap so that the largest frequency comes out first.

---

### 🧾 程式碼 | Code

```python
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))  # 模擬最大堆

        res = []
        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch * (-freq))  # 將字元重複出現次數
        return ''.join(res)
```

```python
count = Counter(s)
```
- 使用 Counter 將字串中的每個字元出現次數統計起來。

- 範例："tree" ➜ {'t': 1, 'r': 1, 'e': 2}

```python
for ch, freq in count.items():
    heapq.heappush(heap, (-freq, ch))
```
- 對每個字元與出現次數 (ch, freq)：

    - 把 (–freq, ch) 推入 heap 中。

    - 為什麼要用 -freq？

        - 因為 heapq 是 min-heap，我們要模擬 max-heap（最大堆），所以頻率取負號。

        - 這樣出現最多的字元會被排在最前面。
```python
res = []
```
- 建立一個空 list，準備儲存結果。
```python
while heap:
    freq,ch = heapq.heappop(heap)
    res.append(ch * (-freq))
```
- freq,ch = heapq.heappop(heap)
    - 因為「需要用到 pop 出來的內容」，所以必須接住它的回傳值

    - heapq.heappop(heap) 會回傳 heap 中最小的元素，通常是一個 tuple，例如 (freq, ch)

    - 只寫 heapq.heappop(heap) 只有在你「只想把它丟掉，不想用它」的時候才會用

- 每次從堆中彈出一個 (–freq, ch)：

    - ch * (-freq)：把字元 ch 重複出現次數次。

    - 例如：('e', 2) ➜ "ee"

- 將結果加入 res 列表中。
```python
return ''.join(res)
```
- 將 list 中的所有字串合併成一個字串並回傳。

- 範例輸出可能是："eetr" 或 "eert"（出現次數正確，順序不限）

### 📘 完整範例
```python
Input: "tree"
Counter: {'t': 1, 'r': 1, 'e': 2}
Heap: [(-2, 'e'), (-1, 'r'), (-1, 't')]
Output: "eetr"（或其他正確順序）
```

### 🧠補充
在 heap 中「誰負責排序，就寫在前面」，因為 heap 會根據 tuple 的第一個元素排序！

### ⏱️ 複雜度 | Time & Space Complexity
- 時間 | Time: O(n log n)（heap 操作）

- 空間 | Space: O(n)（字典與 heap 空間）

---

## ✅ 解法二：排序搭配 Counter
💡 解題想法 | Idea

- 中文：統計每個字元的頻率後，用 Python 內建的 sorted() 根據頻率高低排序。用列表生成式將字元依頻率拼接回結果。

- English: After using Counter, sort the (char, freq) pairs by frequency descending, then rebuild the string.

### 🧾 程式碼 | Code
```python
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return ''.join(ch * freq for ch, freq in sorted_items)
```

```python 
sorted_items = sorted(count.items(), key=lambda x:x[1], reverse=True)
```
- 把 count.items() 轉成一個 list，內容是 (字元, 次數) 的 tuple。

- 使用 sorted() 根據 x[1]（也就是出現次數）排序。

- reverse=True 表示由大到小排序（頻率高的在前面）。

- 範例：sorted_items = [('e', 2), ('t', 1), ('r', 1)]
```python
return ''.join(ch * freq for ch, freq in sorted_items)
```
- for ch, freq in sorted_items：遍歷一個 list，裡面每個元素是 (字元, 次數) 的 tuple。

- ch * freq：把字元 ch 重複 freq 次 ➜ 這是「字串乘法」

- 用「列表生成式」將每個字元依照它的頻率重複出現：

    - 'e' * 2 ➜ 'ee'

    - 't' * 1 ➜ 't'

    - 'r' * 1 ➜ 'r'

- 然後用 ''.join() 把所有字串連接起來，變成：

### 📘 完整範例
```python
Input: "tree"
Counter: {'e': 2, 't': 1, 'r': 1}
排序後: [('e', 2), ('t', 1), ('r', 1)]
輸出: "eetr" 或 "eert"
```
### ⏱️ 複雜度 | Time & Space Complexity
- 時間 | Time: O(n log n)（因為有排序）

- 空間 | Space: O(n)（Counter + 輸出）

---

## ✅ 解法三：桶排序（Bucket Sort）
💡 解題想法 | Idea

- 中文：建立一個「桶」陣列 bucket[i]，存放所有出現 i 次的字元。然後從高頻率往低頻率讀桶中的字元，依次拼接到結果中。

- English: Use bucket sort by frequency. Each index i in the bucket stores characters with frequency i. Collect from high to low.

### 🧾 程式碼 | Code
```python
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]

        for ch, freq in count.items():
            bucket[freq].append(ch)

        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for ch in bucket[freq]:
                res.append(ch * freq)
        return ''.join(res)
```

```python 
bucket = [[] for _ in range(len(s) + 1)]
```
- 建立一個「桶陣列」，每個 index 表示字元出現的次數。

- 為什麼長度是 len(s) + 1？

    - 因為一個字元最多可能出現 n 次（假設全都是同一個字元），所以要加一以容納全部情況。

- 初始狀態像這樣：
```python
bucket = [[], [], [], [], ...]
```

```python
for ch,freq in coun.items():
    bucket[freq].append(ch)
```
- 將每個字元 ch 根據它的出現次數 freq 加入對應的桶中。

- 範例：如果 e 出現 2 次，就加入 bucket[2]
```python
res = []
```
- 建立一個空 list 用來儲存最終的排序結果。
```python
for freq in range(len(bucket) - 1, 0, -1):
```
- 從最大頻率開始往下掃描桶。

- range(..., 0, -1)：倒著走，從最大頻率到 1。

- 為什麼從大到小？因為我們想要「頻率高的字元排在前面」。
```python
for ch in bucket[freq]:
    res.append(ch * freq)
```
- 在每個頻率的桶中，可能有多個字元。

- 對於每個字元 ch，將它重複 freq 次加入結果中。
```python
return ''.join(res)
```
- 把 res 中的所有字串連接起來，變成一個完整的結果字串。

### 📘 完整範例
- 輸入：s = "tree"

- 處理過程：

    1. Counter: {'t':1, 'r':1, 'e':2}

    2. bucket = [[], ['t','r'], ['e']]

    3. 遍歷 bucket：

        - freq = 2 ➜ res = ['ee']

        - freq = 1 ➜ res = ['ee', 't', 'r']

    4. 合併結果 ➜ "eetr" 或 "eert"

### ⏱️ 複雜度 | Time & Space Complexity
- 時間 | Time: O(n)（只遍歷一次字串與 bucket）

- 空間 | Space: O(n)（Counter + bucket）

---

## 🧠 學到的東西 | What I Learned
- ✅ 如何使用 Counter 快速統計字元出現頻率

- ✅ 用 heapq 建立「最大堆」時可以將數值轉為負數處理

- ✅ 熟悉 sorted() + lambda 搭配使用的技巧

- ✅ 桶排序的概念與如何避免排序來優化成 O(n)

---

## 📌 方法比較 | Method Comparison
| 解法           | 時間複雜度      | 優點              | 適合場合          |
| ------------ | ---------- | --------------- | ------------- |
| Max Heap     | O(n log n) | 符合常見 Top K 題型邏輯 | 適合熟練 heap 的人  |
| 排序 + Counter | O(n log n) | 寫法簡潔、直觀         | 適合快速實作題目      |
| 桶排序          | O(n)       | 效率最高，無需排序       | 適合追求效能、處理大量資料 |
