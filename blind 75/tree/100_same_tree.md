# 🌲 LeetCode 100 — Same Tree / 相同的樹
🔗 [題目連結](https://leetcode.com/problems/same-tree/)

---

## 📄 題目說明 | Problem Description

- **中文**：給你兩棵二元樹的根節點 `p` 和 `q`，判斷這兩棵樹是否**相同**。  
  如果兩棵樹的結構完全一樣，且對應節點的值也都相等，就稱為相同的樹；否則不相同。

- **English**: Given two binary tree roots `p` and `q`, determine whether the two trees are the same.  
  Two trees are the same if they are structurally identical and the node values are the same for all corresponding positions.

- **Examples**:
    - Example 1:

        ![](../images/100_ex1.jpg)

        - Input: p = [1,2,3], q = [1,2,3]
        - Output: true

    - Example 2:

        ![](../images/100_ex2.jpg)

        - Input: p = [1,2], q = [1,null,2]
        - Output: false

    - Example 3:
    
        ![](../images/100_ex3.jpg)

        - Input: p = [1,2,1], q = [1,1,2]
        - Output: false

---

## 🧠 解題思路 | Solution Idea

這題很典型地使用 **遞迴 (DFS)** 比較兩棵樹：

1. **基本條件／基底情況**：
   - 如果 `p` 和 `q` 都是 `None`，代表兩棵樹同時到達空節點，算是一致 → 回傳 `True`。
   - 如果只有一棵是 `None`（另一棵不是），或是值不同 → 回傳 `False`。

2. **遞迴比較子樹**：
   - 若當前節點值相同，就繼續比較左子樹：`isSameTree(p.left, q.left)`  
   - 以及比較右子樹：`isSameTree(p.right, q.right)`  
   - 最後只有左與右子樹都一樣時，整棵樹才被視為一樣。

這種方法自然對應樹結構，也容易理解與實作。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 若兩者都是 None，代表這部分一致
        if p is None and q is None:
            return True
        # 若其中一個是 None（另一個不是），或兩者的值不同
        if p is None or q is None or p.val != q.val:
            return False
        # 遞迴比較左子樹與右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```
| 區段                | 程式碼                                                                            | 功能 / 說明                         |
| ----------------- | ------------------------------------------------------------------------------ | ------------------------------- |
| 基底檢查：兩者皆為 None    | `if p is None and q is None: return True`                                      | 如果 `p` 和 `q` 都走到底（空節點），那這部分是一致的 |
| 基底檢查：一個 None 或值不同 | `if p is None or q is None or p.val != q.val: return False`                    | 結構不同或值不同的情況，直接回傳 False          |
| 遞迴比較              | `return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)` | 如果當前節點值一樣，就往下比較左子樹 + 右子樹是否也都一樣  |

```python
return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```
也可以寫成
```python
left_same = self.isSameTree(p.left, q.left)
right_same = self.isSameTree(p.right, q.right)
```
或
```python
if not self.isSameTree(p.left, q.left):
    return False
if not self.isSameTree(p.right, q.right):
    return False
return True
```

---

## 🧪 範例 | Example

假設有以下兩棵樹：
```makefile
p:        1
         / \
        2   3

q:        1
         / \
        2   3
```
- 呼叫 isSameTree(p, q)：

    1. 檢查 p is None and q is None？ → 否（兩者都有節點）

    2. 檢查 p is None or q is None or p.val != q.val？

        - p、q 都不是 None

        - p.val = 1，q.val = 1 → 相等
            所以這一條不成立 → 繼續

    3. 遞迴比較左子樹與右子樹：

        - 比較左子樹：isSameTree(p.left, q.left)

            - p.left.val = 2，q.left.val = 2

            - 它們的子節點都是 None，會走到基底條件 if p is None and q is None → 回傳 True

        - 比較右子樹：isSameTree(p.right, q.right)

            - p.right.val = 3，q.right.val = 3

            - 它們的子節點同樣都是 None → 回傳 True

    4. 因為左右子樹比較都是 True，主呼叫回傳 True → 樹相同。

再一個不同的例子
```makefile
p:        1
         /
        2

q:        1
           \
            2
```
- 呼叫 isSameTree(p, q)：

    1. p 和 q 都非 None，且 p.val = 1, q.val = 1 → 符合繼續

    2. 遞迴比較左子樹與右子樹：

        - 左子樹：isSameTree(p.left, q.left) → p.left 是節點 2，q.left 是 None → 在第二條 if p is None or q is None ... 被檢出，回傳 False

        - 右子樹不必繼續比較（因為用 and），最終主呼叫會回傳 False

- 所以這兩棵樹不相同。

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n)，其中 n 是兩棵樹中節點數的最小者。在最差情況下，需要比較每個節點一次。

- 空間複雜度：O(h)，遞迴呼叫棧佔的空間，h 是樹的高度。若樹很偏（像鏈表形態），高度可達 n。

---

## ✍️ 我學到的東西 | What I Learned

- 遞迴對於樹型結構問題非常自然，用相同的邏輯遞迴子樹就能解很多樹的題目。

- 要先處理 Null 情況／結構不匹配的情形，才能安全取得 .val。

- and 很重要：兩邊子樹都要「相同」才算整棵樹相同，不是任一相同就好。

- 空樹也是一種特例（兩個都是空樹應回傳 True）。