# 📍 LeetCode 79 — Word Search

## 📄 題目說明 | Problem Description

### 中文

給定一個由英文字母組成的二維網格 `board`，以及一個字串 `word`。

請判斷是否可以在網格中找到這個字串。

字串中的字母必須按照順序，由相鄰的格子組成。

相鄰格子只能是：

```text
上

下

左

右
```

不能斜著走。

而且同一個格子在同一條搜尋路徑中，不能重複使用。

---

### English

Given an `m x n` grid of characters `board` and a string `word`, return `True` if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells.

Adjacent cells are horizontally or vertically neighboring.

The same cell may not be used more than once in the same path.

---

### Examples

#### Example 1

Input：

```python
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"
```

Output：

```python
True
```

搜尋路徑：

```text
A → B → C → C → E → D
```

---

#### Example 2

Input：

```python
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "SEE"
```

Output：

```python
True
```

---

#### Example 3

Input：

```python
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCB"
```

Output：

```python
False
```

原因：

雖然可以找到：

```text
A → B → C
```

但最後需要再次使用前面已經使用過的 `B`。

同一條路徑不能重複使用同一個格子。

---

## 🧠 核心觀念 | Key Insight

這題是：

```text
DFS
+
Backtracking
+
二維網格搜尋
```

我們要從每一個格子開始，嘗試看看能不能找到完整的 `word`。

---

### 寫 DFS 前先問：DFS 要回傳什麼？

這題的 DFS 要回答：

> 從目前的 `(row, col)` 開始，能不能找到 `word[index:]`？

所以：

```python
dfs(row, col, index)
```

回傳：

```text
True
```

代表：

```text
從目前格子開始

可以找到 word 從 index 開始的剩餘部分
```

回傳：

```text
False
```

代表：

```text
從目前格子開始

無法完成剩餘字串
```

---

### DFS 的三個參數

```python
def dfs(row, col, index):
```

三個參數分別代表：

```text
row
```

目前所在格子的 row。

```text
col
```

目前所在格子的 column。

```text
index
```

目前要比對 `word` 的哪一個字元。

例如：

```python
word = "ABCCED"
```

如果：

```python
index = 0
```

代表目前要找：

```text
"A"
```

如果：

```python
index = 1
```

代表目前要找：

```text
"B"
```

如果：

```python
index = 2
```

代表目前要找：

```text
"C"
```

---

### 這題的狀態不是 path list

在 LeetCode 17、40、131 中，我們會使用：

```python
path
```

儲存目前選過的內容。

但這題不需要回傳路徑，只需要判斷：

```text
word 存不存在
```

所以不需要真的建立 `path`。

目前已經比對到哪裡，可以直接由：

```python
index
```

表示。

例如：

```python
index = 3
```

代表前面：

```text
word[0]
word[1]
word[2]
```

已經成功找到。

現在要找：

```python
word[3]
```

---

### 從每一個格子開始搜尋

因為不知道字串的第一個字母會出現在哪裡，所以要嘗試所有格子。

```python
for row in range(rows):
    for col in range(cols):
```

對每個格子呼叫：

```python
dfs(row, col, 0)
```

其中：

```python
index = 0
```

代表從 `word` 的第一個字元開始比對。

如果任何一個起點成功：

```python
if dfs(row, col, 0):
    return True
```

就可以直接回傳 `True`。

---

### DFS 的成功條件

```python
if index == len(word):
    return True
```

代表：

```text
word 中的所有字元都已經成功比對完
```

例如：

```python
word = "ABC"
```

當：

```python
index = 3
```

代表：

```text
A、B、C 都已經找到了
```

所以直接回傳：

```python
True
```

---

### 為什麼成功條件要先判斷？

假設：

```python
word = "A"
```

從一個值為 `"A"` 的格子開始。

比對成功後，下一層會呼叫：

```python
dfs(next_row, next_col, 1)
```

因為：

```python
len(word) = 1
```

所以：

```python
index == len(word)
```

代表完整字串已經找到。

這時不需要再檢查新的格子是不是越界。

因此成功條件可以放在最前面。

---

### DFS 的失敗條件

以下情況都要回傳 `False`：

```python
if (
    row < 0
    or row >= rows
    or col < 0
    or col >= cols
    or board[row][col] != word[index]
):
    return False
```

包含：

1. `row < 0`
2. `row >= rows`
3. `col < 0`
4. `col >= cols`
5. 目前格子的字母不等於 `word[index]`

---

### 邊界檢查

假設：

```python
board = [
    ["A", "B"],
    ["C", "D"]
]
```

合法位置：

