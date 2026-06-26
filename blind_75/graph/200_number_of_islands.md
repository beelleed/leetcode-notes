# 🏝️ LeetCode 200 - Number of Islands

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/number-of-islands/)

---

## 題目說明 | Problem Description

### 📘 中文
給定一個由 `'1'`（代表陸地）和 `'0'`（代表水）組成的 `m x n` 二維網格，請你計算島嶼的數量。島嶼總是由相鄰的陸地單元格組成（只能是上下左右方向），並被水圍繞。

### 📘 English
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

#### 範例 | Examples
```markdown
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

---

## 🧠 解題思路 | Solution Strategy

### ✅ 關鍵想法
- 每當我們遇到一個 `'1'` 時，代表發現一座新的島嶼。
    → Every time we encounter a '1', it indicates the discovery of a new island.
- 我們用 DFS 把所有與之相連的 `'1'` 都變成 `'0'`（代表已拜訪過）。
    → We use DFS to turn all connected '1's into '0' to mark them as visited.
- 重複這個過程直到整個網格遍歷完畢。
    → Repeat this process until the entire grid is traversed.

### ✅ 適用技巧
- DFS（深度優先搜尋）
    → DFS (Depth-First Search): Recursively visit and sink connected lands.
- BFS（廣度優先搜尋）也可以
    → BFS (Breadth-First Search): Use a queue to explore layer by layer.
- Union-Find 並查集進階方法
    → Union-Find (Disjoint Set Union): A more advanced method for dynamic connectivity problems.

---

## 🔁 程式碼：DFS 解法 | DFS Python Code

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # 標記為已拜訪
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count
```

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
```
- 建立一個名為 numIslands 的函式。

- 傳入參數是 grid，是一個 List[List[str]] 型態的 2D 陣列。

- 回傳值是一個整數，表示有幾座島。

```python
if not grid:
    return 0
```
- 若 grid 是空的（edge case），直接回傳 0。

```python
rows, cols = len(grid), len(grid[0])
count = 0
```
- rows, cols 是 grid 的行數與列數。

- count 用來記錄發現的島嶼數量。

### 🌊 定義 DFS 函式
```python
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
```
- 如果當前座標超出邊界或該格是水（'0'），就直接 return（不繼續遞迴）。

| 條件          | 意義  |
| ----------- | --- |
| `r < 0`     | 上越界 |
| `r >= rows` | 下越界 |
| `c < 0`     | 左越界 |
| `c >= cols` | 右越界 |

### ✅ 索引從 0 開始
Python 中，list 的索引從 0 開始：
```python
grid = [
    ["1", "0", "1"],  # 第 0 列
    ["0", "1", "0"]   # 第 1 列
]
```
這個 grid 有 2 列，len(grid) = 2，合法索引只有：
- r = 0
- r = 1

### ❓ 為什麼要用 r >= rows
- rows = 2

- 如果 r = 2，那 grid[2] 就會發生錯誤（IndexError）

- 所以我們必須在 r 還沒超過 rows 時就提前阻止！

```python
grid[r][c] = '0'
```
- 將當前格子從 '1' 改成 '0'，表示這塊陸地已經被處理過，不要重複計算。

```python
dfs(r + 1, c)  # 向下探索
dfs(r - 1, c)  # 向上探索
dfs(r, c + 1)  # 向右探索
dfs(r, c - 1)  # 向左探索
```
- 往四個方向繼續遞迴搜尋，只要是連續的 '1' 都會被標記為 '0'。

1. dfs(r + 1, c) → 向下走
    - 代表目前格子的「下方」相鄰位置。

    - row 加 1，column 不變。

2. dfs(r - 1, c) → 向上走
    - 代表目前格子的「上方」相鄰位置。

    - row 減 1，column 不變。

3. dfs(r, c + 1) → 向右走
    - 代表目前格子的「右方」相鄰位置。

    - row 不變，column 加 1。

4. dfs(r, c - 1) → 向左走
    - 代表目前格子的「左方」相鄰位置。

    - row 不變，column 減 1。

### 🔁 遍歷整個 grid
```python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '1':
            count += 1
            dfs(r, c)
