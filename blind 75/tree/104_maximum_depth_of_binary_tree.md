# 🌲 LeetCode 104 - Maximum Depth of Binary Tree

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## 📘 題目說明 | Problem Description

給定一個二元樹的根節點 `root`，請返回其最大深度。

最大深度是從根節點到最遠葉子節點的最長路徑上的節點數。

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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