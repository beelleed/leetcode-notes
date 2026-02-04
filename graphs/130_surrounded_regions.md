# 📍 LeetCode 130 — Surrounded Regions | 被包圍的區域

🔗 [題目連結](https://leetcode.com/problems/surrounded-regions/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給你一個 m x n 的棋盤 board，裡面只有 'X' 和 'O'。

- 規則： 如果一個 'O' 區域「被 'X' 完全包住」（上下左右連通），那這整個區域要被翻成 'X'。

- 例外： 只要這個 'O' 區域有任何一格 連到邊界（第一列/最後一列/第一行/最後一行），它就 不會被翻。

### English

Given an m x n board containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured if it is not connected to the border.

### Examples

- Example 1:

    - Input:
        ```css
        [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
        ```

    - Output:
        ```css
        [["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]]
        ```

    - Explanation:

        ![](../images/130_xogrid.jpg)

        - 中間那團 O 沒有連到邊界 → 被翻成 X

        - 左下那顆 O 在邊界 → 保留
- Example 2:

    - Input: board = [["X"]]

    - Output: [["X"]]

---

## 🧠 方法一: 解題思路 | Solution Idea (DFS)
- 這題在問什麼？

    - 不是在找「哪些 O 被包住」，而是反過來想更簡單：

        - ✅ 邊界上連得到的 O 一定不能翻。
        - ❌ 其他 O 才是「被包圍」要翻掉的。

- 關鍵觀念

    - 只要一個 'O' 可以從邊界的某個 'O' 走到（上下左右），它就「安全」。

    - 所以我們要做的是：

        1. 從所有邊界的 'O' 出發做 DFS/BFS，把走得到的 'O' 標記成安全（例如改成 '#'）。

        2. 掃一次整張圖：

            - 剩下的 'O' → 被包圍 → 翻成 'X'

            - '#' → 安全的 → 變回 'O'

---

## 💻 程式碼實作 | Code (DFS)
```python
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != "O":
                return

            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1) 從邊界的 O 出發，把安全的 O 全標成 #
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        # 2) 翻轉：O -> X（被包圍），# -> O（安全）
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### 邊界檢查
```python
if not board or not board[0]:
    return
```

- 空矩陣直接結束，避免 len(board[0]) 出錯。

#### DFS 函數：標記安全 O
```python
def dfs(r, c):
    if r < 0 or r >= m or c < 0 or c >= n:
        return
    if board[r][c] != "O":
        return
    board[r][c] = "#"
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

```

- 只要是 'O' 才處理

- 用 '#' 表示「這個 O 連到邊界，所以安全」

#### 從邊界出發
##### 掃左右邊界
```python
for r in range(m):
    if board[r][0] == "O":
        dfs(r, 0)
    if board[r][n - 1] == "O":
        dfs(r, n - 1)
```

- (r, 0) 是最左邊一欄

- (r, n-1) 是最右邊一欄

##### 掃上下邊界
```python
for c in range(n):
    if board[0][c] == "O":
        dfs(0, c)
    if board[m - 1][c] == "O":
        dfs(m - 1, c)
```

- (0, c) 最上面一列

- (m-1, c) 最下面一列

- ✅ 這樣做的意義：只要是「邊界上的 O」，它與它能連到的所有 O 都不能翻，所以先全部標成 #。

#### 最後翻轉
```python
for r in range(m):
    for c in range(n):
        if board[r][c] == "O":
            board[r][c] = "X"
        elif board[r][c] == "#":
            board[r][c] = "O"
```

- 還是 O 的：代表 沒連到邊界 → 被包圍 → 翻成 X

- #：代表 安全 → 改回 O

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
X X X X
X O O X
X X O X
X O X X
```
### Step 0：初始

- 邊界上的 O 只有 (3,1)

### Step 1：掃左右邊界（for r）

- r=3 時，board[3][0]="X"、board[3][3]="X"（右邊界也不是 O）→ 這輪左右邊界沒觸發

### Step 2：掃上下邊界（for c）

- 最底列 board[3][1] == "O" → 呼叫 dfs(3,1)

### Step 3：DFS(3,1)

- board[3][1] 是 O → 改成 #

- 往四個方向：

    - (4,1) 越界 return

    - (2,1) 是 X return

    - (3,2) 是 X return

    - (3,0) 是 X return

- 結果變成：
```text
X X X X
X O O X
X X O X
X # X X
```
### Step 4：最終翻轉（掃整張）

- 所有還是 O 的（中間那團）→ 翻成 X

- #: 改回 O

### Output
```text
X X X X
X X X X
X X X X
X O X X
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 設：

    - m, n = board 的高與寬

- 時間複雜度：O(m * n)

    - 每個格子最多被 DFS 訪問/標記一次，再掃一次翻轉。

- 空間複雜度：

    - DFS recursion stack 最差 O(m * n)（整張都是 O 時）

    - 若想避免 recursion depth，可以改 BFS（queue）。

---

## ✍️ 我學到的東西 | What I Learned

- 這題的關鍵不是「找被包住」，而是「找不會被包住」：邊界連通的 O 都安全

- 常見套路：

    - 從邊界開始 flood fill

    - 標記安全區

    - 最後再統一翻轉

- 類似題型看到：

    - surrounded / enclosed / capture regions

    - island + border

    - 👉 優先想 從邊界出發 的 BFS/DFS

---

## 🧠 一句話總結

I mark all 'O' cells connected to the border as safe using DFS, then flip the remaining 'O' to 'X', and restore the safe ones back to 'O'.

---

## 💻 程式碼實作 | Code (Python, BFS)
```python
from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        queue = deque()

        # 1) 把所有邊界上的 'O' 加進 queue，並標記成 '#'
        for r in range(m):
            if board[r][0] == "O":
                board[r][0] = "#"
                queue.append((r, 0))
            if board[r][n - 1] == "O":
                board[r][n - 1] = "#"
                queue.append((r, n - 1))

        for c in range(n):
            if board[0][c] == "O":
                board[0][c] = "#"
                queue.append((0, c))
            if board[m - 1][c] == "O":
                board[m - 1][c] = "#"
                queue.append((m - 1, c))

        # 2) BFS：把所有與邊界連通的 O 標成 '#'
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))

        # 3) 翻轉結果
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### 建立 queue（BFS 核心）
```python
queue = deque()
```

