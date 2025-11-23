# 🌳 LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## 📘 題目說明 | Problem Description

給定一棵二元搜尋樹（BST）以及兩個節點 `p` 和 `q`，請找出它們的「最近共同祖先」。

BST 的定義：
- 左子樹的所有節點值小於根節點
- 右子樹的所有節點值大於根節點

> Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

> According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

### 🧠 解題思路 | Solution Strategy

我們可以利用 BST 的特性來判斷 `p` 和 `q` 的位置：
1. 若 `p.val` 和 `q.val` 都小於當前節點，則共同祖先在左子樹。
2. 若 `p.val` 和 `q.val` 都大於當前節點，則共同祖先在右子樹。
3. 若一個在左一個在右，或其中一個等於當前節點，則當前節點就是共同祖先。

> Leverage the BST property: If both `p` and `q` are less than the root, recurse left. If both are greater, recurse right. If they split or one equals the root, root is the LCA.

---

## 🔁 方法一：遞迴 | Recursive

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

### 🔍 程式碼解釋 | Explanation
- 如果兩個值都比當前節點小，向左遞迴。

- 如果兩個值都比當前節點大，向右遞迴。

- 否則當前節點就是 LCA。

---

## 🔄 方法二：迭代 | Iterative
```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
```
```python
while root:
```
- 用迴圈走過整棵樹（也可以用遞迴方式）
```python
if p.val < root.val and q.val < root.val:
    root = root.left
```
- 如果兩個值都小於當前節點，LCA 在左邊，往左子樹走。
```python
elif p.val > root.val and q.val > root.val:
    root = root.right
```
- 如果兩個值都大於當前節點，LCA 在右邊，往右子樹走。
```python
else:
    return root
```
- 若一個在左、一個在右，或其中一個就是 root，這裡就是他們的最近公共祖先。

### 📘 範例說明：

假設有這棵 BST：
```markdown
        6
       / \
      2   8
     / \ / \
    0  4 7 9
      / \
     3   5
```
- 查詢 p = 2 和 q = 8：

    - 2 < 6 且 8 > 6 → 分別在左右子樹 → 返回 6

- 查詢 p = 2 和 q = 4：

    - 都 < 6 → 往左走 → 到 2

    - 4 > 2 → 分散兩側 → 返回 2

---

## ⏱️ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度：O(h)，其中 h 為樹的高度。

- 空間複雜度：

    - 遞迴版本：O(h)（遞迴堆疊）

    - 迭代版本：O(1)

---

## 🧠 學到的東西 | What I Learned
- 如何利用 BST 的性質（大小關係）來快速定位兩個節點的共同祖先。

- 理解 LCA 的定義：「同時為兩個節點的最深共同祖先節點」。

- 遞迴與迭代的方式都能解，選擇取決於個人熟悉程度與堆疊深度考量。

