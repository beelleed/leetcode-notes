# 🧩 LeetCode 424 — Longest Repeating Character Replacement
[題目連結](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## 📄 題目說明 | Problem Description

- **中文**：給你一個由大寫英文字母組成的字串 `s`，以及一個整數 `k`，你可以最多將 `k` 個字符替換成任何大寫字母。請找到替換後，某一段最長的子字串，使得該子字串裡所有字符都相同，回傳該子字串一個最大長度。  
- **English**: You are given a string `s` consisting of uppercase English letters and an integer `k`. You may replace **up to k characters** in the string with any uppercase English letter. Find the length of the **longest substring** containing the same character you can achieve after performing the replacements.

- **Examples**:
    - Example 1:

        - Input: s = "ABAB", k = 2
        - Output: 4
        - Explanation: Replace the two 'A's with two 'B's or vice versa.

    - Example 2:

        - Input: s = "AABABBA", k = 1
        - Output: 4
        - Explanation: 
            - Replace the one 'A' in the middle with 'B' and form "AABBBBA".
            - The substring "BBBB" has the longest repeating letters, which is 4.
            - There may exists other ways to achieve this answer too.

---

## 🧠 解題思路 | Solution Idea

這題的關鍵觀察是：

- 若我們有一個滑動視窗 [l, r]，設 `max_count` 為該視窗中出現頻率最高的那個字符的次數，視窗長度為 `window_len = r - l + 1`。  
- 為了讓這視窗內所有字符變成同一字母，我們至少要替換 `window_len - max_count` 個字符。  
- 所以對於有效的窗口，我們要保證：window_len - max_count ≤ k 也就是「視窗總長度減去最常見的字符數」要小於或等於我們可替換的次數 `k`。

- 用滑動窗口技巧 + 字典(或陣列)記錄字母頻率來動態維持這個條件。

具體做法：

1. 使用兩指標 `l` 和 `r`，`r` 走訪整個字串。  
2. 用 `count` 或字典記錄 `s[r]` 增加頻率，更新 `max_count`（窗口中最頻繁的字母的次數）。  
3. 若 `窗口長度 - max_count > k`，表示這窗口不能只靠 k 次替換變全同字母 → 縮左邊界：`count[s[l]] -= 1; l += 1`。  
4. 每次 `r` 向右移動時，更新答案 `ans = max(ans, r - l + 1)`。  
5. 最後回傳 `ans`。

這樣我們確保窗口始終是合法的（或剛好過界後被收縮），同時找到最長合法窗口。

---

## 💻 程式碼實作 | Code (Python)

```python
from collections import Counter

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
      count = Counter()
      l = 0
      max_count = 0
      ans = 0

      for r, ch in enumerate(s):
          count[ch] += 1
          # 更新窗口內最頻繁字母的次數
          max_count = max(max_count, count[ch])

          # 若需要替換的字符數超過 k，就縮左邊界
          # window_len = r - l + 1
          # 需要替換 = window_len - max_count
          if (r - l + 1) - max_count > k:
              # 移出左邊字符
              count[s[l]] -= 1
              l += 1

          # 更新答案
          ans = max(ans, r - l + 1)

      return ans
```
### ✅ 初始化區塊
```python
count = Counter()
l = 0
max_count = 0
ans = 0
```
- count：用來記錄當前視窗中每個字母出現的次數。

- l：左邊界索引（Left pointer），代表當前視窗的起點。

- max_count：記錄目前視窗內 最多出現的字母的出現次數。

- ans：儲存目前為止找到的最長合法視窗長度。
### 🔁 主迴圈：右邊界向右滑動
```python
for r, ch in enumerate(s):
    count[ch] += 1
    max_count = max(max_count, count[ch])
```
- 每次移動右指針 r，並更新 count[ch] 表示這個字母出現次數+1。

- max_count 也同步更新，表示目前視窗中出現最多次的那個字母的次數。
### ⚠️ 視窗合法性判斷
```python
if (r - l + 1) - max_count > k:
    count[s[l]] -= 1
    l += 1
```
- r - l + 1 是目前視窗長度。

- max_count 是視窗中出現最多次的字母。

- 若要讓整個視窗變成同一個字母，就要把其他不同的字母都「換成」最多的那個 → 換掉的數量為：視窗長度 - max_count。

- 如果這個值超過 k，代表我們無法用 k 次以內的替換完成 → 左指針往右縮，縮小視窗直到合法。
### 📌 更新最大長度
```python
ans = max(ans, r - l + 1)
```
- 每當當前視窗是合法的，就更新目前找到的最大合法視窗長度。

### 🔚 回傳答案
```python
return ans
```

---

## 🧪 範例流程 | Example Walkthrough

以 s = "AABABBA", k = 1 為例：

| r | s\[r] | count      | max\_count | l | window\_len     | window\_len – max\_count | action   | ans 更新             |
| - | ----- | ---------- | ---------- | - | --------------- | ------------------------ | -------- | ------------------ |
| 0 | A     | {A:1}      | 1          | 0 | 1               | 1−1 = 0 ≤ 1              | 合法       | ans = 1            |
| 1 | A     | {A:2}      | 2          | 0 | 2               | 2−2 = 0 ≤ 1              | 合法       | ans = 2            |
| 2 | B     | {A:2, B:1} | 2          | 0 | 3               | 3−2 = 1 ≤ 1              | 合法       | ans = 3            |
| 3 | A     | {A:3, B:1} | 3          | 0 | 4               | 4−3 = 1 ≤ 1              | 合法       | ans = 4            |
| 4 | B     | {A:3, B:2} | 3          | 0 | 5               | 5−3 = 2 > 1              | 不合法 → 縮左 | l → 1，count\[A]–1  |
|   |       | {A:2, B:2} | 3          | 1 | 窗口變 \[1..4]，長 4 | 4−3 = 1 ≤ 1              | 變合法      | ans = max(4,4) = 4 |
| 5 | B     | {A:2, B:3} | 3          | 1 | 5               | 5−3 = 2 > 1              | 不合法 → 縮左 | l → 2，count\[A]–1  |
|   |       | {A:1, B:3} | 3          | 2 | 窗口變 \[2..5]，長 4 | 4−3 = 1 ≤ 1              | 變合法      | ans = max(4,4) = 4 |
| 6 | A     | {A:2, B:3} | 3          | 2 | 5               | 5−3 = 2 > 1              | 不合法 → 縮左 | l → 3，count\[B]–1  |
|   |       | {A:2, B:2} | 3          | 3 | 窗口 \[3..6] 長 4  | 4−3 = 1 ≤ 1              | 變合法      | ans = max(4,4) = 4 |


最終 ans = 4，表示最多可以得到長度為 4 的子串，使得替換不超過 1 次後所有字母相同。

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類          | 複雜度                                                      |
| ----------- | -------------------------------------------------------- |
| 時間複雜度 Time  | **O(n)**，因為 `r` 往右移一次，左邊界 `l` 最多也移動 n 次，整體線性。            |
| 空間複雜度 Space | **O(1)** 或說 **O(26)**，因為 `count` 最多存 26 個大寫字母頻率，是固定常數級別。 |

---

## ✍️ 我學到了什麼 | What I Learned

- 滑動窗口加上「最頻繁字母次數」的技巧，是解這類「替換使子串符合條件」題的常見模式。

- max_count 只會增不會減：我們不用每次都重算窗口內的最頻繁字母次數，這是一個優化技巧。

- 當 (window_len - max_count) > k 才縮窗口，確保窗口保持合法。

- 重點要說明「為什麼不需要每次重算最頻繁字母」、「為什麼 max_count 可以保持不縮」這種技巧。