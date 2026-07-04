# 📍 LeetCode 323 — Number of Connected Components in an Undirected Graph

🔗 https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

---

## 📄 題目說明 | Problem Description

### 中文

* 給定：

  * `n` 個節點（Node），編號為 `0 ~ n-1`
  * 一個 `edges` 陣列，表示 Graph 中所有的邊（Edge）。

* 每一條 Edge：

```text
[a, b]
```

代表：

```text
a 和 b 可以互相到達
```

因為：

```text
Undirected Graph
```

所以：

```text
a → b

b → a
```

都可以走。

---

你的任務是：

* 找出這張 Graph 一共有幾個：

```text
Connected Component
```

也就是：

```text
互相可以到達的一群 Node
```

最後回傳：

```text
Connected Component 的數量
```

### English

* You are given `n` nodes labeled from `0` to `n - 1`.
* Each edge connects two nodes in an undirected graph.
* Return the number of connected components in the graph.

### Examples

#### Example 1

Input

```python
n = 5

edges = [
    [0,1],
    [1,2],
    [3,4]
]
```

畫成 Graph：

```text
0 —— 1 —— 2

3 —— 4
```

Output

```text
2
```

因為：

```text
Component 1

0 1 2

Component 2

3 4
```

共有：

```text
2 個 Connected Components
```

#### Example 2

Input

```python
n = 5

edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,4]
]
```

畫成 Graph：

```text
0 —— 1 —— 2 —— 3 —— 4
```

Output

```text
1
```

因為：

```text
全部節點都互相連通
```

只有：

```text
1 個 Connected Component
```

---

## 🧠 核心觀念 | Key Insight

題目不是要找：

```text
最短路徑
```

也不是：

```text
Cycle
```

而是要找：

```text
Graph 被分成幾塊
```

例如：

```text
0 —— 1 —— 2

3 —— 4

5
```

可以分成：

```text
第一塊：

0 1 2

第二塊：

3 4

第三塊：

5
```

答案就是：

```text
3
```

### DFS 要做什麼？

DFS 的工作非常簡單：

```text
把同一塊 Component 全部走完
```

例如：

```text
0 —— 1 —— 2
```

如果：

```python
dfs(0)
```

那 DFS 會走到：

```text
0

↓

1

↓

2
```

最後：

```text
整個 Component 都會被拜訪
```
### 為什麼 count 要加 1？

當我們掃描所有 Node：

```python
for node in range(n):
```

如果：

```python
node not in visited
```

代表：

```text
發現一個新的 Component
```

因此：

```python
count += 1
```

然後：

```python
dfs(node)
```

把這整塊全部走完。

例如：

```text
0 —— 1 —— 2

3 —— 4
```

開始：

```text
visited = {}
count = 0
```

掃到：

```text
0
```

沒有拜訪過。

代表：

```text
第一塊 Component
```

所以：

```text
count = 1
```

DFS 完後：

```text
visited

↓

{0,1,2}
```

繼續掃。

掃到：

```text
3
```

沒拜訪過。

代表：

```text
第二塊 Component
```

所以：

```text
count = 2
```

DFS 完：

```text
visited

↓

{0,1,2,3,4}
```

全部掃描完成。

答案：

```text
2
```

---

### 解題流程

### Step 1

建立 Graph。

例如：

```text
0-1
1-2
3-4
```

建立：

```text
0 : [1]

1 : [0,2]

2 : [1]

3 : [4]

4 : [3]
```

---

### Step 2

建立：

```python
visited = set()
```

用來紀錄：

```text
哪些 Node 已經拜訪過
```

---

### Step 3

開始掃描：

```python
for node in range(n):
```

---

### Step 4

如果：

```python
node not in visited
```

代表：

```text
找到新的 Connected Component
```

因此：

```python
count += 1
```

然後：

```python
dfs(node)
```

把整塊全部走完。

### Step 5

所有 Node 都掃描完成。

回傳：

```python
count
```

---

## 💻 Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        count = 0

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count
```

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
graph = defaultdict(list)
```

* 建立 adjacency list。
* 用來記錄每個 node 連到哪些鄰居。
* `defaultdict(list)` 可以讓我們不用先手動建立空 list。


```python
for a, b in edges:
```

* 一條一條處理 edges。
* 每個 edge `[a, b]` 代表 `a` 和 `b` 互相連通。


```python
graph[a].append(b)
graph[b].append(a)
```

* 因為這題是 Undirected Graph。
* 所以 `a` 可以到 `b`。
* `b` 也可以到 `a`。
* 因此兩邊都要加入。

例如：

```text
edges = [[0,1], [1,2]]

graph:
0 : [1]
1 : [0,2]
2 : [1]
```

