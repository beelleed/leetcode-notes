# 🔤 LeetCode 127 — Word Ladder / 單字接龍

🔗 [題目連結](https://leetcode.com/problems/word-ladder/)

---

## 📄 題目說明 | Problem Description

### 中文：
- 給定三個參數：

    - beginWord：起始單字

    - endWord：目標單字

    - wordList：字典中的單字列表

- 每次只能「改變一個字母」，而且改完的新單字必須存在於 wordList 中。
- 請找出從 beginWord 轉換到 endWord 的最短轉換序列長度（包含起點與終點）。 若無法完成轉換，回傳 0。

### English:
- Given beginWord, endWord, and a list of words wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

- Only one letter can be changed at a time

- Each transformed word must exist in the word list
- If no such transformation exists, return 0.

### Examples:

- Example 1

    - Input:
        - beginWord = "hit"
        - endWord = "cog"
        - wordList = ["hot","dot","dog","lot","log","cog"]

    - Output: 5

    - Explanation: hit → hot → dot → dog → cog

- Example 2

    - Input:
    - beginWord = "hit"
    - endWord = "cog"
    - wordList = ["hot","dot","dog","lot","log"]

    - Output: 0

    - Explanation: endWord 不在字典中

---

## 🧠 解題思路 | Solution Idea

- 這題的核心是：找最短路徑，而狀態之間的轉換是「單字 → 單字」。

- 為什麼用 BFS？

- 每個單字都可以視為一個「節點」

- 若兩個單字只差一個字母，就有一條邊

- 題目要求 最短轉換步數

👉 這正是 BFS（廣度優先搜尋） 的經典使用情境

- 關鍵優化：中介樣式（Intermediate Pattern）

- 如果每次都暴力比較「是否只差一個字母」，會非常慢。
- 因此我們先做 預處理：

    - 假設單字長度為 L

    - 對每個單字，把每一個位置換成 *，產生 L 個 pattern

    - 例如單字 hot： *ot , h*t , ho*

    - 然後建立一個表： = pattern_map[pattern] = 所有符合這個 pattern 的單字

    - 這樣一來：只要產生 pattern 就能立刻拿到「只差一個字母的所有鄰居」

---

## 💻 程式碼實作 | Code (Python)
```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)
        L = len(beginWord)

        # 預處理：建立 pattern（中介樣式）對應表
        for w in wordList:
            for i in range(L):
                pattern = w[:i] + '*' + w[i + 1:]
                pattern_map[pattern].append(w)

        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, steps = queue.popleft()

            if current_word == endWord:
                return steps

            for i in range(L):
                pattern = current_word[:i] + '*' + current_word[i + 1:]
                for nei in pattern_map.get(pattern, []):
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))

        return 0
```

### 🔍 程式碼逐段說明 | Line-by-line Explanation
```python
if endWord not in wordList:
    return 0
```

- 如果 endWord 不在字典中，就不可能走到它

- 題目規定「每一步都必須在 wordList 中」
```python
pattern_map = defaultdict(list)
L = len(beginWord)
```

- L：單字長度（之後會用來產生 pattern）

- pattern_map：儲存 pattern → 單字清單
```python
for w in wordList:
    for i in range(L):
        pattern = w[:i] + '*' + w[i + 1:]
        pattern_map[pattern].append(w)
```

- 對字典中每個單字

- 產生 L 個中介樣式

- 建立「pattern → 可轉換單字」的對照表
```python
queue = deque([(beginWord, 1)])
visited = set([beginWord])
```
- BFS queue 存 (目前單字, 已走步數)

- 初始從 beginWord 開始，步數是 1（包含自己）

- visited 用來避免重複走訪（防止無限循環）

    ```text
    (beginWord, 1)      → 一筆資料
    [(beginWord, 1)]    → 裝資料的 list
    deque( ... )        → 把 list 變成 queue
    ```
    - set([beginWord]) 👉 把這個 list 轉成 set

    - 為什麼不能直接寫set(beginWord)？

    - 因為：
    ```python
    set("hit")  # {'h', 'i', 't'} ❌
    ```

    - Python 會把字串當成「可迭代物件」，一個字元一個字元拆。

    所以一定要包成 list：
    ```python
    set(["hit"])  # {'hit'} ✅
    ```
```python
current_word, steps = queue.popleft()
```

- BFS 每次取出最早加入的節點（確保層級順序）
```python
if current_word == endWord:
    return steps
```

- BFS 的關鍵性質：

- 第一次到達 endWord，一定是最短路徑

- 可直接回傳答案
```python
for i in range(L):
    pattern = current_word[:i] + '*' + current_word[i + 1:]
```

- 對目前單字產生所有可能的 pattern
```python
for nei in pattern_map.get(pattern, []):
    if nei not in visited:
        visited.add(nei)
        queue.append((nei, steps + 1))
```
- 為什麼是 pattern, []？

    - 先看 .get() 的語法：
        ```python
        dict.get(key, default)
        ```

    - 字面意思是：「如果 key 存在，就給我對應的 value；如果不存在，就給我 default」

    - 套到這一行
    ```python
    pattern_map.get(pattern, [])
    ```

    - 字面意思是：「如果這個 pattern 有對應的單字列表，就拿出來；如果沒有，就當作它對應一個空 list」

- 從 pattern 表中取出所有只差一個字母的鄰居

- 沒拜訪過才加入 queue

- 步數 +1（代表多走一步）

---

### 🧪 範例流程 | Example Walkthrough
```text
beginWord = "hit"
endWord   = "cog"
wordList  = ["hot","dot","dog","lot","log","cog"]
```

### 🧠 核心概念（跟你的程式碼一樣）

- 先建 pattern_map：pattern → 可能的鄰居單字

- 再 BFS：queue 存 (current_word, steps)

- visited：避免同一個單字重複入 queue

### 1️⃣ 預處理：建立 pattern_map（完全照你的 for 迴圈）

你的程式碼：
```python
pattern_map = defaultdict(list)
L = len(beginWord)  # 3

for w in wordList:
    for i in range(L):
        pattern = w[:i] + '*' + w[i + 1:]
        pattern_map[pattern].append(w)
```
### wordList 每個字產生 3 個 pattern
| w   | i=0   | i=1   | i=2   |
| --- | ----- | ----- | ----- |
| hot | `*ot` | `h*t` | `ho*` |
| dot | `*ot` | `d*t` | `do*` |
| dog | `*og` | `d*g` | `do*` |
| lot | `*ot` | `l*t` | `lo*` |
| log | `*og` | `l*g` | `lo*` |
| cog | `*og` | `c*g` | `co*` |

建完後 pattern_map 長這樣（只列重要的）

- *ot → [hot, dot, lot]

- h*t → [hot]

- ho* → [hot]

- do* → [dot, dog]

- d*t → [dot]

- d*g → [dog]

- lo* → [lot, log]

- l*t → [lot]

- l*g → [log]

- *og → [dog, log, cog]

- c*g → [cog]

- co* → [cog]

👉 這就是為什麼 BFS 時不用掃整個 wordList：只要查 pattern，就能拿到候選鄰居。

### 2️⃣ BFS 初始化（完全照你的程式碼）

你的程式碼：
```python
queue = deque([(beginWord, 1)])
visited = set([beginWord])
```

所以初始：

- queue = [(hit, 1)]

- visited = {hit}

### 3️⃣ BFS 開始跑（每一次 while queue 都詳細列出）

你的 BFS 主體：
```python
while queue:
    current_word, steps = queue.popleft()
    if current_word == endWord:
        return steps
    for i in range(L):
        pattern = current_word[:i] + '*' + current_word[i + 1:]
        for nei in pattern_map.get(pattern, []):
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, steps + 1))
```
### ✅ Round 1：pop 出 hit

- popleft() → current_word = "hit", steps = 1

- 檢查：

    - hit == cog ❌

- 對 "hit" 產生 3 個 pattern：

    1. i=0 → *it → pattern_map 沒有 → []

    2. i=1 → h*t → [hot]

    3. i=2 → hi* → pattern_map 沒有 → []

- 所以只會找到鄰居 hot

    - hot 不在 visited → 加入

- 更新後：

    - visited = {hit, hot}

    - queue = [(hot, 2)]

### ✅ Round 2：pop 出 hot

- pop → current_word="hot", steps=2

- hot == cog ❌

- hot 的 patterns：

    1. *ot → [hot, dot, lot]

    2. h*t → [hot]

    3. ho* → [hot]

- 依序掃鄰居（完全照你的內層 for）：

    - 從 *ot 拿到：hot, dot, lot

        - hot 已 visited → 跳過

        - dot 未 visited → 加入 (dot, 3)

        - lot 未 visited → 加入 (lot, 3)

    - h*t → [hot]（已訪問）

    - ho* → [hot]（已訪問）

- 更新後：

    - visited = {hit, hot, dot, lot}

    - queue = [(dot, 3), (lot, 3)]

### ✅ Round 3：pop 出 dot

- pop → current_word="dot", steps=3

- dot == cog ❌

- dot 的 patterns：

    1. *ot → [hot, dot, lot]

    2. d*t → [dot]

    3. do* → [dot, dog]

- 掃鄰居：

    - *ot：

        - hot visited

        - dot visited

        - lot visited

    - d*t：dot visited

    - do*：

        - dot visited

        - dog 未 visited → 加入 (dog, 4)

    - 更新後：

        - visited = {hit, hot, dot, lot, dog}

        - queue = [(lot, 3), (dog, 4)]

### ✅ Round 4：pop 出 lot

- pop → current_word="lot", steps=3

- lot == cog ❌

- lot 的 patterns：

    1. *ot → [hot, dot, lot]

    2. l*t → [lot]

    3. lo* → [lot, log]

- 掃鄰居：

    - *ot 全 visited

    - l*t lot visited

    - lo*：

        - lot visited

        - log 未 visited → 加入 (log, 4)

- 更新後：

    - visited = {hit, hot, dot, lot, dog, log}

    - queue = [(dog, 4), (log, 4)]

### ✅ Round 5：pop 出 dog

- pop → current_word="dog", steps=4

- dog == cog ❌

- dog 的 patterns：

    1. *og → [dog, log, cog]

    2. d*g → [dog]

    3. do* → [dot, dog]

- 掃鄰居：

    - *og：

        - dog visited

        - log visited

        - cog 未 visited → 加入 (cog, 5)

    - d*g dog visited

    - do* dot/dog visited

- 更新後：

    - visited = {hit, hot, dot, lot, dog, log, cog}

    - queue = [(log, 4), (cog, 5)]

### ✅ Round 6：pop 出 log

- pop → current_word="log", steps=4

- log == cog ❌

- log patterns：

    1. *og → [dog, log, cog]

    2. l*g → [log]

    3. lo* → [lot, log]

- 掃鄰居：

    - *og：dog/log/cog 都 visited（cog 已經在 visited 了）

    - 其他也都是 visited

- 更新後：

    - queue = [(cog, 5)]（不變）

### ✅ Round 7：pop 出 cog（命中 endWord）

- pop → current_word="cog", steps=5

- cog == endWord ✅

- 直接：
```python
return steps  # 5
```
### ✅ 最終答案

- 回傳：5

- 最短路徑之一： hit → hot → dot → dog → cog

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 預處理：O(N × L)

    - BFS：每個單字最多進 queue 一次，整體約 O(N × L)

- 空間複雜度：

    - pattern_map：O(N × L)

    - visited + queue：O(N)

---

## ✍️ 我學到的東西 | What I Learned

- 只要題目出現「最短步數／最少轉換」→ 先想 BFS

- 單字題常可用「中介樣式（pattern）」來優化鄰居查找

- BFS + visited 是避免 TLE 與無限循環的關鍵

- s  把「字」想成「圖的節點」，問題會瞬間清楚很多