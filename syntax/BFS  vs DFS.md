# 🔍 BFS vs DFS 筆記 | BFS vs DFS Study Notes

---

## 📘 什麼是 BFS 和 DFS？| What Are BFS and DFS?

BFS（Breadth-First Search，廣度優先搜尋）與 DFS（Depth-First Search，深度優先搜尋）是遍歷樹或圖的兩種常見方式。

BFS and DFS are two fundamental ways to traverse trees or graphs.

---

## 📌 差異總覽 | Key Differences

| 比較項目 | BFS（廣度優先） | DFS（深度優先） |
|----------|------------------|------------------|
| 遍歷順序 | 一層一層遍歷     | 一條路走到底     |
| 使用結構 | Queue（佇列）    | Stack / 遞迴      |
| 適合問題 | 層數、最短路徑   | 結構、深度、所有路徑 |
| 空間複雜度 | O(n)             | O(h)（h 是樹高） |
| 範例題目 | LeetCode 104（用 queue 算深度） | LeetCode 104（用遞迴算深度） |

---

## 🧠 圖解比較 | Visual Comparison

```markdown
        1
      /   \
     2     3
    / \     \
   4   5     6
```

### 📌 BFS 遍歷順序：
`1 → 2 → 3 → 4 → 5 → 6`

→ 一層一層往下走，先處理所有兄弟節點，再往下一層。

### 📌 DFS 遍歷順序（前序）：
`1 → 2 → 4 → 5 → 3 → 6`

→ 一路往左或右走到底，再回頭處理其他子樹。

---

## 🔧 程式碼比較 | Code Comparison

### ✅ BFS（使用 queue）

```python
from collections import deque

def maxDepth(root):
    if not root:
        return 0
    q = deque([root])
    depth = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        depth += 1
    return depth
``` 

### ✅ DFS（使用遞迴）
```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

## 🎯 什麼時候該用 BFS？DFS？

使用 BFS 的情境：

    - 要找最短路徑（如迷宮問題）

    - 計算某個節點的層數（例如最大深度）

    - 廣播型問題（每層逐步擴散）

使用 DFS 的情境：

    - 要遍歷整棵樹或所有路徑

    - 解決圖中是否有環（cycle）

    - 複雜的巢狀結構或結構搜尋（像括號配對）

---

## ✅ 學到什麼 | What I Learned
- BFS 適合「由淺入深」，逐層探索，常用 queue

- DFS 適合「一路到底」，再回頭處理，常用 stack 或遞迴

- 兩種都會寫才能靈活應對各類資料結構題

- LeetCode 許多題目（如 104, 102, 226）都能同時用 BFS 或 DFS 解