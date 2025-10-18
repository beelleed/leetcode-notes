# 🌳 LeetCode 297 – Serialize and Deserialize Binary Tree
🔗 題目連結：[https://leetcode.com/problems/serialize-and-deserialize-binary-tree/](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

---

## 📄 題目說明 | Problem Description

**中文**：

給定一棵二元樹，需要實作兩個方法：`serialize(root)` 把樹轉成字串；`deserialize(data)` 把那個字串轉回原本的樹結構。序列化格式可以自己決定，但要能完整還原。

**English**: 

Given a binary tree, implement two functions: `serialize(root)` to convert the tree into a string, and `deserialize(data)` to reconstruct the exact same binary tree from that string. You can choose any format as long as it preserves structure.

### Examples
- Example 1:

![](../images/297_serdeser1.jpg)

    Input: root = [1,2,3,null,null,4,5]
 
    Output: [1,2,3,null,null,4,5]

- Example 2:

    - Input: root = []
    - Output: []

---

## 🧠 解題思路 | Solution Idea

兩種常見方法：

1. **Level‑order (BFS) 方法**（層級遍歷）：  
   - 在序列化時，以 BFS 遍歷所有節點，包括 `None`（空節點）作為標記。  
   - 在反序列化時，以同樣的順序讀取資料，重建每個父節點的左子與右子。

2. **Pre-order 或 Post-order DFS 方法**（遞迴）：  
   - 序列化時用遞迴先序遍歷（pre-order），空節點用特殊標記（如 `#` 或 `null`）表示。  
   - deserialize 用同樣格式的遞迴方法／iterator 重建樹。

選擇 BFS 或 DFS 都可以，只要一致：serialize 和 deserialize 必須配對。

| 方法 | 優點 | 缺點 |
|---|-----|------|
| **Preorder DFS**（遞迴先序遍歷 + null 標記） | 程式簡短清楚；容易寫白板／口頭解釋；結構緊湊只標記 null 必要位置 | 字串可能有很多 null；遞迴深度可能有 stack 深度問題（極度偏斜樹） |
| **Level‑order BFS**（層序遍歷 + 包括 null 節點） | 視覺直觀；易於理解每層節點關係；在反序列化時可以用 queue 保存 parent-child 關係 | 字串可能比較長；需要處理很多 null；操作稍微複雜一點 |

---

## 💻 程式碼實作 | Code

### ✅ 方法一：Preorder DFS 版本

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    NULL = "#"

    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                vals.append(Codec.NULL)
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        parts = data.split(",")
        self.index = 0
        def dfs() -> Optional[TreeNode]:
            val = parts[self.index]
            self.index += 1
            if val == Codec.NULL:
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
```
```python
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right
```
- 定義基本的二元樹節點：每個節點有值 val、左節點 left、右節點 right。
```python
class Codec:
    NULL = "#"

    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                vals.append(Codec.NULL)
                return 
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)
```
✏️ 解析：

- NULL = "#" 是一個常數，用來標記空節點（None）。這樣反序列化時能知道哪裡該插 None。

- serialize 接受一棵樹的根節點 root。

- vals = [] 用來收集 DFS 遍歷過程的每個節點（包括空節點）的標記／值。

- dfs(node) 是遞迴函式：

    1. 如果 node 是 None，就把 "#" 加到 vals，然後 return（不繼續深入這支支線）。

    2. 否則，把這個節點的值 node.val 轉成字串放入 vals。

    3. 遞迴呼叫 dfs(node.left)，處理左子樹。

    4. 遞迴呼叫 dfs(node.right)，處理右子樹。

- dfs(root)：從根節點開始整棵樹的 DFS。

- ",".join(vals)：把 vals 裡面的元素用逗號串起來成為一個字串。這就是最終的序列化結果。例如：
    ```arduino
    "1,2,#,#,3,4,#,#,5,#,#"
    ```
```python
def deserialize(self, data: str) -> Optional[TreeNode]:
    if not data:
        return None
    parts = data.split(",")
    self.index = 0
    def dfs() - > Optional[TreeNode]:
        val = parts[self.index]
        self.index += 1
        if val == Codec.NULL:
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
```
✏️ 解析：

- 如果 data 是空字串（"" 或者 None 的情況），就直接回傳 None，代表樹也空。

- parts = data.split(",")：把序列化字串切割成一個 list，每個元素是節點值或 "#"。

- self.index = 0：這是一個類屬性，用來追蹤目前讀到 parts 的哪一個位置。因為 DFS 先序遍歷；反序列化時也要按照這個順序「讀值 → 建節點 or 空節點」。

- dfs() 函式：

    1. 讀 parts[self.index] 作為 val，然後 self.index += 1 推進位置。

    2. 如果 val == Codec.NULL（也就是 "#"），代表這是一個空節點，就回傳 None。

    3. 否則，把 val 轉成整數，用 TreeNode(int(val)) 建一個節點。

    4. 遞迴呼叫 dfs() 建這個節點的左子樹（node.left = dfs()）。

    5. 遞迴呼叫 dfs() 建右子樹（node.right = dfs()）。

    6. 回傳這個 node。

- 最後 return dfs()：從最外層的根節點開始還原整棵樹。

---

### 🧪 範例

假設樹為：
```markdown
    1
   / \
  2   3
     / \
    4   5
```
- 序列化結果會是：

    ```arduino
    "1,2,#,#,3,4,#,#,5,#,#"
    ```

還原過程如下：

- index=0：建立 TreeNode(1)

- index=1：建立 TreeNode(2)

- index=2：遇到 #，左子為 None

- index=3：遇到 #，右子為 None → TreeNode(2) 完成

- index=4：建立 TreeNode(3)

- index=5：建立 TreeNode(4)

- index=6、7：都是 # → TreeNode(4) 完成

- index=8：建立 TreeNode(5)

- index=9、10：都是 # → TreeNode(5) 完成

最後還原成與原本完全一致的樹。

---

### 🌀 方法二：BFS (Level‑order) 版本
```python
from collections import deque
from typing import Optional

class CodecBFS:
    NULL = "#"

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node:
                vals.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                vals.append(CodecBFS.NULL)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        parts = data.split(",")
        root = TreeNode(int(parts[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < len(parts):
                left_val = parts[i]
                i += 1
                if left_val != CodecBFS.NULL:
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)
            if i < len(parts):
                right_val = parts[i]
                i += 1
                if right_val != CodecBFS.NULL:
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
        return root
```

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 方法              | 時間複雜度 Time                              | 空間複雜度 Space                                |
| --------------- | --------------------------------------- | ------------------------------------------ |
| DFS 方法 | O(n) — 遍歷每個節點一次 serialize + deserialize | O(n) — recursion stack + 儲存 null 標記 + 字串長度 |
| BFS 方法          | O(n) — 每個節點/enqueue/dequeue 見一次         | O(n) — queue + 字串長度 + 儲存 null              |

---

## ✍️ 我學到了什麼 | What I Learned

- 樹的序列化與反序列化要記得標記空節點，否則結構會遺失

- BFS 跟 DFS 各有優劣：BFS 用於保留整個層級結構直觀；DFS 在實作上更簡潔

- 在序列化 + 反序列化時，一定要保持對應格式一致（標記用什麼、節點與空節點的順序）

- 邊界情況要處理好，如根節點為 null、只有一條分支（偏斜樹）等