# 🛤️ LeetCode 62 - Unique Paths
🔗 [題目連結](https://leetcode.com/problems/unique-paths/)

---

## 💡 題目描述 | Problem Description

### 中文
給定一個 m x n 的網格，從左上角出發，每次只能向右或向下移動一步，問總共有多少條不同的路徑可以走到右下角。

### English
Given a grid of size m x n, return the number of unique paths from the top-left corner to the bottom-right corner. You can only move either down or right at any point in time.

### Examples
- Example 1:

    ![](../images/62_robot_maze.png)

    - Input: m = 3, n = 7
    - Output: 28

- Example 2:

    - Input: m = 3, n = 2
    - Output: 3
    - Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down
 

---

## ✅ 動態規劃（Dynamic Programming）

### 🔍 思路說明 | Solution Idea

- 使用一個 `dp[i][j]` 表示從 `(1,1)` 到 `(i,j)` 的不同路徑數。

- 狀態轉移公式為：

    dp[i][j] = dp[i-1][j] + dp[i][j-1]


    因為機器人只能從「上方」或「左方」走到當前格子。

### ✅ 初始化條件：
- `dp[1][1] = 1`：從起點出發只有一種方式。
- 注意：這裡用 **1-based index**，所以要初始化 `dp = [[0] * (n+1) for _ in range(m+1)]`。

---

## 🧠 Python 程式碼
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]
```

---

## 🧪 範例 | Example
```python
Input: m = 3, n = 7
Grid:
1 1 1 1 1 1 1
1 2 3 4 5 6 7
1 3 6 10 15 21 28

Output: 28
```

---

## ⏱️ 複雜度分析 | Time & Space Complexity
| 類型       | 複雜度      |
| -------- | -------- |
| 時間複雜度 ⏰  | O(m × n) |
| 空間複雜度 💾 | O(m × n) |

---

## 📘 學到的東西 | What I Learned

- 使用 1-based 索引時，要多留一列與一欄來避免邊界錯誤。

- DP 是求「從一點走到另一點」的經典方法，找出狀態與轉移是關鍵。

- 初始條件與跳過條件設定清楚（如起點）可以讓轉移更簡單。