```text
(0,0) (0,1)
(1,0) (1,1)
```

如果走到：

```text
(-1,0)
(2,0)
(0,-1)
(0,2)
```

都已經超出 board。

所以要檢查：

```python
row < 0
row >= rows
col < 0
col >= cols
```

---

### 字母不符合就失敗

假設：

```python
word[index] = "C"
```

但是目前格子：

```python
board[row][col] = "B"
```

表示目前路徑無法繼續。

所以：

```python
return False
```

---

### 同一個格子不能重複使用

這題最重要的限制之一：

```text
同一條搜尋路徑中

同一個格子不能用兩次
```

例如：

```python
board = [
    ["A", "B"],
    ["C", "D"]
]
```

如果正在尋找：

```text
"ABA"
```

不能：

```text
A → B → 回到原本的 A
```

因為第一個 `A` 已經使用過。

---

### 如何記錄格子已經使用？

最常見的方法是暫時修改 board。

```python
temp = board[row][col]
board[row][col] = "#"
```

例如原本：

```text
A
```

暫時改成：

```text
#
```

因為 `word` 中不會需要匹配 `#`，所以其他 DFS 再走回這個格子時，就會失敗。

---

### 為什麼可以直接修改 board？

因為我們只需要在目前這條 DFS 路徑中，標記這個格子已經被使用。

探索完目前路徑後，再把它恢復：

```python
board[row][col] = temp
```

所以這個修改只是暫時的。

這就是 Backtracking：

```text
做選擇

↓

標記目前格子已使用

↓

遞迴探索

↓

恢復目前格子
```

---

### 為什麼一定要恢復？

假設：

```python
board[row][col] = "#"
```

之後沒有恢復。

那麼其他起點或其他搜尋路徑也會認為這個格子不能使用。

但題目只規定：

```text
同一條路徑不能重複使用
```

不同的搜尋路徑可以重新使用同一個格子。

所以遞迴完成後一定要：

```python
board[row][col] = temp
```

---

### 四個方向

從目前格子可以走：

```text
上
下
左
右
```

對應：

```python
dfs(row + 1, col, index + 1)
dfs(row - 1, col, index + 1)
dfs(row, col + 1, index + 1)
dfs(row, col - 1, index + 1)
```

---

### 為什麼是 `index + 1`？

因為目前：

```python
board[row][col]
```

已經成功比對：

```python
word[index]
```

下一個格子就要比對：

```python
word[index + 1]
```

所以四個方向都傳：

```python
index + 1
```

---

### 使用 `or` 合併四個方向

```python
found = (
    dfs(row + 1, col, index + 1)
    or dfs(row - 1, col, index + 1)
    or dfs(row, col + 1, index + 1)
    or dfs(row, col - 1, index + 1)
)
```

只要任何一個方向成功：

```text
found = True
```

就代表從目前格子開始可以完成剩餘字串。

---

### `or` 有短路效果

Python 的 `or` 具有 short-circuit。

例如：

```python
True or dfs(...)
```

第一個條件已經是 `True`，後面的 DFS 就不會再執行。

所以找到一條成功路徑後，就不需要繼續搜尋其他方向。

---

### 為什麼不能找到成功後直接 return，卻不恢復 board？

錯誤寫法：

```python
board[row][col] = "#"

if dfs(row + 1, col, index + 1):
    return True

board[row][col] = temp
```

如果下一層成功，會直接：

```python
return True
```

這樣：

```python
board[row][col] = temp
```

永遠不會執行。

board 會維持被修改的狀態。

所以比較安全的寫法是：

```python
found = (...)

board[row][col] = temp

return found
```

先儲存搜尋結果，再恢復 board，最後回傳。

---

### 這題的 Backtracking 模板

```python
temp = board[row][col]

board[row][col] = "#"

found = (
    dfs(...)
    or dfs(...)
    or dfs(...)
    or dfs(...)
)

board[row][col] = temp

return found
```

完整意思：

```text
保存原本字元

↓

標記目前格子已使用

↓

搜尋四個方向

↓

恢復原本字元

↓

回傳搜尋結果
```

---

## 💻 Code

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            board[row][col] = temp

            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
