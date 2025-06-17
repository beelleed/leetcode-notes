# 014. Longest Common Prefix 最長共同前綴
[LeetCode 題目連結](https://leetcode.com/problems/longest-common-prefix/)

## 🧩 題目描述 Description

**中文**
給定一組字串陣列 strs，找出其中所有字串的最長共同前綴。如果不存在共同前綴，回傳空字串 ""。

**English**
Given an array of strings strs, return the longest common prefix among them. If no common prefix exists, return an empty string.

---

## ✅ 解法一：以第一個字串為基準

### 💡 解題想法 Idea

**中文**: 
假設第一個字串為共同前綴的開始點，逐字元比對每個字元位置是否與所有其他字串一致。若有不一致，立即回傳已累積的前綴。

**English**: 
Assume the first string is the starting point of the common prefix. Compare each character position against every other string; if a mismatch occurs, return the prefix built so far.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        for i in range(len(strs[0])):  # 逐位置比對
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return prefix  # 一遇到不一樣就結束
            prefix += char  # 如果都一樣，加入 prefix
        return prefix
```

## 🔍 解題步驟說明
- 若 strs 為空，直接回傳 ""。

- 使用第一個字串的長度作為「最大可能前綴長度」。

- 對每一個字元位置 i：

    - 取出 ch = strs[0][i]，作為基準字元。

    - 遍歷所有 word in strs：

        - 若某字串長度不足、或 word[i] 不等於 ch，就回傳目前前綴。

- 若第一個字串一整串都比對完，代表所有字串相同，回傳整串。

## 🧾 示意圖解（以 ["flower", "flow", "flight"] 為例）：
| index | word1 | word2 | word3 | 結論          |
| ----- | ----- | ----- | ----- | ----------- |
| 0     | f     | f     | f     | 加入          |
| 1     | l     | l     | l     | 加入          |
| 2     | o     | o     | i     | 結束，因為 i ≠ o |
最終答案為 "fl"

## ✅ 注意優缺點
- 優點：邏輯直觀，易於理解。

- 缺點：需要額外檢查 i >= len(word)，避免越界；效能雖 OK，但略不優雅。

## ⏱️ 複雜度 Complexity
- 時間 Time: 最多比較 n * m 次，n 是字串數，m 是第一個字串長度 → O(n * m)

- 空間 Space: 除了 prefix 儲存使用常數外，無額外空間 → O(1)

---

## ✅ 解法二：以最短字串為基準

### 💡 解題想法 Idea

**中文**: 
因為共同前綴不會超過最短字串長度，所以先找最短字串作為基準。依位置比對所有字串的字元，第一個不匹配的位置即為前綴結束點。

**English**: 
The common prefix can't exceed the length of the shortest string. So we find the shortest string first, then compare each position across all strings. The first mismatch determines the end of the prefix.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 找出最短字串，因為前綴不可能長過最短字串
        shortest = min(strs, key=len)
        
        # 逐字符比對
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    # 一旦發現不同，回傳目前 i 所構成的子串
                    return shortest[:i]
        # 全部相同就返回最短整串
        return shortest
```

## 🔍 解題步驟說明

- 若 strs 為空，回傳 ""。

- 使用 shortest = min(strs, key=len) 取得最短字串作為長度上限。

- 逐字符比對

    - 外迴圈：for i, ch in enumerate(shortest)，代表位置 0、1、2...

    - 內迴圈：遍歷 strs 中其他每條字串

    - 若不等於 ch → 回傳 shortest[:i]，即當前比對成績。

    - 若整個 shortest 都比對過，代表共同前綴即為 shortest，直接回傳。

## ✅ 優勢比較
- 自然避開越界問題：不用再做長度檢查。

- 程式簡潔、閱讀性高：邏輯易懂且 Pythonic。

- 效能更穩健：不做不必要的檢查。

## ⏱️ 複雜度 Complexity
- 時間 Time: 最多比較 n * m 次，n 是字串數，m 是最短字串長度 → O(n * m)

- 空間 Space: 常數空間使用 → O(1)

## 🔍 方法比較 Summary
| 項目       | 方法一：以第一個字串為基準           | 方法二：以最短字串為基準  |
| -------- | ----------------------- | ------------- |
| 大前提原則    | 根據第一個字串做比對              | 根據所有字串中最短者比對  |
| 是否需要越界判斷 | ✅ 是（需 `i >= len(word)`） | ❌ 不需要         |
| 語意清晰度    | ✅ 直覺理解好                 | ✅ 更安全且更符合現實前提 |
| 程式碼簡潔度   | 中等                      | ✅ 簡潔且乾淨       |

## ✅ 學到什麼（Takeaways）
- 共同前綴必定不長於最短字串。

- 逐字比較並遇到第一個不匹配即中止，是尋找共同前綴的核心邏輯。

- 方法二更專注在安全與程式可讀性上，適合面試與實務使用。