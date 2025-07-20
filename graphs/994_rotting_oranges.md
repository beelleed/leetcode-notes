# 🍊 LeetCode 994 - Rotting Oranges

- 題目連結：[https://leetcode.com/problems/rotting-oranges](https://leetcode.com/problems/rotting-oranges)
- 題型：BFS、Matrix Traversal
- 難度：Medium

---

## 📘 題目說明 | Problem Description

### ✅ 中文：
給定一個 `m x n` 的網格 `grid`，每個格子可以是以下三種之一：
- `0`：空格
- `1`：新鮮橘子
- `2`：腐爛的橘子

每分鐘內，任何爛橘子都會讓上下左右相鄰的新鮮橘子變爛。請返回讓所有新鮮橘子腐爛所需的最短時間（以分鐘為單位）。若無法讓所有橘子腐爛，請回傳 `-1`。

### ✅ English:
You are given an `m x n` grid where:
- `0` represents an empty cell,
- `1` represents a fresh orange,
- `2` represents a rotten orange.

Every minute, any rotten orange rots its adjacent fresh oranges (up, down, left, right).  
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return `-1`.

### Examples
- Example 1:
![](../images/994_ex1.png)
    - Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    - -Output: 4

- Example 2:

    - Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    - Output: -1
    - Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

- Example 3:

    - Input: grid = [[0,2]]
    - Output: 0
    - Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

---

## 🧠 解題思路 | Solution Strategy

| 中文說明                                                                 | English Explanation                                                        |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 使用 BFS 模擬每一分鐘的感染過程                                          | Use BFS to simulate the rotting process minute by minute                   |
| 先將所有爛橘子的座標加入 queue                                          | Enqueue all the initially rotten oranges                                   |
| 每次從 queue 中處理一層，表示過了一分鐘                                  | Each level of BFS represents one minute passing                            |
| 被感染的新鮮橘子加入下一層 queue，直到沒有可感染的新鮮橘子               | Infect neighboring fresh oranges and enqueue them for the next round       |
| 如果 BFS 結束後仍有新鮮橘子，表示無法完全腐爛                            | If any fresh orange remains, return -1                                     |

---

## 🔧 程式碼 | Python Code (BFS)

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            if queue:
                minutes += 1

        return minutes if fresh_count == 0 else -1
```

```python
from collections import deque
from typing import List
```
- 匯入 deque 用來實作 BFS 的隊列（比 list 更高效）

- 匯入型別提示工具 List

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
```
- 定義主類別 Solution 和方法 orangesRotting

- 傳入參數 grid 是 2D 整數列表，代表橘子狀態（0、1、2）
```python
rows, cols = len(grid), len(grid[0])
```
- 取得 grid 的行與列數，用來做邊界檢查
```python
queue = deque()
fresh_count = 0
```
- queue 是我們用來進行 BFS 的隊列，初始為空

- fresh_count 記錄有多少新鮮橘子
```python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 2:
            queue.append((r, c))
        elif grid[r][c] == 1:
            fresh_count += 1
```
- 遍歷整張 grid：

    - 如果是腐爛橘子（2），記錄到 queue 中，作為 BFS 起點

    - 如果是新鮮橘子（1），計數加一
```python
if fresh_count == 0:
    return 0
```
- 若一開始就沒有新鮮橘子，直接回傳 0 分鐘
```python
minutes = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```
- 初始化分鐘數為 0

- 定義四個方向：上、下、左、右，用來找鄰近橘子
```python
while queue:
    for _ in range(len(queue)):
        r, c = queue.popleft()
```
- 當 queue 還有腐爛橘子時，繼續進行 BFS

- 每次只處理目前這一層的腐爛橘子（代表同一分鐘）
```python
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
        grid[nr][nc] = 2
        fresh_count -= 1
        queue.append((nr, nc))
```
#### for dr, dc in directions:
- directions 是一個列表，裡面有四個二維方向向量：
    - directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    - 分別代表：

        - 上（row - 1）

        - 下（row + 1）

        - 左（col - 1）

        - 右（col + 1）
#### nr, nc = r + dr, c + dc
- nr（new row）和 nc（new col）是相鄰格子的座標

- 把目前腐爛橘子的位置 (r, c) 加上方向 (dr, dc)

- 計算下一步要檢查的位置

#### if 0 <= nr < rows and 0 <= nc < cols

- 邊界檢查（不能走出 grid 的外面）

    - nr 必須在第 0 列與第 rows-1 列之間

    - nc 必須在第 0 行與第 cols-1 行之間

- 避免 IndexError

#### and grid[nr][nc] == 1
- 只處理「新鮮橘子」（值為 1）

- 如果是空格（0）或已腐爛（2），就跳過不處理

#### grid[nr][nc] = 2
- 將這個新鮮橘子設為腐爛

- 表示已感染

#### fresh_count -= 1
- 新鮮橘子數量減 1

- 幫助後面判斷是否已全部腐爛

#### queue.append((nr, nc))
- 將這個剛剛被感染的橘子加入隊列

- 代表它會在「下一分鐘」成為感染者，繼續傳播

#### 🔄 小流程示意
1. 假設我們現在正在處理 (1,1)

2. 往四個方向走，發現 (1,2) 是新鮮橘子

3. 把 (1,2)：

    - 改成腐爛

    - fresh_count -1

    - 加入 BFS 隊列等待下一輪處理

- 走上下左右四個方向

- 如果新位置是新鮮橘子，則：

    - 將其變為腐爛

    - 將新腐爛橘子加入下一層 BFS 隊列

    - 新鮮橘子數減一
```python
if queue:
    minutes += 1
```
- 只有當還有新橘子加入 queue 時，才增加分鐘數
```python
return minutes if fresh_count == 0 else -1
```
- 若全部新鮮橘子已腐爛，回傳分鐘數

- 若還有新鮮橘子，代表無法腐爛完，回傳 -1

### 📌 小結與學習重點
1. BFS 適合模擬時間層層推進的場景（像波浪一樣一層一層擴散）

2. queue 控制 BFS 層級，每一層代表一分鐘

3. 使用 fresh_count 追蹤剩餘新鮮橘子數量

4. 方向陣列是網格題常見技巧，用來走上下左右

### 🧠 流程圖解釋 | Flowchart Explanation
#### ✅ 初始狀態 | Initial State
假設輸入的 grid 為：
```lua
[[2,1,1],
 [1,1,0],
 [0,1,1]]
```
- 2：腐爛的橘子 (Rotten Orange)

- 1：新鮮的橘子 (Fresh Orange)

- 0：空格 (Empty Cell)

#### 🔄 每分鐘的變化 | Minute-by-Minute Changes
每分鐘，所有腐爛的橘子會使其上下左右相鄰的新鮮橘子變爛。

⏱️ 第 1 分鐘 | Minute 1
- 腐爛橘子位於 (0,0)

- 感染相鄰的新鮮橘子：

    - (0,1)

    - (1,0)

更新後的 grid：
```lua 
[[2,2,1],
 [2,1,0],
 [0,1,1]]
```
⏱️ 第 2 分鐘 | Minute 2
- 腐爛橘子位於 (0,1) 和 (1,0)

- 感染相鄰的新鮮橘子：

    - (0,2)

    - (1,1)

更新後的 grid：
```lua
[[2,2,2],
 [2,2,0],
 [0,1,1]]
```
⏱️ 第 3 分鐘 | Minute 3
- 腐爛橘子位於 (0,2) 和 (1,1)

- 感染相鄰的新鮮橘子：

    - (2,1)

更新後的 grid：
```lua
[[2,2,2],
 [2,2,0],
 [0,2,1]]
```
⏱️ 第 4 分鐘 | Minute 4
- 腐爛橘子位於 (2,1)

- 感染相鄰的新鮮橘子：

    - (2,2)

更新後的 grid：
```lua
[[2,2,2],
 [2,2,0],
 [0,2,2]]
```

#### ✅ 結果 | Result
所有新鮮橘子在 4 分鐘內全部腐爛，因此返回 4。

### 🔁 BFS 流程圖 | BFS Flowchart
以下是 BFS 解法的流程圖：
```sql
Start
  |
  v
Initialize queue with positions of all rotten oranges
  |
  v
Count number of fresh oranges
  |
  v
If fresh oranges == 0:
    Return 0
  |
  v
minutes = 0
  |
  v
While queue is not empty:
    |
    v
    For each orange in the current queue:
        |
        v
        For each adjacent cell (up, down, left, right):
            |
            v
            If adjacent cell is a fresh orange:
                |
                v
                Turn it into a rotten orange
                Decrease fresh orange count by 1
                Add position to queue
    |
    v
    If queue is not empty:
        Increase minutes by 1
  |
  v
If fresh oranges == 0:
    Return minutes
Else:
    Return -1
```

---

## ⏱️ 複雜度分析 | Time & Space Complexity
| 分析項目  | 中文說明     | English Explanation               |
| ----- | -------- | --------------------------------- |
| 時間複雜度 | O(M × N) | Each cell is visited at most once |
| 空間複雜度 | O(M × N) | Queue may contain up to all cells |

---

## 📘 我學到的事 | What I Learned
### ✅ 中文：
- 如何使用 BFS 模擬多輪感染過程

- 使用 queue 處理多層資料，並追蹤時間流逝

- 邊界檢查與剩餘數量控制的重要性

### ✅ English:
- How to simulate level-by-level infection with BFS

- Using queue to manage state transitions across minutes

- Importance of boundary checks and final validation
