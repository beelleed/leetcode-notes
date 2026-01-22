# 🆔 LeetCode 383 – Ransom Note | 勒索信
🔗 題目連結：[https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

---

## 📄 題目說明 | Problem Description

- **中文：**  
  給你兩個字串 `ransomNote` 和 `magazine`，判斷是否能用 `magazine` 的字母拼出 `ransomNote`。每個字母只能使用一次。

- **English:**  
  Given two strings, `ransomNote` and `magazine`, return `true` if you can construct the `ransomNote` using letters from `magazine`. Each letter in `magazine` can only be used once.

### Examples
- Example 1:

    - Input: ransomNote = "a", magazine = "b"
    - Output: false

- Example 2:

    - Input: ransomNote = "aa", magazine = "ab"
    - Output: false

- Example 3:

    - Input: ransomNote = "aa", magazine = "aab"
    - Output: true

---

## 🧠 解法邏輯 | Solution Idea

### 方法一
- 這題可以拆成 兩個非常清楚的步驟：

    - 先統計每個字元出現的次數

    - 再照原字串順序，找第一個次數為 1 的字元

- 關鍵在於：

    - 「第一個」→ 一定要照原字串順序掃

    - 「出現一次」→ 需要事先知道每個字元的總次數

👉 使用 Counter 可以讓第 1 步非常乾淨。

### 方法二
運用 **字母頻率計數**（Frequency Counting）快速檢查每個字母是否足夠：

1. 建立一個 HashMap 或長度 26 的陣列 `count`，記錄 `magazine` 每個字母出現的頻率。
2. 遍歷 `ransomNote`，逐字符檢查並扣減對應的字母數量：
   - 若某次扣減後頻率變為負值，表示 `magazine` 不足以提供該字母 → 直接回傳 `false`。
3. 完成遍歷後，若都沒有發生匱乏，則回傳 `true`。

---

## 💻 程式碼範例 | Python Code
### 方法一
```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
```python
count = Counter(s)
```

- Counter(s) 會統計字串中每個字元出現的次數

- key 是字元，value 是次數
    例如：
    ```python
    s = "leetcode"
    count = {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}
    ```
```python
for i, c in enumerate(s):
```

- 用 enumerate 同時取得：

    - i：index

    - c：字元

- 確保是「照原字串順序」掃描
```python
if count[c] == 1:
    return i
```

- 檢查目前字元 c 是否只出現一次

- 第一個符合條件的字元，直接回傳 index
```python
return -1
```

- 如果整個字串掃完都沒有找到

- 代表不存在不重複字元

---

## 🧪 範例 | Example Walkthrough
- Example 1
```text
s = "leetcode"
```

- count = {l:1, e:3, t:1, c:1, o:1, d:1}

- 掃描順序：

    - i=0, c='l' → count['l']=1 ✅
        
        → 回傳 0

- Example 2
```text
s = "loveleetcode"
```

- 掃描：

    - l(2), o(2), v(1) ✅

- 回傳 index = 2

- Example 3
```text
s = "aabb"
```

- 所有字元出現次數都 > 1

- 回傳 -1

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - Counter(s)：O(n)

    - 再掃一次字串：O(n)

    - 👉 總體 O(n)

- 空間複雜度：

    - Counter 儲存所有不同字元

    - 👉 O(Σ)，Σ 為字元種類數

---

## ✍️ 我學到的東西 | What I Learned

- Counter 非常適合用在「字元出現次數統計」的題目

- 題目要求「第一個」時，一定要再掃一次原字串

- 不要把 index 跟字元混在一起當 key

- enumerate 可以讓 index 與字元同時保持清楚

---

### 方法二
```python
from collections import Counter
from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for ch in ransomNote:
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        return True
```
```python
counts = Counter(magazine)
```
🧮 用 Counter 統計 magazine 中每個字母出現的次數。
例如：
```python
magazine = "aab"
counts = {'a': 2, 'b': 1}
```
```python
for ch in ransomNote:
```
🔁 遍歷 ransomNote 中的每一個字母 ch，看看能不能從 counts 裡找出來。
```python
counts[ch] -= 1
```
✂️ 每用掉一個字母，就把對應的數量 -1。
```python
if counts[ch] < 0:
    return False
```
🚨 如果扣完某個字母後數量小於 0，代表 magazine 中該字母已經不夠用了，直接回傳 False。
```python
return True
```
✅ 如果所有字母都夠用，代表可以構造 ransomNote，就回傳 True。
### 🧠 小結

- 這段程式碼透過 Counter 快速建立字母頻率表，逐一扣減，檢查是否足夠。

    - 簡單高效

    - Counter 提供預設值，查不到會自動視為 0，不會報錯。

---

## 🧪 示例流程 | Example Walkthrough

範例一：ransomNote = "aab", magazine = "baa"

```python
counts = Counter(magazine)  # ➜ Counter({'b': 1, 'a': 2})
```
開始處理 ransomNote = "aab"：

### 第一步：處理字元 'a'
```python
counts['a'] -= 1   # 由 2 減為 1
if counts['a'] < 0: ➜ False
```
✅ a 還有剩，不用返回。

### 第二步：處理字元 'a'（第二個）
```python
counts['a'] -= 1   # 由 1 減為 0
if counts['a'] < 0: ➜ False
```
✅ a 剛好用完，也沒問題。

### 第三步：處理字元 'b'
```python
counts['b'] -= 1   # 由 1 減為 0
if counts['b'] < 0: ➜ False
```
✅ b 剛好夠用。

### 全部處理完畢
```python
return True
```
因為全部字元都有足夠的數量可以使用，所以最後成功回傳 True。
### 📦 最後狀態：
```python
counts = Counter({'a': 0, 'b': 0})
```

---

## ⏱ 複雜度分析 | Complexity Analysis
| 分類    | 複雜度                                          |
| ----- | -------------------------------------------- |
| 時間複雜度 | `O(m + n)`  (m=magazine 長度, n=ransomNote 長度) |
| 空間複雜度 | `O(1)` — 因為固定字符集（26 個英文字母）                   |

---

## 注意事項 | Tips & Pitfalls

- 不可只檢查是否存在該字母，必須確認數量是否足夠。

- Counter 自帶方便的預設值行為（查不到字母時為 0），非常適合這題型使用。

---