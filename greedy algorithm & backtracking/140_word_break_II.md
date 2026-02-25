# 📍 LeetCode 140 — Word Break II | 回傳所有可拆分句子（DFS + Memo）

🔗 https://leetcode.com/problems/word-break-ii/

---

## 📄 題目說明 | Problem Description
### 中文

給你字串 s 和字典 wordDict，請把 s 拆成「由字典單字組成的句子」，回傳所有可能句子（單字之間用空格）。

### English

Return all possible sentences where s can be segmented into words from wordDict.

### Examples
- Example 1:

    - Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    - Output: ["cats and dog","cat sand dog"]
- Example 2:

    - Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
    - Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    - Explanation: Note that you are allowed to reuse a dictionary word.
- Example 3:

    - Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    - Output: []

---

## 🧠 解題思路 | Solution Idea（標準正解：DFS + Memo）

- 這題要「列出所有句子」，不是只回傳 True/False → Backtracking/DFS

- 同一個位置 i（同一段 suffix s[i:]）會被重複計算很多次 → Memoization 把結果記起來

- 定義 dfs(i)：

    - 回傳：從 s[i:] 開始，能組成的所有句子（list[str]）

---

## 💻 程式碼實作 | Code (Python)
```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}  # memo[i] = 所有從 s[i:] 能組出的句子 (List[str])

        def dfs(i: int) -> List[str]:
            # 1) 如果這個 i 已經算過，直接回傳記憶的結果
            if i in memo:
                return memo[i]

            # 2) base case：i 走到字串尾端，代表後面沒有字了
            #    回傳 [""] 是為了讓上層做拼接時好處理最後一個字
            if i == n:
                return [""]

            res = []  # 3) 用來收集所有從 s[i:] 開始的句子

            # 4) 嘗試字典中的每個單字 w
            for w in word_set:
                # 5) 如果 s 從位置 i 開始的前綴是 w，代表 w 可以當作下一個單字
                if s.startswith(w, i):
                    # 6) 遞迴：去找剩下的部分 s[i+len(w):] 能組成哪些句子
                    tails = dfs(i + len(w))

                    # 7) 把 w 和每個 tail 句子拼起來
                    for tail in tails:
                        if tail == "":
                            # 8) tail 為空代表 w 已經是最後一個字，不要加空格
                            res.append(w)
                        else:
                            # 9) tail 不空：w + 空格 + tail
                            res.append(w + " " + tail)

            # 10) 記憶化：把 i 的答案存起來
            memo[i] = res
            # 11) 回傳從 s[i:] 開始能形成的所有句子
            return res

        # 12) 題目要從 0 開始的所有句子
        return dfs(0)
```

### ✅ 1. 建立字典集合（加速查找 / 去重）
```python
word_set = set(wordDict)
```
- 把 list 轉成 set

- 優點：

    - 自動去重（不是主要目的）

    - 迭代與 membership 查找更快

- 這題主要是「避免 wordDict 有重複字」以及後面做 startswith 時不受重複影響

### ✅ 2. 取得字串長度
```python
n = len(s)
```
- 後面用來判斷 base case：i == n 代表到尾端

### ✅ 3. 記憶化字典
```python
memo = {}
```
- memo[i] 會存「從 s[i:] 開始能形成的所有句子」

- 避免同一個 i 重複 DFS（不然會 TLE）

### ✅ 4. 定義 DFS：從 i 開始能組出哪些句子
```python
def dfs(i: int) -> List[str]:
```
- i 是目前在 s 的索引位置

- 回傳 list[str]：所有從 s[i:] 能形成的句子

### ✅ 5. 先看 memo（有算過就直接拿）
```python
if i in memo:
    return memo[i]
```
- 這是最關鍵的加速

- 一旦某個 i 算過，後面遇到同 i 直接 O(1) 拿結果

### ✅ 6. base case：走到字串尾端
```python
if i == n:
    return [""]
```
- 為什麼回傳 [""] 而不是 []？
    - 因為 [""] 表示：

        - 「我已經成功拆到底了，有 1 種完成方式，就是後面沒有任何字」

