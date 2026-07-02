# 📍 LeetCode 261 — Graph Valid Tree

🔗 https://leetcode.com/problems/graph-valid-tree/

## 📄 題目說明 | Problem Description

### 中文

* 給定：

  * `n` 個節點（編號 `0 ~ n-1`）
  * `edges`，表示無向圖（Undirected Graph）的所有邊。

* 判斷這張 Graph 是否是一棵合法的 Tree。

### English

* Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges.
* Return `true` if the graph forms a valid tree, otherwise return `false`.

### Examples

#### Example 1

```text
n = 5

edges =
[[0,1],
 [0,2],
 [0,3],
 [1,4]]
```

畫成圖：

```text
      0
    / | \
   1  2  3
   |
   4
```

Output

```text
true
```

#### Example 2

```text
n = 5

edges =
[[0,1],
 [1,2],
 [2,3],
 [1,3],
 [1,4]]
```

畫成圖：

```text
      0
      |
      1
    / | \
   2--3  4
```

Output

```text
false
```

因為：

```text
2 → 1 → 3 → 2
```

形成 Cycle。

---

## 🧠 核心觀念 | Key Insight

一棵 Tree 必須同時滿足兩個條件：

### ① 沒有 Cycle

例如：

```text
0
|\
| \
1--2
```

可以一直繞圈：

```text
0 → 1 → 2 → 0
```

因此：

```text
不是 Tree
```

### ② 所有節點都必須連通（Connected）

例如：

```text
0 — 1

2 — 3
```

Graph 被分成兩塊。

因此：

```text
不是 Tree
```

所以 Tree 的判斷就是：

```text
No Cycle
+

Connected
```

另外還有一個非常重要的性質：

```text
Tree 的 Edge 數一定是：

n - 1
```

例如：

```text
5 個 Node

一定只有 4 條 Edge
```

因此一開始就可以先判斷：

```python
if len(edges) != n - 1:
    return False
```

如果不是：

```text
一定不是 Tree
```

完全不用 DFS。

---

## 🧠 解題流程

### Step 1

先判斷：

```python
len(edges) == n - 1
```

不是：

直接回傳：

```python
False
```
### Step 2

建立 Graph。

例如：

```text
0-1
0-2
1-4
```

建立：

```python
graph = {
0:[1,2],
1:[0,4],
2:[0],
3:[],
4:[1]
}
```

### Step 3

從任意一個 Node 開始 DFS。

通常：

```python
dfs(0)
```

### Step 4

DFS 拜訪所有可以到達的 Node。

利用：

```python
visited
```

避免重複拜訪。

### Step 5

DFS 結束。

如果：

```python
len(visited) == n
```

代表：

```text
所有 Node 都拜訪到了
```

Graph Connected。

因此：

```text
Valid Tree
```
---

## 💻 Code

```python
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:

                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
```

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
if len(edges) != n - 1:
    return False
```

* Tree 一定有：

```text
Edge = Node - 1
```

* 如果不是：

```text
一定不是 Tree
```

* 可以直接結束。

例如：

```text
n = 5

edges = 5
```

一定有 Cycle。

```python
graph = defaultdict(list)
```

* 建立 Adjacency List。
* 用來表示每個 Node 可以走到哪些鄰居。

```python
for a, b in edges:
```

* 一條一條 Edge 建立 Graph。

例如：

```text
0 - 1
```

```python
graph[a].append(b)
graph[b].append(a)
```

* 因為是：

```text
Undirected Graph
```

所以：

```text
0 可以到 1

1 也可以到 0
```

兩邊都要加入。

例如：

```text
0-1
0-2
1-4
```

Graph：

```text
0 : [1,2]
1 : [0,4]
2 : [0]
3 : []
4 : [1]
```

```python
visited = set()
```

* 紀錄哪些 Node 已經拜訪過。

避免：

```text
一直重複走
```


```python
def dfs(node, parent):
```

* DFS。

除了目前 Node。

還要知道：

```text
我是從誰走來的
```

因此多傳：

```python
parent
```

```python
if node in visited:
    return False