```
- 每當遇到一個尚未拜訪過的 '1'，代表發現了一座新島嶼。

- 呼叫 dfs，將整座島淹掉（標記為 '0'），避免重複計數。

### 🔚 回傳最終答案
```python
return count
```
- 所有島嶼統計完畢，回傳總數。

### 📌 總結這段程式碼的核心邏輯：
1. 遍歷整個 grid。

2. 遇到 '1' 就啟動 DFS，將相連的所有 '1' 標記為 '0'。

3. 每啟動一次 DFS，就代表發現一座新的島嶼，count +1。

4. 遍歷完畢後，回傳 count。

---

## 🧪 Example Walkthrough

### Example 1

- Input：
```python
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```
畫成地圖：
```python
      c0 c1 c2 c3 c4
r0     1  1  0  0  0
r1     1  1  0  0  0
r2     0  0  1  0  0
r3     0  0  0  1  1
```
一開始：
```python
count = 0
```
#### Step 1：開始掃描 Grid

從：
```python
(r, c) = (0, 0)
```
開始。

目前：

grid[0][0] = "1"

代表：

找到一座新的島

因此：

count += 1

現在：

count = 1

接著開始：
```python
dfs(0, 0)
```
#### Step 2：DFS(0,0)

目前位置：

(0,0)

值：

1

先把它改成：
```python
grid[0][0] = "0"
```
Grid 變成：
```python
0 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
接著依序往四個方向走：
```python
dfs(1,0)
dfs(-1,0)
dfs(0,1)
dfs(0,-1)
```
#### Step 3：DFS(1,0)

來到：

(1,0)

值：

1

改成：

0

Grid：
```python
0 1 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
再往四個方向：
```python
dfs(2,0)
dfs(0,0)
dfs(1,1)
dfs(1,-1)
```
#### Step 4：DFS(2,0)

目前：

grid[2][0] = 0

因此：
```python
return
```
不用繼續。

#### Step 5：DFS(0,0)

目前：

grid[0][0] = 0

代表：

已經拜訪過

因此：
```python
return
```
#### Step 6：DFS(1,1)

目前：

grid[1][1] = 1

改成：

0

Grid：
```python
0 1 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
```
再往四個方向：
```python
dfs(2,1)
dfs(0,1)
dfs(1,2)
dfs(1,0)
```
#### Step 7：DFS(0,1)

目前：

grid[0][1] = 1

改成：

0

Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
```
它四個方向全部都是：

0

或：

超出邊界

因此全部 return。

#### Step 8：第一座島完成

DFS 全部結束。

目前 Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
```
可以看到：

第一座島

已經全部變成：

0

因此之後掃描到它們時：
```python
if grid[r][c] == "1":
```
都不會再次計算。

#### Step 9：繼續掃描

一路掃到：

(2,2)

目前：

grid[2][2] = 1

代表：

第二座島

因此：

count += 1

現在：

count = 2

開始：
```python
dfs(2,2)
```
#### Step 10：DFS(2,2)

先改成：

0

Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
```
四個方向都是：

0

因此立刻結束。

#### Step 11：繼續掃描

一路掃到：

(3,3)

目前：

grid[3][3] = 1

代表：

第三座島

因此：

count += 1

現在：

count = 3

開始：
```python
dfs(3,3)
```
#### Step 12：DFS(3,3)

改成：

0

Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 1
```
往右：
```python
dfs(3,4)
```
#### Step 13：DFS(3,4)

目前：
```python
grid[3][4] = 1
```
改成：

0

Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```
四個方向都是：

0

因此結束。

#### Step 14：全部掃描完成

最後 Grid：
```python
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```
所有島都已經被 DFS 改成：

0

因此不會重複計算。

最後：

count = 3

回傳：
```python
3
```
#### 🌊 為什麼只會數到 3 座島？

第一次遇到島：
```python
■■
■■
```
DFS 一次就把整座島全部改成：
```python
□□
□□
```
所以之後掃描時：

都是 0

不會再次：
```python
count += 1
```
因此：

第一座島 → +1

第二座島 → +1

第三座島 → +1

Total = 3


---

## ⏱️ 複雜度分析 | Complexity
- 時間複雜度 Time Complexity：O(m × n)

    - 每個格子最多被訪問一次

- 空間複雜度 Space Complexity：

    - O( m × n)（最壞情況下的遞迴堆疊深度）

---

## 📚 學到的東西 | What I Learned
- 如何使用 DFS 處理二維矩陣中的連通區域問題

- DFS 的應用技巧：遞迴與邊界檢查

- 遍歷後需要標記已訪問節點，避免重複計算

