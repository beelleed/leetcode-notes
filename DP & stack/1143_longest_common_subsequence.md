# 1143. Longest Common Subsequence 最長公共子序列

[題目連結](https://leetcode.com/problems/longest-common-subsequence/)

---

## 🧩 題目描述 Description

給定兩個字串 `text1` 和 `text2`，回傳它們的「最長公共子序列」長度。子序列需保持原有順序但不需連續。

Given two strings `text1` and `text2`, return the length of their longest common subsequence. The subsequence does not need to be contiguous, but must preserve the relative order of characters.

---

## ✅ 正確解法 Correct Solution (Dynamic Programming)

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

## 📘 解題思路 Explanation
初始條件 Initialization
- 第一行與第一列初始化為 0，表示空字串與任何字串的 LCS 為 0。

狀態定義 State Definition
- dp[i][j]: 表示 text1 前 i 個字元 與 text2 前 j 個字元 的最長公共子序列長度

- dp[i][j] =

    - 若 text1[i-1] == text2[j-1], dp[i-1][j-1] + 1 
    -  否則 max(dp[i-1][j], dp[i][j-1])

## ⏱️ 時間複雜度 Time Complexity
- O(m * n)

## 💾 空間複雜度 Space Complexity
- 標準解法：使用 dp[m+1][n+1] 的二維陣列，空間複雜度為：O(m * n)

- 優化空間：若只需回傳長度（不需回溯出序列內容），可使用兩行滾動陣列：
    - prev = [0] * (n + 1)
    - curr = [0] * (n + 1)
→ 空間複雜度變為：O(n)

## 🧠 學習重點 Key Takeaways
- 子序列可不連續，但順序必須一致。

- 題目要求「最長」且「兩個序列都有」，通常使用 DP。

- 用 dp[i][j] 表示兩個序列前綴的解。

## 📊 範例解析 Example
🧪 假設輸入：
```python
text1 = "abcde"
text2 = "ace"
```
長度為：

- m = 5（text1）

- n = 3（text2）

## 📊 初始化空表格 dp（大小為 (m+1) × (n+1)）
- 這代表 dp[0][*] 與 dp[*][0] 是 base case（空字串對比），都為 0。

|   |   | a | c | e |
| - | - | - | - | - |
|   | 0 | 0 | 0 | 0 |
| a | 0 |   |   |   |
| b | 0 |   |   |   |
| c | 0 |   |   |   |
| d | 0 |   |   |   |
| e | 0 |   |   |   |

🧠 按照遞推公式填表格：

|   |   | a | c | e |
| - | - | - | - | - |
|   | 0 | 0 | 0 | 0 |
| a | 0 | 1 | 1 | 1 |
| b | 0 | 1 | 1 | 1 |
| c | 0 | 1 | 2 | 2 |
| d | 0 | 1 | 2 | 2 |
| e | 0 | 1 | 2 | 3 |

最終答案為右下角 dp[5][3] = 3，對應最長公共子序列為 "ace"，長度為 3

---

## 📊 dp 填表邏輯細節（text1 橫列，text2 直欄）
| i (text1) | j (text2) | text1\[i-1] | text2\[j-1] | 相同？ | dp\[i]\[j] 如何計算                             |
| --------- | --------- | ----------- | ----------- | --- | ------------------------------------------- |
| 1         | 1         | a           | a           | ✅   | dp\[0]\[0] + 1 = 1                          |
| 1         | 2         | a           | c           | ❌   | max(dp\[0]\[2], dp\[1]\[1]) = max(0, 1) = 1 |
| 1         | 3         | a           | e           | ❌   | max(dp\[0]\[3], dp\[1]\[2]) = max(0, 1) = 1 |
| 2         | 1         | b           | a           | ❌   | max(dp\[1]\[1], dp\[2]\[0]) = max(1, 0) = 1 |
| 2         | 2         | b           | c           | ❌   | max(dp\[1]\[2], dp\[2]\[1]) = max(1, 1) = 1 |
| 2         | 3         | b           | e           | ❌   | max(dp\[1]\[3], dp\[2]\[2]) = max(1, 1) = 1 |
| 3         | 1         | c           | a           | ❌   | max(dp\[2]\[1], dp\[3]\[0]) = max(1, 0) = 1 |
| 3         | 2         | c           | c           | ✅   | dp\[2]\[1] + 1 = 1 + 1 = 2                  |
| 3         | 3         | c           | e           | ❌   | max(dp\[2]\[3], dp\[3]\[2]) = max(1, 2) = 2 |
| 4         | 1         | d           | a           | ❌   | max(dp\[3]\[1], dp\[4]\[0]) = max(1, 0) = 1 |
| 4         | 2         | d           | c           | ❌   | max(dp\[3]\[2], dp\[4]\[1]) = max(2, 1) = 2 |
| 4         | 3         | d           | e           | ❌   | max(dp\[3]\[3], dp\[4]\[2]) = max(2, 2) = 2 |
| 5         | 1         | e           | a           | ❌   | max(dp\[4]\[1], dp\[5]\[0]) = max(1, 0) = 1 |
| 5         | 2         | e           | c           | ❌   | max(dp\[4]\[2], dp\[5]\[1]) = max(2, 1) = 2 |
| 5         | 3         | e           | e           | ✅   | dp\[4]\[2] + 1 = 2 + 1 = 3                  |

---

## ✅ 額外筆記 Extra Notes
- 本題適合練習「二維 dp 陣列的狀態設計」

- 常見應用：DNA 比對、文本相似度、Git diff 比較

- 類似題：72. Edit Distance, 115. Distinct Subsequences
