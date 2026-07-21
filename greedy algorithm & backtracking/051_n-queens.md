# 📍 LeetCode 51 — N-Queens

## 📄 題目說明 | Problem Description

### 中文

給定一個整數 `n`，請在一個 `n x n` 的棋盤上放置 `n` 個皇后，使得任何兩個皇后都不能互相攻擊。

皇后可以攻擊：

```text
同一個 row

同一個 column

同一條左上到右下對角線

同一條右上到左下對角線
```

請回傳所有合法的棋盤排列方式。

棋盤中的：

```text
"Q"
```

代表皇后。

```text
"."
```

代表空格。

---

### English

Given an integer `n`, return all distinct solutions to the `n-queens` puzzle.

The goal is to place `n` queens on an `n x n` chessboard such that no two queens attack each other.

A queen can attack horizontally, vertically, and diagonally.

---

### Examples

#### Example 1

Input：

```python
n = 4
```

Output：

```python
[
    [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
    ],
    [
        "..Q.",
        "Q...",
        "...Q",
        ".Q.."
    ]
]
```

---

#### Example 2

Input：

```python
n = 1
```

Output：

```python
[
    ["Q"]
]
```

---

## 🧠 核心觀念 | Key Insight

這題是經典 Backtracking。

我們要做的是：

```text
一個 row 一個 row 地放皇后
```

每一個 row 只能放一個皇后。

所以每一層遞迴代表：

```text
目前要在第幾個 row 放皇后
```

---

### 寫 Backtracking 前先問：函式要做什麼？

這題的：

```python
backtrack(row)
```

表示：

> 從目前的 `row` 開始，嘗試完成剩下所有皇后的放置。

這題不需要回傳 `True` 或 `False`。

因為我們不是只找一組答案，而是要找：

```text
所有合法解
```

所以 DFS / Backtracking 的工作是：

```text
找到完整答案時加入 res

然後繼續搜尋其他可能
```

---

### 為什麼一層只處理一個 row？

因為同一個 row 不能有兩個皇后。

所以我們可以直接固定：

```text
第 0 層處理 row 0

第 1 層處理 row 1

第 2 層處理 row 2
```

這樣就不需要另外檢查：

```text
同一個 row 是否已經有皇后
```

因為每個 row 本來就只會放一次。

---

### 每一層的選擇是什麼？

每一層會嘗試：

```text
目前 row 的每一個 column
```

例如：

```python
n = 4
row = 0
```

可以嘗試：

```text
column 0

column 1

column 2

column 3
```

所以會使用：

```python
for col in range(n):
```

---

### 需要檢查哪些衝突？

假設我們想在：

```python
(row, col)
```

放皇后。

要確認三件事：

```text
這個 column 沒有皇后

左上到右下對角線沒有皇后

右上到左下對角線沒有皇后
```

不需要檢查 row，因為每一層只處理一個 row。

---

### 如何記錄 column？

使用：

```python
cols = set()
```

如果皇后放在：

```python
(row, col)
```

就加入：

```python
cols.add(col)
```

表示：

```text
這個 column 已經有皇后
```

例如：

```python
cols = {1, 3}
```

代表 column `1` 和 column `3` 已經不能使用。

---

### 如何判斷左上到右下對角線？

左上到右下的對角線具有特性：

```text
row - col 相同
```

例如：

```text
(0,0) → 0 - 0 = 0

(1,1) → 1 - 1 = 0

(2,2) → 2 - 2 = 0

(3,3) → 3 - 3 = 0
```

這些位置都在同一條對角線。

再例如：

```text
(0,1) → 0 - 1 = -1

(1,2) → 1 - 2 = -1

(2,3) → 2 - 3 = -1
```

也在同一條對角線。

所以使用：

```python
neg_diag = set()
```

儲存：

```python
row - col
```

---

### 為什麼叫 `neg_diag`？

因為：

```python
row - col
```

有時候會是負數。

例如：

```python
row = 0
col = 3
```

得到：

```python
row - col = -3
```

所以常命名為：

```python
neg_diag
```

---

### 如何判斷右上到左下對角線？

右上到左下的對角線具有特性：

```text
row + col 相同
```

例如：

```text
(0,3) → 0 + 3 = 3

(1,2) → 1 + 2 = 3

(2,1) → 2 + 1 = 3

(3,0) → 3 + 0 = 3
```

