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
### 中文
運用 **字母頻率計數**（Frequency Counting）快速檢查每個字母是否足夠：

1. 建立一個 HashMap 或長度 26 的陣列 `count`，記錄 `magazine` 每個字母出現的頻率。
2. 遍歷 `ransomNote`，逐字符檢查並扣減對應的字母數量：
   - 若某次扣減後頻率變為負值，表示 `magazine` 不足以提供該字母 → 直接回傳 `false`。
3. 完成遍歷後，若都沒有發生匱乏，則回傳 `true`。

### English
Use Frequency Counting to quickly check whether each letter is sufficient:

1. Build a HashMap or an array of length 26 to record the frequency of each character in magazine.

2. Iterate through ransomNote and check each character one by one:

    - If the frequency of any character becomes negative after decrementing, it means magazine does not have enough of that character → return false immediately.

3. If the loop completes without any shortage, return true.

---

## 💻 程式碼範例 | Python Code

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