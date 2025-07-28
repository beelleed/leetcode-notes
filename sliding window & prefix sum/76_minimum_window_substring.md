# 📘 LeetCode 76 - 最小覆蓋子串 (Minimum Window Substring)
🔗 [題目連結](https://leetcode.com/problems/minimum-window-substring/)

## 🧾 題目描述 | Problem Description

- 給定兩個字串 `s` 和 `t`，找出 `s` 中最短的一個子字串，它包含了 `t` 中所有字符（包括重複）。
- Given two strings `s` and `t`, return the minimum window in `s` which contains all the characters in `t` (including duplicates).

### Examples
- Example 1:

    - Input: s = "ADOBECODEBANC", t = "ABC"
    - Output: "BANC"
    - Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

- Example 2:

    - Input: s = "a", t = "a"
    - Output: "a"
    - Explanation: The entire string s is the minimum window.

- Example 3:

    - Input: s = "a", t = "aa"
    - Output: ""
    - Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

---

## 📌 解題思路 | Solution Idea

使用滑動窗口（Sliding Window）+ 雙指針 + 字典統計：

1. 用一個字典 `need` 記錄 t 中每個字符需要出現的次數。
2. 用 `window` 記錄當前視窗中字符的出現次數。
3. 當視窗滿足條件（所有 `need` 中的字符都被包含且數量足夠）時，嘗試收縮左邊界以獲得更小的子串。
4. 每次找到更小的合法子串就更新起點與長度。

---

## 💡 Python 程式碼 | Python Code

```python
from collections import Counter

def minWindow(s: str, t: str) -> str:
    need = Counter(t)
    window = {}
    left = right = 0
    valid = 0
    start = 0
    min_len = float('inf')

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need):
            if right - left < min_len:
                start = left
                min_len = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return "" if min_len == float('inf') else s[start:start + min_len]
```
```python
from collections import Counter
```
- 引入 Counter，用來計算 t 中每個字符出現的次數。
```python
def minWindow(s: str, t: str) -> str:
```
- 定義函數，目的是找出 s 中包含 t 所有字符的最短子串。

### 🧱 初始化變數
```python
need = Counter(t)  # {'A':1, 'B':1, 'C':1}
window = {}
left = right = 0
valid = 0
start = 0
min_len = float('inf')
```
- need：記錄 t 中每個字符需要的數量。

- window：記錄目前滑動窗口中出現的字符與數量。

- left 和 right：雙指針，表示目前視窗範圍 [left, right)

- valid：有幾種字元已經滿足需要（window 中某字元數量 == need 中要求的數量）

- start / min_len：記錄最短合法視窗的起始位置與長度

### 🔁 主迴圈：右邊擴張窗口
```python
while right < len(s):
    c = s[right]
    right += 1
```
- 循環移動右邊界，把字符加入窗口中。

### 🧮 更新 window & valid
```python
if c in need:
    window[c] = window.get(c, 0) + 1
    if window[c] == need[c]:
        valid += 1
```
- 如果 c 是需要的字元，就把它加入 window 計數。

- 如果這個字元的數量剛好達標，就讓 valid +1，表示這個字元達標了。

### 🔄 左邊收縮窗口（當所有字元達標）
```python
while valid == len(need)
```
- 只有當所有 need 中的字符都已滿足時，才進入收縮流程。

```python
if right - left < min_len:
    start = left
    min_len = right - left
```
- 若目前視窗比之前記錄的更短，就更新最短範圍。

### ✂️ 移除左邊字元並更新狀態
```python
d = s[left]
left += 1
if d in need:
    left += 1
    if d in need:
        if window[d] == need[d]:
            valid -= 1
        window[d] -= 1
```
- 把最左邊的字元從 window 移除。

- 如果這個字元是必要的，且剛好達標 → 那它被移除後就「不再滿足」，要讓 valid -1。

### ✅ 結果輸出
```python
return "" if min_len == float('inf') else s[start:start + min_len]
```
- 如果沒找到任何合法子串，回傳空字串。

- 否則回傳最短視窗的子串。

### 🔁 範例追蹤（s = "ADOBECODEBANC", t = "ABC"）：
- 一開始 need = {'A':1, 'B':1, 'C':1}

- 視窗往右擴："ADOBEC" 逐步滿足 A、B、C

- 收縮左邊直到 "BANC" 是最短

- 回傳 "BANC"

---

## 🪜 流程圖概念 | Sliding Window 流程圖
```markdown
初始化
↓
建立 need 字典，計算 t 每個字元的需求數量
↓
右指針 right 開始向右滑動：

    - 加入字元到 window 中

    - 若該字元在 need 中，更新計數

    - 若 window[x] == need[x]，valid += 1
        ↓
      當 valid == need 種類數時（視窗合法）：

    - 判斷當前視窗長度是否更短，是就記錄

    - 左指針 left 開始收縮：

        - 將左邊字元移出 window

        - 若該字元在 need 中，檢查是否影響 valid
            ↓
          重複滑動與收縮直到 right 掃完 s
            ↓
          回傳最短視窗對應的子字串或 ""
```

---
## 🔍 視覺化指針移動

```plaintext
s = "ADOBECODEBANC"
t = "ABC"
need = {'A':1, 'B':1, 'C':1}

步驟：
right 滑到 'A' → window['A'] = 1 → valid += 1
...
right 滑到 'C' → window['C'] = 1 → valid == 3 ✅
→ 開始嘗試從 left 收縮，找到 "BANC"
```

---

## 📚 程式邏輯要點
| 名稱        | 用途說明                 |
| --------- | -------------------- |
| `need`    | 字典，記錄 t 中每個字元需要的次數   |
| `window`  | 當前視窗中的字元出現次數         |
| `valid`   | 當前有幾個字元滿足 `need` 的要求 |
| `left`    | 視窗左邊界，控制收縮           |
| `right`   | 視窗右邊界，控制擴張           |
| `min_len` | 記錄目前為止最短合法視窗的長度      |
| `start`   | 最短視窗的起始位置，用來最後回傳子串範圍 |

---

## 🧠 核心觀念整理
- 滑動窗口技巧＝右擴左縮，邊擴張邊檢查是否滿足條件。

- Two Hash Maps：need 是目標、window 是目前狀態。

- valid 判斷視窗是否合法：只有當全部需求字元都滿足時才進入收縮。

- 每次合法時嘗試更新最小視窗長度，這樣最終得到最短解。

---

## ⏱️ 複雜度分析 | Complexity
- 時間複雜度 Time: O(m + n)，m 為 s 的長度，n 為 t 的長度

- 空間複雜度 Space: O(n)，用於記錄 t 中每個字元的計數

---

## 📚 學到什麼 | What I Learned
- 滑動窗口技巧適合處理子字串包含、最短/最長等問題。

- 使用兩個字典分別記錄「需要」與「當前窗口」的狀態，是控制條件的關鍵。

- 注意右邊先擴張、左邊再收縮的邏輯順序，這是雙指針結構的經典模式。