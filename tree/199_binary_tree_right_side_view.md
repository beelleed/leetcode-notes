# 🌳 LeetCode 199 – Binary Tree Right Side View
🔗 題目連結：[https://leetcode.com/problems/binary-tree-right-side-view/](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## 📄 題目說明 | Problem Description

- **中文**：給定一棵二元樹的根節點 `root`，從右側看這棵樹時，你能看到哪些節點？（每層最右邊的節點）從上到下回傳這些節點的值。
- **English**: Given the root of a binary tree, imagine standing on the right side of it; return the values of the nodes you can see ordered from top to bottom — i.e. at each tree level, the rightmost node.

### Examples
- Example 1:

    - Input: root = [1,2,3,null,5,null,4]

    - Output: [1,3,4]

    - Explanation:

        ![](../images/199_tmpd5jn43fs-1.png)

- Example 2:

    - Input: root = [1,2,3,4,null,null,null,5]

    - Output: [1,3,4,5]

    - Explanation:

        ![](../images/199_tmpkpe40xeh-1.png)

- Example 3:

    - Input: root = [1,null,3]

    - Output: [1,3]

- Example 4:

    - Input: root = []

    - Output: []

---

## 🧠 解題思路 | Solution Idea

### BFS 方法（層序遍歷）

- 使用 queue 逐層處理節點。
- 每層取最後一個節點加入結果列表。

### DFS 方法（遞迴 + 優先右子樹）

- 使用深度遞迴，帶入 `depth`。
- 若目前 `depth` 尚未出現在結果中，則表示是該層最右邊節點。

---

## 💻 程式碼（BFS）

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: List[int] = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
```
### 🧱 邊界檢查 & 初始化
```python
if not root:
    return []
result: List[int] = []
queue = deque([root])
```
- 如果樹為空，直接回傳空列表。

- 建立 queue 保存 BFS 使用的節點，初始加入根節點。

- result 用來儲存答案。
### 🔁 BFS 迴圈
```python
while queue:
    level_size = len(queue)
```
- 當前層節點數量（代表目前 queue 裡有多少節點要處理）。

### 📥 處理每一層節點
```python
for i in range(level_size):
    node = queue.popleft()
```
- 用迴圈處理當層的所有節點，依序從 queue 取出節點。
```python
if i == level_size - 1:
    result.appens(node.val)
```
- 若是該層最後一個節點（最右邊），加入結果中。
```python
if node.left:
    queue.append(node.left)
if node.right:
    queue.append(node.right)
```
- 把下一層的左、右子節點加入 queue 中，準備下一輪 BFS。

### ✅ 回傳結果
```python 
return result
```

---

## 🌳 範例二元樹
```text
       1
     /   \
    2     3
     \     \
      5     4
```
這棵樹的結構如下：

- root = 1

- 左子樹 = 2 → 右子節點是 5

- 右子樹 = 3 → 右子節點是 4

### 初始化：
```python
queue = deque([1])
result = []
```
### ⏱ 第 1 層：
```python
level_size = 1
queue = [1]
```
- i = 0，node = 1

- i == level_size - 1：result.append(1)

- 加入 node.left → 2，node.right → 3
```python
result = [1]
queue = [2, 3]
```
### ⏱ 第 2 層：
```python
level_size = 2
queue = [2, 3]
```
- i = 0，node = 2

    - 加入 node.right → 5

- i = 1，node = 3

    - i == level_size - 1：result.append(3)

    - 加入 node.right → 4
```python
result = [1, 3]
queue = [5, 4]
```
### ⏱ 第 3 層：
```python
level_size = 2
queue = [5, 4]
```
- i = 0，node = 5

- i = 1，node = 4

    - i == level_size - 1：result.append(4)
```python
result = [1, 3, 4]
queue = []
```
### ✅ 結果：
```python
return [1, 3, 4]
```
這代表從右側觀看此二元樹時可以看到的節點值。

---

## ⏱ 複雜度分析 | Complexity

時間複雜度：O(n)，每個節點只會進出 queue 一次

空間複雜度：O(w)，w 為最大層寬

---

## ✍️ 我學到了什麼 | What I Learned

✅ 遇到「層級」問題優先考慮 BFS

✅ 若要抓每層特定節點（像右側視圖），可以觀察 queue 裡每層的順序

✅ 也能用 DFS 遞迴，但需優先走右邊