```python
visited = set()
```

* 建立 `visited`。
* 用來記錄哪些 node 已經被拜訪過。
* 避免 DFS 重複走同一個 node。


```python
def dfs(node):
```

* 建立 DFS function。
* 這題的 DFS 目的很單純：

```text
把同一個 connected component 裡的所有 node 都走完
```

* 所以它不需要回傳 `True` 或 `False`。

```python
if node in visited:
    return
```

* 如果這個 node 已經拜訪過。
* 代表之前已經從同一個 component 的某個 node 走到它了。
* 所以直接 return。
* 這可以避免無限遞迴。

例如：

```text
0 —— 1
```

* 從 `0` 走到 `1`。
* `1` 又會看到 `0`。
* 但 `0` 已經在 visited 裡，所以直接 return。

---

```python
visited.add(node)
```

* 把目前 node 標記成已拜訪。
* 代表它已經屬於目前正在 DFS 的 component。

---

```python
for nei in graph[node]:
```

* 走訪目前 node 的所有鄰居。
* `nei` 是 neighbor 的縮寫。

---

```python
dfs(nei)
```

* 對每個鄰居繼續 DFS。
* 目標是把同一個 component 裡所有能到達的 node 都加入 `visited`。

---

```python
count = 0
```

* `count` 用來記錄 connected components 的數量。
* 一開始還沒發現任何 component，所以是 `0`。

---

```python
for node in range(n):
```

* 掃描所有 node。
* 因為有些 node 可能完全沒有邊。
* 例如：

```text
n = 3
edges = [[0,1]]

node 2 是獨立 component
```

* 所以不能只掃 edges，一定要掃 `0 ~ n-1`。

```python
if node not in visited:
```

* 如果這個 node 還沒被拜訪過。
* 代表它不屬於之前任何一個 component。
* 所以它是：

```text
一個新的 connected component 的起點
```

```python
count += 1
```

* 發現一個新的 component。
* 所以答案加一。

```python
dfs(node)
```

* 從這個 node 開始 DFS。
* 把這整個 component 裡的所有 node 都標記成 visited。
* 這樣之後掃到同一個 component 裡的其他 node 時，就不會再加 count。

```python
return count
```

* 回傳 connected components 的總數。

---

## 🧠 為什麼這題不用 parent？

* 在 LeetCode 261 Graph Valid Tree 裡，我們要判斷：

```text
有沒有 cycle
```

* 所以 DFS 遇到 visited node 時，可能代表 cycle。
* 因此要用 `parent` 區分：

```text
是走回上一個 node
還是真的遇到 cycle
```

* 但 LeetCode 323 不是要判斷 cycle。
* 它只需要知道：

```text
哪些 node 已經被同一個 component 拜訪過
```

* 所以遇到 visited node 時，直接 return 就好。
* 不需要判斷它是不是 parent。

---

## 🧠 為什麼這題 dfs 不用 return True / False？

* LeetCode 261 的 DFS 要回答：

```text
從這個 node 出發有沒有 cycle？
```

* 所以需要回傳 `True` 或 `False`。


* LeetCode 323 的 DFS 只要做一件事：

```text
把同一塊 component 全部走完
```

* 它不需要回報成功或失敗。
* 所以只要：

```python
return
```

即可。

---

## 🧠 323 vs 261 差別

```text
261 Graph Valid Tree

目標：
判斷是不是合法 Tree

需要檢查：
No Cycle + Connected

DFS 需要：
parent
return True / False
```

```text
323 Number of Connected Components

目標：
數有幾個 component

需要檢查：
有幾塊 connected component

DFS 需要：
visited
不需要 parent
不需要 return True / False
```
---

## 🧪 Example Walkthrough

### Example 1

Input：

```python
n = 5

edges = [
    [0,1],
    [1,2],
    [3,4]
]
```

Graph：

```text
0 —— 1 —— 2

3 —— 4
```

### Step 1：建立 Graph

* 從 edges 建立 adjacency list。

```text
0 : [1]
1 : [0,2]
2 : [1]
3 : [4]
4 : [3]
```

### Step 2：初始化

```python
visited = set()
count = 0
```

目前：

```text
visited = {}

count = 0
```

### Step 3：掃描 node 0

```python
node = 0
```

* `0` 不在 `visited`。
* 代表找到一個新的 connected component。
* 所以：

```python
count += 1
```

目前：

```text
count = 1
```

開始：

```python
dfs(0)
```

### Step 4：dfs(0)

```python
visited.add(0)
```

目前：

```text
visited = {0}
```

Node 0 的鄰居：

```text
[1]
```

所以呼叫：

```python
dfs(1)
```

### Step 5：dfs(1)

