# 📍 LeetCode 36 — Valid Sudoku | 有效的數獨

🔗 [題目連結](https://leetcode.com/problems/valid-sudoku/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 給定一個 9 × 9 的數獨棋盤 board，請判斷目前填入的數字是否有效。

- 有效的數獨需滿足三個條件：

    - 每一列（row） 不能有重複的數字 1–9

    - 每一行（column） 不能有重複的數字 1–9

    - 每一個 3 × 3 的小方格（sub-box） 不能有重複的數字 1–9

    - 空格以 '.' 表示

    - 不需要判斷是否「可解」，只需檢查目前狀態是否違規

### English:

- Determine if a 9 × 9 Sudoku board is valid.
Only the filled cells need to be validated according to the rules.

### Examples
- Example 1:
    
    ![](../images/36_Sudoku-by-L2G-20050714.svg.png)

    - Input: board = 
        
        [["5","3",".",".","7",".",".",".","."]

        ,["6",".",".","1","9","5",".",".","."]

        ,[".","9","8",".",".",".",".","6","."]

        ,["8",".",".",".","6",".",".",".","3"]

        ,["4",".",".","8",".","3",".",".","1"]

        ,["7",".",".",".","2",".",".",".","6"]

        ,[".","6",".",".",".",".","2","8","."]

        ,[".",".",".","4","1","9",".",".","5"]

        ,[".",".",".",".","8",".",".","7","9"]]
    - Output: true

- Example 2:

    - Input: board = 
        
        [["8","3",".",".","7",".",".",".","."]

        ,["6",".",".","1","9","5",".",".","."]

        ,[".","9","8",".",".",".",".","6","."]

        ,["8",".",".",".","6",".",".",".","3"]

        ,["4",".",".","8",".","3",".",".","1"]

        ,["7",".",".",".","2",".",".",".","6"]

        ,[".","6",".",".",".",".","2","8","."]

        ,[".",".",".","4","1","9",".",".","5"]

        ,[".",".",".",".","8",".",".","7","9"]]
    - Output: false
    - Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

---

## 🧠 解題思路 | Solution Idea（核心概念）
- 關鍵觀察

    - 題目沒有要 解數獨

    - 只是要 檢查有沒有重複

    - 重複出現的地方只有三種：

        1. row

        2. column

        3. 3×3 box

- 👉 本質是 「重複檢查」問題

- 為什麼用 Set？

    - 我們只需要知道：

        - 「某個數字是否已經出現過」

    - Set 的特性：

        - 查找 / 插入：O(1)

        - 非常適合做「是否重複」判斷

---

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
- 初始化三個結構
```python
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
```

- rows[i]：第 i 列出現過的數字

- cols[j]：第 j 行出現過的數字

- boxes[k]：第 k 個 3×3 小格出現過的數字

👉 各自獨立追蹤，互不干擾

- 掃描整個棋盤
```python
for r in range(9):
    for c in range(9):
```

- r：row index

- c：column index

- 一格一格檢查（固定 9×9）

- 跳過空格
```python
val = board[r][c]
if val == ".":
    continue
```

- 題目規定 '.' 代表空

- 空格不參與任何檢查

- 計算 box index（超重要）
```python
box_index = (r // 3) * 3 + (c // 3)
```
### 🧠 第一層：直覺怎麼想（先不要管公式）

數獨的 9 個 box 長這樣（編號 0–8）：
```text
┌─────┬─────┬─────┐
│  0  │  1  │  2  │
├─────┼─────┼─────┤
│  3  │  4  │  5  │
├─────┼─────┼─────┤
│  6  │  7  │  8  │
└─────┴─────┴─────┘
```

- 所以其實我們要做的是兩件事：

    - 這一格在 第幾排 box（上 / 中 / 下）

    - 這一格在 第幾個 column box（左 / 中 / 右）

### 🧮 第二層：r // 3、c // 3 在幹嘛？
#### 🔹 r // 3 → 第幾排 box
```text
r = 0,1,2 → r//3 = 0  (上排)
r = 3,4,5 → r//3 = 1  (中排)
r = 6,7,8 → r//3 = 2  (下排)
```
#### 🔹 c // 3 → 第幾個 column box
```text
c = 0,1,2 → c//3 = 0  (左)
c = 3,4,5 → c//3 = 1  (中)
c = 6,7,8 → c//3 = 2  (右)
```
### 🧩 第三層：為什麼是 (r // 3) * 3 + (c // 3)？
- 想成「二維 → 一維」的編號

    - (r // 3)：第幾排 box

    - 每一排有 3 個 box

    - 所以要先 跳過前面整排的 box

- 👉 (r // 3) * 3

- 然後再加上：
    -  (c // 3)：在這一排中的第幾個

### 📊 對照表

| r | c | r//3 | c//3 | box_index |
| - | - | ---- | ---- | --------- |
| 0 | 0 | 0    | 0    | 0         |
| 0 | 4 | 0    | 1    | 1         |
| 1 | 8 | 0    | 2    | 2         |
| 3 | 1 | 1    | 0    | 3         |
| 4 | 4 | 1    | 1    | 4         |
| 5 | 7 | 1    | 2    | 5         |
| 6 | 2 | 2    | 0    | 6         |
| 7 | 5 | 2    | 1    | 7         |
| 8 | 8 | 2    | 2    | 8         |


- 👉 把 9 個小格編號為 0–8
- 👉 非常標準、面試常考

- 檢查是否重複
```python
if val in rows[r] or val in cols[c] or val in boxes[box_index]:
    return False
```

- 只要 任一地方出現過

- 立刻違規 → 回傳 False

- 記錄目前數字
```python
rows[r].add(val)
cols[c].add(val)
boxes[box_index].add(val)
```

- 表示「這個數字已經被用過了」

- 後面再看到就能抓到

- 全部掃完都沒問題
```python
return True
```

---

## 🧪 範例流程 | Example Walkthrough

- 假設：
```text
board =
[
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ...
]

```

## 🔹 Step 0：初始化（對應這段）
```python
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
```

此時：
```text
rows  = [∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅]
cols  = [∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅]
boxes = [∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅, ∅]
```
## 🔹 Step 1：r = 0, c = 0
```python
val = board[0][0]  # "5"
```

- val != "." → 繼續

- 計算 box index：
```python
box_index = (0 // 3) * 3 + (0 // 3) = 0
```

檢查：
```python
"5" in rows[0]?  ❌
"5" in cols[0]?  ❌
"5" in boxes[0]? ❌
```

→ 合法，加入 set：
```python
rows[0].add("5")
cols[0].add("5")
boxes[0].add("5")
```

狀態變為：
```text
rows[0]  = {"5"}
cols[0]  = {"5"}
boxes[0] = {"5"}
```
## 🔹 Step 2：r = 0, c = 1
```python
val = board[0][1]  # "3"
box_index = (0//3)*3 + (1//3) = 0
```

檢查：
```python
"3" in rows[0]?  ❌
"3" in cols[1]?  ❌
"3" in boxes[0]? ❌
```

→ 加入：
```text
rows[0]  = {"5", "3"}
cols[1]  = {"3"}
boxes[0] = {"5", "3"}
```
## 🔹 Step 3：r = 0, c = 2
```python
val = board[0][2]  # "."
```

對應程式碼：
```python
if val == ".":
    continue
```

👉 直接跳過，rows / cols / boxes 都不變

## 🔹 Step 4：r = 0, c = 4
```python
val = board[0][4]  # "7"
box_index = (0//3)*3 + (4//3) = 1
```

檢查：
```python
"7" in rows[0]?  ❌
"7" in cols[4]?  ❌
"7" in boxes[1]? ❌
```

→ 加入：
```text
rows[0]  = {"5", "3", "7"}
cols[4]  = {"7"}
boxes[1] = {"7"}
```
## 🔹 Step 5：假設遇到違規情況

假設之後掃描到：
```text
board[1][0] = "5"
```
```python
r = 1, c = 0
box_index = (1//3)*3 + (0//3) = 0
```

檢查：
```python
"5" in rows[1]?  ❌
"5" in cols[0]?  ✅  ← 已經有 "5"
```

👉 對應程式碼：
```python
if val in rows[r] or val in cols[c] or val in boxes[box_index]:
    return False
```

➡ 直接 return False，整個函式結束

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 固定 9 × 9 = 81 格

    - 👉 O(1)（常數時間）

- 空間複雜度：

    - 3 × 9 個 set

    - 👉 O(1)

---

## 方法二: set() + 「標記字串」

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                row_key = ("r", r, val)
                col_key = ("c", c, val)
                box_key = ("b", r // 3, c // 3, val)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True
```
### 🧠 核心想法 | Key Idea

- 把三種限制 轉成可以丟進 set 的唯一 key

- 每個數字會產生三個 key：
```text
("r", row_index, value)        → 列約束
("c", col_index, value)        → 行約束
("b", box_row, box_col, value) → 3×3 方格約束
```

- 只要其中任一 key 重複 → 數獨違規

### 🔍 為什麼這樣一定不會衝突？

- key 的第一個元素 "r" / "c" / "b" 用來區分規則類型

- row / col / box 的 index 讓位置唯一

- value 代表實際填入的數字

- 👉 不同規則、不同位置，永遠不會產生相同 key

---

## 🧪 範例流程 | Example Walkthrough

假設目前處理到：
```python
r = 0
c = 1
val = "3"
```

產生的 key 為：
```python
row_key = ("r", 0, "3")
col_key = ("c", 1, "3")
box_key = ("b", 0, 0, "3")
```

檢查：
```python
if row_key in seen or col_key in seen or box_key in seen:
```

- 若任一存在 → 代表「這個數字已經在同一列 / 行 / 方格出現過」

- 直接 return False

否則：
```python
seen.add(row_key)
seen.add(col_key)
seen.add(box_key)
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 固定掃描 9 × 9 個格子

    - 👉 O(1)

- 空間複雜度：

    - 最多儲存 81 × 3 個 key

    - 👉 O(1)

---

## ✍️ 我學到的東西 | What I Learned

- Valid Sudoku ≠ Solve Sudoku

- 本質是： 「row / column / box 的去重檢查」

- box_index = (r//3)*3 + (c//3) 是必背公式

- 題目看到：

    - Valid

    - Check duplicates

    - Fixed size

- 👉 Set + one pass 掃描

---

## 🧠 一句話總結

I scan the board once and use three sets per row, column, and 3×3 box to detect duplicates.
If any number appears more than once in any of them, the Sudoku is invalid.