class Solution:
```

* 定義 LeetCode 使用的 `Solution` 類別。

---

```python
def exist(self, board: List[List[str]], word: str) -> bool:
```

* 定義主要函式 `exist`。
* `board` 是二維字元網格。
* `word` 是要搜尋的字串。
* 回傳：

```python
True
```

表示找到。

回傳：

```python
False
```

表示找不到。

---

```python
rows = len(board)
```

* 取得 board 的 row 數量。

例如：

```python
board = [
    ["A", "B", "C"],
    ["D", "E", "F"]
]
```

則：

```python
rows = 2
```

---

```python
cols = len(board[0])
```

* 取得 board 的 column 數量。

上面的例子中：

```python
cols = 3
```

---

```python
def dfs(row, col, index):
```

* 定義 DFS 函式。
* `row`、`col` 是目前格子位置。
* `index` 是目前要比對 `word` 的 index。
* 回傳布林值。

DFS 要回答：

```text
從 board[row][col] 開始

能不能找到 word[index:]
```

---

```python
if index == len(word):
    return True
```

* 如果 `index` 已經等於字串長度，代表所有字元都成功匹配完成。

例如：

```python
word = "ABC"
index = 3
```

表示：

```text
A、B、C 都已經找到
```

因此回傳 `True`。

---

```python
if (
    row < 0
    or row >= rows
    or col < 0
    or col >= cols
    or board[row][col] != word[index]
):
    return False
```

* 檢查目前狀態是否無效。

---

### `row < 0`

```python
row < 0
```

表示往上走超出 board。

---

### `row >= rows`

```python
row >= rows
```

表示往下走超出 board。

---

### `col < 0`

```python
col < 0
```

表示往左走超出 board。

---

### `col >= cols`

```python
col >= cols
```

表示往右走超出 board。

---

### `board[row][col] != word[index]`

* 目前格子的字母，不等於現在需要的字母。
* 這條路徑無法繼續。

---

### 為什麼邊界條件要寫在字母檢查前面？

因為如果：

```python
row = -1
```

還直接執行：

```python
board[row][col]
```

就可能讀取到錯誤位置。

因此一定要先透過 `or` 檢查邊界。

Python 的 `or` 具有短路效果。

一旦：

```python
row < 0
```

成立，後面的：

```python
board[row][col]
```

就不會執行。

---

```python
temp = board[row][col]
```

* 保存目前格子的原始字元。

例如：

```python
board[row][col] = "A"
```

則：

```python
temp = "A"
```

稍後 Backtracking 時要用它恢復。

---

```python
board[row][col] = "#"
```

* 暫時將目前格子改成 `#`。
* 表示目前這條搜尋路徑已經使用過這個格子。

如果下一層再走回來：

```python
board[row][col] != word[index]
```

會成立，所以無法重複使用。

---

```python
found = (
    dfs(row + 1, col, index + 1)
    or dfs(row - 1, col, index + 1)
    or dfs(row, col + 1, index + 1)
    or dfs(row, col - 1, index + 1)
)
```

* 搜尋四個方向。
* 只要有一個方向成功，`found` 就是 `True`。

---

### 往下

```python
dfs(row + 1, col, index + 1)
```

row 加一。

---

### 往上

```python
dfs(row - 1, col, index + 1)
```

row 減一。

---

### 往右

```python
dfs(row, col + 1, index + 1)
```

col 加一。

---

### 往左

```python
dfs(row, col - 1, index + 1)
```

col 減一。

---

```python
board[row][col] = temp
```

* 搜尋完四個方向後，恢復目前格子的原始字元。
* 讓其他搜尋路徑仍然可以使用這個格子。

這一步就是 Backtracking 的撤銷選擇。

---

```python
return found
```

* 回傳從目前位置開始，是否可以完成剩餘字串。

---

```python
for row in range(rows):
```

* 遍歷每一個 row。

---

```python
for col in range(cols):
```

* 遍歷每一個 column。
* 因此會檢查 board 中所有格子。

---

```python
if dfs(row, col, 0):
    return True
```

* 從目前格子開始搜尋。
* `0` 表示從 `word[0]` 開始比對。
* 如果任何一個起點成功，就直接回傳 `True`。

---

```python
return False
```

* 所有格子都嘗試過，仍然找不到完整字串。
* 回傳 `False`。

---

## 🧪 Example Walkthrough

### Example

Input：

```python
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"
```

board index：

```text
        col
         0   1   2   3

row 0    A   B   C   E
row 1    S   F   C   S
row 2    A   D   E   E
```

要搜尋：

```text
A → B → C → C → E → D
```

---

### 從 `(0,0)` 開始

```python
dfs(0, 0, 0)
```

目前：

```python
board[0][0] = "A"
word[0] = "A"
```

符合。

暫時標記：

```text
# B C E
S F C S
A D E E
```

接著搜尋下一個字母：

```python
word[1] = "B"
```

---

### 搜尋四個方向

從 `(0,0)`：

```text
下：(1,0) = S
上：(-1,0) 越界
右：(0,1) = B
左：(0,-1) 越界
```

