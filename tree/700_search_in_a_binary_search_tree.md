# 🌳 LeetCode 700 - 在二元搜尋樹中搜尋 | Search in a Binary Search Tree

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/search-in-a-binary-search-tree/)

---

## 📘 題目說明 | Problem Description

給定一棵二元搜尋樹（BST）和一個整數 `val`，請在 BST 中搜尋值等於 `val` 的節點，並返回以該節點為根的子樹。如果該節點不存在，則返回 `null`。

> Given the root of a binary search tree (BST) and an integer `val`, find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

### Example
- Input: root = [4,2,7,1,3], val = 2
- Output: [2,1,3]

- Input: root = [4,2,7,1,3], val = 5
- Output: []

---

## 🧠 解題思路 | Solution Strategy

利用 BST 的特性：
- 左子樹的所有節點值小於根節點。
- 右子樹的所有節點值大於根節點。

從根節點開始：
1. 如果當前節點為 `null`，表示未找到，返回 `null`。
2. 如果當前節點的值等於 `val`，返回當前節點。
3. 如果 `val` 小於當前節點的值，遞迴搜尋左子樹。
4. 如果 `val` 大於當前節點的值，遞迴搜尋右子樹。

> Leverage the BST property: if `val` is less than the current node's value, search the left subtree; if greater, search the right subtree; if equal, return the current node.

---

## 🧾 程式碼實作 | Code Implementation

### 方法一：遞迴 | Recursive

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
```
- 定義一個方法 searchBST，傳入：

    - root：BST 的根節點（可能是空）

    - val：要搜尋的目標值

- 回傳型別為 Optional[TreeNode]，表示可能回傳某個節點，也可能回傳 None。

```python
if not root or root.val == val:
    return root
```
- 第一個條件：如果 root 是 None，表示已經走到底部，沒有找到這個值，回傳 None。

- 第二個條件：如果 root.val == val，代表目前這個節點就是要找的值，直接回傳該節點。

```python
if val < root.val:
    return self.searchBST(root.left, val)
```
- 如果目標值小於當前節點的值，說明答案應該在左子樹中。

- 遞迴往左子節點繼續搜尋。

```python
else:
    return self.searchBST(root.right, val)
```
- 否則，如果目標值大於當前節點的值，答案應該在右子樹中。

- 遞迴往右子節點繼續搜尋。

### 🧠 為什麼這樣寫？
- BST 特性：左邊的值都小於節點、右邊的值都大於節點。

- 因此，對於任意節點，都可以透過比較 val 來決定往哪邊走（左或右），不用遍歷整棵樹。

### ✅ 範例說明
假設樹如下，val = 2：
```markdown
      4
     / \
    2   7
   / \
  1   3
```
執行流程會是：

    - 4 != 2 → 2 < 4 → 走左邊（2）

    - 2 == 2 → 找到 → 回傳節點 2

---

### 方法二：迭代 | Iterative
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None
```

```python
while root:
```
- 使用 while 迴圈持續遍歷節點。

- 只要還有節點沒遍歷完（即 root 不為 None），就繼續找。

```python
if val == root.val:
    return root
```
- 如果當前節點的值等於 val，表示找到了這個節點，直接回傳。

```python
elif val < root.val:
    root = root.left
```
- 若目標值比當前節點小，根據 BST 性質，「較小值」必定在左子樹，因此將 root 指向左子節點繼續找。

```python
else:
    root = root.right
```
- 若目標值比當前節點大，則將 root 指向右子節點繼續查找。

```python
return None
```
- 如果整個樹都找完還找不到（while 退出），代表該值不在樹中，回傳 None。

### 🔍 為什麼這樣寫？
- 相比遞迴，這種 迭代寫法節省空間，不會佔用呼叫堆疊。

- 效率與遞迴一致：時間複雜度 O(h)，其中 h 是樹的高度。
 
### ✅ 範例說明
若 BST 結構如下，搜尋值為 3：
```markdown
      5
     / \
    3   8
```
步驟如下：

- 5 ≠ 3，3 < 5 → 走左子樹

- 3 == 3 → 回傳該節點

---

## ⏱️ 時間與空間複雜度 | Time and Space Complexity
- 時間複雜度 Time Complexity：O(h)，其中 h 為樹的高度。

    - 最佳情況（平衡樹）：O(log n)

    - 最壞情況（退化為鏈表）：O(n)

- 空間複雜度 Space Complexity：

    - 遞迴方法：O(h)，遞迴堆疊的深度。

    - 迭代方法：O(1)，只使用常數空間。

---

## 🧠 學習重點 | What I Learned
- 理解並應用 BST 的性質可以有效地進行搜尋操作。

- 遞迴與迭代兩種方法各有優缺點，選擇取決於具體情況。

- 注意在遞迴時要正確地返回結果，避免漏寫 return 導致錯誤。