這些位置都在同一條對角線。

所以使用：

```python
pos_diag = set()
```

儲存：

```python
row + col
```

---

### 為什麼叫 `pos_diag`？

因為：

```python
row + col
```

永遠是非負數。

所以常命名為：

```python
pos_diag
```

---

### 三個檢查條件

想在：

```python
(row, col)
```

放皇后時，要確認：

```python
col not in cols
```

```python
row - col not in neg_diag
```

```python
row + col not in pos_diag
```

如果其中任何一個已經存在，就代表有衝突。

所以可以寫：

```python
if (
    col in cols
    or row - col in neg_diag
    or row + col in pos_diag
):
    continue
```

---

### 為什麼使用 `continue`？

如果目前這個 `col` 有衝突，只代表：

```text
目前這一格不能放
```

但同一個 row 的其他 column 可能可以放。

所以：

```python
continue
```

跳過目前 column，繼續嘗試下一個。

不能使用：

```python
break
```

因為目前 column 不合法，不代表後面的 column 也不合法。

---

### board 要怎麼表示？

可以建立：

```python
board = [
    ["."] * n
    for _ in range(n)
]
```

例如：

```python
n = 4
```

得到：

```python
[
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."]
]
```

放皇后：

```python
board[row][col] = "Q"
```

撤銷：

```python
board[row][col] = "."
```

---

### Backtracking 的做選擇

當 `(row, col)` 合法時：

```python
board[row][col] = "Q"
```

並記錄：

```python
cols.add(col)
neg_diag.add(row - col)
pos_diag.add(row + col)
```

這些代表：

```text
目前這個皇后已經佔用了

一個 column

一條 row - col 對角線

一條 row + col 對角線
```

---

### 進入下一層

目前 row 已經放好皇后。

下一層要處理：

```python
row + 1
```

所以：

```python
backtrack(row + 1)
```

---

### Backtracking 的撤銷選擇

探索完成後要恢復：

```python
board[row][col] = "."
```

並移除：

```python
cols.remove(col)
neg_diag.remove(row - col)
pos_diag.remove(row + col)
```

這樣才能嘗試目前 row 的其他 column。

完整流程：

```text
放皇后

↓

記錄 column 與 diagonal

↓

進入下一個 row

↓

恢復棋盤

↓

移除 column 與 diagonal
```

---

### 什麼時候找到答案？

當：

```python
row == n
```

代表：

```text
row 0 到 row n - 1

全部都成功放了一個皇后
```

因此已經放完 `n` 個皇后。

這時要把 board 轉換成題目要求的格式。

---

### 為什麼要 `"".join(row)`？

目前 board 是：

```python
[
    [".", "Q", ".", "."],
    [".", ".", ".", "Q"],
    ["Q", ".", ".", "."],
    [".", ".", "Q", "."]
]
```

但題目要求每一個 row 是字串：

```python
[
    ".Q..",
    "...Q",
    "Q...",
    "..Q."
]
```

所以要使用：

```python
["".join(row) for row in board]
```

---

### 為什麼要建立新的 board？

當找到答案時：

```python
res.append(["".join(row) for row in board])
```

這會建立一個新的字串陣列。

因此之後即使：

```python
board[row][col] = "."
```

也不會修改已經存進 `res` 的答案。

---

