# 🧮 LeetCode 647 — Palindromic Substrings（加入 DP 方法）  
🔗 [題目連結](https://leetcode.com/problems/palindromic-substrings/)

---

## 題目說明 | Problem Statement  
給定一個字串 `s`，請你統計它有多少個 **連續子字串（substring）** 是回文（palindrome）。  
A substring is palindromic if it reads the same forwards and backwards.

比方說：  
- 輸入：`"abc"` → 輸出：3 （"a", "b", "c"）  
- 輸入：`"aaa"` → 輸出：6 （"a","a","a","aa","aa","aaa"） 

限制條件：`1 ≤ s.length ≤ 1000` 

### Examples
- Example 1:

    - Input: s = "abc"
    - Output: 3
    - Explanation: Three palindromic strings: "a", "b", "c".

- Example 2:

    - Input: s = "aaa"
    - Output: 6
    - Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

---

## 解題思路 | Solution Idea

### 中心擴展法（Expand Around Center）

- 每個回文都有一個「中心」：  
  - 對於奇數長度回文，中心在某個單一字符  
  - 對於偶數長度回文，中心在兩個字符之間  
- 所以，我們可以對每個可能的中心往左右擴展，只要左右字符相等就算一個回文。  
- 為了覆蓋奇數與偶數情況，我們對每個索引 `i` 做兩次擴展：一次 `expand(i, i)`（odd），一次 `expand(i, i+1)`（even）。  
- 每次成功擴展時就加一個計數器。  

這種方法時間複雜度是O(n^2)，空間複雜度O(1)（僅用幾個指標）。

也可以用動態規劃（DP）做：用 `dp[i][j]` 表示 `s[i..j]` 是否為回文，若 `s[i] == s[j]` 且 `dp[i+1][j-1]` 為真則為真。這法也能 O(n^2) 解，但空間是 O(n^2)。

---

## 程式碼示例（Python：中心擴展法）

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> int:
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(n):
            # odd-length 回文，以 s[i] 為中心
            count += expand(i, i)
            # even-length 回文，以 s[i] 和 s[i+1] 為中心
            count += expand(i, i + 1)

        return count
```
```python
        def expand(l: int, r: int) -> int:
            res = 0
            # 當左右沒超出邊界，且兩邊字符一樣（是回文）
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1        # 是一個回文子字串
                l -= 1          # 向左擴展
                r += 1          # 向右擴展
            return res          # 回傳這次中心擴展找到的回文數量
```
- 這個 helper function 是中心擴展的核心：
    - 只要左右字符還相等，就持續向外擴展，並記錄找到的回文數量。

```python
        for i in range(n):
            # 奇數長度回文：中心是 s[i]
            count += expand(i, i)

            # 偶數長度回文：中心是 s[i] 和 s[i+1]
            count += expand(i, i + 1)
```
- 這裡對每個 i，都進行兩次擴展：

    - 以 s[i] 為中心，找奇數長度回文

    - 以 s[i] 和 s[i+1] 為中心，找偶數長度回文

```python
        return count
```
- 回傳總共找到的回文子字串數量

---

## 🧪 範例說明：s = "abba"

程式會跑以下內容來計算所有回文子字串數量：
```python
s = "abba"
n = 4
```
### i = 0

1. expand(0, 0)：中心是 'a'

    - 'a' → 是回文 → count = 1

2. expand(0, 1)：中心是 'a' 和 'b'

    - 'ab' → 不是回文 → count = 1

### i = 1

1. expand(1, 1)：中心是 'b'

    - 'b' → 是回文 → count = 2

2. expand(1, 2)：中心是 'b' 和 'b'

    - 'bb' → 是回文 → count = 3

    - 'abba'（左擴右擴）→ 是回文 → count = 4

### i = 2

1. expand(2, 2)：中心是 'b'

    - 'b' → 是回文 → count = 5

2. expand(2, 3)：中心是 'b' 和 'a'

    - 'ba' → 不是回文 → count = 5

### i = 3

1. expand(3, 3)：中心是 'a'

    - 'a' → 是回文 → count = 6

2. expand(3, 4)：超出邊界 → 不做

### ✅ 最終結果：count = 6

- 所有回文子字串包括：

    - 單字元："a", "b", "b", "a"

    - 多字元："bb", "abba"

### ⏱ 時間與空間複雜度 | Complexity
| 項目 | 複雜度                        |
| -- | -------------------------- |
| 時間 | ( O(n^2) )（每個中心最多向外擴展 n 次） |
| 空間 | ( O(1) )（只用變數記錄 count）     |

---

## 動態規劃（DP） | Dynamic Programming Approach  

### 說明 | Idea  

- 我們可以建立一個二維布林陣列 `dp[i][j]`，表示子字串 `s[i..j]` 是否為回文（inclusive）。  
- 初始條件：  
  • 當 `i == j` 時（長度為 1 的子字串），一定是回文 → `dp[i][i] = True`  
  • 當 `j = i+1`（長度為 2 的子字串），若 `s[i] == s[j]` 則也是回文 → `dp[i][j] = (s[i] == s[j])`  
- 對於長度 ≥ 3 的子字串 `s[i..j]`：  
  若 `s[i] == s[j]` 且 `dp[i+1][j-1]` 為真，則 `dp[i][j] = True`。  
- 每當我們發現 `dp[i][j] = True`，就把計數 `count` 加 1。  
- 最後 `count` 就是所有回文子字串的數量。  

這樣方法時間複雜度是 \(O(n^2)\)，空間複雜度也是 \(O(n^2)\)（因為我們要存一個 n×n 的 dp 陣列）。  

---

## ✅ 程式碼（Python + DP 方法）

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示 s[i..j] 是否為回文
        dp = [[False] * n for _ in range(n)]
        count = 0

        # 填長度為 1 和 2 的基本情況
        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # 處理長度 ≥ 3
        # len_sub 是子字串長度
        for length in range(3, n + 1):  # 從 3 到 n
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count
```
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示 s[i..j] 是否為回文
        dp = [[False] * n for _ in range(n)]
        count = 0
```
- n = len(s)：取得字串長度

- dp = [[False] * n for _ in range(n)]：建立一個 n×n 的二維陣列，初始都設為 False

- count = 0：計數回文子字串的個數

### ✅ 處理長度為 1 的子字串（每個單字符）
```python
for i in range(n):
    dp[i][i] = True
    count += 1
```
- 每個單字符 s[i] 自己本身就是一個回文

- 所以把 dp[i][i] 設為 True，並 count++

### ✅ 處理長度為 2 的子字串
```python
for i in range(n - 1):
    if s[i] == s[i + 1]:
        dp[i][i + 1] = True
        count += 1
```
- 對每個相鄰對 (i, i+1)，若 s[i] == s[i+1]，那麼 s[i..i+1] 是回文

- 把 dp[i][i+1] = True 並把 count 加 1

### ✅ 處理長度 ≥ 3 的子字串
```python
for length in range(3, n + 1):  # 子字串長度從 3 到 n
    for i in range(0, n - length + 1):
        j = i + length - 1
        if s[i] == s[j] and dp[i + 1][j - 1]:
            dp[i][j] = True
            count += 1
```
- length：代表子字串的長度，從 3 開始到 n

- i：子字串起始索引

- j = i + length - 1：子字串結尾索引

- 條件：s[i] == s[j]（首尾相等）且裡面的子字串 dp[i+1][j-1] 是回文

    - 如果這兩個條件都成立，就把 dp[i][j] = True，並 count++

### ✅ 回傳結果
```python
return count
```
- 最後把計算好的回文子字串數量回傳

---

## 🧪 範例：s = "ababa"

- 字串長度 n = 5。最終要算出所有回文子字串數量。

- 初始：
```ini
dp = 5×5 的 False 陣列
count = 0
```

### 1. 處理長度 1（單一字母）

對每個 i：

- dp[0][0] = True，count = 1 → 子字串 "a"

- dp[1][1] = True，count = 2 → 子字串 "b"

- dp[2][2] = True，count = 3 → "a"

- dp[3][3] = True，count = 4 → "b"

- dp[4][4] = True，count = 5 → "a"

此時 dp 主對角線都是 True。

### 2. 處理長度 2

檢查每對相鄰字母：

- i = 0 → 比 "a" 和 "b"：不相等 → dp[0][1] 保持 False

- i = 1 → 比 "b" 和 "a"：不相等 → dp[1][2] False

- i = 2 → 比 "a" 和 "b"：不相等

- i = 3 → 比 "b" 和 "a"：不相等

這個例子裡沒有連續兩個字母相同，所以長度 2 的 dp 都是 False，count 不變。

### 3. 處理長度 ≥ 3

我們從 length = 3 開始：

#### length = 3

- i = 0, j = 2 → 子字串 "aba"
    - 檢查 s[0] == s[2]？是（'a' == 'a'）
    - 檢查 dp[1][1]？是 True（內部 "b" 是回文）

        → 所以 dp[0][2] = True，count = 6

- i = 1, j = 3 → "bab"
    - s[1] == s[3] → 'b' == 'b'
    - dp[2][2] 是 True
    
        → dp[1][3] = True，count = 7

- i = 2, j = 4 → "aba"
    - s[2] == s[4] → 'a' == 'a'
    - dp[3][3] 是 True
        
        → dp[2][4] = True，count = 8

#### length = 4

- i = 0, j = 3 → "abab"
    - s[0] == s[3]？'a' 和 'b' 不同 → 跳過

- i = 1, j = 4 → "baba"
    - s[1] == s[4]？'b' 和 'a' 不同 → 跳過

#### length = 5

- i = 0, j = 4 → "ababa"
    - s[0] == s[4]？是
    - dp[1][3] 是 True（我們在 length = 3 時標記了 "bab" 是回文）
        
        → dp[0][4] = True，count = 9

### 4. 最終結果

count = 9

列出所有回文子字串（含重複位置）：
```arduino
"a", "b", "a", "b", "a",    (5 個長度 1)
"aba", "bab", "aba",        (3 個長度 3)
"ababa"                      (1 個長度 5)
```

總共 9 個。

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度： O(n^2)
    - 雙層迴圈：length 從 3 到 n，i 從 0 到約 n，裡面檢查常數操作

- 空間複雜度： O(n^2)
    - 使用一個 n×n 的 dp 陣列

---

## 🧠 我學到什麼 / What I Learned

- DP 方法能系統地利用已知子問題（內部子字串是否回文）來決定較長子字串是否回文。

- 雖然空間花得比較多，但邏輯清楚易懂。

- 中心擴展法比 DP 省空間（只用 O(1) 空間），但 DP 常作為備選方案，尤其在變體題目裡很好用。

- 在面試中，能同時提出這兩法並做比較是加分的。