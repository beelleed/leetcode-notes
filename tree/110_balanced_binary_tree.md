# 📍 LeetCode 110 — Balanced Binary Tree | 平衡二元樹
🔗 [題目連結](https://leetcode.com/problems/balanced-binary-tree/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給你一棵二元樹，判斷它是不是「高度平衡」。


- 高度平衡定義：對樹上每個節點，都要滿足
    - |左子樹高度 - 右子樹高度| <= 1

### English
Given a binary tree, determine if it is height-balanced: for every node, the height difference between left and right subtrees is at most 1.
### Examples

- Example 1:

    ![](../images/110_balance_1.jpg)

    - Input: [3,9,20,null,null,15,7]

    - Output: True

- Example 2:

    ![](../images/110_balance_2.jpg)

    - Input: [1,2,2,3,3,null,null,4,4]

    - Output: False

- Example 3:

    - Input: root = []
    
    - Output: true

---

## 🧠 解題思路 | Solution Idea

- 不是只看 root，而是 每一個節點都要平衡。

- 最直覺但慢的方法（不推薦）

    - 對每個節點都算一次左右高度 → O(n^2)（退化成鏈狀樹會超慢）

- 標準解法：後序遍歷 + 早停（推薦）

    - 用 DFS（postorder）：

        - 先拿到左右子樹高度

        - 再判斷當前節點是否平衡

        - 如果任何地方不平衡，直接往上回傳「失敗訊號」


- 技巧：用 -1 當作不平衡的 sentinel

    - dfs(node) 回傳：

        - 正常：該子樹高度

        - 不平衡：-1

---

## 💻 程式碼實作 | Code (Python)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_h = height(node.left)
            if left_h == -1:
                return -1

            right_h = height(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return 1 + max(left_h, right_h)

        return height(root) != -1
```

### 🔍 程式碼逐段說明 | Line-by-line Explanation
### 定義高度函數（回傳高度或 -1）
```python
def height(node):
    if not node:
        return 0
```
- 空節點高度 = 0（base case）

### 算左邊高度 + 早停
```python
left_h = height(node.left)
if left_h == -1:
    return -1
```

- 如果左子樹已經不平衡，整棵一定不平衡 → 直接回傳 -1

### 算右邊高度 + 早停
```python
right_h = height(node.right)
if right_h == -1:
    return -1
```
### 檢查當前節點是否平衡
```python
if abs(left_h - right_h) > 1:
    return -1
```

- 高度差超過 1 → 不平衡

### 平衡就回傳高度
```python
return 1 + max(left_h, right_h)
```

- 當前高度 = 自己這層 + 左右較高那邊

### 最終答案
```python
return height(root) != -1
```

- height(root) 如果回傳 -1 → 不平衡 → False

- 否則回傳高度（>=0）→ 平衡 → True

---

## 🧪 範例流程 | Example Walkthrough
```text
    1
   /
  2
 /
3
```

### Step 1：算 height(3)

- height(None)=0、height(None)=0

- abs(0-0)=0 ≤ 1 → 回傳 1

### Step 2：算 height(2)

- left_h = 1（來自 3）

- right_h = 0（None）

- abs(1-0)=1 ≤ 1 → 回傳 2

### Step 3：算 height(1)

- left_h = 2（來自 2）

- right_h = 0（None）

- abs(2-0)=2 > 1 → 回傳 -1

### 最後：

- height(root) != -1 → False

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n)

    - 每個節點最多被訪問一次

    - early stop 可能更快（不平衡很早被發現時）

- 空間複雜度：O(h)

    - recursion stack 深度 = 樹高

    - 最差鏈狀樹 O(n)，平衡樹約 O(log n)

---

## ✍️ 我學到的東西 | What I Learned
- 這題最重要的是：不要重複算高度

- -1 sentinel 超好用：

    - 一旦發現不平衡 → 立刻 early stop

    - height() 同時做到「算高度 + 檢查平衡」

---

## 🧠 一句話總結
I compute subtree heights using postorder DFS and return -1 as a signal for imbalance, so the tree can be checked in one pass.