# ✅ LeetCode 98. 驗證二元搜尋樹 | Validate Binary Search Tree

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/validate-binary-search-tree/)

## 📘 題目說明 | Problem Description

給定一棵二元樹，請判斷它是否是一棵有效的「二元搜尋樹」（Binary Search Tree, BST）。

有效的 BST 需滿足以下條件：
- 左子樹所有節點的值 < 根節點的值
- 右子樹所有節點的值 > 根節點的值
- 左右子樹本身也必須是 BST

> Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.

- The right subtree of a node contains only nodes with keys greater than the node's key.

- Both the left and right subtrees must also be binary search trees.

### Examples

- Example 1

    ![](../images/98_tree1.jpg)

        Input: root = [2,1,3]

        Output: true

- Example 2

    ![](../images/98_tree2.jpg)

        Input: root = [5,1,4,null,null,3,6]

        Output: false

        Explanation: The root node's value is 5 but its right child's value is 4.

---

## 🧠 解題思路 | Solution Strategy

### 方法一：中序遍歷法（In-order Traversal）
**中文**
- 中序遍歷 BST 會產生「嚴格遞增」的數列。
- 我們可以使用一個變數 `prev` 保存上一個節點的值，與當前節點進行比較。
- 一旦出現當前節點 ≤ `prev`，就不是有效 BST。

**English**
- In-order traversal of a BST yields a strictly increasing sequence.

- In-order traversal of a BST yields a strictly increasing sequence.

- If we ever encounter a node whose value is less than or equal to prev, the tree is not a valid BST.

### 🧾 程式碼與詳細解釋 | Code with Detailed Explanation

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None  # 保存中序遍歷中前一個節點的值

        def inorder(node):
            if not node:
                return True

            # 遞迴左子樹
            if not inorder(node.left):
                return False

            # 中序訪問當前節點，與前一個節點比較
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val  # 更新 prev

            # 遞迴右子樹
            return inorder(node.right)

        return inorder(root)
```
```python
def inorder(node):
    if not node:
        return True
```
- 若目前節點是空的（None），代表已走到底部（如葉節點的左右子樹），回傳 True 表示這部分是合法的 BST。

```python
if not inorder(node.left):
    return False
```
- 遞迴處理左子樹。

- 如果左子樹不是 BST（也就是有節點違反規則），則立即回傳 False。

```python
if self.prev is not None and node.val <= self.prev:
    return False
```
- 判斷目前節點值是否大於前一個節點值。

- 若不是「嚴格大於」，代表中序排序錯誤，違反 BST 條件，直接回傳 False。

```python
self.prev = node.val
```
- 若當前節點合法，更新 self.prev 為目前節點的值，方便與下個節點做比較。

```python
return inorder(node.right)
```
- 遞迴處理右子樹，若有違規則也會返回 False。

### 📍 範例 1：合法 BST

樹結構：
```markdown
    2
   / \
  1   3
```
- 中序遍歷順序：1 → 2 → 3

- self.prev 比較過程：

    - prev=None, node=1 ✅

    - prev=1, node=2 → 2 > 1 ✅

    - prev=2, node=3 → 3 > 2 ✅

- 全部都嚴格遞增 → return True ✅

### 📍 範例 2：非法 BST

樹結構：
```markdown
    5
   / \
  1   4
     / \
    3   6
```
- 中序遍歷順序：1 → 5 → 3 → 4 → 6

- self.prev 比較過程：

    - prev=None, node=1 ✅

    - prev=1, node=5 ✅

    - prev=5, node=3 → 3 ≤ 5 ❌

- 偵測到「不是嚴格遞增」 → return False ❌

### 🌳 中序遍歷驗證 BST 的流程圖
```plaintext
             [開始] isValidBST(root)
                    │
                    ▼
          ┌────────────────────┐
          │ 呼叫 inorder(root) │
          └────────────────────┘
                    │
                    ▼
          ┌────────────────────┐
          │ 目前節點是否為 None? │
          └────────────────────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
    [是，回傳 True]      [否，繼續處理]
          │                   │
          ▼                   ▼
  [遞迴檢查左子樹 inorder(node.left)]
          │
          ▼
  [若左子樹回傳 False，則回傳 False]
          │
          ▼
  [檢查當前節點值是否大於 prev]
          │
          ▼
  [若不滿足，回傳 False]
          │
          ▼
  [更新 prev 為當前節點值]
          │
          ▼
  [遞迴檢查右子樹 inorder(node.right)]
          │
          ▼
  [若右子樹回傳 False，則回傳 False]
          │
          ▼
          [回傳 True]
```

### 🧠 補充說明
- prev：用來記錄中序遍歷過程中前一個節點的值，初始為 None。

- 中序遍歷特性：對於合法的 BST，中序遍歷的結果應該是嚴格遞增的序列。

- 遞迴結束條件：當節點為 None 時，表示已到達葉節點的下一層，回傳 True。

- 違反 BST 規則的情況：如果發現當前節點的值不大於 prev，則說明不是合法的 BST，立即回傳 False。

---

## 📘 方法二：上下界限制法 | Method 2: Recursive with Bounds

### 🧠 解題思路 | Strategy Explanation

- 對於每個節點，我們遞迴檢查它的值是否在一個「有效區間」之內。
- 左子樹的所有節點值應小於其祖先節點的值，右子樹的節點值應大於其祖先節點的值。
- 每層遞迴都會根據當前節點的值更新上下界。

> For each node, we recursively check whether its value falls within a valid range.
> The left subtree must be less than the current node, and the right subtree must be greater.
> These bounds are updated during recursion.

### ✅ Python 程式碼 | Python Code

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)
```
```python
if val <= lower or val >= upper:
    return False
```
- 如果節點值不在指定範圍內，代表不是 BST

```python
if not helper(node.left, lower, val):
```
- 遞迴檢查左子樹，新的上限是當前節點值

```python
if not helper(node.right, val, upper):
```
- 遞迴檢查右子樹，新的下限是當前節點值

---

## ⏱️ 時間與空間複雜度 | Time and Space Complexity
- 時間複雜度：O(n)，其中 n 為節點數，每個節點僅被訪問一次。

- 空間複雜度：O(h)，其中 h 為樹的高度，遞迴堆疊的深度。

---

## 🧠 學到的東西 | What I Learned 

✅ 方法一：中序遍歷法（In-order Traversal）
- 利用了 BST 的中序遍歷為「嚴格遞增序列」這一性質。

- 實作簡潔，只需一個 prev 變數來記錄上一個節點。

- 缺點是相對不直觀，對 BST 結構理解較弱時容易犯錯。

I learned that a valid BST should yield a strictly increasing sequence during in-order traversal. Using a single prev variable is efficient but can be error-prone if the BST property isn’t fully understood.

✅ 方法二：上下界遞迴法（Recursive Bounds Check）
- 更符合 BST 的定義：左子樹值 < 節點 < 右子樹值。

- 每一層都遞迴地傳遞「上下限」，對結構限制更嚴格。

- 這種寫法較直觀，也比較好解釋錯誤原因。

I learned how to explicitly enforce the BST property at every level using min and max bounds. This method is easier to reason about and ensures each node is valid in its whole subtree.

---

## ✅ 方法對比與總結 | Comparison & Summary
| 方法   | 優點        | 缺點      | 適用場景       |
| ---- | --------- | ------- | ---------- |
| 中序遍歷 | 實作簡單，空間低  | 容易忽略樹結構 | 小題快速實作     |
| 區間遞迴 | 嚴謹正確、符合定義 | 多傳參數略複雜 | 解釋錯誤、面試時使用 |
