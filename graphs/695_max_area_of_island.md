# 🌊 LeetCode 695 - Max Area of Island 最大島嶼面積

- 題目連結：[https://leetcode.com/problems/max-area-of-island](https://leetcode.com/problems/max-area-of-island)
- 題型：DFS（深度優先搜尋）
- 難度：Medium

---

## 📘 題目說明 | Problem Description

### ✅ 中文：

給定一個由 `0`（水）和 `1`（陸地）組成的 2D 網格，找出最大的「島嶼面積」。島嶼是由相鄰的 `1` 組成（僅限上下左右方向），並且不能對角連接。你可以假設網格邊緣都被水包圍。

### ✅ English:

Given a 2D grid of `0`s (water) and `1`s (land), return the area of the largest island. An island is a group of `1`s connected **4-directionally** (horizontal and vertical). You may assume all four edges of the grid are surrounded by water.

### Examples
```markdown
Example 1:
![](../images/695_maxarea1-grid.jpg)
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

---

## 🧠 解題思路 | Solution Strategy

### ✅ 中文

- 遍歷整個網格（grid）。
- 每當遇到一個尚未訪問的陸地（值為 1）時，啟動 DFS。
- 使用 DFS 將這塊連續的島嶼整個沉沒（改成 0），並統計其面積。
- 最後回傳最大的面積。

### ✅ English

- Traverse the entire grid.
- Whenever an unvisited land cell (`1`) is found, start DFS.
- Use DFS to sink the entire connected island (set to `0`) and calculate its area.
- Return the maximum area found.

---

## 🔧 程式碼 | Code

```python
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # 越界或遇到水時停止
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # 標記為已訪問（沉島）
            # 計算當前區域面積 = 1（自己）+ 四個方向延伸的面積
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
```

---

## ⏱️ 複雜度分析 | Complexity Analysis
| 類型    | 中文說明                          | English Description                     |
| ----- | ----------------------------- | --------------------------------------- |
| 時間複雜度 | O(M × N)，M 為列數，N 為欄數，最多遍歷所有格子 | O(M × N), each cell is visited once     |
| 空間複雜度 | O(M × N)（最壞情況下遞迴深度為整張網格）      | O(M × N) in worst case due to recursion |

💡 在 Python 中遞迴深度有限，如遇大型網格可考慮用 BFS 替代。

---

## 📌 學到的觀念 | What I Learned
| 主題     | 說明（中文）                          | 說明（English）                                       |
| ------ | ------------------------------- | ------------------------------------------------- |
| DFS 遞迴 | 對每個陸地做遞迴探索，處理所有相連格子             | Recursively explore all adjacent land cells       |
| 邊界判斷   | `r < 0`、`r >= rows` 是必要的防越界     | Boundary checks are needed to avoid index errors  |
| 網格變動標記 | 用 `grid[r][c] = 0` 標記已訪問，避免重複計算 | Use `grid[r][c] = 0` to mark cells as visited     |
| 回傳面積總和 | DFS 回傳每座島的面積，累加後比較最大值           | DFS returns island area, we keep track of the max |

---

## 📘 額外練習建議
LeetCode 200 - Number of Islands（統計數量）

LeetCode 733 - Flood Fill（染色演算法）

LeetCode 130 - Surrounded Regions（邊界擴展）