- 這讓上層可以做拼接：

    - 如果 tail 是 ""，代表目前單字是最後一個字 → 不加空格

### ✅ 7. 建立結果 list
```python
res = []
```
- 收集從 s[i:] 形成的所有句子

- 最後會存到 memo[i]

### ✅ 8. 嘗試每個字 w
```python
for w in word_set:
```
- 這裡是在「試下一個單字可以選誰」

- 每個 w 都是一個分支

### ✅ 9. 檢查 w 是否能接在位置 i
```python
if s.startswith(w, i):
```
- 代表：s[i:i+len(w)] == w

- 如果不符合，w 不能當下一個字

- 符合就往下遞迴

### ✅ 10. 遞迴求剩下 suffix 的所有句子
```python
tails = dfs(i + len(w))
```
- 把問題縮小：

    - 原本：要拆 s[i:]

    - 現在：選了 w 之後，要拆 s[i+len(w):]

- tails 是「剩下那段能形成的句子列表」

### ✅ 11. 把 w 和每個 tail 組合起來
```python
for tail in tails:
```
- tails 可能有很多句子

- 每個 tail 都要和 w 拼出一個完整句子

### ✅ 12. tail == "" 表示 w 是最後一個字
```python
if tail == "":
    res.append(w)
```
- 因為 base case 回傳 [""]

- 當 tail 是空字串，代表：

    - 後面沒有字了

    - 這句完整就是 w 本身

- 避免 "w " 多一個空格

### ✅ 13. tail 不空就加空格拼接
```python
else:
    res.append(w + " " + tail)
```
- 例如 w="cats"，tail="and dog"

- 拼出 "cats and dog"

### ✅ 14. 存 memo
```python
memo[i] = res
```
- 這行是性能關鍵

- 以後遇到同 i 就不用再算 DFS

### ✅ 15. 回傳結果
```python
return res
```
- 回傳「從 s[i:] 開始」所有句子

### ✅ 16. 從 dfs(0) 開始
```python
return dfs(0)
```
- 題目要拆整個 s，所以從 index 0 開始

---

## 🧪 範例流程 | Example Walkthrough
```text
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
```
### Step 1：dfs(0)

可匹配：

- "cat" → dfs(3)

- "cats" → dfs(4)

### 路徑 A：選 "cat"

- dfs(3) 處理 "sanddog"

    - 匹配到 "sand" → dfs(7)

- dfs(7) 處理 "dog"

    - 匹配到 "dog" → dfs(10)

- dfs(10) = i==n → return [""]

    - 回來拼接：

        - dfs(7) 得 ["dog"]

        - dfs(3) 得 ["sand dog"]

        - dfs(0) 得 ["cat sand dog"]

### 路徑 B：選 "cats"

- dfs(4) 處理 "anddog"

    - 匹配到 "and" → dfs(7)

- 注意：dfs(7) 已 memo，直接拿 ["dog"]

- 拼接：

    - dfs(4) 得 ["and dog"]

    - dfs(0) 加上 ["cats and dog"]

### ✅ 最終輸出
```python
["cat sand dog", "cats and dog"]
```

---

## ⏱ 複雜度分析 | Complexity Analysis
- 時間複雜度

    - 最壞情況輸出數量可能很多（指數級）

    - DFS + memo 會避免重複算同一個 i

    - 但仍然可能產生大量句子

    - ✅ 常用面試說法：

        - Time = O(total output size)（至少要把所有句子輸出出來）

- 空間複雜度

    - memo 會存所有 suffix 的句子列表，可能非常大

    - recursion depth 最深 O(n)

    - ✅ Space = O(total output size) + O(n)

---

## ✍️ 我學到的東西 | What I Learned

- 140 跟 139 最大差別：

    - 139 → dp boolean（可不可）

    - 140 → 要列出所有 → DFS + memo

- memo 的 key 用 index i，因為重複子問題是 s[i:]

- base case 回傳 [""] 是為了拼接最後單字不加空格

---

## 🧠 一句話總結

I use DFS to enumerate all valid sentences and memoize results for each starting index to avoid recomputing the same suffix.