# 🔤 LeetCode 139 – Word Break | 單詞拆分
🔗 題目連結：[https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)
---

## 📘 題目說明 | Problem Description

- **中文：**  
  給定一個字串 `s` 和一個字典 `wordDict`，判斷是否能將 `s` 完整拆成由字典中的單詞組成的序列。拆分後字串必須完全覆蓋 `s`，且字典內的單詞可重複使用。

- **English:**  
  Given a string `s` and a list of words `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. All characters must be used; words can be reused. :contentReference[oaicite:0]{index=0}

###  例子 Illustrations

| 輸入 (Input)                           | 輸出 (Output) |
|----------------------------------------|---------------|
| `s = "leetcode", wordDict = ["leet","code"]`             | `true`        |
| `s = "applepenapple", wordDict = ["apple","pen"]`       | `true`        |
| `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]` | `false`   |

---

## 🧠 動態規劃（Bottom‑Up DP）

### 中文思路：
1. 建立長度為 `n + 1` 的布林陣列 `dp`，其中 `dp[i]` 代表子字串 `s[0:i]` 是否可拆分。
2. 初始：`dp[0] = true`（空字串始終可拆分）。
3. 對每個 `i`（1~n），檢查所有可能拆分點 `j`（0~i-1），若 `dp[j]` 是 `true` 且 `s[j:i]` 在字典中，則標記 `dp[i] = true` 並跳出內層迴圈。
4. 回傳 `dp[n]` 表示是否能完整拆分 `s`。:contentReference[oaicite:1]{index=1}

### English Explanation:
1. Define a boolean DP array `dp` of size `n + 1`, where `dp[i]` indicates if `s[0:i]` can be segmented.
2. Set `dp[0] = true` (empty string).
3. For each `i`, loop through each `j` below `i`. If `dp[j]` is true and `s[j:i]` is in the word set, set `dp[i] = true` and break.
4. Return whether the entire string can be segmented. 

---

## 💻 Python 程式碼 | Code

```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```
```python
word_set = set(wordDict)
```
- 將 wordDict 轉為 set，加速後續查找（平均時間為 O(1)）。
```python
n = len(s)
```
- 記錄 s 的長度，方便後續 DP 陣列的大小設定。
```python
dp = [False] * (n + 1)
dp[0] = True
```
- 建立一個布林值陣列 dp，長度為 n + 1。

    - dp[i] 表示子字串 s[0:i] 是否能被拆分成字典中的單詞。

    - 初始化 dp[0] = True，代表空字串可以被「成功拆分」。
```python
for i in range(1, n + 1):
```
- 外層迴圈遍歷每個可能拆分位置 i，從 1 到 n。
```python
for j in range(i):
```
- 內層迴圈遍歷所有切分點 j，用來把 s[0:i] 分為兩段：

    - 左段是 s[0:j]

    - 右段是 s[j:i]
```python
if dp[j] and s[j:i] in word_set:
```
- 只在「左段 dp[j] 已被確認可拆分」且「右段 s[j:i] 在字典中」時才成立。
```python
dp[i] = True
break
```
- 若上述條件滿足，將 dp[i] 標記為 True，並跳出內層迴圈。表示 s[0:i] 可以被合法拆分。
```python
return dp[n]
```
- 最後，回傳 dp[n] 的值，即整個字串 s 是否可以完整拆分。

### 小結：
| 概念      | 說明                                                         |
| ------- | ---------------------------------------------------------- |
| `dp` 陣列 | `dp[i]` 表示 `s[0:i]` 是否可拆分                                  |
| 初始值     | `dp[0] = True`（空字串可拆分）                                     |
| 狀態轉移    | 若 `dp[j]` = True 且 `s[j:i]` in dictionary → `dp[i]` = True |
| 最終判斷    | 回傳 `dp[n]` 判定整串能否拆分                                        |

---

## 範例
```mathematica
s = "leetcode"，長度 n = 8
word_set = {"leet", "code"}
dp = [True, False, False, False, False, False, False, False, False]
  index:  0     1      2      3      4      5      6      7      8
```

###  主迴圈模擬（逐步填滿 dp）

### i = 1 至 3 （「l」「le」「lee」）

- 嘗試不同 j：
  - j = 0：檢查 `"l"` / `"le"` / `"lee"` 是否在字典中？
  - 都不在 → `dp[1] = dp[2] = dp[3] = False`

### i = 4（`"leet"`）

- j = 0：`dp[0] = True`，且 `"leet"` 在字典中 → `dp[4] = True`，跳出內層迴圈  

### i = 5 至 7 分析

- 這些子字串分別是 `"leetc"`, `"leetco"`, `"leetcod"`

- 即使遍歷 j，也沒能同時符合 `dp[j] = True` 且字典內的條件  
    → 所以 `dp[5] = dp[6] = dp[7] = False`
    - 索引: 0 1 2 3 4 5 6 7 8
    - dp: [T, F, F, F, T, F, F, F, T ]
    - `dp[8] = True`，代表整串可拆分成功。

### 視覺化比對（dp 變化）
|   i | 拆分點 (j)            | 條件                         | dp\[i] 結果 |
| --: | ------------------ | -------------------------- | --------- |
| 1–3 | 無法拆成字典詞            | `"l"`、`"le"`、`"lee"` 不在字典  | False     |
|   4 | j=0 (`"leet"` 在字典) | `dp[0]=True` 且 `"leet"` 合法 | **True**  |
| 5–7 | 無切分成功              | 無 j 同時滿足條件                 | False     |
|   8 | j=4 (`"code"` 在字典) | `dp[4]=True` 且 `"code"` 合法 | **True**  |

### 解題關鍵技巧 | Insights

- 使用 dp[i] 記錄是否可拆分到特定位置。

- 內層 break 提升效率。

- 善用 set 優化字典查詢。

- 這是 bottom‑up DP，清晰易懂又效率高。

---

## ⏱ 複雜度分析 | Complexity
| 類型    | 複雜度       |
| ----- | --------- |
| 時間複雜度 | O(n² × k) |
| 空間複雜度 | O(n)      |

- n 為字串長度，k 為平均計算子字串存在於字典中的成本（使用 set 為 O(1)）。
- O(n² × k) 其中 k 是子字串平均或最長長度（最壞可達 n）。

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- DP 解法能有效地避免重複計算，從指標 dp[j] 知道前半部分是否可拆分再判斷後半即可。

- Hash set 的字典查找 O(1) 提升效能。

- Top‑Down 與 BFS 是這題常用的替代策略。

### English：

- DP provides an optimal solution by building up from smaller substrings.

- Using a hash set for lookup dramatically improves performance.

- Memoized recursion or BFS are valid alternate patterns depending on preference and context.