#  🌳 LeetCode 102 – Binary Tree Level Order Traversal | 二元樹層序遍歷
🔗 題目連結：[https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

## 📘 題目說明 | Problem Description

- **中文：**  
  給定一棵二元樹的根節點 `root`，請依照層（從左到右、從上到下）將每層節點的值輸出為一個列表。

- **English:**  
  Given the root of a binary tree, return its values in level order traversal (i.e., from left to right, level by level).

### Examples
- Example 1:

![](../images/102_tree1.jpg)

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

- Example 2:

    - Input: root = [1]
    - Output: [[1]]

- Example 3:

    - Input: root = []
    - Output: []

---

## 🧠 解法核心：廣度優先搜尋（BFS）

我們運用 BFS 來一次處理每一層節點，這樣可以自然達到「按層遍歷」的順序。

### 中文思路：
1. 若 `root` 是空，直接回傳空列表。
2. 使用隊列（`deque`），初始時放入根節點。
3. 每輪迴圈記錄目前隊列的長度（也就是這一層節點數量）。
4. 依序將這一層的節點值蒐集進 `level` list，並將節點的左右子節點加入隊列。
5. 當前層處理完畢後，把 `level` 加入結果，並重複至隊列為空。

### English Explanation:
1. Return `[]` if the tree is empty.
2. Use a queue (BFS) starting with the root node.
3. For each level, capture the number of nodes and process them, collecting their values and enqueueing children.
4. Append the current level values to the result list and continue until the queue is empty.

---

## 🧾 Python 程式碼 | Code

```python
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
```
```python
if not root:
    return []
```
- 如果樹是空的（root 是 None），那就直接回傳空 list，代表沒有層可遍歷。
```python
result = []
queue = deque([root])
```
- result: 存放每層節點的值（答案的主體）。

- queue: 使用雙端隊列（deque）進行 BFS。初始時放入 root。
```python
while queue:
```
- 只要 queue 裡還有節點，表示還有層需要處理，就繼續進行迴圈。
```python
level_size = len(queue)
level = []
```
- level_size: 記錄這一層總共有幾個節點（非常重要！這樣才能一層一層分開）。

- level: 用來收集目前這一層的節點值。
```python
for _ in range(level_size):
    node = queue.popleft()
    level.append(node.val)
```
- 用 for 迴圈跑這層的每一個節點。

- node = queue.popleft()：從左邊取出節點。

- level.append(node.val)：把該節點的值加到當前層結果中。
```python
if node.left:
    queue.append(node.left)
if node.right:
    queue.append(node.right)
```
- 如果當前節點有左或右子節點，就加入 queue，等到下一層再處理它們。
```python
result.append(level)
```
- 一層處理完後，將這層的值加入 result。
```python
return result
```
- 最後回傳完整結果，每層節點都是一個 list。

---

## 🧪 範例
假設我們的二元樹長這樣：
```markdown
        3
       / \
      9  20
         / \
        15  7
```
用 List 表示為：[3,9,20,null,null,15,7]

### 📘 初始化
```python
result = []
queue = deque([3])
```
### 🔄 第一層處理（根節點）
```python
level_size = 1
level = []
```
- 取出 node = 3

- level = [3]

- 把 3.left = 9、3.right = 20 加入 queue
```python
queue = deque([9, 20])
result = [[3]]
```
### 🔄 第二層處理
```python
level_size = 2
level = []
```
- 第一次：

    - node = 9 → level = [9]

    - 9 沒有左右子節點，不加進 queue

- 第二次：

    - node = 20 → level = [9, 20]

    - 把 20.left = 15、20.right = 7 加入 queue
```python
queue = deque([15, 7])
result = [[3], [9, 20]]
```
### 🔄 第三層處理
```python
level_size = 2
level = []
```
- 第一次：

    - node = 15 → level = [15]

    - 沒有子節點

- 第二次：

    - node = 7 → level = [15, 7]

    - 沒有子節點
```python
queue = deque([])
result = [[3], [9, 20], [15, 7]]
```
### ✅ 最後結果
```python
return [[3], [9, 20], [15, 7]]
```

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分析項目  | 複雜度                                |
| ----- | ---------------------------------- |
| 時間複雜度 | `O(n)` — 每個節點恰好進出隊列一次              |
| 空間複雜度 | `O(n)` — 最多保存一層所有節點，在完全二叉樹下為 `n/2` |

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- BFS 是處理「層序遍歷」這類題型的核心技巧。

- 使用 for _ in range(level_size) 確保只遍歷當前層的節點，避免多層交錯。

- 結構清晰，容易閱讀的層級控制流程是主流寫法。

### English:

- BFS is perfect for level-order traversal in tree problems.

- Capturing the current queue size allows you to isolate levels cleanly.

- The resulting pattern is both efficient and easy to understand.