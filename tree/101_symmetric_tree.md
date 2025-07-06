# 🌳 LeetCode 101：對稱二元樹（Symmetric Tree）

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/symmetric-tree/)

---

## 📘 題目說明 | Problem Description

**中文：**  
給定一個二元樹的根節點 `root`，檢查該樹是否是其自身的鏡像（即圍繞其中心對稱）。

**English：**  
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

---

## 🧠 解題思路 | Solution Strategy

要判斷一棵二元樹是否對稱，我們需要比較其左子樹和右子樹是否為鏡像。具體而言：

1. 兩個節點的值相等。
2. 左節點的左子樹與右節點的右子樹對稱。
3. 左節點的右子樹與右節點的左子樹對稱。

這可以通過遞迴或迭代的方式實現。

To determine whether a binary tree is symmetric, we need to check if the left and right subtrees are mirror images of each other. Specifically:

1. The two nodes must have equal values.
2. The left subtree of the left node must be a mirror of the right subtree of the right node.
3. The right subtree of the left node must be a mirror of the left subtree of the right node.

This can be achieved using recursion or iteration.

---

## 🔁 遞迴解法 | Recursive Solution

我們定義一個輔助函式 `isMirror`，用來比較兩個子樹是否為鏡像。

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root, root)
```
### ✅ 程式碼解析 | Code Explanation
- isSymmetric：主函式，檢查整棵樹是否對稱。

- isMirror：輔助函式，遞迴地比較兩個子樹是否為鏡像。

    - 如果兩個節點都為 None，則對稱。

    - 如果其中一個為 None，則不對稱。

    - 如果兩個節點的值不相等，則不對稱。

    - 遞迴比較左節點的左子樹與右節點的右子樹，以及左節點的右子樹與右節點的左子樹。

### 範例 | Example
```markdown
       1
     /   \
    2     2
   / \   / \
  3  4  4   3
```
#### 🧠 執行流程：

1. isSymmetric(root)

     ↓

2. isMirror(root, root)
     → t1.val == t2.val == 1 ✅
     → 遞迴：isMirror(t1.left, t2.right) 和 isMirror(t1.right, t2.left)

#### 👇 遞迴展開流程：
```scss
isMirror(1, 1)
├── isMirror(2, 2)
│   ├── isMirror(3, 3)
│   │   ├── isMirror(None, None) ✅ → True
│   │   └── isMirror(None, None) ✅ → True
│   └── isMirror(4, 4)
│       ├── isMirror(None, None) ✅ → True
│       └── isMirror(None, None) ✅ → True
└── 最終回傳 True
```

#### ✅ 每一層檢查內容：
- t1.val == t2.val

- t1.left 與 t2.right 是對稱

- t1.right 與 t2.left 是對稱

若全部成立則這兩棵子樹對稱。

---

## 🔁 迭代解法 | Iterative Solution

我們可以使用佇列來進行層序遍歷，並在每一層比較對稱位置的節點。
```python
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True
```

### ✅ 程式碼解析 | Code Explanation
- queue：佇列，用於儲存需要比較的節點對。

- 每次從佇列中取出一對節點 t1 和 t2：

    - 如果兩個節點都為 None，則繼續。

    - 如果其中一個為 None，或兩個節點的值不相等，則不對稱。

    - 將 t1 的左子節點和 t2 的右子節點、t1 的右子節點和 t2 的左子節點加入佇列。

### 範例 | Example
```markdown
       1
     /   \
    2     2
   / \   / \
  3  4  4   3

初始 queue：
```css
[(2, 2)] ← root.left, root.right
```
步驟：
1. 比較 (2, 2) → ✅ 相等

    - 加入 (3, 3) 和 (4, 4)

2. 比較 (3, 3) → ✅ 相等

    - 加入 (None, None), (None, None)

3. 比較 (4, 4) → ✅ 相等

    - 加入 (None, None), (None, None)

4. queue 剩下全部是 (None, None) → ✅ 通過

5. ✅ 最終回傳 True → 樹是對稱的

---

## 🖼️ 圖示說明 | Visual Explanation
考慮以下二元樹：

```markdown
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

- 左子樹：2 → 3, 4

- 右子樹：2 → 4, 3

這棵樹是對稱的，因為左子樹和右子樹是彼此的鏡像。

---

## 📊 複雜度分析 | Complexity Analysis
- 時間複雜度（Time Complexity）：O(n)，其中 n 是節點數。每個節點最多被訪問一次。

- 空間複雜度（Space Complexity）：

    - 遞迴：O(h)，h 為樹的高度（遞迴堆疊）。

    - 迭代：O(n)，最壞情況下佇列需存儲所有節點。

---

## ✅ 小結 | Summary
- 這題測試你對二元樹的遞迴與 BFS 的掌握。

- 遞迴法簡潔直觀，適合初學者。

- 迭代法適合處理深度較大的樹，避免遞迴限制。
