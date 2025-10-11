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
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
```
- 定義一個 Solution 類別，內部有一個方法 uniquePaths，接收 m（列數）和 n（行數）作為輸入。

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
```
- 初始化一個 2D 陣列 dp，大小為 (m+1) x (n+1)，初始值都為 0。
-  為什麼要多一行一列？→ 因為這裡用的是 1-based index（從 1 開始），這樣在寫 dp[i-1][j] 等公式時就不會超出邊界。

```python
dp[1][1] = 1
```
-  初始化起點 (1,1) 為 1，代表：到起點的路徑只有「站在原地」這一條。

```python
for i in range(1, m + 1):
    for j in range(1, n + 1):
```
-  開始走過整個 dp 陣列的每一格（從 1 開始），表示我們從第 1 行第 1 列開始更新每一格的值。

```python
if i == 1 and j == 1:
    continue
```
- 跳過 (1,1)，因為它已經在前面設定為 1，不用再更新。

```python
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```
-  核心遞推公式：

    - 可以從「上方格子」走下來：dp[i-1][j]

    - 或從「左方格子」走過來：dp[i][j-1] 所以總路徑數為兩者的和。

```python
return dp[m][n]
```
-  最終回傳右下角格子的值，即為從左上角走到右下角的總路徑數。

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