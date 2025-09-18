# 📘 LeetCode 94 – Binary Tree Inorder Traversal | 二元樹中序遍歷
🔗 題目連結：[https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)

---

## 📄 題意說明 | Problem Description

### 中文：
給定一棵二元樹的根節點 root，要求回傳一個列表，表示對該樹做 中序遍歷（Inorder Traversal） 後節點值的順序。中序遍歷的順序是：左子樹 → 根節點 → 右子樹。

### English:
Given the root of a binary tree, return the list of values of its nodes ordered by inorder traversal. The inorder sequence for each node is: traverse its left subtree first, then visit the node itself, then traverse its right subtree.

### Examples
- Example 1:

    - Input: root = [1,null,2,3]

    - Output: [1,3,2]

- Explanation:

![](../images/94_1.png)

- Example 2:

    - Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

    - Output: [4,2,6,5,7,1,3,9,8]

- Explanation:

![](../images/94_2.png)

- Example 3:

    - Input: root = []

    - Output: []

- Example 4:

    - Input: root = [1]

    - Output: [1]

---

## 🧠 解題思路 | Solution Idea
### 中文
- 有兩種常用方法：

    1. 遞迴（Recursion）： 利用呼叫堆疊自動處理「左 → 根 → 右」的順序，很直接。

    2. 疊代 + Stack（Iteration with Stack）： 模擬遞迴的流程，用 stack 手動追蹤節點，先一路往左放進 stack，左邊走到頭後再回來 visit 節點，再走右邊。

### English
There are two common approaches:

- Recursion: 
    Use the call stack to naturally handle the "Left → Root → Right" order. It's straightforward and concise.

- Iteration with Stack:
    Simulate the recursive process manually by using a stack. Continuously traverse to the left subtree and push nodes onto the stack. Once the leftmost node is reached, start visiting nodes by popping from the stack, then move to the right subtree.

---

## 💻 程式碼
- 方法 1：遞迴
```python
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
```
```python
result: List[int] = []
```
- 建立一個空的 result 陣列，用來收集中序遍歷的結果。
```python
def dfs(node: Optional[TreeNode])
```
- 定義一個內部的遞迴函式 dfs，用來執行中序遍歷。

- 接收參數 node，是目前正在處理的節點。
```python
if not node:
    return
```
- 基本條件：當遇到 None（空節點）時直接返回，代表葉節點走到底了。
```python
dfs(node.left)
```
- 遞迴呼叫左子節點，確保先走左邊。

- 中序遍歷順序是：左 → 中 → 右，這一步實現「左」。
```python
result.append(node.val)
```
- 訪問當前節點，將它的值加入結果中。

- 這一步實現「中」。
```python
dfs(node.right)
```
- 遞迴呼叫右子節點。

- 這一步實現「右」。
```python
dfs(root)
```
- 從整棵樹的 root 開始進行 DFS 遞迴。
```python
return result
```
- 返回完整的中序走訪結果。
### 🧪 範例樹
假設有棵二元樹如下：
```markdown
     4
    / \
   2   5
  / \
 1   3
```
中序遍歷（inorder）會輸出 [1, 2, 3, 4, 5]

### 🔍 Trace 步驟對應程式碼

1. inorderTraversal(root) 被呼叫，result = []，然後 dfs(root)，此時 node 是根節點 4

2. 在 dfs(4)：

    - node 不為 None

    - 呼叫 dfs(node.left) → dfs(2)

3. 在 dfs(2)：

    - node 不為 None

    - 呼叫 dfs(node.left) → dfs(1)

4. 在 dfs(1)：

    - node 不為 None

    - 呼叫 dfs(node.left) → dfs(None) → 回傳（base case）

    - result.append(node.val) → append 1 → result = [1]

    - 呼叫 dfs(node.right) → dfs(None) → 回傳

5. 回到 dfs(2)：

    - 左子樹處理完

    - result.append(node.val) → append 2 → result = [1, 2]

    - 呼叫 dfs(node.right) → dfs(3)

6. 在 dfs(3)：

    - 呼叫 dfs(3.left) → None → 回

    - result.append(3) → result = [1, 2, 3]

    - 呼叫 dfs(3.right) → None → 回

7. 回到 dfs(4)：

    - 左子樹（整個 2 子樹）已完成

    - result.append(4) → result = [1, 2, 3, 4]

    - 呼叫 dfs(4.right) → dfs(5)

8. 在 dfs(5)：

    - dfs(5.left) → None

    - result.append(5) → result = [1, 2, 3, 4, 5]

    - dfs(5.right) → None

9. 所有遞迴呼叫完成後 dfs(root) 結束，回到 inorderTraversal，回傳 result，也就是 [1,2,3,4,5]

