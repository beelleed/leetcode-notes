# 📍 LeetCode 1091 — Shortest Path in Binary Matrix

🔗 [題目連結](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給一個 n x n 的矩陣 grid

- 0 表示可走、1 表示障礙

- 從左上角 (0,0) 出發，要走到右下角 (n-1, n-1)

- 可以走 8 個方向（上下左右 + 四個對角）

- 回傳最短路徑長度（包含起點與終點，所以起點本身算 1）

- 如果走不到，回傳 -1

### English

Return the length of the shortest clear path from top-left to bottom-right in a binary matrix, moving in 8 directions. Return -1 if not possible.

### Examples
- Example 1:

    ![](../images/1091_example1_1.png)
    
    - Input: grid = [[0,1],[1,0]]
    - Output: 2
- Example 2:

    ![](../images/1091_example2_1.png)

    - Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    - Output: 4
- Example 3:

    - Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    - Output: -1

---

## 🧠 看到這題為什麼想到 BFS？

1. 題目要 shortest path / 最短路徑

2. 每走一步成本都一樣（走一格就是 +1）

3. 從一個格子擴展到鄰居格子（狀態擴展）

4. BFS 的特性：第一次到終點一定是最短

---

## 🧠 解題思路 | Solution Idea 
```text
(row, col, dist)
```

- (row, col)：目前站在哪一格

- dist：從起點走到這格的路徑長度（包含起點）

### visited :

- 把走過的格子從 0 改成 1

- 代表「這格已經訪問過，不要再進 queue」

這樣不用額外 visited 陣列。

---

## 💻 程式碼實作 | Code
```python
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 起點或終點被擋住，直接不可能
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 個方向
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque()
        queue.append((0, 0, 1))  # (row, col, path_length)

        # 標記已訪問（直接改 grid）
        grid[0][0] = 1

        while queue:
            r, c, dist = queue.popleft()

            # 到達終點
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1
```
### 1️⃣ n = len(grid)
```python
n = len(grid)
```

- 矩陣是 n x n

- 目標位置是 (n-1, n-1)

### 2️⃣ 起點 / 終點不可走直接結束
```python
if grid[0][0] == 1 or grid[n-1][n-1] == 1:
    return -1
```

- 如果起點是 1：根本出不去

- 如果終點是 1：根本到不了

- 直接回 -1（剪枝）

### 3️⃣ directions：8 個方向
```python
directions = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]
```

- 用方向陣列避免寫 8 次 if

- 每次從 (r,c) 加上 (dr,dc) 就得到下一格

### 4️⃣ queue 初始化：把起點丟進去
```python
queue = deque()
queue.append((0, 0, 1))
```

- queue 裡放 (row, col, dist)

- dist = 1 是因為：

    - 路徑長度「包含起點」

    - 起點自己就算 1 格

### 5️⃣ 標記起點已訪問
```python
grid[0][0] = 1
```

- 把起點改成 1

- 表示「這格走過了」

- 避免之後從別的格子又走回來，造成重複進 queue

### 6️⃣ BFS 主迴圈
```python
while queue:
    r, c, dist = queue.popleft()
```

- popleft()：拿出目前距離最短的狀態（BFS 保證）

- dist 是到 (r,c) 的最短距離

### 7️⃣ 到終點就直接回 dist
```python
if r == n - 1 and c == n - 1:
    return dist
```

- BFS 的特性：第一個到終點的距離一定最短

- 所以可以直接 return

### 8️⃣ 擴展 8 方向鄰居
```python
for dr, dc in directions:
    nr, nc = r + dr, c + dc
```

- 逐方向產生鄰居 (nr,nc)

### 9️⃣ 邊界檢查 + 是否可走
```python
if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
```

- 這行一次做三件事：

    1. 0 <= nr < n：row 沒出界

    2. 0 <= nc < n：col 沒出界

    3. grid[nr][nc] == 0：是可走且未訪問的格子

### 🔟 標記訪問 + 加入 queue（dist + 1）
```python
grid[nr][nc] = 1
queue.append((nr, nc, dist + 1))
```

- 先標記訪問（避免重複加入 queue）

- 加入 queue 時距離 +1（多走一步）

### 1️⃣1️⃣ queue 空了還沒到終點
```python
return -1
```

- BFS 把所有可走的格子都探索完了

- 還沒碰到終點 → 無解

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
grid = [
  [0, 1, 0],
  [0, 0, 0],
  [1, 0, 0]
]
n = 3
終點是 (2,2)
```
### Step 0：初始化

- 檢查起點、終點都不是 1 ✅

- directions 設定好

- 初始化 queue：
```text
queue = [(0,0,1)]
grid[0][0] = 1  # 標記走過
```

此時 grid 變成：
```text
[
  [1, 1, 0],
  [0, 0, 0],
  [1, 0, 0]
]
```
### Step 1：while 第一次迴圈
```python
r, c, dist = queue.popleft()
# r=0, c=0, dist=1
```

- 還不是終點

- 開始跑 8 個方向，找鄰居

- 從 (0,0) 出發的合法鄰居（且 grid==0）

    - (1,0) ✅

    - (1,1) ✅
    
    - (0,1) 是 1 不行，其他出界

所以程式會做：
```python
grid[1][0] = 1
queue.append((1,0,2))

grid[1][1] = 1
queue.append((1,1,2))
```

此時：
```text
queue = [(1,0,2), (1,1,2)]
grid =
[
  [1, 1, 0],
  [1, 1, 0],
  [1, 0, 0]
]
```
### Step 2：while 第二次迴圈

pop 出第一個：
```python
r, c, dist = (1,0,2)
```

- 從 (1,0) 探索鄰居，合法且未訪問的 0：

    - (2,1) ✅（對角）

    - (1,1) 已經是 1（走過）❌

    - (0,2) 太遠，不是鄰居

    - (1, -1) 出界 ❌

所以加入：
```text
queue append (2,1,3)
```

更新：
```text
queue = [(1,1,2), (2,1,3)]
grid[2][1] = 1
```

grid：
```text
[
  [1, 1, 0],
  [1, 1, 0],
  [1, 1, 0]
]
```
### Step 3：while 第三次迴圈

pop：
```python
r, c, dist = (1,1,2)
```

- 合法鄰居且 grid==0：

    - (0,2) ✅

    - (1,2) ✅

    - (2,2) ✅（終點也會先被加入 queue，不是立刻 return，因為 return 在 pop 時才判斷）

加入：
```text
queue = [(2,1,3), (0,2,3), (1,2,3), (2,2,3)]
```

並把它們標記為 1。

### Step 4：到達終點（關鍵）

等到 (2,2,3) 被 pop 出來時：
```python
r, c, dist = (2,2,3)
if r == n-1 and c == n-1:
    return dist
```

✅ 回傳 3

### ✅ 最終輸出
```text
3
```

（包含起點與終點，所以最短路徑長度是 3）

---

## ⏱ 複雜度分析 | Complexity Analysis 

### 時間複雜度 | Time Complexity

- O(n²)

- 每個格子最多被放入 queue 一次（因為一旦訪問就改成 1）

- 每次 pop 會檢查最多 8 個方向 → 常數

### 空間複雜度 | Space Complexity

- O(n²)

- 最壞情況 queue 可能同時放很多格子

- 另外你是「直接改 grid」當 visited，所以沒有額外 visited matrix

---

## ✍️ 我學到的東西 | What I Learned

- 看到 shortest path + 每步成本相同 + grid 擴展 → BFS

- queue 裡存 (r, c, dist)，pop 出來就是「目前最短距離」

- visited 一定要做：不然會一直重複進 queue

---

## 🧠 一句話總結

I use BFS starting from (0,0), exploring 8-direction neighbors level by level; the first time we pop the destination cell, its distance is guaranteed to be the shortest path length.

---

## Code
```python
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # 起點不能走
        if grid[0][0] != 0:
            return -1

        queue = deque([(0, 0)])
        grid[0][0] = 1  # visited
        steps = 1

        directions = [
            (0,1),(0,-1),(1,0),(-1,0),
            (1,1),(1,-1),(-1,1),(-1,-1)
        ]

        while queue:
            for _ in range(len(queue)):  # 🔥 layer
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return steps

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            steps += 1  # 🔥 一層結束

        return -1
```

---

## Example
```text
grid =
0 0 0
1 1 0
1 1 0
```

### 🧠 初始化
```python
queue = deque([(0, 0)])
steps = 1
```
👉 現在 queue：[(0,0)]

### 🔥 Layer 1（steps = 1）

👉 進 while 前：queue = [(0,0)]

👉 這一層的大小：
```python
len(queue) = 1
```
👉 開始這一層

處理 (0,0)：

可以走到：
```text
(0,1) ✅
(1,0) ❌
(1,1) ❌
```
👉 queue 變成：[(0,1)]

👉 這一層結束：
```python
queue = [(0,1)]
steps = 2
```
### 🟡 Layer 2（steps = 2）

👉 進 while：queue = [(0,1)]

👉 這一層大小：
```python
len(queue) = 1
```
👉 處理 (0,1)

可以走到：
```text
(0,2) ✅
(1,2) ✅
```
👉 queue 變成：
```text
[(0,2), (1,2)]
```
👉 這一層結束：
```python
queue = [(0,2), (1,2)]
steps = 3
```
### 🔵 Layer 3（steps = 3）

👉 進 while：queue = [(0,2), (1,2)]

👉 這一層大小：
```python
len(queue) = 2   # 🔥 這層有兩個點！
```
👉 處理 (0,2)

可能走到：
```text
(1,2)（但已訪問）
```
👉 處理 (1,2)

可以走到：
```text
(2,2) ✅（終點）
```
👉 queue 變成：
```text
[(2,2)]
```
👉 這一層結束：
```python
queue = [(2,2)]
steps = 4
```
### 🟣 Layer 4（steps = 4）

👉 queue：[(2,2)]

👉 這就是終點 → return

### 🎯 超關鍵總結
```python
Layer 1: [(0,0)]
Layer 2: [(0,1)]
Layer 3: [(0,2), (1,2)]
Layer 4: [(2,2)]
```