右邊是 `B`，所以成功進入：

```python
dfs(0, 1, 1)
```

---

### 目前在 `(0,1)`

```python
board[0][1] = "B"
word[1] = "B"
```

符合。

標記：

```text
# # C E
S F C S
A D E E
```

下一個要找：

```python
word[2] = "C"
```

右邊：

```python
board[0][2] = "C"
```

符合。

進入：

```python
dfs(0, 2, 2)
```

---

### 目前在 `(0,2)`

匹配：

```text
C
```

標記後：

```text
# # # E
S F C S
A D E E
```

下一個仍然要找：

```python
word[3] = "C"
```

往下：

```python
board[1][2] = "C"
```

符合。

---

### 目前在 `(1,2)`

標記：

```text
# # # E
S F # S
A D E E
```

下一個找：

```python
word[4] = "E"
```

往下：

```python
board[2][2] = "E"
```

符合。

---

### 目前在 `(2,2)`

下一個找：

```python
word[5] = "D"
```

往左：

```python
board[2][1] = "D"
```

符合。

---

### 找到最後一個字母

當 `D` 匹配完成後，下一層：

```python
index = 6
```

而：

```python
len(word) = 6
```

所以：

```python
index == len(word)
```

回傳：

```python
True
```

---

### True 向上傳遞

```text
D 找到 → True

E 能走到 D → True

C 能走到 E → True

C 能走到 C → True

B 能走到 C → True

A 能走到 B → True
```

最後：

```python
dfs(0, 0, 0)
```

回傳 `True`。

主函式直接：

```python
return True
```

---

### 路徑圖

```text
A → B → C
        ↓
        C
        ↓
D ← E
```

完整順序：

```text
(0,0) A
→
(0,1) B
→
(0,2) C
→
(1,2) C
→
(2,2) E
→
(2,1) D
```

---

### Backtracking 恢復過程

雖然找到答案後會一路回傳 `True`，但每一層都會先執行：

```python
board[row][col] = temp
```

所以最後 board 仍然恢復成：

```python
[
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
```

不會保留 `#`。

---

## 🌳 Recursion Tree

以：

```python
word = "ABCCED"
```

簡化表示：

```text
dfs(A, index=0)
│
├── 下：S ≠ B → False
├── 上：越界 → False
├── 右：B = B
│   │
│   ├── 下：F ≠ C → False
│   ├── 上：越界 → False
│   ├── 右：C = C
│   │   │
│   │   ├── 下：C = C
│   │   │   │
│   │   │   ├── 下：E = E
│   │   │   │   │
│   │   │   │   └── 左：D = D
│   │   │   │       │
│   │   │   │       └── index == len(word) → True
│   │   │   │
│   │   │   └── True
│   │   │
│   │   └── True
│   │
│   └── True
│
└── True
```

---

## 🔄 為什麼這題是 Backtracking？

因為每個格子都會經過：

```text
選擇目前格子

↓

標記不能再次使用

↓

探索四個方向

↓

恢復目前格子
```

程式對應：

```python
temp = board[row][col]

board[row][col] = "#"

found = dfs(...)

board[row][col] = temp
```

這就是：

```text
做選擇

↓

遞迴

↓

撤銷選擇
```

---

## 🆚 使用 `visited` Set 的寫法

也可以使用：

```python
visited = set()
```

記錄目前路徑使用過的位置。

例如：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
                or board[row][col] != word[index]
            ):
                return False

            visited.add((row, col))

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            visited.remove((row, col))

            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
```

---

### 原地修改 vs visited set

| 方法            | 做法              |   額外空間 |
| ------------- | --------------- | -----: |
| 原地修改          | 將字元暫時改成 `#`     |     較少 |
| `visited` set | 儲存 `(row, col)` | `O(L)` |

其中：

```text
L = word 的長度
```

原地修改通常更簡潔，也比較省空間。

---

## ⏱ Complexity Analysis

設：

```text
m = board 的 row 數

n = board 的 column 數

L = word 的長度
```

---

### Time Complexity

主程式可能從每個格子開始搜尋：

```text
m × n
```

個起點。

每個字元最多可以往四個方向走。

第一步最多有：

```text
4
```

個方向。

之後因為不能走回上一個已使用的格子，通常最多只剩：

```text
3
```

個方向。

因此更精確的上界常寫成：

```text
O(m × n × 3^L)
```

有些簡化分析也會寫：

```text
O(m × n × 4^L)
```

其中 `4^L` 是較寬鬆的上界。

面試時可以說：

