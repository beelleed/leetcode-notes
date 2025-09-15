# 🎓 LeetCode 210 – Course Schedule II
🔗 題目連結：[https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)

---

## 📄 題目說明 | Problem Description

- **中文**：有 `numCourses`門課程，編號從 `0` 到 `numCourses-1`。有些課程有先修課（prerequisites），給定 `prerequisites` 陣列，其中每個元素 `[a, b]` 表示想要修課程 `a`，必須先修課程 `b`。請回傳一個可以修完所有課程的順序；如果不可能（例如有環狀依賴），回傳空陣列。

- **English**: You have `numCourses` courses labeled from `0` to `numCourses-1`. Some courses have prerequisites, given as pairs `[a, b]` meaning you must take course `b` before course `a`. Return an order in which you can finish all courses. If there are multiple valid orders, any is fine. If it's impossible to finish all courses (due to cycles), return an empty list.

### Examples
- Example 1:

    - Input: numCourses = 2, prerequisites = [[1,0]]
    
    - Output: [0,1]

    - Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

- Example 2:

    - Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    
    - Output: [0,2,1,3]
    
    - Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

- Example 3:

    - Input: numCourses = 1, prerequisites = []
    
    - Output: [0]

---

## 🧠 解題思路 | Solution Idea

使用 **拓撲排序 (Topological Sort)** 的技巧，有兩種常見實現方式：

- **BFS 方法 / Kahn’s Algorithm**  
  1. 建圖（adjacency list）＋ 計算每門課的入度（in‑degree = 有多少先修課程）  
  2. 把所有入度為 0 的課程加入 queue（這些可先修）  
  3. 一個一個從 queue 拿出來加入結果，並把它能「解鎖」的課程的入度減一，如果減到 0 就加入 queue  
  4. 最後，如果結果列表裡課程數量等於 `numCourses`，回傳結果；否則有 cycle，回傳空列表

- **DFS 方法 + 狀態標記**  
  用遞迴＋三狀態標記（未訪問、訪問中、已完成）來發現 cycle，並在遞迴完成後把節點加到結果 list（後序方式）。最終反轉結果以得到正確順序。

---

## 💻 程式碼實作 | Code (Python, BFS / Kahn’s Algorithm)

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建圖與計算入度
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 初始化 queue，所有入度為 0 的課程
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # 拓撲排序
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 檢查是否所有課程都能排進順序中
        if len(order) == numCourses:
            return order
        else:
            return []
```
### 建圖 + 入度初始化
```python
graph = defaultdict(list)
indegree = [0] * numCourses
for course, pre in prerequisites:
    graph[pre].append(course)
    indegree[course] += 1
```
- graph（adjacency list）：儲存每一門課 (pre) 被哪些課依賴（哪些課要等它先修完）。也就是有邊從 pre → course。

- indegree 是一個長度為 numCourses 的陣列，indegree[i] 表示課程 i 有幾個先修課（幾條入邊）。

- 遍歷 prerequisites，每對 [course, pre] 表示要先修 pre 再修 course：

    - 在 graph[pre] 裡加上 course

    - indegree[course] += 1 增加 course 的入度

### 初始化 queue 和結果 list
```python
queue = deque([i for i in range(numCourses) if indegree[i] == 0])
order = []
```
- queue 裡頭放所有 入度為 0 的課程，那些課程沒有任何先修限制，可以先修。

- order 用來儲存結果，也就是我們要回傳的修課順序。

### BFS 拓撲排序主迴圈
```python
while queue:
    curr = queue.popleft()
    order.appeend(curr)
    for next_course in graph[curr]:
        indegree[next_course] -= 1
        if indgree[next_course] == 0:
            queue.append(next_course)
```
這是核心邏輯：

- 當 queue 不空的時候，從 queue 拿出一門課 curr（入度為 0 的課），把它加入 order，表示我們選這門先修

- 接著看這門課 curr 解鎖（提供先修條件）的所有課 next_course（那些在 graph[curr] 中）：

    - 對於每個 next_course，把它的 indegree[next_course] 減 1（因為一個先修條件被滿足了）

    - 如果 next_course 的入度減到 0，代表它所有先修都滿足了，就把它加入 queue，等後面排順序

### 檢查 cycle 並回傳結果
```python
return order if len(order) == numCourses else []
```
- 最後把 order 回傳，但有個必要的檢查：如果 order 中的課程數量跟 numCourses 一樣，代表所有課都被排進順序裡（沒有 cycle）

- 如果 order 長度少於 numCourses，代表有一些課因為依賴循環或無法滿足先修條件而沒辦法排進來 → 回傳空陣列 []

---

## 🧪 範例
假設輸入：
```python
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
```
代表：

- 修 1 要先修 0

- 修 2 要先修 0

- 修 3 要先修 1 和 2

### 🚦 初始狀態

- graph 建好後長這樣：
```markdown
graph[0] = [1, 2]
graph[1] = [3]
graph[2] = [3]
graph[3] = []
```
- indegree 陣列：
```ini
indegree = [0, 1, 1, 2]  
# 課程 0 無先修 (0)，1 有 1 個先修 (0)，2 有 1 個先修 (0)，3 有 2 個先修 (1 和 2)
```
- 初始 queue 裡入度為 0 的課程是 [0]

- order = []

### 🔁 主迴圈走幾步
| 步驟 | queue 狀況 | 取出的課程 `curr` | order 變為   | 處理 curr 的鄰接課程有哪些 & 入度變化                                     | 新增到 queue 的課程                             |
| -- | -------- | ------------ | ---------- | ----------------------------------------------------------- | ----------------------------------------- |
| 1  | \[0]     | curr = 0     | \[0]       | graph\[0] = \[1,2] → 減入度： indegree\[1]=1→0，indegree\[2]=1→0 | queue → append 1,2 → queue becomes \[1,2] |
| 2  | \[1,2]   | curr = 1     | \[0,1]     | graph\[1] = \[3] → indegree\[3]=2→1                         | no 一門課入度變 0 所以未加                          |
| 3  | \[2]     | curr = 2     | \[0,1,2]   | graph\[2] = \[3] → indegree\[3]=1→0                         | queue append 3 → queue becomes \[3]       |
| 4  | \[3]     | curr = 3     | \[0,1,2,3] | graph\[3] is \[] → 沒有鄰接課程                                   | nothing new added                         |

### ✅ 最終結果

- order = [0,1,2,3]

- 長度確實等於 numCourses = 4

- 所以回傳 [0,1,2,3]

---

## ⏱ 複雜度分析 | Complexity
| 分類            | 複雜度                                                                                  |
| ------------- | ------------------------------------------------------------------------------------ |
| 時間複雜度 (Time)  | $O(V + E)$：V 是課程數（numCourses），E 是 prerequisites 的數量。建圖 + 入度初始化 + BFS 拓撲排序都各訪問節點與邊一次。 |
| 空間複雜度 (Space) | $O(V + E)$：圖（adjacency list）要存邊，入度陣列和 queue 和結果 list 都要空間，最壞情況需要存很多                  |

---

## ✍️ 我學到了什麼 | What I Learned

- 拓撲排序是解決「有依賴關係的順序問題」的標準技巧（courses, task schedule, build order 等都常用）

- Kahn’s algorithm 裡面的「入度 = 0」這個概念很重要 — 表示該節點目前沒有未完成的先修條件

- 檢查 cycle：如果最後不能得到所有節點的順序（order 長度比 numCourses 小），代表有 cycle，不可完成順序

- BFS 與 DFS 都可以做 topological sort，但 BFS（Kahn’s）在這種問題中常用且直觀