- BFS 一定需要 queue

- 存的是 (row, col)

#### Step 1：找「邊界的 O」
```python
if board[r][0] == "O":
    board[r][0] = "#"
    queue.append((r, 0))
```

- 為什麼 立刻改成 # 再丟進 queue？

    - 👉 避免重複加入

- 一旦標成 #

- 後面就不會再被當成 O 重複處理

- 邊界一共四條：

    - 左邊 (r, 0)

    - 右邊 (r, n-1)

    - 上邊 (0, c)

    - 下邊 (m-1, c)

#### Step 2：BFS 擴散（flood fill）
```python
while queue:
    r, c = queue.popleft()
```

- 每次從 queue 拿一個「已知安全的 O」

- 嘗試往四個方向擴展
```python
if board[nr][nc] == "O":
    board[nr][nc] = "#"
    queue.append((nr, nc))
```

- 只處理 O

- 一旦加入 queue，立刻標成 #

- 保證每個格子只會進 queue 一次

#### Step 3：最後翻轉
```python
if board[r][c] == "O":
    board[r][c] = "X"
elif board[r][c] == "#":
    board[r][c] = "O"
```

- 剩下的 O：沒連到邊界 → 被包圍

- #：安全 → 還原成 O

---

## 🧪 範例流程 | Example Walkthrough（BFS）
### Input
```text
X X X X
X O O X
X X O X
X O X X
```
### Step 0：初始化
```text
queue = []
```
### Step 1：掃邊界

- (3,1) 是邊界 O
```text
board[3][1] = "#"
queue = [(3,1)]
```
### Step 2：BFS

- pop (3,1)

- 四周不是 O → 無擴散
```text
X X X X
X O O X
X X O X
X # X X
```
### Step 3：翻轉

- 中間的 O → X

- #→ O

### Final
```text
X X X X
X X X X
X X X X
X O X X
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 設 m x n 為 board 大小

- 時間複雜度：O(m * n)

    - 每個格子最多進 queue 一次

- 空間複雜度：O(m * n)

    - queue 最差情況會存整張圖（全是 O 且連通）

---

## ✍️ 我學到的東西 | What I Learned

- 130 是 經典「邊界 flood fill」題

- DFS / BFS 只是工具不同：

    - DFS：recursive

    - BFS：queue

- BFS 的關鍵技巧：

    - 進 queue 當下就標記

    - 不要等 pop 才標，避免重複

---

## 🧠 一句話總結

I push all border 'O' cells into a queue, use BFS to mark all border-connected regions as safe, then flip the remaining 'O' to 'X'.