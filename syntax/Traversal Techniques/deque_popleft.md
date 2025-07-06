# 🔧 Python `deque.popleft()` 用法筆記

## 📌 函式簡介 | Function Overview

```python
from collections import deque

queue = deque()
queue.append(1)
x = queue.popleft()
```
- deque.popleft() 是 Python collections.deque 提供的方法

- 用來「從左側（前端）移除並回傳一個元素」

- 符合 先進先出（FIFO） 的操作邏輯

---

## ✅ 典型用途 | Common Use Cases

### 🔁 1. 廣度優先搜尋（BFS）
```python
from collections import deque

queue = deque([(root.left, root.right)])
while queue:
    t1, t2 = queue.popleft()  # 取出當前節點配對
    ...
```
- 適用於 BFS 樹、圖的層序遍歷

- 每次從「佇列左側」取出資料

### 🔁 2. 時間序列或滑動視窗處理
```python
from collections import deque

window = deque([1, 2, 3])
window.popleft()  # 移除最舊數值
```

---

## ❗ 為什麼不用 list.pop(0)？
- list.pop(0) 是 O(n) 時間複雜度（需搬移所有元素）

- deque.popleft() 是 O(1)，效率更高！

---

## ⚠️ 注意事項
- 使用前需 from collections import deque

- 若佇列為空時使用 popleft() → 會拋出 IndexError

---

## 🧠 小結 | Summary
| 功能    | 描述                  |
| ----- | ------------------- |
| 方法名稱  | `popleft()`         |
| 所屬類別  | `collections.deque` |
| 操作行為  | 從左邊彈出一個元素           |
| 典型用途  | BFS、滑動視窗、FIFO結構     |
| 時間複雜度 | O(1)                |
