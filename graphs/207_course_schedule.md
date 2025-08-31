# 207. Course Schedule – 可以完成課程嗎？

[Leetcode 207](https://leetcode.com/problems/course-schedule/)

---

## 題目說明 | Problem Description

- **中文：**  
  給定 `numCourses` 表示總課程數（從 0 到 `numCourses-1`），及一個 `prerequisites` 陣列，其中每個元素 `[a, b]` 表示要修 `a`，必須先修 `b`。請判斷是否可以完成所有課程（不存在環狀依賴），能完成回傳 `True`，否則 `False`。

- **English:**  
  You are given `numCourses` and a list of prerequisite pairs, where `[a, b]` means you must take course `b` before course `a`. Determine if you can complete all courses without conflicts (i.e., no cycles). Return `True` if possible, otherwise `False`.

### Examples
- Example 1:

    - Input: numCourses = 2, prerequisites = [[1,0]]
    - Output: true
    - Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

- Example 2:

    - Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    - Output: false
    - Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

---

## 💡 解題思路 | Solution Idea

### 🔁 用拓樸排序檢查「有向圖是否有環」：

- 將課程關係視為一張 **有向圖**。
- 使用 **Kahn’s Algorithm（BFS）**：
  - 建立圖（鄰接表）與入度表。
  - 將入度為 0 的課程加入 queue。
  - 每次移除一個課程，將它指向的其他課程入度減 1。
  - 若全部課程都能移除，代表無環。

---

## 🧠 演算法核心步驟

1. 🏗 建立課程圖和入度表  
2. 🌀 把所有入度為 0 的課程丟進 queue  
3. ⏭ 不斷從 queue 中取出課程，更新相鄰課程的入度  
4. 🧮 如果最後能處理完所有課程 → ✅ 無環 → 可以完成

---

## 🧾 Python 實作程式碼

```python
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses
```
```python
graph = [[] for _ in range(numCourses)]
```
- 初始化鄰接表（圖）：

    - graph[i] 儲存哪些課程要依賴第 i 門課

    - 例如 graph[0] = [1,2] → 課程 1 和 2 需要課程 0

```python
indegree = [0] * numCourses
```
- 建立「入度表」：

    - indegree[i] 表示有幾門課要先修才能上第 i 門課

    - 如果 indegree[i] == 0，代表可以直接上
```python
for a, b in prerequisites:
    graph[b].append(a)
    indegree[a] += 1
```
- 填入前置關係：

    - [a, b] 表示要上 a，必須先上 b

    - 所以從 b 指向 a → graph[b].append(a)

    - 並且 a 的入度 +1 → indegree[a] += 1

```python
queue = deque([i for in range(numCourses) if indegree[i] == 0])
```
- 將所有「入度為 0」的課程加入 queue：

    - 表示它們可以被「最先處理」
```python
count = 0
```
- 記錄處理過的課程數
```python
while queue:
    node = queue.popleft()
    count += 1
```
- 進行 BFS：

    - 每次取出一個可以開始的課程（入度為 0）

    - 處理過的課程數 count +1
```python
for nei in grapgh[node]:
    indegree[nei] -= 1
    if indegree[nei] == 0:
        queue.append(nei)
```
- 走訪該課程的相鄰節點（需要它當前置的課程）

- 將它們的入度 -1（代表少了一個依賴）

- 若入度降為 0，代表現在可以修了 → 加入 queue
```python
return count == numCourses
```
- 最後檢查是否所有課程都處理過

- 如果 count == numCourses → 表示無循環，課程安排成功

- 否則代表有循環（卡住），回傳 False

### 🔁 小結重點
| 區塊         | 意義            |
| ---------- | ------------- |
| `graph`    | 課程依賴圖（誰要先修）   |
| `indegree` | 每門課還有幾個依賴沒完成  |
| `queue`    | 所有可以馬上修的課     |
| `count`    | 處理過的課程數       |
| 回傳條件       | 能否處理完全部課程（無環） |


---

## 🧪 Step‑by‑Step 流程模擬
Example:
```lua
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]
```
| 步驟    | graph                       | indegree   | queue  | count |
| ----- | --------------------------- | ---------- | ------ | ----- |
| Init  | 0->\[1,2], 1->\[3], 2->\[3] | \[0,1,1,2] | \[0]   | 0     |
| pop 0 | -                           | \[0,0,0,2] | \[1,2] | 1     |
| pop 1 | -                           | \[0,0,0,1] | \[2]   | 2     |
| pop 2 | -                           | \[0,0,0,0] | \[3]   | 3     |
| pop 3 | -                           | \[0,0,0,0] | \[]    | 4     |

結果 count == numCourses = 4 → 回傳 True。

---

## ⏱ 複雜度分析

- 時間複雜度：O(V + E)，V = 課程數，E = 前置關係數。

- 空間複雜度：O(V + E)，儲存圖與入度與 queue。

---

## ✅ 我學到了什麼 | What I Learned

- 拓樸排序（Topological Sort）是檢查 DAG（Directed Acyclic Graph）是否有環的關鍵方法。

- BFS 版本（Kahn’s algorithm）通過入度來找到無依賴節點，層級化逐步處理。

- 對於「依賴關係」題型，辨識為 DAG + 循環檢測 → 拓樸排序是優選解法。