# 🧩 LeetCode 133 - Clone Graph

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/clone-graph) 

---

## 📘 題目說明 | Problem Description
### 中文說明：
給你一個連通的無向圖的節點引用 node，請你回傳該圖的深度拷貝（clone）。圖中的每個節點都包含一個值 val 和一個鄰居列表 neighbors。

### English:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains a value (val) and a list of neighbors (neighbors).

### Examples
- Example 1:
![](../images/133_clone_graph_question.png)
    - Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    - Output: [[2,4],[1,3],[2,4],[1,3]]
    - Explanation: There are 4 nodes in the graph.
        - 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        - 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        - 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        - 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

- Example 2:
    - Input: adjList = [[]]
    - Output: [[]]
    - Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

- Example 3:
    - Input: adjList = []
    - Output: []
    - Explanation: This an empty graph, it does not have any nodes.

---

## 🧠 解題思路 | Solution Strategy
### ✅ 中文思路：
- 圖可能包含環，因此不能用單純遞迴，否則會無限循環。

- 使用 DFS 遍歷整張圖，並用 visited 字典記錄每個已經克隆過的節點。

- 當遇到一個新節點時，就創建一個新的副本，並遞迴處理其所有鄰居。

- 如果節點已經克隆過，就直接回傳已克隆的節點，避免重複。

### ✅ English Idea:
- Since the graph may contain cycles, we must track visited nodes to avoid infinite recursion.

- Use DFS to traverse the graph, and store cloned nodes in a dictionary visited.

- For each unvisited node, create a new copy, then recursively copy all its neighbors.

- If a node has already been cloned, return the clone directly.

---

## 🧩 題目提供的節點定義 | Node Definition
```python
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

---

## 🧪  解法程式碼 | Python Code
### DFS
```python
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]

            clone = Node(current_node.val)
            visited[current_node] = clone

            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
```

#### 🔍 程式碼解析 | Code Explanation
-  if not node: return None
    - 如果圖是空的（沒有節點），直接回傳 None。

-  visited = {}
    - 建立一個字典來記錄已經被「複製（clone）」過的節點。

    - key 是原圖的節點（Node 實體），value 是對應的「新圖」中節點（克隆後的 Node 實體）。

-  def dfs(current_node): ...
    - 這是我們用來遞迴複製整個圖的函式。

-  if current_node in visited: return visited[current_node]
    - 意義：這個節點之前已經被複製過了，所以我們直接回傳那個複製品。

    - 作用：防止無限遞迴，也確保圖中所有邊的連線不會重複建立節點。

-  clone = Node(current_node.val)
    - 建立當前節點的新副本，使用它的 val。

    - 這時候 neighbors 是空的，稍後會一一補上。

-  visited[current_node] = clone
    - 把這個新節點加到 visited 字典中，方便其他地方引用。

-  for neighbor in current_node.neighbors:
    - 遍歷原圖中 current_node 的所有鄰居。

    - 對每個鄰居執行 DFS 遞迴，並將回傳的新節點加入 clone.neighbors。

-  clone.neighbors.append(dfs(neighbor))
    - 遞迴呼叫 dfs(neighbor) 來複製鄰居節點，並將其加入目前這個節點的鄰接關係中。

    - 這是建立圖的核心步驟：確保連線關係保持一致。

-  return clone
    - 回傳新建好的節點，這個會被上層節點加進去作為 neighbors。

-  return dfs(node)
    - 呼叫遞迴的起點。

    - 我們從原圖的 node 開始進行深度優先複製。

#### ✅ 補充說明

- 這段程式碼的核心技巧在於「避免重複建立節點」與「遞迴建立鄰接關係」，它的設計非常精簡：

    - 每個節點只會建立一次。

    - 每條邊只會訪問兩次（雙向）。

    - 利用字典避免 cycle。

    - 適合處理圖的深拷貝問題。

#### 🖼 圖解 | Visualization
假設圖如下：
```lua
1 -- 2
|    |
4 -- 3
```
鄰接表表示：
```python
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}
```
每個節點都會被 DFS 克隆一次，並建立對應的鄰居連結。

### 📍 DFS 遞迴流程圖
```text
Start cloneGraph(node=1)
↓
Check if node is None → No
Initialize visited = {}

