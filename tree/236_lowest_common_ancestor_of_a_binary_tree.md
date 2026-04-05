# 🌳 LeetCode 236 — Lowest Common Ancestor of a Binary Tree / 二元樹的最近共同祖先

🔗 [題目連結](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

## 📄 題目說明 | Problem Description

### 中文：
給一棵二元樹的根節點 root，以及兩個節點 p、q，請找出它們的最近共同祖先（LCA）。最近共同祖先指的是：同時是 p 與 q 的祖先，且離它們最近（深度最大）的那個節點。

### English: 
Given a binary tree root root and two nodes p and q, return their lowest common ancestor (LCA). The LCA is the deepest node that has both p and q as descendants (a node can be a descendant of itself).

### Example
- Example 1:

    ![](../images/236_binarytree.png)

    - Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    - Output: 3
    - Explanation: The LCA of nodes 5 and 1 is 3.
- Example 2:

    ![](../images/236_binarytree2.png)

    - Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    - Output: 5
    - Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
- Example 3:

    - Input: root = [1,2], p = 1, q = 2
    - Output: 1

---

## 🧠 核心觀念 | Key Insight

- 這題最重要的「一句話」：

    - 在某個節點 node：

        - 如果 p、q 分別出現在左右子樹（或其中一個就是 node），那 node 就是 LCA。

---
## 🧠 解題思路 | Solution Idea
### ✅ 方法一：DFS 遞迴 | Recursive DFS

- 對每個節點 node 做遞迴：

    1. Base case

        - 如果 node 是 None：回傳 None

        - 如果 node == p 或 node == q：回傳 node

            - 因為你已經找到其中一個目標，往上回傳給祖先做判斷

    2. 遞迴左右子樹

        - left = dfs(node.left)

        - right = dfs(node.right)

    3. 判斷 LCA

        - 如果 left 和 right 都不是 None → p、q 分別在兩邊 → node 是 LCA

        - 否則回傳非空的那邊（表示兩個都在同一側，或只找到其中一個）

---

## 💻 程式碼 | Code (Python)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        # 如果 root 本身就是 p 或 q，直接回傳 root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p, q 分別在左右子樹 -> root 是 LCA
        if left is not None and right is not None:
            return root

        # 否則回傳存在的那一邊（可能是 p/q 或 LCA）
        return left if left is not None else right
```

### 🔍 程式碼逐段拆解 | Detailed Explanation
#### 1. Base case：空節點
```python
if root is None:
    return None
```

- 走到底了，這條路找不到 p 或 q

#### 2. Base case：遇到 p 或 q
```python
if root == p or root == q:
    return root
```

- 很重要：這代表「我在這個子樹裡找到目標了」

- 不代表它就是 LCA（還要看另一個目標在哪裡）

- 但它會一路往上回傳，讓祖先做判斷

#### 3. 往左右子樹找
```python
left = self.lowestCommonAncestor(root.left, p, q)
right = self.lowestCommonAncestor(root.right, p, q)
```

- left：在左子樹找到的結果（可能是 p、q、LCA、或 None）

- right：同理

#### 4. 左右都找到 → root 是 LCA
```python
if left is not None and right is not None:
    return root
```

- 左邊回傳代表「左子樹包含 p 或 q」

- 右邊回傳代表「右子樹包含 p 或 q」

- 兩邊都有 → p 和 q 分散在兩側 → 最近交會點就是 root

#### 5. 否則把找到的那邊往上丟
```python
return left if left is not None else right
```

- 代表 p、q 都在同一側（或只找到其中一個），繼續交給上一層判斷

---

## 🧪 範例 | Example 
**Example**

樹：
```text
        3
      /   \
     5     1
    / \   / \
   6   2 0   8
      / \
     7   4
```
### 🧪 Case 1：p = 5, q = 1
從 root = 3 開始
```python
root = 3
```

- root ≠ p, q → 繼續
```python
left = LCA(5)
right = LCA(1)
```
- 左邊：root = 5
```python
if root == p:
    return 5
```

👉 left = 5

- 右邊：root = 1
```python
if root == q:
    return 1
```

👉 right = 1

回到 root = 3
```python
if left is not None and right is not None:
    return root
```

👉 回傳 3
✅ LCA = 3

### 🧪 Case 2：p = 5, q = 4
#### ▶️ 呼叫 1
```python
LCA(root=3, p=5, q=4)
```
| 變數   | 值 |
| ---- | - |
| root | 3 |
| p    | 5 |
| q    | 4 |

程式碼檢查
```python
root is None ❌
root == p or q ❌
```

👉 繼續往下
```python
left = LCA(5, 5, 4)
right = LCA(1, 5, 4)
```
#### ▶️ 呼叫 2（左子樹）
```python
LCA(root=5, p=5, q=4)
```
| 變數   | 值 |
| ---- | - |
| root | 5 |
| p    | 5 |
| q    | 4 |

程式碼檢查
```python
root == p ✅
```

👉 直接 return 5
```python
return 5
```

⚠️ 注意：
- 這一層 不會再跑 left / right

#### ▶️ 呼叫 3（右子樹）
```python
LCA(root=1, p=5, q=4)
```
| 變數   | 值 |
| ---- | - |
| root | 1 |
| p    | 5 |
| q    | 4 |

程式碼檢查
```python
root == p or q ❌
```

👉 繼續
```python
left = LCA(0, 5, 4)
right = LCA(8, 5, 4)
```
#### ▶️ 呼叫 4
```python
LCA(root=0, p=5, q=4)
```

- 0 ≠ p, q

- 左右都是 None
```python
left = None
right = None
return None
```
#### ▶️ 呼叫 5
```python
LCA(root=8, p=5, q=4)
```

- 8 ≠ p, q

- 左右都是 None
```python
return None
```
⬆️ 回到呼叫 3（root = 1）
| 變數    | 值    |
| ----- | ---- |
| left  | None |
| right | None |


#### ⬆️ 回到最上層（root = 3）
現在我們有：
| 變數    | 值    |
| ----- | ---- |
| left  | 5    |
| right | None |

執行判斷
```python
if left is not None and right is not None:
    ❌

return left if left is not None else right
```

👉 回傳 5

### 🧠 為什麼 root == p or root == q 要寫在前面？

- 如果不寫：

    - 當 p 是 q 的祖先時

    - 你會錯過「祖先本身就是答案」這件事

- 這一行保證：一個節點可以是自己的祖先

---

## ⏱️ 複雜度分析 | Complexity

- 時間複雜度：O(n) 最壞情況需要走訪整棵樹

- 空間複雜度：O(h) 遞迴 call stack 深度（h 是樹高度，最壞可到 n）

---

## ✅ 方法二：用 parent map（迭代） | Iterative with Parent Pointers

>> 這個方法很適合想「不用遞迴」或「想更像圖論 BFS/DFS」的寫法。

- 思路

    1. DFS/BFS 建立 parent：記錄每個節點的父節點

    2. 從 p 往上走，把所有祖先放入 set

    3. 從 q 往上走，第一個出現在 set 的就是 LCA

---

## Code
```python
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]

        # 建 parent map，直到 p 和 q 都出現
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        cur = p
        while cur:
            ancestors.add(cur)
            cur = parent[cur]

        cur = q
        while cur not in ancestors:
            cur = parent[cur]
        return cur
```

- 時間：O(n)

- 空間：O(n)（parent map + ancestors set）

---

## ✍️ 我學到的東西 | What I Learned

- LCA 遞迴解法的本質是：把「找到 p/q 的訊號」往上回傳，讓祖先判斷左右是否各有一個

- root == p or root == q 這個 base case 非常重要：
因為「一個節點也可以是自己的祖先」

- 遞迴法更短、更直覺；parent map 更像通用圖論做法但更吃空間

---

## Code

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node == p:
                return p
            if node == q:
                return q
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right
        return dfs(root)
```
- Time complexity is O(N) since we visit each node once.
- Space complexity is O(H) due to recursion stack, where H is the height of the tree.