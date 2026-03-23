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

### 中文
使用滑動窗口（Sliding Window）+ 雙指針 + 字典統計：

1. 用一個字典 `need` 記錄 t 中每個字符需要出現的次數。
2. 用 `window` 記錄當前視窗中字符的出現次數。
3. 當視窗滿足條件（所有 `need` 中的字符都被包含且數量足夠）時，嘗試收縮左邊界以獲得更小的子串。
4. 每次找到更小的合法子串就更新起點與長度。

### English
Using the Sliding Window technique with two pointers and character frequency dictionaries:

1. Use a dictionary need to record how many times each character in t must appear.

2. Use another dictionary window to track the frequency of characters within the current sliding window in s.

3. When the current window satisfies the condition (contains all required characters with the correct frequencies), try to shrink the left boundary to find a smaller valid substring.

4. Each time a smaller valid substring is found, update the starting index and minimum length.

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

- min_len = float('inf'): 先設一個『不可能的最大值』，之後只要有合法子串，一定比它短。float('inf') = 正無限大（∞）

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
- 這裡的 right 是 開區間右邊界，不是視窗內最後一個 index。
    - 對於區間：s[left:right]
    - 長度就是：right - left 不需要再 +1
        - 假設：left = 2, right = 5
            - 那視窗是：s[2:5] 包含 index 2, 3, 4

### ✂️ 移除左邊字元並更新狀態
```python
d = s[left]
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
### 🌱 初始狀態：
```plaintext
left = 0
right = 0
window = {}
valid = 0
need = {'A':1, 'B':1, 'C':1}
```
### 🧭 Sliding Window 執行過程：
| 步驟   | right | 字元 | 行動                  | window 更新                           | valid | left | 視窗內容          |
| ---- | ----- | -- | ------------------- | ----------------------------------- | ----- | ---- | ------------- |
| 1    | 0     | A  | 加入 → 是 need 中       | {'A': 1}                            | ✅1    | 0    | A             |
| 2    | 1     | D  | 加入 → 不是必要字          | {'A': 1, 'D': 1}                    | 1     | 0    | AD            |
| 3    | 2     | O  | 加入 → 不是必要字          | {'A': 1, 'D': 1, 'O': 1}            | 1     | 0    | ADO           |
| 4    | 3     | B  | 加入 → 是 need 中       | {'A':1, 'D':1, 'O':1, 'B':1}        | ✅2    | 0    | ADOB          |
| 5    | 4     | E  | 加入 → 不是必要字          | {'A':1, 'D':1, 'O':1, 'B':1, 'E':1} | 2     | 0    | ADOBE         |
| 6    | 5     | C  | 加入 → 是 need 中       | {..., 'C':1}                        | ✅3    | 0    | ADOBEC ✅ 合法視窗 |
| 🔁收縮 |       |    | left = 0, 移除 A      | A 數量不足 → valid -=1 = 2              | ❌2    | 1    | DOBEC         |
| 7    | 6     | O  | 加入                  | O: 2                                | 2     | 1    | DOBECO        |
| 8    | 7     | D  | 加入                  | D: 2                                | 2     | 1    | DOBECOD       |
| 9    | 8     | E  | 加入                  | E: 2                                | 2     | 1    | DOBECODE      |
| 10   | 9     | B  | 加入                  | B: 2                                | 2     | 1    | DOBECODEB     |
| 11   | 10    | A  | 加入 → A: 1 == need A | valid +=1 → valid = 3 ✅             | ✅3    | 1    | DOBECODEBA    |
| 🔁收縮 |       |    | left = 1, 移除 D      | D:1 → 不影響 valid                     | 3     | 2    | OBECODEBA     |
|      |       |    | left = 2, 移除 O      | O:1 → 不影響 valid                     | 3     | 3    | BECODEBA      |
|      |       |    | left = 3, 移除 B      | B:1 → 還夠 → valid 不變                 | 3     | 4    | ECODEBA       |
|      |       |    | left = 4, 移除 E      | E:1 → 不影響 valid                     | 3     | 5    | CODEBA        |
|      |       |    | left = 5, 移除 C      | C:0 → valid -=1 → ❌2                | ❌2    | 6    | ODEBA         |
| 12   | 11    | N  | 加入 → 不影響 valid      | N:1                                 | 2     | 6    | ODEBAN        |
| 13   | 12    | C  | 加入 → valid +=1      | C:1 == need C → ✅3                  | ✅3    | 6    | ODEBANC       |
| 🔁收縮 |       |    | left = 6, 移除 O      | O:0 → 不影響 valid                     | 3     | 7    | DEBANC        |
|      |       |    | left = 7, 移除 D      | D:1 → 不影響 valid                     | 3     | 8    | EBANC         |
|      |       |    | left = 8, 移除 E      | E:1 → 不影響 valid                     | 3     | 9    | BANC ✅最短合法    |
|      |       |    | left = 9, 移除 B      | B:1 → 不足 → valid -=1 → ❌2           | ❌2    | 10   | ANC           |


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