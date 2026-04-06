# 🌳 LeetCode 112 — Path Sum / 路徑總和

🔗 [題目連結](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 給一棵二元樹 root 和一個整數 targetSum，判斷是否存在一條「從 root 到 leaf」的路徑，使得所有節點值的總和等於 targetSum。

### English:

- Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that the sum equals targetSum.

---

## 🧠 核心觀念 | Key Insight

- 一定要是 root → leaf 的路徑

- 不是：

    - 任意節點 ❌
    - 中間停下來 ❌

- 是：

    - 「走到葉節點，且總和剛好等於 target」

---

## 🧠 解題思路 | Solution Idea
- 方法：DFS（Top-down）

- 跟 236 最大差別：

| 題目  | 思維                 |
| --- | ------------------ |
| 236 | bottom-up（往上回傳）    |
| 112 | 🔥 top-down（往下帶資訊） |

---

## 🧩 定義 dfs
```python
dfs(node, current_sum)
```
- current_sum = 從 root 走到這個 node 的總和

---

## 🧩 遞迴流程
### 1️⃣ Base case：空節點
```python
if not node:
    return False
```
- 沒有路徑 → 失敗

### 2️⃣ 更新 sum
```python
current_sum += node.val
```
- 代表走到這個 node

### 3️⃣ 判斷 leaf
```python
if node.left is None and node.right is None:
    return current_sum == targetSum
```
- 只有在「葉節點」才可以判斷成功

### 4️⃣ 往下搜尋
```python
left = dfs(node.left, current_sum)
right = dfs(node.right, current_sum)
```

### 5️⃣ 回傳結果
```python
return left or right
```

---

## 🔍 重點拆解
- return left or right 是什麼意思？

    - left / right 是 boolean：

| 變數    | 意思        |
| ----- | --------- |
| left  | 左邊有沒有成功路徑 |
| right | 右邊有沒有成功路徑 |

### 🧩 三種情況
| left  | right | 結果    |
| ----- | ----- | ----- |
| True  | False | True  |
| False | True  | True  |
| False | False | False |

- 所以：

    - 「只要有一條路成功，就回 True」

### 🧠 等價寫法
```python
if left:
    return True
if right:
    return True
return False
```
👉 =
```python
return left or right
```

---

## 💻 程式碼 | Code (Python)
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val

            # leaf 判斷（關鍵）
            if node.left is None and node.right is None:
                return current_sum == targetSum

            left = dfs(node.left, current_sum)
            right = dfs(node.right, current_sum)

            return left or right

        return dfs(root, 0)
```

---

## 🧪 範例
```python
    5
   / \
  4   8
 /
11
```
target = 20

- 路徑： 5 → 4 → 11 = 20 ✅

- dfs 過程：
    - 到 5 → sum = 5
    - 到 4 → sum = 9
    - 到 11 → sum = 20（leaf）
- return True

---

## 常見錯誤
### ❌ 1. 忘記 leaf 判斷
```python
if current_sum == targetSum:
    return True
```
👉 ❌ 錯（中間節點會誤判）

### ❌ 2. 把 sum 重設
```python
dfs(node.left, 0)
```
👉 ❌ 會失去累積

### ❌ 3. leaf 判斷放太後面

👉 ❌ 會多跑 recursion

### ❌ 4. 沒有 return dfs
```python
dfs(root, 0)
return True
```
👉 ❌ 永遠 True

---

## ⏱️ 複雜度分析 | Complexity
- 時間：O(N)
- 空間：O(H)

---

## ✍️ 我學到的東西 | What I Learned
- top-down：帶著狀態往下走（current_sum）
- leaf 判斷一定要先做
- return left or right = 任一成功即可
- recursion 不只是寫 code，是在「傳遞資訊」