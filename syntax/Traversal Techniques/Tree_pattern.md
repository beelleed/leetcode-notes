# 🎯 Pattern：BST + inorder + prev
## 🧩 結構（幾乎固定）
```python
def dfs(node):
    if not node:
        return
    
    dfs(node.left)
    
    # ⭐ 在這裡做事（關鍵）
    
    dfs(node.right)
```

### 📊 同一個 pattern，不同題目
- 230（Kth Smallest）
```python
count += 1
if count == k:
    ans = node.val
```
- 98（Validate BST）
```python
if prev is not None and node.val <= prev:
    return False
prev = node.val
```
-  530 / 783（Min Difference）
```python
if prev is not None:
    ans = min(ans, node.val - prev)
prev = node.val
```

---

## 🔥 Tree Bottom-up 模板
```python
def dfs(node):
    if not node:
        return None
    
    left = dfs(node.left)
    right = dfs(node.right)

    # ⭐ 在這裡做決策
    if 條件:
        return something

    return something
```
### 🎯 特徵
- 問「某個 node 的答案是什麼」
- 不需要一路帶狀態
- 用 child 結果來決定 parent

---

## 🔥 Top-down（往下帶資訊）
```python
def dfs(node, state):
    if not node:
        return False  # 或 return
    
    # 更新狀態
    state = ...

    # ⭐ 通常在這裡判斷（很重要）
    if leaf:
        return 條件

    left = dfs(node.left, state)
    right = dfs(node.right, state)

    return left or right
```
### 🎯 特徵
- 有「累積資訊」（sum / path / string）
- 要判斷 root → leaf
- 常用 boolean 或 list

### ⚠️ 常見錯誤
- 忘記 leaf 判斷
- state 被重設
- return 寫錯（沒寫 left or right）

---

## Backtracking（收集所有結果）
```python
def dfs(node, path):
    if not node:
        return
    
    path.append(node.val)

    if leaf:
        result.append(path.copy())

    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()  # ⭐ 關鍵
```
### 🎯 特徵
- 要「全部答案」
- 用 list
- 一定有 pop()

---

## BFS（層序）
```python
from collections import deque

queue = deque([root])

while queue:
    node = queue.popleft()

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
```
### 🎯 特徵
- 一層一層
- queue
- 常搭配 level size
