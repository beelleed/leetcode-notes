# 📍 LeetCode 543 — Diameter of Binary Tree | 二元樹直徑

🔗 [題目連結] (https://leetcode.com/problems/diameter-of-binary-tree/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給你一棵二元樹

- 直徑（diameter） 定義為： 任意兩個節點之間「最長路徑上的邊數」

- 這條路徑 不一定經過 root

### English

The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

### Examples
- Example 1:

    ![](../images/543_diamtree.jpg)

    - Input: root = [1,2,3,4,5]
    - Output: 3
    - Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
- Example 2:

    - Input: root = [1,2]
    - Output: 1

---

## 🧠 解題思路 | Solution Idea
- 關鍵觀念一句話

    - 直徑 = 某個節點的「左子樹高度 + 右子樹高度」的最大值

- 也就是說：

    - 對每一個節點

    - 想像「路徑從左子樹某點 → 經過這個節點 → 右子樹某點」

    - 那條路徑的長度就是： left_height + right_height

    - 我們要找的是：👉 所有節點中，最大的那一次

- 🔑 為什麼要用 DFS（後序遍歷）

    - 因為：

        - 要先知道 左、右子樹高度

        - 才能算「經過這個節點的直徑」

    - 👉 所以 traversal 順序是：postorder（左右中）

---

## 💻 程式碼實作 | Code
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            # 更新直徑（邊數）
            self.ans = max(self.ans, left + right)

            # 回傳高度
            return 1 + max(left, right)

        depth(root)
        return self.ans
```

### 1️⃣ 全域變數 self.ans
```python
self.ans = 0
```

- 用來記錄目前找到的 最大直徑

- 因為 DFS 會經過所有節點

- 每個節點都可能成為「直徑的中繼點」

### 2️⃣ depth(node) 的定義
```python
def depth(node):
```

- 這個函式 同時扮演兩個角色：

| 功能  | 說明                 |
| --- | ------------------ |
| 回傳值 | 以 `node` 為根的子樹高度   |
| 副作用 | 嘗試更新全域的 `self.ans` |

### 3️⃣ Base case：空節點
```python
if not node:
    return 0
```

- 空樹高度定義為 0

- 不影響直徑計算

### 4️⃣ 計算左右子樹高度
```python
left = depth(node.left)
right = depth(node.right)
```

- 一定是先算 left、right

- 所以 traversal 是 postorder（左右中）

### 5️⃣ 更新直徑（整題最重要的一行）
```python
self.ans = max(self.ans, left + right)
```

- 這一行的意思是：

    - left：左子樹高度（邊數角度看）

    - right：右子樹高度

    - left + right：經過這個節點的最長路徑（邊數）

- 我們對「每一個節點」都試一次，保留最大值。

- ⚠️ 注意：

    - 題目要的是「邊數」

    - 而 depth 回傳的是「高度（節點數）」

    - 剛好 left + right 就是邊數，不用再減 1

### 6️⃣ 回傳高度給父節點
```python
return 1 + max(left, right)
```

- 父節點只關心「較深的那一邊」

- 所以高度 = 自己 + max(left, right)

### 7️⃣ 啟動 DFS 並回傳答案
```python
depth(root)
return self.ans
```

- depth(root) 只是為了跑完整棵樹

- 真正答案存在 self.ans

---

## 🧪 範例流程 | Example Walkthrough
- Example
```text
       1
      / \
     2   3
    / \
   4   5
```
- DFS 過程（由下往上）

    - node 4 → left=0, right=0 → ans=0

    - node 5 → left=0, right=0 → ans=0

    - node 2 → left=1, right=1 → ans=2

    - node 3 → left=0, right=0 → ans=2

    - node 1 → left=2, right=1 → ans=3 ✅

- Output：
```text
3
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n)

    - 每個節點只走一次

- 空間複雜度：O(h)

    - 遞迴呼叫深度（最壞為樹高）

---

## ✍️ 我學到的東西 | What I Learned

- 很多樹題的套路是：

    - DFS 回傳一個值 + 順便更新全域答案

- 這題和：

    - 104 Maximum Depth

    - 110 Balanced Binary Tree 👉 是同一個「高度家族」

---    

## 🧠 一句話總結

I use DFS to compute the height of each subtree and update the diameter at each node as the sum of its left and right subtree heights.