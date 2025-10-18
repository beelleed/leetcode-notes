# 🌊 LeetCode 417 — Pacific Atlantic Water Flow / 太平洋 & 大西洋水流
🔗 [題目連結](https://leetcode.com/problems/pacific-atlantic-water-flow/)


---

## 📄 題目簡述 | Problem Summary

### 中文  
給一個 m×n 的高度矩陣 `heights`。水可以從格子 (r, c) 流到鄰近格子 (r', c')，條件是鄰近格子的高度 **不低於** 當前格子。  
太平洋相接矩陣的上邊界與左邊界；大西洋相接矩陣的下邊界與右邊界。  
找出所有從哪個格子出發，水可以流同時流到太平洋和大西洋。

### English  
Given an m×n matrix `heights` of non-negative integers representing height, water can flow from a cell (r, c) to its neighbor (r', c') if `heights[r'][c'] >= heights[r][c]`.  
The Pacific touches the top row and left column; the Atlantic touches the bottom row and right column.  
Return all coordinates from which water can flow to **both** the Pacific and Atlantic.

### Examples:
- Example 1:
    
    ![](../images/417_waterflow-grid.jpg)

    - Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    - Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    - Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
        - [0,4]: 
            - [0,4] -> Pacific Ocean 

            - [0,4] -> Atlantic Ocean

        - [1,3]: 
            - [1,3] -> [0,3] -> Pacific Ocean 

            - [1,3] -> [1,4] -> Atlantic Ocean

        - [1,4]: 
            - [1,4] -> [1,3] -> [0,3] -> Pacific Ocean

            - [1,4] -> Atlantic Ocean

        - [2,2]: 
            - [2,2] -> [1,2] -> [0,2] -> Pacific Ocean

            - [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        - [3,0]: 
            - [3,0] -> Pacific Ocean 
                 
            - [3,0] -> [4,0] -> Atlantic Ocean

        - [3,1]: 
            - [3,1] -> [3,0] -> Pacific Ocean

            - [3,1] -> [4,1] -> Atlantic Ocean
        
        - [4,0]: 
            - [4,0] -> Pacific Ocean 
                
            - [4,0] -> Atlantic Ocean
        - Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

- Example 2:

    - Input: heights = [[1]]
    - Output: [[0,0]]
    - Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

---

## 🧠 解法思路 | Solution Idea

這版程式是典型的「從海洋邊界往內 DFS」作法：

- 我們用兩個布林矩陣 `pacific`、`atlantic`，分別標記哪些格子能接水流到太平洋 / 大西洋。  
- 從海洋邊界（上、左邊界對太平洋；下、右邊界對大西洋）出發做 DFS，向內探索高度遞增的方向。  
- 探索過程中，只能走向高度更大或相等的格子（即反向思考：若水能從內流出，反方向從海洋可走回去）。  
- 最後取兩個矩陣都標記為 True 的格子，就是可以同時流到兩個海洋的格子。

---

## 💻 程式碼版本

```python
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int, visited: List[List[bool]], prev_height: int):
            # 若越界、已訪問或高度低於來路高度，無法繼續
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or visited[r][c]
                    or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # 太平洋邊界：上邊（row 0 的所有列）、左邊（col 0 的所有行）
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result
```
```python
if not heights:
    return []
```
- 檢查空輸入
    - 如果 heights 是空的（沒有行或沒有列），直接回傳空列表，因為無法有任何格子可以流水。

```python
rows, cols = len(heights), len(heights[0])
pacific = [[False] * cols for _ in range(rows)]
atlantic = [[False] * cols for _ in range(rows)] 
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
```
- 初始化與變數設置

    - rows, cols 分別是矩陣的行數與列數。

    - pacific / atlantic 是與 heights 同尺寸的布林矩陣，用來標記哪些格子能逆向到達太平洋 / 大西洋。

    - directions 是四個方向向量，用來 DFS 探索上下左右。

```python
def dfs(r, c, visited, prev_height):
    if (r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or heights[r][c] < prev_height):
        return
    visited[r][c] = True
    for dr, dc in directions:
        dfs(r + dr, c + dc, visited, heights[r][c])
```
- DFS 函式

    - 判斷停止條件：

        1. (r, c) 越界

        2. 已被訪問過（visited[r][c] 已為 True）(visited[r][c] 是一個 布林值 (True / False) 的矩陣)

        3. 當前格子的高度比前一格 (prev_height) 小 → 代表這條路「逆向」不合法

    - 若通過檢查，標記當前格子為可達（visited[r][c] = True）

    - 然後對四個方向繼續做 DFS，把 prev_height 更新為 heights[r][c]（下一步比較用）。
```python
for c in range(cols):
    dfs(0, c, pacific, heights[0][c])
    dfs(rows - 1, c, atlantic, heights[rows - 1][c])
for r in range(rows):
    dfs(r, 0, pacific, heights[r][c])
    dfs(r, cols - 1, atlantic, heights[r][cols - 1])
```
- 從邊界發起 DFS

    - 太平洋相關的 DFS 從上邊界（row = 0）與左邊界（col = 0）發起

    - 大西洋相關的 DFS 從下邊界（row = rows–1）與右邊界（col = cols–1）發起

    - 這樣做的目的是：逆向探索哪些格子能從內部「流到」這些邊界的海洋。
```python
result = []
for r in range(rows):
    for c in range(cols):
        if pacific[r][c] and atlantic[r][c]:
            result.append([r, c])
return result
```
- 取交集 & 回傳結果

    - 掃描所有格子 (r, c)

    - 如果該格同時在 pacific 和 atlantic 裡都被標記為 True，代表那個格子可以往兩個海洋流

    - 把這些格子的座標加入結果 result，最後回傳。

---

## 🧪 範例 | Example
```python
heights = [
  [1, 2],
  [4, 3]
]
```
- 大小：2 行 × 2 列（rows = 2, cols = 2）

- 初始：

    - pacific = [[False, False], [False, False]]

    - atlantic = [[False, False], [False, False]]

### Step 1：從太平洋邊界做 DFS

- 太平洋邊界：第一行 (row = 0) 的所有列 + 第一列 (col = 0) 的所有行

    - a) dfs(0, 0, pacific, heights[0][0] = 1)

        - r=0, c=0, prev_height=1

        - 條件檢查：沒越界、未訪問、且 heights[0][0] = 1 >= prev_height = 1 → 合法

        - 標記 pacific[0][0] = True

    - 探四方向：

        - 向下 → dfs(1, 0, pacific, heights[0][0] = 1)

            - heights[1][0] = 4 >= 1 → 合法

            - 標記 pacific[1][0] = True

            - 再從 (1,0) 探方向：

                - 向右 → dfs(1,1, pacific, heights[1][0] = 4)

                    - heights[1][1] = 3 < 4 → 不合法 → 返回

                - 向上 → (0,0) 已訪問 → 返回

                - 向左 或 向下 → 越界或不合法 → 返回

            - 回到 (0,0) 繼續探索其他方向

        - 向上 → (−1,0) 越界 → 返回

        - 向右 → dfs(0,1, pacific, heights[0][0] = 1)

            - heights[0][1] = 2 >= 1 → 合法

            - 標記 pacific[0][1] = True

            - 從 (0,1) 探方向：

                - 向下 → dfs(1,1, pacific, heights[0][1] = 2)

                    - heights[1][1] = 3 >= 2 → 合法

                    - 標記 pacific[1][1] = True

                    - 從 (1,1) 繼續四方向探，但大多會失敗條件檢查

                - 向右 / 向上 / 向左 → 越界或已訪問 / 不合法

        - 向左 → (0,−1) 越界 → 返回

- 之後 dfs(0,1, pacific, heights[0][1])、dfs(1,0, pacific, heights[1][0])、dfs(1,0, pacific, ...)… 等也被呼叫，但大多已標記或不再擴展。

- 最終 pacific 標記可能是：
```python
pacific = [
  [True, True],
  [True, True]
]
```

- 也就是整個矩陣都能從某些格子逆向流到太平洋。

### Step 2：從大西洋邊界做 DFS

- 大西洋邊界：最後一行 (row = 1)、最後一列 (col = 1)

    - b) dfs(1, 1, atlantic, heights[1][1] = 3)

        - r=1, c=1, prev_height=3

        - 檢查合法性：沒越界、未訪問、heights[1][1] = 3 >= prev_height = 3 → 合法

        - 標記 atlantic[1][1] = True

        - 探方向：

            - 向左 → dfs(1,0, atlantic, heights[1][1] = 3)

                - heights[1][0] = 4 >= 3 → 合法

                - 標記 atlantic[1][0] = True

                - 從 (1,0) 繼續方向探，但多數失敗條件

            - 向上 → dfs(0,1, atlantic, heights[1][1] = 3)

                - heights[0][1] = 2 < 3 → 不合法 → 返回

            - 向下 / 向右 → 越界或不合法

    - c) dfs(1, 0, atlantic, heights[1][0] = 4)、dfs(0,1, atlantic, heights[0][1] = 2) 等也會被呼叫：

        - dfs(0,1, atlantic, heights[0][1] = 2)

            - 標記 atlantic[0][1] = True

            - 探方向 (向左 → (0,0): 1 < 2 → 不合法) etc.

- 最終 atlantic 標記可能是：
```python
atlantic = [
  [False, True],
  [True, True]
]
```

### Step 3：交集 & 結果

- 最後掃描每個 (r, c)：

    - (0,0): pacific = True, atlantic = False → 不加入

    - (0,1): True & True → 加入 [0,1]

    - (1,0): True & True → 加入 [1,0]

    - (1,1): True & True → 加入 [1,1]

- 結果：
```python
result = [[0,1], [1,0], [1,1]]
```

---

## ⏱ 複雜度分析

- 時間複雜度：O(m×n)每個格子最多被 dfs 訪問一次（對太平洋 + 大西洋兩次）

- 空間複雜度：O(m×n)使用兩個布林矩陣 + 遞迴棧空間等

---

## ✍ 我學到了什麼 / What I Learned

- 這種「從目標邊界反過來做 DFS」的技巧，在可達性 / 流動問題中非常強大

- 遞迴進入條件要嚴格（高度限制、越界、訪問記錄）

- 最後結果是「兩個 visited 矩陣的交集」

- 與直觀從每格出發相比，這種反向 DFS 方法更有效率