```python
visited.add(1)
```

目前：

```text
visited = {0,1}
```

Node 1 的鄰居：

```text
[0,2]
```

先看 `0`：

```python
dfs(0)
```

但是：

```text
0 已經在 visited
```

所以：

```python
return
```

接著看 `2`：

```python
dfs(2)
```

### Step 6：dfs(2)

```python
visited.add(2)
```

目前：

```text
visited = {0,1,2}
```

Node 2 的鄰居：

```text
[1]
```

呼叫：

```python
dfs(1)
```

但是：

```text
1 已經在 visited
```

所以：

```python
return
```

`dfs(2)` 結束。
`dfs(1)` 結束。
`dfs(0)` 結束。

### Step 7：第一個 Component 完成

目前：

```text
visited = {0,1,2}

count = 1
```

代表：

```text
0,1,2
```

這一整塊都已經拜訪完。


### Step 8：掃描 node 1

```python
node = 1
```

* `1` 已經在 `visited`。
* 代表它已經屬於第一個 component。
* 不需要加 count。
* 不需要再 DFS。

### Step 9：掃描 node 2

```python
node = 2
```

* `2` 已經在 `visited`。
* 跳過。

### Step 10：掃描 node 3

```python
node = 3
```

* `3` 不在 `visited`。
* 代表發現第二個 connected component。
* 所以：

```python
count += 1
```

目前：

```text
count = 2
```

開始：

```python
dfs(3)
```

### Step 11：dfs(3)

```python
visited.add(3)
```

目前：

```text
visited = {0,1,2,3}
```

Node 3 的鄰居：

```text
[4]
```

呼叫：

```python
dfs(4)
```

### Step 12：dfs(4)

```python
visited.add(4)
```

目前：

```text
visited = {0,1,2,3,4}
```

Node 4 的鄰居：

```text
[3]
```

呼叫：

```python
dfs(3)
```

但是：

```text
3 已經在 visited
```

所以：

```python
return
```

`dfs(4)` 結束。
`dfs(3)` 結束。

### Step 13：全部掃描完成

目前：

```text
visited = {0,1,2,3,4}

count = 2
```

回傳：

```python
return count
```

答案：

```text
2
```

### 為什麼答案是 2？

Graph 可以分成：

```text
Component 1:

0 —— 1 —— 2
```

```text
Component 2:

3 —— 4
```

所以總共有：

```text
2 個 Connected Components
```

---

## ⏱ Complexity Analysis

### Time Complexity

* 建立 Graph 需要走過所有 edges：

```text
O(E)
```

* DFS 最多拜訪每個 node 一次：

```text
O(V)
```

* DFS 中也會走過所有 edge：

```text
O(E)
```

所以總時間複雜度：

```text
O(V + E)
```

其中：

```text
V = n
E = len(edges)
```


### Space Complexity

* Graph adjacency list 需要：

```text
O(V + E)
```

* `visited` 最多存所有 node：

```text
O(V)
```

* DFS recursion stack 最差可能是：

```text
O(V)
```

所以總空間複雜度：

```text
O(V + E)
```

---

## 🎯 Interview Takeaways

* 看到題目問：

```text
有幾個 connected components
```

* 要想到：

```text
DFS / BFS / Union Find
```

* DFS 的核心是：

```text
每遇到一個沒拜訪過的 node
就代表找到一個新的 component
```

所以：

```python
count += 1
dfs(node)
```

* DFS 的工作不是回傳答案。
* DFS 的工作是：

```text
把這個 component 全部標記成 visited
```

* 這題不需要 `parent`。
* 因為不需要判斷 cycle。
* 遇到 visited node 直接 return 即可。

---

## ✍️ 我學到的東西 | What I Learned

* Connected Component 是：

```text
一群彼此可以互相到達的 nodes
```

* 每次在 outer loop 遇到沒拜訪過的 node：

```text
代表一個新的 component
```

* `dfs(node)` 會把同一個 component 的所有 node 都走完。
* 所以同一塊 component 不會被重複計算。
* 323 和 261 很像，但目的不同：

  * 323：數 component
  * 261：判斷 valid tree

---

## 🏆 Cheat Sheet

```text
LeetCode 323

Number of Connected Components

Build graph

visited = set()

count = 0

for node in range(n):

    if node not in visited:

        count += 1

        dfs(node)

DFS:

    if visited:
        return

    add visited

    dfs(neighbor)

Answer:
count
```

---

## 🌟 One Sentence Summary

> Count how many times DFS needs to start from an unvisited node; each DFS call marks one entire connected component.

> 每次從未拜訪過的節點開始 DFS，就代表找到一個新的 connected component；DFS 會把整塊 component 全部標記起來。