```

* 如果目前 Node 已經拜訪過。

代表：

```text
Cycle
```

因此：

```python
return False
```

```python
visited.add(node)
```

* 把目前 Node 標記成已拜訪。

例如：

```text
visited

{}

↓

{0}
```

```python
for nei in graph[node]:
```

* 走訪所有鄰居。

例如：

```text
0

↓

1
2
3
```

會依序拜訪：

```text
1

2

3
```

```python
if nei == parent:
    continue
```

* 這一行非常重要。

因為：

```text
Undirected Graph
```

一定會有：

```text
0 → 1

1 → 0
```

如果不跳過：

會一直：

```text
0

↓

1

↓

0

↓

1
```

無限遞迴。

因此：

```python
if nei == parent:
    continue
```

代表：

```text
不要走回剛剛來的地方
```

```python
if not dfs(nei, node):
    return False
```

* 繼續 DFS。

如果下面子樹發現：

```text
Cycle
```

直接一路回傳：

```python
False
```

```python
return True
```

* 代表：

```text
目前這條 DFS

沒有發現 Cycle
```

```python
if not dfs(0, -1):
    return False
```

* 從 Node 0 開始 DFS。

因為：

```text
Root 沒有 Parent
```

所以：

```python
parent = -1
```

```python
return len(visited) == n
```

* DFS 結束。

如果：

```python
len(visited) == n
```

代表：

```text
所有 Node 都拜訪到了
```

Graph 是：

```text
Connected
```

因此：

```text
Valid Tree
```

否則：

代表：

```text
還有 Node 沒拜訪到
```

Graph 被分成很多塊。

不是 Tree。

---

## 🧪 Example Walkthrough

### Example 1

Input：

```python
n = 5

edges = [
    [0,1],
    [0,2],
    [0,3],
    [1,4]
]
```

畫成 Graph：

```text
      0
    / | \
   1  2  3
   |
   4
```

### Step 1：先判斷 Edge 數量

```python
len(edges) = 4
```

因為：

```python
n - 1 = 5 - 1 = 4
```

所以：

```text
符合 Tree 的第一個條件
```

繼續做 DFS。

### Step 2：建立 Graph

一條一條加入。

加入：

```text
0 - 1
```

Graph：

```text
0 : [1]
1 : [0]
```

加入：

```text
0 - 2
```

Graph：

```text
0 : [1,2]
1 : [0]
2 : [0]
```

加入：

```text
0 - 3
```

Graph：

```text
0 : [1,2,3]
1 : [0]
2 : [0]
3 : [0]
```

加入：

```text
1 - 4
```

Graph：

```text
0 : [1,2,3]
1 : [0,4]
2 : [0]
3 : [0]
4 : [1]
```
### Step 3：開始 DFS

初始化：

```text
visited = {}
```

開始：

```python
dfs(0, -1)
```

### Step 4：拜訪 Node 0

加入：

```text
visited = {0}
```

Graph：

```text
      0
    / | \
   1  2  3
   |
   4
```

開始拜訪鄰居：

```text
1

2

3
```

先走：

```python
dfs(1,0)
```

### Step 5：拜訪 Node 1

加入：

```text
visited = {0,1}
```

Node 1 的鄰居：

```text
0