Call dfs(1)
↓
1 not in visited → create clone Node(1)
visited = {1: clone_1}

Iterate neighbors of 1 → [2, 4]

  ┌── Call dfs(2)
  │   ↓
  │   2 not in visited → create clone Node(2)
  │   visited = {1: clone_1, 2: clone_2}
  │
  │   Iterate neighbors of 2 → [1, 3]
  │
  │     ┌── dfs(1) already in visited → return clone_1
  │     └── Call dfs(3)
  │          ↓
  │          3 not in visited → create clone Node(3)
  │          visited = {1, 2, 3}
  │
  │          Iterate neighbors of 3 → [2, 4]
  │
  │            ┌── dfs(2) already in visited → return clone_2
  │            └── Call dfs(4)
  │                 ↓
  │                 4 not in visited → create clone Node(4)
  │                 visited = {1, 2, 3, 4}
  │
  │                 Iterate neighbors of 4 → [1, 3]
  │                   ┌── dfs(1) → clone_1
  │                   └── dfs(3) → clone_3
  │                 clone_4.neighbors = [clone_1, clone_3]
  │
  │          clone_3.neighbors = [clone_2, clone_4]
  │
  │   clone_2.neighbors = [clone_1, clone_3]

clone_1.neighbors = [clone_2, clone_4]

return clone_1
```
#### 🔄 簡要流程說明
1. 用 DFS 遍歷整張圖。

2. 每訪問一個節點：

    - 建立它的 clone

    - 記錄在 visited 字典裡

3. 如果一個節點已經訪問過，就直接從 visited 拿 clone，不重複建立。

4. 每個 clone node 的鄰居也是 clone 過的鄰居。

---

### BFS
```python
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])

        return visited[node]
```
#### 🔍 BFS 解法說明
✅ 初始化
- queue 是一個佇列，用來廣度搜尋整張圖。

- visited 字典記錄每個節點對應的 clone 節點。

✅ while loop
- 每次從 queue 拿出當前節點 current。

- 遍歷其所有 neighbor：

    - 若 neighbor 還沒被複製，就複製它並加進 queue。

    - 把對應的 clone 加進 current 的 clone 的 neighbors。

✅ 結果回傳
- 回傳最初傳入節點的 clone：visited[node]

✅ 適用情境
- 避免遞迴爆棧：當圖的節點很多很廣，DFS 可能會爆遞迴堆疊，BFS 是穩定選擇。

- 執行效率好：對寬度大的圖，BFS 擴展更快。

---

## ✅ 差異比較：DFS vs BFS
| 特性     | DFS              | BFS               |
| ------ | ---------------- | ----------------- |
| 遍歷順序   | 一條路走到底，遇到再回溯     | 一層一層擴展所有節點        |
| 使用結構   | 遞迴（或使用 stack 模擬） | queue（佇列）         |
| 適用情境   | 遞迴直覺寫法，適合小圖      | 迴圈處理、可避免遞迴堆疊溢出    |
| 空間使用   | 最多堆疊深度為 O(N)     | 最多 queue 可能為 O(N) |
| 實際效率差異 | 取決於圖的形狀，無絕對優劣    | 對「廣而淺」的圖可能略快      |

---

## 📈 時間與空間複雜度 | Time & Space Complexity
- ⏱ Time Complexity: O(N + E)，其中 N 為節點數，E 為邊數。

- 💾 Space Complexity: O(N)，需要存 visited 字典與 DFS 遞迴棧。

---

## 📚 學到什麼 | What I Learned
- 如何複製一張圖（有環的結構）需要用 visited 防止重複。

- 用 DFS/BFS 搭配資料結構（dict）來處理複雜資料關係。

- 在面對參照型資料結構時，「深拷貝」是一項重要技能。