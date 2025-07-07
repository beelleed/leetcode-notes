# 🌳 LeetCode 226. Invert Binary Tree 翻轉二元樹

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/invert-binary-tree/)

---

## 📘 題目說明 | Problem Description
描述：給定一棵二元樹，請將其左右子樹互換，並返回其根節點。

英文：Given the root of a binary tree, invert the tree, and return its root.

### 🧪 範例 | Example

原始樹：
```markdown
    4
   / \
  2   7
 / \ / \
1  3 6  9
```
翻轉後：
```markdown
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

---

## 🧠 解題思路 | Solution Strategy
### 🔁 遞迴法（DFS）

- 核心概念：對於每個節點，遞迴地翻轉其左右子樹，然後交換左右子節點。

- English：For each node, recursively invert its left and right subtrees, then swap the left and right children.

### 🔄 迭代法（BFS）

- 核心概念：使用佇列進行層序遍歷，對每個節點交換其左右子節點，並將非空子節點加入佇列。

- English：Use a queue for level-order traversal, swap the left and right children of each node, and enqueue non-null children.

---

## 🧾 程式碼與解析 | Code and Explanation

### 🔁 遞迴法（DFS）
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TradeNode]:
        if not root:
            return None
        # 遞迴翻轉左右子樹
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # 交換左右子節點
        root.left, root.right = right, left
        return root
```
解析：

1. 若節點為空，返回 None。

2. 遞迴翻轉左子樹和右子樹。

3. 交換左右子節點。

4. 返回當前節點。

```python
left = self.invertTree(root.left)
right = self.invertTree(root.right)
```
- 對左子樹呼叫 invertTree()，並把結果存在 left

- 對右子樹呼叫 invertTree()，並把結果存在 right

這表示程式會一直往下走，直到最底層，然後才往回合併翻轉後的子樹。

---

### 🔄 迭代法（BFS）
```python
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            current = queue.popleft()
            # 交換左右子節點
            current.left, current.right = current.right, current.left

        # 將非空子節點加入佇列
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root
```
解析：

1. 若根節點為空，返回 None。

2. 初始化佇列，將根節點加入。

3. 進行層序遍歷，對每個節點：

    - 交換左右子節點。

    - 將非空子節點加入佇列。

4. 返回根節點。

#### 🔁 BFS 佇列初始化
```python 
queue = deque([root])
```
- 建立一個佇列（queue），並將根節點加入。

- 這是 BFS 的起點（從根節點開始層序處理）。

#### 👉 取出當前節點 & 翻轉
```python 
current = queue.popleft()
current.left, current.right = current.right, current.left
```
- 使用 popleft() 拿出最前面節點（符合先進先出 FIFO）

- 直接交換 current 的左右子節點（這是翻轉的核心操作）

#### ➕ 加入下一層節點
```python
if current.left:
    queue.append(current.left)
if current.right:
    queue.append(current.right)
```
- 如果 current.left 存在，就加入佇列（下一層要翻轉的節點）

- 同理，右節點也加入

- 這確保我們會處理整棵樹的所有節點

#### ✅ 回傳根節點
```python
return root
```
- 所有節點處理完後，回傳翻轉後的樹的根節點。

---

## 📊 流程圖解 | Flowchart Explanation
### 🔁 遞迴法流程圖
```scss
invertTree(4)
├── invertTree(2)
│   ├── invertTree(1) → None
│   └── invertTree(3) → None
│   → swap 1 and 3
├── invertTree(7)
│   ├── invertTree(6) → None
│   └── invertTree(9) → None
│   → swap 6 and 9
→ swap 2 and 7
```

### 🔄 迭代法流程圖
```yaml
Queue: [4]
Process 4: swap 2 and 7 → Queue: [7, 2]
Process 7: swap 6 and 9 → Queue: [2, 9, 6]
Process 2: swap 1 and 3 → Queue: [9, 6, 3, 1]
Process 9: no children
Process 6: no children
Process 3: no children
Process 1: no children
```

---

## ⏱️ 時間與空間複雜度 | Time and Space Complexity
- 時間複雜度：O(n)，其中 n 為節點數，需遍歷每個節點一次。

- 空間複雜度：

    - 遞迴法：O(h)，h 為樹的高度，遞迴棧的深度。

    - 迭代法：O(n)，最壞情況下佇列中會包含 n/2 個節點。

---

## 🧠 BFS 與 DFS 差異
| 方法  | 翻轉順序 | 資料結構  | 適合場景   |
| --- | ---- | ----- | ------ |
| DFS | 從下往上 | 遞迴    | 樹高不深時  |
| BFS | 從上往下 | queue | 層層對應處理 |

---

## 📌 學到的技巧 | What I Learned
- 如何用 DFS 遞迴處理二元樹結構。

- 如何用 queue 搭配 BFS 層序遍歷處理節點。

- Python 中 root.left, root.right = right, left 的交換技巧。

