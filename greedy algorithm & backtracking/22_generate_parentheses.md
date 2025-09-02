# 22. Generate Parentheses | 生成有效括號組合

[Leetcode 22](https://leetcode.com/problems/generate-parentheses/)

---

##  題目說明 | Problem Description

- **中文：**  
  給定一個整數 `n`，代表括號對數，請生成所有由 `n` 對括號構成的 **合法括號組合**。

- **English:**  
  Given an integer `n`, generate all combinations of `n` pairs of well-formed parentheses.

### Examples
- Example 1:

    - Input: n = 3
    - Output: ["((()))","(()())","(())()","()(())","()()()"]

- Example 2:

    - Input: n = 1
    - Output: ["()"]


---

##  💡 解題思路 | Solution Approach

### 中文思路：
- 使用 **回溯法（Backtracking）** 或深度優先搜尋（DFS）。
- 維護三個狀態：
  - `left`：已放入的左括號數量  
  - `right`：已放入的右括號數量  
  - `current`：目前組合的字串
- 剪枝條件（保持合法狀態）：
  - `left > n` 或 `right > n` → 使用過多括號
  - `right > left` → 右括號多於左括號（非法）
- 當 `left == n` 且 `right == n` 時，收集這組合法組合。

### English Explanation:
- Use **backtracking** to build all valid strings.
- Track three states in the recursion:
  - `left`: number of '(' used so far  
  - `right`: number of ')' used so far  
  - `current`: the current parentheses string
- Prune invalid states:
  - `left > n` or `right > n` → too many parentheses  
  - `right > left` → invalid order
- When both `left == n` and `right == n`, add the current string to results.

---

##  Python 程式碼 | Code

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left: int, right: int, current: str):
            # 剪枝：非法狀態
            if left > n or right > n or right > left:
                return
            # 基本條件：形成完整合法組合
            if left == n and right == n:
                result.append(current)
                return
            # 遞迴：加入 '('
            backtrack(left + 1, right, current + "(")
            # 遞迴：加入 ')'
            backtrack(left, right + 1, current + ")")

        backtrack(0, 0, "")
        return result
```
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
```
- 建立一個結果列表 result，用來儲存所有合法括號的組合。

- n 表示要生成 n 對括號（即總共 2n 個字元）。

### 🧠 回溯函式定義
```python
def backtrack(left: int, right: int, current: str):
```
定義遞迴函式 backtrack，包含三個參數：

- left：目前用掉的左括號數量 '('

- right：目前用掉的右括號數量 ')'

- current：當前構造中的括號字串

### ✂️ 剪枝條件（提前中止）
```python
if left > n or right > n or right > left:
    return
```
- left > n：左括號用超過了 → 不合法

- right > n：右括號用超過了 → 不合法

- right > left：右括號比左括號多 → 不合法（例如 ")(" 是錯的）

這一行的目的是減少不必要的遞迴。

### ✅ 終止條件：合法組合完成
```python
if left == n and right == n:
    result.append(current) # 加入結果
    return                 # 停止遞迴，返回上一層
```
當左右括號都用完時，表示我們已經生成了一個合法的括號字串，加入結果列表中。

❌ 如果沒寫 return 會怎樣？

如果你省略 return，程式會繼續往下跑這兩行：
```python
backtrack(left + 1, right, current + "(")
backtrack(left, right + 1, current + ")")
```
但此時：

- left > n 或 right > n → 下一層會立即被剪枝

- 雖然不會出錯，但會產生不必要的遞迴呼叫，降低效率

### 🔁 遞迴邏輯：嘗試加入括號
```python
backtrack(left + 1, right, current + "(")
```
- 嘗試加一個 '(' 左括號 → 左括號數量 +1，遞迴繼續。
```python
backtrack(left, right + 1, current + ")")
```
- 嘗試加一個 ')' 右括號 → 右括號數量 +1，遞迴繼續。

### 🔚 開始回溯
```python
backtrack(0,0, "")
```
- 從空字串開始、左右括號都還沒用的狀態出發。

### 🔁 回傳最終結果
```python
return result
```
- 返回所有可能的合法括號組合。

---

## 🧪 範例：n = 2 時會產生：
### 🧭 遞迴步驟模擬（對應程式碼）
```sql
初始狀態: left = 0, right = 0, current = ""
```
🔹 加左括號 '('
```bash
backtrack(1, 0, "(")   # 加了一個左括號
```
🔹 再加左括號 '('
```bash
backtrack(2, 0, "((")  # 左括號達到上限，接下來只能加右括號
```
🔹 加右括號 ')'
```scss
backtrack(2, 1, "(()")
```
🔹 再加右括號 ')'
```scss
backtrack(2, 2, "(())") ✅ 收集起來
```
### 🔙 回到狀態：left = 1, right = 0, current = "("
🔹 加右括號 ')'
```scss
backtrack(1, 1, "()" )
```
🔹 加左括號 '('
```scss
backtrack(2, 1, "()(")
```
🔹 加右括號 ')'
```scss
backtrack(2, 2, "()()") ✅ 收集起來
```
### ✅ 最終結果
```python
["(())", "()()"]
```
### 🧠 對應邏輯關鍵字
| 遞迴狀態           | 加 '(' 條件     | 加 ')' 條件 |
| -------------- | ------------ | -------- |
| `left < n`     | 還有左括號可以用     |          |
| `right < left` | 確保目前還合法（右不多） |          |

### 🧠 核心觀念小總結
| 部分 | 說明                |
| -- | ----------------- |
| 剪枝 | 保證只產生合法組合（剪掉錯的分支） |
| 遞迴 | 不斷構建括號組合直到完成      |
| 回溯 | 嘗試所有可能路徑，並把合法的留下來 |


---

## ⏱ 時間與空間複雜度 | Complexity

- 時間複雜度 Time: 與 Catalan 數相關，約為 O(4^n / √n) 。

- 空間複雜度 Space: 遞迴深度最多為 2n，因此為 O(n)（忽略輸出空間）。

---

## ✅ 我學到了什麼 | What I Learned
### 中文：

- 遇到生成所有組合的題目，Backtracking 是常見且強大的技法。

- 剪枝條件是提高效率的關鍵：合法性判斷要寫在遞迴進入前，避免多餘計算。

- 學會維護狀態（left, right, current）並遞迴，是解這類問題的基礎。

### English:

- Backtracking is essential when generating all valid combinations in a constrained space.

- Validity pruning early in recursion greatly improves efficiency.

- Keeping and updating state (left, right, current) is central to designing clean recursive solutions.