# 🌲 LeetCode 104 - Maximum Depth of Binary Tree

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## 📘 題目說明 | Problem Description
### 中文
給定一個二元樹的根節點 `root`，請返回其最大深度。

最大深度是從根節點到最遠葉子節點的最長路徑上的節點數。

### English
Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Examples
- Example 1:

    ![](../images/104_tmp-tree.jpg)

    - Input: root = [3,9,20,null,null,15,7]
    - Output: 3

- Example 2:

    - Input: root = [1,null,2]
    - Output: 2
 
---

## 🧠 解題思路 | Solution Strategy

### 方法一：遞迴解法（DFS）

- 如果節點為空（`None`），回傳 0
- 否則遞迴計算左子樹與右子樹的深度
- 最後回傳 `1 + max(左深度, 右深度)`

這是處理二元樹問題最常見的方式，簡潔又清楚。

### Method 1: Recursive DFS

- If the node is `None`, return 0
- Otherwise, recursively compute the max depth of the left and right subtree
- Return `1 + max(left_depth, right_depth)`

This is a common and clean approach for binary tree problems using Depth-First Search (DFS).

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### if not root: return 0

- 如果 root 是空的（即節點為 None），表示已經到達葉節點的下一層，深度為 0。

- 這是 遞迴的終止條件（Base Case）。

### return 1 + max(...)

- 每經過一個節點，深度就要加 1。

- 所以從當前節點開始，會加上 1 並選擇左右子樹中深度較大的那一邊。

### max(self.maxDepth(root.left), self.maxDepth(root.right))

- 這段會同時遞迴左子樹和右子樹。

- 分別計算兩邊的最大深度，然後取較大值。

---

## 🧪 範例輸入
```python
Input: root = [1, 2, 3, 4, None, None, 5]
```

這棵樹長這樣：
```markdown
        1
       / \
      2   3
     /     \
    4       5
```
### 🔍 遞迴過程（DFS）
```python
maxDepth(1)
→ 1 + max(maxDepth(2), maxDepth(3))
```
### ✅ 左子樹 maxDepth(2)
```python
maxDepth(2)
→ 1 + max(maxDepth(4), maxDepth(None))
```

- maxDepth(4) → 1 + max(maxDepth(None), maxDepth(None)) → 1

- maxDepth(None) → 0

所以：
```python
maxDepth(2) = 1 + max(1, 0) = 2
```
### ✅ 右子樹 maxDepth(3)
```python
maxDepth(3)
→ 1 + max(maxDepth(None), maxDepth(5))
```

- maxDepth(5) → 1 + max(maxDepth(None), maxDepth(None)) → 1

- maxDepth(None) → 0

所以：
```python
maxDepth(3) = 1 + max(0, 1) = 2
```
### ✅ 回到根節點
```python
maxDepth(1) = 1 + max(2, 2) = 3
```
### 🧾 最終輸出
```python
Output: 3
```

---

### 方法二：迭代解法（BFS）

- 使用 queue 一層一層遍歷（層序遍歷）
- 每次處理完一層就把 `depth` 加 1
- 最後回傳總層數

適合處理節點多、遞迴可能stack Overflow的情況。

### Method 2: Iterative BFS

- Use a queue to traverse the tree level by level
- Increment the depth after processing each level
- Return the final depth count

This approach is helpful for wide trees and avoids recursion stack overflow.

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
```
### if not root: return 0

- 若樹是空的（根節點為 None），則深度為 0，直接回傳。

### queue = deque([root])

- 使用 deque 作為 BFS 的隊列，初始只放入根節點。

- 我們會一層一層地處理所有節點。

### depth = 0

- 記錄目前遍歷到的深度（層數）。

### while queue:

- 只要隊列中還有節點，就表示還有下一層。

### for _ in range(len(queue)):

- 這段確保我們一次處理「當前層」的所有節點。

- len(queue) 是這層節點的個數。

### node = queue.popleft()

- 從隊列中取出目前層的節點。

### if node.left: queue.append(node.left)
### if node.right: queue.append(node.right)

- 將目前節點的左右子節點加入隊列，準備處理下一層。

### depth += 1

- 當這一層的所有節點都處理完，深度就加 1

---

## 🧪 範例輸入
```python
Input: root = [1, 2, 3, 4, None, None, 5]
```

- 這棵樹長這樣：
```markdown
        1
       / \
      2   3
     /     \
    4       5
```
### ▶️ BFS 過程

初始化：
```python
queue = deque([1])
depth = 0
```
### 🔁 第 1 層：

- queue = [1]

- depth = 0 → 1

- 處理節點 1，加入左右子節點：2、3
```python
queue = [2, 3]
```
### 🔁 第 2 層：

- queue = [2, 3]

- depth = 1 → 2

- 處理節點 2 → 加入 4

- 處理節點 3 → 加入 5
```python
queue = [4, 5]
```
### 🔁 第 3 層：

- queue = [4, 5]

- depth = 2 → 3

- 處理節點 4 → 沒有子節點

- 處理節點 5 → 沒有子節點
```python
queue = []
```

---

## ⏱️ 時間與空間複雜度 | Complexity
| 方法     | 時間複雜度 | 空間複雜度              |
| ------ | ----- | ------------------ |
| 遞迴 DFS | O(n)  | O(h)（樹的高度）         |
| 迭代 BFS | O(n)  | O(n)（queue 最多裝滿一層） |

---

## 📌 學到的東西 | What I Learned
- 二元樹深度問題可以用 DFS 或 BFS 解

- 遞迴解法簡潔易寫，適合入門理解樹結構

- BFS 適用於節點很多、避免遞迴爆棧的場景

- BFS 通常搭配 queue，DFS 搭配遞迴或 stack