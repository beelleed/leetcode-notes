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

---

## 🧪 範例 | Example

範例：
```text
grid =
[
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
```
### 初始化掃描（對應程式碼最前面的雙層 for）

- 腐爛橘子座標：(0,0) → 進 queue

- 新鮮橘子數量 fresh_count：

    - row0: (0,1),(0,2) → 2

    - row1: (1,0),(1,1) → +2 = 4

    - row2: (2,1),(2,2) → +2 = 6

- 所以：

    - queue = [(0,0)]

    - fresh_count = 6

    - minutes = 0

### ⏱ Minute 0 → Minute 1（第一層 BFS）
```python
for _ in range(len(queue)):  # len=1
    r, c = queue.popleft()
```
#### 目前 queue 長度 = 1，所以這一輪只處理 (0,0)

- 取出 (0,0)，看四個方向：

    - 上 (-1,0) → (-1,0) 出界 ❌

    - 下 (1,0) → (1,0) = 1 ✅ 腐爛

    - 左 (0,-1) 出界 ❌

    - 右 (0,1) = 1 ✅ 腐爛

- 更新：

    - grid[1][0] = 2，fresh_count 6 → 5，queue append (1,0)

    - grid[0][1] = 2，fresh_count 5 → 4，queue append (0,1)

- 此時（第一層結束）：

    - queue = [(1,0),(0,1)]

    - fresh_count = 4

- 因為 queue 還有東西，程式碼會：
```python
if queue:
    minutes += 1
```

- 所以：

    - minutes = 1

#### grid 變成：
```text
[
  [2,2,1],
  [2,1,0],
  [0,1,1]
]
```
### ⏱ Minute 1 → Minute 2（第二層 BFS）

此時 queue 長度是 2，所以這一分鐘會同時處理 (1,0) 與 (0,1)（這就是「一層 = 一分鐘」）。

#### 先處理 (1,0)

- 四方向：

    - 上 (0,0)=2 ❌

    - 下 (2,0)=0 ❌

    - 左 (1,-1) 出界 ❌

    - 右 (1,1)=1 ✅ 腐爛 → 變 2，fresh_count 4 → 3，append (1,1)

#### 再處理 (0,1)

- 四方向：

    - 上 (-1,1) 出界 ❌

    - 下 (1,1) 現在已經被腐爛成 2 ❌（你的程式碼只吃 ==1）

    - 左 (0,0)=2 ❌

    - 右 (0,2)=1 ✅ 腐爛 → fresh_count 3 → 2，append (0,2)

- 第二層結束：

    - queue = [(1,1),(0,2)]

    - fresh_count = 2

    - queue 不空 → minutes = 2

grid：
```text
[
  [2,2,2],
  [2,2,0],
  [0,1,1]
]
```
### ⏱ Minute 2 → Minute 3（第三層 BFS）

- queue 長度 = 2，處理 (1,1)、(0,2)。

#### 處理 (1,1)

- 四方向：

    - 上 (0,1)=2 ❌

    - 下 (2,1)=1 ✅ 腐爛 → fresh_count 2 → 1，append (2,1)

    - 左 (1,0)=2 ❌

    - 右 (1,2)=0 ❌

#### 處理 (0,2)

- 四方向：

    - 上 (-1,2) 出界 ❌

    - 下 (1,2)=0 ❌

    - 左 (0,1)=2 ❌

    - 右 (0,3) 出界 ❌

- 第三層結束：

    - queue = [(2,1)]

    - fresh_count = 1

    - queue 不空 → minutes = 3

grid：
```text
[
  [2,2,2],
  [2,2,0],
  [0,2,1]
]
```
### ⏱ Minute 3 → Minute 4（第四層 BFS）

queue 長度 = 1，處理 (2,1)。

- 四方向：

    - 上 (1,1)=2 ❌

    - 下 (3,1) 出界 ❌

    - 左 (2,0)=0 ❌

    - 右 (2,2)=1 ✅ 腐爛 → fresh_count 1 → 0，append (2,2)

- 第四層結束：

    - queue = [(2,2)]

    - fresh_count = 0

    - queue 不空 → minutes = 4

grid：
```text
[
  [2,2,2],
  [2,2,0],
  [0,2,2]
]
```
### ⏱ Minute 4（最後一輪：只 pop，不會加分鐘）

#### 處理 (2,2)：

四方向全不是 1，沒有新增腐爛橘子，所以 queue 會變空。

這時你的程式碼：
```python
if queue:
    minutes += 1
```

因為 queue 已經空了，所以 不會再 minutes+1
👉 這就是為什麼最後答案不會多算 1 分鐘。

### ✅ 最終回傳

- 最後：

    - fresh_count == 0 ✅

    - 回傳 minutes = 4
```python
return minutes if fresh_count == 0 else -1
```

答案：4

---

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
| 時間複雜度 | O(M × N) = O(rows * cols)| Each cell is visited at most once |
| 空間複雜度 | O(M × N) = O(rows * cols) | Queue may contain up to all cells |

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