> 每個格子都可能是起點，而每一層 DFS 最多往四個方向搜尋，深度最多為 word 長度，因此時間複雜度上界是 `O(m × n × 4^L)`；考慮不能立即回到已使用格子，可更精確寫成 `O(m × n × 3^L)`。

---

### Space Complexity

遞迴深度最多是：

```text
L
```

因為每成功匹配一個字元，`index` 加一。

因此額外遞迴空間：

```text
O(L)
```

如果使用原地修改，不需要額外的 `visited` set。

如果使用 `visited` set，也最多儲存 `L` 個位置，因此仍然是：

```text
O(L)
```

---

## 🎯 Interview Takeaways

* 看到二維網格中搜尋字串，想到 DFS + Backtracking。
* DFS 要回傳：

```text
從目前格子開始

能不能找到剩餘字串
```

* DFS 狀態：

```python
dfs(row, col, index)
```

* Base case：

```python
if index == len(word):
    return True
```

* 失敗條件：

```text
越界

或

目前字母不符合
```

* 同一條路徑不能重複使用格子。
* 可以原地將目前格子改成 `#`。
* 遞迴結束後一定要恢復原字元。
* 搜尋四個方向。
* 下一層使用：

```python
index + 1
```

* 使用 `or`，只要任一方向成功就回傳 `True`。
* 外層要從所有格子嘗試作為起點。

---

## ✍️ 我學到的東西 | What I Learned

* 這題的 DFS 回傳值是 `bool`。
* `dfs(row, col, index)` 表示從目前位置能不能找到 `word[index:]`。
* `index` 代表目前要匹配的字元。
* 當 `index == len(word)`，代表完整字串已經找到。
* 在讀取 `board[row][col]` 前要先確認沒有越界。
* 可以暫時修改 board，避免同一條路徑重複使用格子。
* 原地修改後一定要恢復，否則會影響其他搜尋路徑。
* `or` 可以讓搜尋在找到成功方向後提前停止。
* 不需要 `path`，因為題目只問存在與否。
* Backtracking 不一定都要有 list。
* 只要有「做選擇、遞迴、撤銷選擇」，就是 Backtracking。
* 外層雙迴圈負責選起點。
* 內層 DFS 負責尋找完整字串。

---

## 🏆 Cheat Sheet

```text
LeetCode 79 — Word Search

DFS 要回答：

從目前 (row, col)

能不能找到 word[index:]

↓

成功：

if index == len(word):
    return True

↓

失敗：

越界
或
board[row][col] != word[index]

↓

保存原字元：

temp = board[row][col]

↓

標記已使用：

board[row][col] = "#"

↓

搜尋四方向：

dfs(row + 1, col, index + 1)
dfs(row - 1, col, index + 1)
dfs(row, col + 1, index + 1)
dfs(row, col - 1, index + 1)

↓

恢復：

board[row][col] = temp

↓

回傳：

return found
```

### DFS 模板

```python
def dfs(row, col, index):
    if index == len(word):
        return True

    if (
        row < 0
        or row >= rows
        or col < 0
        or col >= cols
        or board[row][col] != word[index]
    ):
        return False

    temp = board[row][col]
    board[row][col] = "#"

    found = (
        dfs(row + 1, col, index + 1)
        or dfs(row - 1, col, index + 1)
        or dfs(row, col + 1, index + 1)
        or dfs(row, col - 1, index + 1)
    )

    board[row][col] = temp

    return found
```

### LeetCode 79 vs LeetCode 200

| 題目           | DFS 回傳什麼 | 是否需要恢復 |
| ------------ | -------- | ------ |
| LeetCode 79  | `bool`   | 需要     |
| LeetCode 200 | 通常不回傳    | 通常不需要  |

原因：

LeetCode 79 中：

```text
同一格只是在目前路徑暫時不能使用
```

所以要恢復。

LeetCode 200 中：

```text
島嶼格子被永久標記為已拜訪
```

通常不需要恢復。

### LeetCode 79 vs 一般 Backtracking

| 題目           | 做選擇                     | 撤銷選擇         |
| ------------ | ----------------------- | ------------ |
| LeetCode 40  | `path.append()`         | `path.pop()` |
| LeetCode 131 | `path.append()`         | `path.pop()` |
| LeetCode 79  | `board[row][col] = "#"` | 恢復原字元        |

---

## 🌟 One Sentence Summary

> Start DFS from every cell, match one character at a time, temporarily mark each used cell, explore four directions, and restore the cell during backtracking.

> 從每個格子開始 DFS，一次比對一個字元，暫時標記已使用的格子，往四個方向搜尋，並在 Backtracking 時恢復原本字元。