## 💻 Code

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        neg_diag = set()
        pos_diag = set()

        board = [
            ["."] * n
            for _ in range(n)
        ]

        res = []

        def backtrack(row):
            if row == n:
                res.append([
                    "".join(current_row)
                    for current_row in board
                ])
                return

            for col in range(n):
                if (
                    col in cols
                    or row - col in neg_diag
                    or row + col in pos_diag
                ):
                    continue

                board[row][col] = "Q"

                cols.add(col)
                neg_diag.add(row - col)
                pos_diag.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."

                cols.remove(col)
                neg_diag.remove(row - col)
                pos_diag.remove(row + col)

        backtrack(0)

        return res
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
class Solution:
```

* 定義 LeetCode 使用的 `Solution` 類別。

---

```python
def solveNQueens(self, n: int) -> List[List[str]]:
```

* 定義主要函式。
* `n` 代表棋盤大小，也是皇后數量。
* 回傳所有合法棋盤。

---

```python
cols = set()
```

* 儲存目前已經被皇后使用的 column。

例如：

```python
cols = {1, 3}
```

代表 column `1` 和 column `3` 已經有皇后。

---

```python
neg_diag = set()
```

* 儲存左上到右下對角線。
* 使用：

```python
row - col
```

作為對角線編號。

---

```python
pos_diag = set()
```

* 儲存右上到左下對角線。
* 使用：

```python
row + col
```

作為對角線編號。

---

```python
board = [
    ["."] * n
    for _ in range(n)
]
```

* 建立 `n x n` 棋盤。
* 每一格初始都是 `"."`。

例如：

```python
n = 3
```

得到：

```python
[
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
```

---

```python
res = []
```

* 儲存所有合法棋盤。

---

```python
def backtrack(row):
```

* 定義 Backtracking 函式。
* `row` 表示目前要放皇后的 row。

例如：

```python
row = 2
```

代表：

```text
row 0 和 row 1 已經放好皇后

現在要處理 row 2
```

---

```python
if row == n:
```

* 如果 `row` 已經等於 `n`，表示所有 row 都已經成功放置皇后。

例如：

```python
n = 4
row = 4
```

代表：

```text
row 0、1、2、3 都已經完成
```

---

```python
res.append([
    "".join(current_row)
    for current_row in board
])
```

* 將每一個 row 從字元 list 轉成字串。
* 再將完整棋盤加入答案。

例如：

```python
[".", "Q", ".", "."]
```

轉成：

```python
".Q.."
```

---

```python
return
```

* 一組完整答案已經加入。
* 結束目前分支。
* 回上一層繼續找其他解。

---

```python
for col in range(n):
```

* 嘗試目前 row 的每一個 column。

例如：

```python
n = 4
```

`col` 會依序是：

```text
0、1、2、3
```

---

```python
if (
    col in cols
    or row - col in neg_diag
    or row + col in pos_diag
):
    continue
```

* 檢查目前位置是否與之前皇后衝突。

---

### `col in cols`

表示：

```text
目前 column 已經有皇后
```

不能放。

---

### `row - col in neg_diag`

表示：

```text
目前位置和之前皇后位於同一條左上到右下對角線
```

不能放。

---

### `row + col in pos_diag`

表示：

```text
目前位置和之前皇后位於同一條右上到左下對角線
```

不能放。

---

```python
continue
```

* 目前 column 不合法。
* 跳過它，嘗試下一個 column。

---

```python
board[row][col] = "Q"
```

* 在目前位置放皇后。

例如：

```python
row = 0
col = 1
```

棋盤第一列會變成：

```python
[".", "Q", ".", "."]
```

---

```python
cols.add(col)
```

* 記錄目前 column 已被使用。

---

```python
neg_diag.add(row - col)
```

* 記錄目前左上到右下對角線已被使用。

---

```python
pos_diag.add(row + col)
```

* 記錄目前右上到左下對角線已被使用。

---

```python
backtrack(row + 1)
```

* 目前 row 已經放好皇后。
* 下一層處理下一個 row。

---

```python
board[row][col] = "."
```

* 撤銷剛才放置的皇后。
* 將棋盤恢復。

---

```python
cols.remove(col)
```

* 釋放目前 column。

---

```python
neg_diag.remove(row - col)
```

* 釋放目前左上到右下對角線。

---

```python
pos_diag.remove(row + col)
```

* 釋放目前右上到左下對角線。

---

```python
backtrack(0)
```

* 從 row `0` 開始放置皇后。

---

```python
return res
```

* 回傳所有合法棋盤。

---

## 🧪 Example Walkthrough

### Example

Input：

```python
n = 4
```

初始棋盤：

```text
. . . .
. . . .
. . . .
. . . .
```

初始狀態：

```python
cols = set()
neg_diag = set()
pos_diag = set()
```

呼叫：

```python
backtrack(0)
```

---

### Row 0

先嘗試：

```python
col = 0
```

位置：

```text
(0,0)
```

目前沒有衝突。

放皇后：

```text
Q . . .
. . . .
. . . .
. . . .
```

更新：

```python
cols = {0}
neg_diag = {0}
pos_diag = {0}
```

進入：

```python
backtrack(1)
```

---

### Row 1

嘗試：

```python
col = 0
```

因為：

```python
0 in cols
```

衝突，跳過。

嘗試：

```python
col = 1
```

位置：

```text
(1,1)
```

計算：

```python
row - col = 1 - 1 = 0
```

而：

```python
0 in neg_diag
```

表示和 `(0,0)` 在同一條對角線。

跳過。

嘗試：

```python
col = 2
```

位置：

```text
(1,2)
```

檢查：

```python
2 not in cols
```

```python
1 - 2 = -1
```

不在 `neg_diag`。

```python
1 + 2 = 3
```

不在 `pos_diag`。

所以可以放：

```text
Q . . .
. . Q .
. . . .
. . . .
```

進入 row 2。

---

### Row 2

依序檢查所有 column。

```python
col = 0
```

column 衝突。

```python
col = 1
```

與 `(1,2)` 在對角線衝突。

```python
col = 2
```

column 衝突。

```python
col = 3
```

與 `(1,2)` 在對角線衝突。

這一個 row 沒有任何位置能放皇后。

所以返回上一層。

---

### Backtracking

回到 row 1：

```python
board[1][2] = "."
```

並移除：

```python
cols.remove(2)
neg_diag.remove(-1)
pos_diag.remove(3)
```

然後繼續嘗試 row 1 的其他 column。

---

### 第一條路徑失敗

從：

```text
row 0 放在 col 0
```

開始的所有可能最後都無法完成四個皇后。

所以會回到 row 0，撤銷：

```text
(0,0)
```

接著嘗試：

```python
col = 1
```

---

### Row 0 放在 Column 1

棋盤：

```text
. Q . .
. . . .
. . . .
. . . .
```

接著成功找到：

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

也就是：

```python
[
    ".Q..",
    "...Q",
    "Q...",
    "..Q."
]
```

---

### 找到答案後仍要繼續

當：

```python
row == 4
```

加入答案後：

```python
return
```

回到上一層。

然後撤銷最後一個皇后，繼續尋找其他可能。

最後還會找到：

```python
[
    "..Q.",
    "Q...",
    "...Q",
    ".Q.."
]
```

---

### 最終答案

```python
[
    [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
    ],
    [
        "..Q.",
        "Q...",
        "...Q",
        ".Q.."
    ]
]
```

---

## 🌳 Recursion Tree

以 `n = 4` 簡化表示：

```text
row 0
├── col 0
│   ├── row 1 col 2
│   │   └── row 2 無位置 ×
│   └── row 1 col 3
│       └── 最後失敗 ×
│
├── col 1
│   └── row 1 col 3
│       └── row 2 col 0
│           └── row 3 col 2
│               └── 找到答案 ✓
│
├── col 2
│   └── row 1 col 0
│       └── row 2 col 3
│           └── row 3 col 1
│               └── 找到答案 ✓
│
└── col 3
    └── 所有分支失敗 ×
```

---

## 🔍 對角線為什麼是 `row - col` 和 `row + col`？

### 左上到右下

```text
(0,0)  (1,1)  (2,2)  (3,3)
```

計算：

```text
0 - 0 = 0

1 - 1 = 0

2 - 2 = 0

3 - 3 = 0
```

所以：

```python
row - col
```

相同。

---

### 右上到左下

```text
(0,3)  (1,2)  (2,1)  (3,0)
```

計算：

```text
0 + 3 = 3

1 + 2 = 3

2 + 1 = 3

3 + 0 = 3
```

所以：

```python
row + col
```

相同。

---

### 記憶方式

```text
\ 對角線
row - col 相同

/ 對角線
row + col 相同
```

---

## 🔄 為什麼這題是 Backtracking？

因為每一次都會：

```text
嘗試放皇后

↓

記錄 column 與 diagonal

↓

遞迴處理下一個 row

↓

撤銷皇后

↓

移除 column 與 diagonal
```

程式：

```python
board[row][col] = "Q"

cols.add(col)
neg_diag.add(row - col)
pos_diag.add(row + col)

backtrack(row + 1)

board[row][col] = "."

cols.remove(col)
neg_diag.remove(row - col)
pos_diag.remove(row + col)
```

這就是標準：

```text
做選擇

↓

遞迴

↓

撤銷選擇
```

---

## ⏱ Complexity Analysis

### Time Complexity

第一個 row 最多有：

```text
n
```

個位置。

第二個 row 因為不能使用相同 column，最多剩下：

```text
n - 1
```

個位置。

接著大約是：

```text
n - 2
```

因此最壞情況可以看成：

```text
O(n!)
```

實際上對角線限制會剪掉很多分支，所以通常比單純排列更快。

每找到一組答案時，需要建立棋盤字串：

```text
O(n²)
```

如果答案數量是 `S`，輸出答案還需要：

```text
O(S × n²)
```

---

### Space Complexity

不包含答案：

遞迴深度最多：

```text
O(n)
```

三個 set 最多各儲存：

```text
O(n)
```

棋盤需要：

```text
O(n²)
```

所以整體額外空間：

```text
O(n²)
```

如果不把棋盤本身算作輔助空間，僅看遞迴與 set，則是：

```text
O(n)
```

---

## 🎯 Interview Takeaways

* 一層遞迴處理一個 row。
* 每個 row 嘗試所有 column。
* 不需要檢查 row，因為每層只會放一個皇后。
* 使用 `cols` 檢查 column。
* 使用 `row - col` 檢查 `\` 對角線。
* 使用 `row + col` 檢查 `/` 對角線。
* 有衝突時使用：

```python
continue
```

* Base case：

```python
if row == n:
```

* 找到答案後要把 board 轉成字串。
* 放皇后後要記錄三種限制。
* 遞迴返回後一定要撤銷。
* 這題要找所有答案，所以不能找到一組後就直接停止全部搜尋。

---

## ✍️ 我學到的東西 | What I Learned

* `backtrack(row)` 代表處理目前 row。
* 每一個 row 一定只放一個皇后。
* 每一層的選擇是不同 column。
* `cols` 記錄已使用的 column。
* `row - col` 可以辨認左上到右下對角線。
* `row + col` 可以辨認右上到左下對角線。
* 三個條件都沒有衝突時才能放皇后。
* 放皇后後，要把 column 和 diagonal 加入 set。
* 遞迴完成後，要把皇后與 set 狀態全部恢復。
* 當 `row == n`，代表已經成功放完 `n` 個皇后。
* 找到答案時要建立新的棋盤字串。
* 這題的 Backtracking 狀態不需要 `path`。
* board 本身就是目前的選擇狀態。

---

## 🏆 Cheat Sheet

```text
LeetCode 51 — N-Queens

一層處理一個 row

backtrack(row)

↓

找到完整答案

if row == n:
    res.append(...)
    return

↓

嘗試所有 column

for col in range(n):

↓

檢查衝突

col in cols
row - col in neg_diag
row + col in pos_diag

↓

有衝突

continue

↓

做選擇

board[row][col] = "Q"

cols.add(col)
neg_diag.add(row - col)
pos_diag.add(row + col)

↓

下一個 row

backtrack(row + 1)

↓

撤銷選擇

board[row][col] = "."

cols.remove(col)
neg_diag.remove(row - col)
pos_diag.remove(row + col)
```

### 對角線公式

```text
\ 對角線：

row - col

/ 對角線：

row + col
```

### Backtracking 模板

```python
for col in range(n):
    if (
        col in cols
        or row - col in neg_diag
        or row + col in pos_diag
    ):
        continue

    board[row][col] = "Q"

    cols.add(col)
    neg_diag.add(row - col)
    pos_diag.add(row + col)

    backtrack(row + 1)

    board[row][col] = "."

    cols.remove(col)
    neg_diag.remove(row - col)
    pos_diag.remove(row + col)
```

### LeetCode 51 vs LeetCode 79

| 題目          | 每層代表什麼 | 做選擇      | 撤銷選擇     |
| ----------- | ------ | -------- | -------- |
| LeetCode 51 | 一個 row | 放 `"Q"`  | 改回 `"."` |
| LeetCode 79 | 一個字元位置 | 標記 `"#"` | 恢復原字元    |

---

## 🌟 One Sentence Summary

> Place one queen per row, track used columns and diagonals with sets, and backtrack after exploring each valid position.

> 每一層在一個 row 放置一個皇后，使用 set 記錄已被佔用的 column 與兩種對角線，探索完成後再撤銷選擇。
