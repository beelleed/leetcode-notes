# LeetCode 785 - Is Graph Bipartite? | 判斷圖是否為二分圖

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/is-graph-bipartite/)

---

## 📘 題目說明 | Problem Description

**中文：**
給定一個無向圖 `graph`，其中 `graph[i]` 是與節點 `i` 相鄰的所有節點的列表。請判斷該圖是否為「二分圖」。

若能將節點分成兩組，且每條邊都只連接兩組中不同組的節點，則為二分圖。

**English:**
Given an undirected graph `graph`, where `graph[i]` is a list of all the nodes adjacent to node `i`, return `true` if and only if the graph is bipartite.

### Examples

- Example 1:
![](../images/785_ex1.jpg)
    - Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    - Output: false
    - Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

- Example 2:
![](../images/785_ex2.jpg)
    - Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    - Output: true
    - Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

---

## 🧠 解題思路 | Solution Strategy

### 中文
- 嘗試把節點染成兩種顏色（用 1 和 -1 表示），讓所有相鄰的節點顏色不同。
- 若能成功染色全圖，代表是二分圖。
- 若在染色過程中遇到相鄰節點顏色相同，則不是二分圖。

**核心技巧：DFS + 染色法**

### English
- Try to color the graph using two colors (e.g., 1 and -1), such that no two adjacent nodes have the same color.

- If the entire graph can be colored without conflicts, then it is bipartite.

- If any adjacent nodes have the same color, the graph is not bipartite.

**Key Idea: Use DFS with coloring technique**

---

## ✅ 程式碼 | Code (DFS Approach)

```python
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # 圖的節點數量
        colors = [0] * n  # 初始化顏色列表，0 表示未染色

        def dfs(node: int, color: int) -> bool:
            colors[node] = color  # 將當前節點染色
            for neighbor in graph[node]:  # 遍歷所有相鄰節點
                if colors[neighbor] == 0:  # 若尚未染色
                    if not dfs(neighbor, -color):  # 嘗試染成相反顏色，若失敗則回傳 False
                        return False
                elif colors[neighbor] == color:  # 若相鄰節點顏色相同，違反二分圖定義
                    return False
            return True  # 該節點與其所有相鄰節點合法

        for i in range(n):  # 遍歷所有節點（防止圖不連通）
            if colors[i] == 0:  # 若此節點尚未被染色
                if not dfs(i, 1):  # 從該節點開始染色（預設為 1）
                    return False
        return True  # 若整張圖都染色成功，則為二分圖

```

### 🎨 圖解流程：DFS 染色法判斷二分圖
我們以以下圖為例：
```markdown
0 —— 1
|    |
3 —— 2
```
對應的鄰接表表示為：

#### 🧮 對應的鄰接表
節點 0：
- 和 1、3 相連 → graph[0] = [1, 3]

節點 1：
- 和 0、2 相連 → graph[1] = [0, 2]

節點 2：
- 和 1、3 相連 → graph[2] = [1, 3]

節點 3：
- 和 0、2 相連 → graph[3] = [0, 2]

✅ 所以最後的鄰接表為：
```python
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
```
我們嘗試使用兩種顏色（例如：紅色和藍色）來對節點進行染色，使得相鄰的節點不會有相同的顏色。

#### 🧭 步驟 1：初始化
- 建立一個 colors 陣列，初始值為 0，表示所有節點尚未染色。
```python
colors = [0, 0, 0, 0]
```
#### 🧭 步驟 2：從節點 0 開始 DFS
- 將節點 0 染成紅色（用 1 表示）：
```python
colors[0] = 1
```
- 節點 0 的相鄰節點為 1 和 3。

#### 🧭 步驟 3：處理節點 1
- 節點 1 尚未染色，將其染成藍色（用 -1 表示）：
```python
colors[1] = -1
```
- 節點 1 的相鄰節點為 0 和 2。

- 節點 0 已染色為紅色，與節點 1 的藍色不同，符合條件。

- 節點 2 尚未染色，將其染成紅色（1）：
```python
colors[2] = 1
```
#### 🧭 步驟 4：處理節點 2
- 節點 2 的相鄰節點為 1 和 3。

- 節點 1 已染色為藍色，與節點 2 的紅色不同，符合條件。

- 節點 3 尚未染色，將其染成藍色（-1）：
```python
colors[3] = -1
```
#### 🧭 步驟 5：處理節點 3
- 節點 3 的相鄰節點為 0 和 2。

- 節點 0 已染色為紅色，與節點 3 的藍色不同，符合條件。

- 節點 2 已染色為紅色，與節點 3 的藍色不同，符合條件。

#### ✅ 結論
- 所有節點都已成功染色，且相鄰節點的顏色不同，因此該圖為二分圖。

---

## ⏱️ 複雜度分析 | Time & Space Complexity
- 時間複雜度 (Time Complexity): O(V + E)
    - V 是節點數（vertices），E 是邊數（edges）

    - 我們會對圖中每個節點最多遍歷一次（O(V)）

    - 每個節點的相鄰節點也會被訪問一次（累積 O(E)）

    - 所以總時間複雜度是 O(V + E)

- 空間複雜度 (Space Complexity): O(V)，因為用 colors 陣列儲存顏色狀態

---

## 📚 學到的東西 | What I Learned
- 二分圖的定義與應用

- 如何用 DFS/BFS 配合染色法判斷圖是否二分

- 在處理圖時，要記得考慮不連通的情況（需對每個節點進行遍歷）

---

## 🔍 延伸練習
- LeetCode 886. Possible Bipartition

- LeetCode 886 與 785 題概念幾乎相同，可作為練習加深理解