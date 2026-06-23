# 🌳 LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal
🔗 題目連結：[https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

## 📘 題目說明 | Problem Description

- **中文**：給定一個二元樹的前序與中序遍歷結果，請重建該二元樹。
- **English**: Given preorder and inorder traversal of a binary tree, construct the binary tree.

### Examples
- Example 1:

![](../images/105_tree1.jpg)

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    
    Output: [3,9,20,null,null,15,7]

- Example 2:

    - Input: preorder = [-1], inorder = [-1]
    - Output: [-1]
 

---

## 🧠 解題思路 | Solution Idea

1. **前序遍歷**的第一個元素是根節點（root）。
2. 在 **中序遍歷**中找到這個根的位置：
   - 左邊是左子樹
   - 右邊是右子樹
3. 遞迴建構左右子樹，根據子樹大小來分割 preorder 的區段。
4. 使用 `inorder_index_map` 加速查找中序位置，避免重複搜尋。

---

## 💻 程式碼 | Code (Python)

```python
from typing import List, Optional

# 樹節點定義
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建一個字典，讓 inorder 值 → index 查找為 O(1)
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        # 遞迴函式，處理 preorder[start_pre : start_pre + size], inorder[start_in : start_in + size]
        def helper(pre_start: int, in_start: int, size: int) -> Optional[TreeNode]:
            if size == 0:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # inorder 中 root 的位置
            root_in_index = inorder_index_map[root_val]
            # 左子樹節點數量 = inorder 中根左邊的節點數
            left_size = root_in_index - in_start
            # 右子樹節點數量 = size - left_size - 1

            # 建立左子樹
            root.left = helper(
                pre_start + 1,
                in_start,
                left_size
            )
            # 建立右子樹
            root.right = helper(
                pre_start + 1 + left_size,
                root_in_index + 1,
                size - left_size - 1
            )

            return root

        return helper(0, 0, len(preorder))
```
```python
inorder_index_map = {val: i for i, val in enumerate(inorder)}
```
- 建立一個字典 inorder_index_map，把中序遍歷陣列中每個值對應到它的索引位置。

    | 部分                                   | 意思                                 |
    | ------------------------------------ | ---------------------------------- |
    | `enumerate(inorder)`                 | 同時取出陣列的 **索引 (idx)** 與 **值 (val)** |
    | `for idx, val in enumerate(inorder)` | 迴圈掃過整個陣列                           |
    | `{val: idx for ...}`                 | 建立一個字典：鍵是 val，值是 idx               |

    - 為什麼要這樣做？因為後面經常要在 inorder 裡找某個 root 的位置，若沒字典就要每次線性搜尋，效率會差。字典查找是𝑂(1)。
    - 如果 inorder = [9, 3, 15, 20, 7]，那 inorder_index_map 會是：
    ```python
    {
    9: 0,
    3: 1,
    15: 2,
    20: 3,
    7: 4
    }
    ```
    - ✅ 用法：
        當我們拿到 root_val = preorder[pre_start]，就能立刻查出這個值在 inorder 中的索引：
        ```python
        root_in_index = inorder_index_map[root_val]
        ```
    - 🚀 優點：查找一個值的位置只需要 O(1) 時間（比用 inorder.index(val) 快）。


### 遞迴 helper 函式定義
```python
def helper(pre_start: int, in_start: int, size: int):
    if size == 0:
        return None
```
- helper 是遞迴函式，用來建子樹。

- 參數說明：

    - pre_start: 在 preorder 中，這個 subtree 的首個節點的 index

    - in_start: 在 inorder 中，這個 subtree 的首個節點的 index

    - size: 這個 subtree 有多少個節點

- 如果 size == 0，代表這個子樹沒有節點，直接回傳 None。

### 建立 root 節點 & 找 inorder 中 root 位置
```python
root_val = preorder[pre_start]
root = TreeNode(root_val)

root_in_index = inorder_index_map[root_val]
```
- root_val 從 preorder[pre_start] 拿到，preorder 的第一個元素一定是 subtree 的 root。

- 建立節點 root。

- 用字典查 root_val 在 inorder 的位置 root_in_index。

### 計算左子樹大小 & 切分 preorder/inorder
```python
left_size = root_in_index - in_start
# 右子樹節點數量 = size - left_size - 1
```
- 左子樹節點數量就是 inorder 中從 in_start 到 root_in_index - 1 的那些節點數：也就是 left_size = root_in_index - in_start。

- 右子樹大小就剩下總 size 減去 root 本身再減掉左子樹的大小。

### 遞迴做左子樹 & 右子樹
```python
root.left = helper(
    pre_start + 1,
    in_start,
    left_size
)
root.right = helper(
    pre_start + 1 + left_size,
    root_in_index + 1,
    size - left_size - 1
)
```
- 左子樹：

    - preorder 的範圍從根的下一個 pre_start + 1

    - inorder 的範圍從 in_start

    - 節點數量是 left_size

- 右子樹：

    - preorder 要跳過 root 和左子樹的元素，所以是 pre_start + 1 + left_size

    - inorder 要從 root_in_index + 1 開始（root 右邊）

    - 節點數為 size - left_size - 1

### 回傳 root 節點
```python
return root
```
- 左右子樹都被遞迴建好後，把整個 subtree 的 root 節點回傳給上一層。

### 最外層呼叫 helper
```python
return helper(0, 0, len(preorder))
```
- 用整個 preorder/inorder 的範圍建整棵樹：

    - preorder 從 0 開始

    - inorder 從 0 開始

    - size 是全部節點數 len(preorder)（因為 preorder 與 inorder 長度相同）

### ✅ 小結

- 利用 preorder 的特性找 root。

- 利用 inorder 找 root 分界點，可以知道左子樹 / 右子樹節點數量。

- 遞迴切分範圍來建子樹。

---

## 🔍 範例說明 | Example Walkthrough

輸入：
```python
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```
### 初始呼叫
```scss
helper(pre_start=0, in_start=0, size=5)
```
- preorder[0] = 3 → 此 subtree 的根是 3

- 在 inorder 裡找到 3 的 index → root_in_index = 1

計算：

- 左子樹節點數量 left_size = root_in_index - in_start = 1 - 0 = 1

- 右子樹節點數量 right_size = size - left_size - 1 = 5 - 1 - 1 = 3

建立：
```markdown
         3
        / \
      ?     ?
```
接著建：

- 左子樹：helper(pre_start + 1 =1, in_start =0, size = left_size =1)

- 右子樹：helper(pre_start + 1 + left_size =2, in_start = root_in_index + 1 =2, size = right_size =3)

### 左子樹部分

呼叫：
```scss
helper(pre_start=1, in_start=0, size=1)
```
- preorder[1] = 9 → 根是 9

- 在 inorder 裡找到 9 的 index → 0

計算：

- left_size = 0 - 0 = 0

- right_size = 1 - 0 - 1 = 0

建立節點 9，左子樹與右子樹皆為 None，結束這支子樹。
### 右子樹部分

呼叫：
```scss
helper(pre_start=2, in_start=2, size=3)
```
- preorder[2] = 20 → 根是 20

- 在 inorder 找到 20 的 index → 在 inorder 是 inorder_index_map[20] = 3

計算：

- left_size = root_in_index - in_start = 3 - 2 = 1

- right_size = size - left_size - 1 = 3 - 1 - 1 = 1

建立節點 20：
```markdown
        20
       /   \
     ?       ?
```
繼續建左與右子樹：

- 左子樹：helper(pre_start=3, in_start=2, size=1)

- 右子樹：helper(pre_start=3 + left_size =4, in_start= root_in_index + 1 =4, size=1)
### 右子樹的左子節點（20 的左子樹）

呼叫：
```scss
helper(pre_start=3, in_start=2, size=1)
```
- preorder[3] = 15 → 根是 15

- 在 inorder 找到 15 的位置 → index = 2

計算：

- left_size = 2 - 2 = 0

- right_size = 1 - 0 - 1 = 0

節點 15，左右都 None。
### 右子節點（20 的右子樹）

呼叫：
```scss
helper(pre_start=4, in_start=4, size=1)
```
- preorder[4] = 7 → 根是 7

- 在 inorder 找到 7 的位置 → index = 4

計算：

- left_size = 4 - 4 = 0

- right_size = 1 - 0 - 1 = 0

節點 7，左右皆 None
### 最後的重建樹結構：
```markdown
    3
   / \
  9  20
     / \
    15  7
```
### 📊 步驟對照表（preorder/inorder 區段）
| 範圍階段    | preorder 範圍                     | inorder 範圍                     | 根節點 | 左子樹大小 | 右子樹大小 |
| ------- | ------------------------------- | ------------------------------ | --- | ----- | ----- |
| 整棵樹     | preorder\[0:5] = \[3,9,20,15,7] | inorder\[0:5] = \[9,3,15,20,7] | 3   | 1     | 3     |
| 左子樹     | preorder\[1:2] = \[9]           | inorder\[0:1] = \[9]           | 9   | 0     | 0     |
| 右子樹     | preorder\[2:5] = \[20,15,7]     | inorder\[2:5] = \[15,20,7]     | 20  | 1     | 1     |
| 20 的左子樹 | preorder\[3:4] = \[15]          | inorder\[2:3] = \[15]          | 15  | 0     | 0     |
| 20 的右子樹 | preorder\[4:5] = \[7]           | inorder\[4:5] = \[7]           | 7   | 0     | 0     |

---

## 🧠 思路來源：根據 traversal 的特性
### 📌 1. 前序遍歷（Preorder） ➜ 根 → 左 → 右

- preorder[0] 一定是整棵樹的根（root）

### 📌 2. 中序遍歷（Inorder） ➜ 左 → 根 → 右

- 在 inorder 中，根節點左邊是左子樹，右邊是右子樹

### 🧩 關鍵拆解步驟
🔹 root_val = preorder[pre_start]

    → 因為前序第一個一定是根（根在最前面）

🔹 root_in_index = inorder_index_map[root_val]

    → 在中序中找出這個根的位置

🔹 left_size = root_in_index - in_start

    → 中序中從 in_start 到 root_in_index - 1 就是左子樹的節點 → 所以這段的長度就是左子樹的節點數

### 🌲 為什麼 helper 的參數要這樣遞增？
- root.left = helper(pre_start + 1, in_start, left_size)

    - 下一個 preorder 的位置就是左子樹的根（因為是 根 → 左 → 右）

    - pre_start + 1：左子樹的根在 preorder 中緊接著 root

    - in_start：左子樹在 inorder 的起點

    - left_size：左子樹節點數量

-  root.right = helper(pre_start + 1 + left_size, root_in_index + 1, size - left_size - 1)

    - 前序中跳過 root（+1）和左子樹（+left_size）後，才是右子樹的根

    - inorder 中右子樹是從 root_in_index + 1 開始

    - 右子樹大小是剩下的節點：size - left_size - 1

### 🎯 小總結

- 前序的順序是：根 → 左子樹 → 右子樹

- 中序可以幫你分出：左子樹 / 根 / 右子樹

→ 所以前序先抓根，然後根據中序來計算左右子樹的長度，就能切出正確的子問題，進行遞迴。


---

## ⏱ 複雜度分析 | Time & Space Complexity

- 時間複雜度: O(n)，n 是節點數。每個節點建立一次；查找根在 inorder 中的位置透過字典是 O(1)。

- 空間複雜度: O(n)。主要來自字典 + 遞迴調用堆疊最壞情況。

---

## ✍️ 我學到了什麼 | What I Learned

- 前序＋中序遍歷能唯一決定一棵二元樹（節點值唯一這個條件很重要）。

- 用一個 map (value → index) 可以避免在 inorder 中重複進行線性搜尋。

- index 切分的方式（preorder 與 inorder 的對應片段計算）是這題容易錯的地方，一定要確認左子樹與右子樹的起點與大小算對。

---

## Code
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
```

## Complexity
### 時間複雜度

每次遞迴：

1. inorder.index()
```python
mid = inorder.index(preorder[0])
```
要掃整個 inorder。

成本：O(k)

其中 k 是目前子樹大小。

2. slicing
```python
preorder[1:mid+1]
preorder[mid+1:]
inorder[:mid]
inorder[mid+1:]
```
每個 slice 都要複製新陣列。

總成本：O(k)

所以每層遞迴成本：O(k)

假設樹平衡：
```python
n
├─ n/2
├─ n/2
```
則：
```python
T(n) = 2T(n/2)+O(n)
```
根據 Master Theorem：
```python
O(n log n)
```
但最壞情況：
```python
1
 \
  2
   \
    3
     \
      4
```
每次：
```python
index -> O(n)
slice -> O(n)
```
而且遞迴：
```python
n + (n-1) + (n-2) + ...
```
所以：
```python
O(n²)
```
### 空間複雜度

兩部分：

#### 遞迴棧

平衡樹：O(log n)

退化樹：O(n)

#### Slicing

例如：
```python
preorder[1:mid+1]
```
會建立新 list。

總共會複製很多元素。

最壞情況：
```python
n + (n-1) + (n-2) + ... = O(n²)
```
額外記憶體。

所以這個版本：

| Complexity | Value            |
| ---------- | ---------------- |
| Time       | O(n²) worst case |
| Space      | O(n²) worst case |