### 🧠 小總結

這段程式碼實現的是「中序遍歷（Inorder Traversal）」的遞迴解法，符合順序 左 → 根 → 右。
使用 result 來儲存結果，並透過 dfs 函式遞迴地走訪每個節點，邏輯清晰又簡潔。

---

### 方法 2：疊代 + Stack
```python
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []                # 儲存中序遍歷的結果
        stack: List[TreeNode] = []            # 用來模擬遞迴過程的 stack
        current = root                        # 初始化從根節點開始

        while current or stack:               # 當前節點不為空，或 stack 中還有未訪問節點
            # 一直向左走，直到最底層，把沿途節點存進 stack
            while current:
                stack.append(current)         # 將節點加入 stack
                current = current.left        #  向左子節點前進

            # 左邊到底了，開始回溯
            current = stack.pop()             # 從 stack 拿出一個節點（回到上一層）
            result.append(current.val)        # 訪問該節點（中序：左 → 根 → 右）

            # 接下來要處理右子樹
            current = current.right           # 移動到右子節點

        return result                         # 回傳最終結果

```
### 🧠 重點說明
#### 🔄 while current or stack:

中序遍歷流程是「左 → 根 → 右」。這個條件確保：

- 還沒走到最左邊時，current 不為空。

- 回到上一層節點處理右子樹時，stack 中會有東西。

#### ⬅️ while current:

這個內層 while 是將目前節點一路向左走，並把所有沿途節點放進 stack，因為中序遍歷要先處理左子樹。

#### 🔙 current = stack.pop()

走到底後，開始回到上一層，取出上個節點來處理（也就是「根節點」的部分）。

#### ➡️ current = current.right

根處理完後，轉往右子樹繼續進行遞迴（或模擬遞迴）。

### 🔍 範例流程 | Example 

假設樹如下：
```markdown
    4
   / \
  2   5
 / \
1   3
```
中序遍歷應該輸出 [1,2,3,4,5]

遞迴方式：

- 起始從 root = 4 → 遞迴左子樹 2

- 在 2 → 遞迴左子樹 1 → 左子為 None 回來 → visit 1 → 右子為 None

- 回回來到 2 → visit 2 → 遞迴右子樹 3 → visit 3

- 回到 4 → visit 4

- 遞迴右子樹 5 → visit 5

疊代方式：

| 動作                         | current | stack          | result       |
| -------------------------- | ------- | -------------- | ------------ |
| 初始                         | 4       | \[]            | \[]          |
| 向左 push                    | 2       | \[4]           | \[]          |
| 向左 push                    | 1       | \[4,2]         | \[]          |
| current becomes None，pop 1 | None    | \[4,2] → pop 1 | \[1]         |
| current = 1.right → None   | None    | \[4,2]         | \[1]         |
| pop 2                      | None    | \[4] → pop 2   | \[1,2]       |
| current = 2.right → 3      | 3       | \[4]           | \[1,2]       |
| push 3.left = None (skip)  | 3       | \[4,3]         | \[1,2]       |
| pop 3                      | None    | \[4] → pop 3   | \[1,2,3]     |
| current = 3.right = None   | None    | \[4]           | \[1,2,3]     |
| pop 4                      | None    | \[] → pop 4    | \[1,2,3,4]   |
| current = 4.right = 5      | 5       | \[]            | \[1,2,3,4]   |
| push left = None skip      | 5       | \[5]           | \[1,2,3,4]   |
| pop 5                      | None    | \[] → pop 5    | \[1,2,3,4,5] |
| current = 5.right = None   | None    | \[]            | \[1,2,3,4,5] |

---

## ⏱ 複雜度分析 | Complexity Analysis
| 分類    | 複雜度                                                                                |
| ----- | ---------------------------------------------------------------------------------- |
| 時間複雜度 | O(n)，每個節點拜訪一次。                                                   |
| 空間複雜度 | O(n)，遞迴的 call stack 或疊代的 stack 在最壞情況（像線性鏈表）下為 n；平均在平衡樹中為 O(h)，h 是樹高。  |

---

## 📝 我學到了什麼 | What I Learned

- 遞迴方式寫法簡潔且直觀，非常符合「分治 + DFS」的思維。

- 疊代方式雖然稍微複雜一點，但能避免遞迴造成的 call stack 過深問題，也比較適合一些語言環境遞迴效率 or stack 空間比較受限的情況。

- 中序遍歷是很多樹與 BST（Binary Search Tree）操作的基礎，理解這個順序對後面做很多題—像 BST 的驗證、生成、搜尋範圍查詢 等很重要。