4
```

第一個：

```text
0
```

但是：

```python
0 == parent
```

所以：

```python
continue
```

不走回去。

接著拜訪：

```python
dfs(4,1)
```

### Step 6：拜訪 Node 4

加入：

```text
visited = {0,1,4}
```

Node 4 的鄰居：

```text
1
```

但是：

```python
1 == parent
```

因此：

```python
continue
```

沒有其他鄰居。

回傳：

```python
True
```

DFS 回到：

```text
Node 1
```

Node 1 也完成。

回傳：

```python
True
```

### Step 7：回到 Node 0

目前：

```text
visited = {0,1,4}
```

繼續拜訪下一個：

```python
dfs(2,0)
```

加入：

```text
visited = {0,1,2,4}
```

Node 2 只有：

```text
0
```

因為：

```python
0 == parent
```

所以：

```python
continue
```

回傳：

```python
True
```
### Step 8：拜訪 Node 3

加入：

```text
visited = {0,1,2,3,4}
```

Node 3 的鄰居：

```text
0
```

因為：

```python
0 == parent
```

直接跳過。

DFS 結束。

### Step 9：確認是否全部拜訪

目前：

```python
len(visited)
```

等於：

```text
5
```

也就是：

```python
n
```

因此：

```text
所有 Node 都連通
```

沒有 Cycle。

因此：

```python
return True
```

### Example 2

Input：

```python
n = 5

edges = [
 [0,1],
 [1,2],
 [2,3],
 [1,3],
 [1,4]
]
```

畫成 Graph：

```text
      0
      |
      1
    / | \
   2--3  4
```

### Step 1：Edge 數量

```python
len(edges) = 5
```

但是：

```python
n - 1 = 4
```

因此：

```text
Edge 數就已經錯了
```

代表：

```text
一定存在 Cycle
```

直接：

```python
return False
```

甚至：

```text
不用 DFS
```

### 如果沒有這個判斷呢？

DFS：

```text
0

↓

1

↓

2

↓

3
```

此時：

Node 3 又可以回到：

```text
1
```

而：

```text
1
```

不是：

```text
parent
```

因此：

```python
dfs(1,3)
```

會發現：

```python
1 in visited
```

代表：

```text
Cycle
```

因此：

```python
return False
```

---

## ⏱ Complexity Analysis

### Time Complexity

建立 Graph：

```text
O(E)
```

DFS：

```text
O(V + E)
```

總共：

```text
O(V + E)
```

其中：

```text
V = Node 數量

E = Edge 數量
```

### Space Complexity

Graph：

```text
O(V + E)
```

Visited：

```text
O(V)
```

Recursive Stack：

最差：

```text
O(V)
```

因此：

```text
O(V + E)
```

---

## 🎯 Interview Takeaways

* Tree 必須同時滿足：

```text
No Cycle

+

Connected
```

* Tree 一定有：

```text
Edge = Node - 1
```

因此第一行通常就是：

```python
if len(edges) != n - 1:
    return False
```

* DFS 時一定要傳：

```python
parent
```

因為：

```text
Undirected Graph

一定可以走回上一個 Node
```

如果不跳過 Parent：

```text
0

↓

1

↓

0

↓

1

↓

0
```

會一直無限遞迴。


* DFS 完還要確認：

```python
len(visited) == n
```

否則：

Graph 沒有完全連通。

---

## ✍️ 我學到的東西 | What I Learned

* Graph Valid Tree 本質就是：

```text
判斷

No Cycle

+

Connected
```

* Edge 數量：

```text
一定是

n - 1
```

* Undirected Graph 做 DFS：

一定要傳：

```python
parent
```

* DFS 完：

還要確認：

```python
len(visited) == n
```

---

## 🏆 Cheat Sheet

```text
261

Graph Valid Tree

Tree

=

No Cycle

+

Connected

先判斷：

edges == n-1

↓

建立 Graph

↓

DFS(node,parent)

↓

跳過 parent

↓

如果遇到 visited

Cycle

↓

DFS 完

visited == n

True
```

---

## 🌟 One Sentence Summary

> A graph is a valid tree if and only if it has exactly `n-1` edges, contains no cycle, and every node is connected.

> 一張 Graph 是合法 Tree 的條件是：**邊數等於 `n-1`、沒有 Cycle，且所有節點都互相連通。**
