# 🆚 Heap vs Stack 資料結構差異比較

---

## 📖 定義說明 | What Are They?

### 🏗️ Heap（堆積）

**EN**  
A heap is a tree-based data structure that satisfies the heap property:
- In a **min-heap**, the parent node is less than or equal to its children.
- In a **max-heap**, the parent node is greater than or equal to its children.

Python supports **min-heap** by default using the `heapq` module.

**ZH**  
Heap 是一種以**完全二元樹**為基礎的資料結構：
- **最小堆（min-heap）**：每個父節點都小於等於子節點
- **最大堆（max-heap）**：每個父節點都大於等於子節點

Python 中可用 `heapq` 模組實作 min-heap。

---

### 📚 Stack（堆疊）

**EN**  
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.  
You can only insert and remove elements from the top.

**ZH**  
Stack 是一種**線性結構**，遵循「後進先出（LIFO）」原則：  
只能從頂端新增（push）或刪除（pop）元素。

---

## 🆚 Heap vs Stack 差異比較
| 項目           | **Heap（堆積）**            | **Stack（堆疊）**                   |
| ------------ | ----------------------- | ------------------------------- |
| 📚 資料結構類型    | 樹狀結構（通常是二元樹）            | 線性結構（先進後出 LIFO）                 |
| 🔼 存取順序      | 依 **大小順序** 優先處理（最小/最大）  | **最後放進的先拿出（Last In First Out）** |
| 🔍 主要應用場景    | 優先佇列、Top K、排程系統         | 遞迴、歷史記錄、字元比對、括號配對等              |
| 🔧 Python 工具 | `heapq`（min-heap，非內建類別） | `list` + `.append()` / `.pop()` |
| ⌛ 時間複雜度      | 插入/刪除：O(log n)，查堆頂：O(1) | 插入/刪除：O(1)                      |
| 🧠 特點        | 自動幫你維持最小（或最大）順序         | 只處理最新加入的資料                      |

---

### 🎯 舉例
🔹 Stack（堆疊）例子：
```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 輸出 3（最後進先出）
```
#### 📦 Stack 視覺圖（LIFO 結構）
```diff
Stack（後進先出）

  ↑ Top
+-------+
|   3   |  ← 最後放進 → 最先取出
+-------+
|   2   |
+-------+
|   1   |
+-------+
↓ Bottom

操作：
- push(4) ⇒ 加到頂部
- pop()   ⇒ 拿出 3（頂部）
```

特點：
- 線性結構

- 操作：push() / pop()

- 適合模擬呼叫堆疊、括號比對、DFS 遞迴等場景

---

🔹 Heap（堆積）例子：
```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 輸出 1（最小值優先）
```

#### 🏗️ Min Heap 視覺圖（二元樹結構）
```markdown
Min-Heap（二元堆，最小值在頂部）

        1
       / \
     3     5
    / \   /
   4   8  9

- 每個節點都 ≤ 子節點
- 堆頂 heap[0] 是最小的（在 Python 中）

操作：
- heappush(2) ⇒ 插入並重排
- heappop()   ⇒ 拿出 1（最小值），並重新維持堆性質
```
特點：
- 樹狀結構

- 每次操作維持「堆的順序性」

- 適合做 Top K、優先隊列、時間排序任務等問題

---

## 🆚 結構比較小結
| 比較項目 | Stack       | Heap               |
| ---- | ----------- | ------------------ |
| 結構類型 | 線性（list）    | 樹狀（二元堆）            |
| 存取順序 | 最後進先出（LIFO） | 最小（或最大）優先          |
| 堆頂是？ | 最新加入的元素     | 最小（或最大）的元素         |
| 用途   | 括號配對、遞迴、回溯等 | Top K、優先順序處理、最小值查找 |

---

## 🧠 關鍵差異比較 | Key Differences
| Feature 特性 | Heap（堆積）       | Stack（堆疊）                   |
| ---------- | -------------- | --------------------------- |
| 結構         | 樹狀結構（完全二元樹）    | 線性結構（列表）                    |
| 存取順序       | 根據值大小（最小/最大優先） | 後進先出（Last-In-First-Out）     |
| 使用情境       | Top K、優先佇列、排程  | 括號配對、遞迴、歷史記錄、回溯等            |
| Python 工具  | `heapq` 模組     | list + `append()` / `pop()` |
| 插入/刪除效率    | O(log n)       | O(1)                        |
| 查找重點       | 最小（或最大）元素      | 最近加入的元素                     |

---

## ✅ 簡單記法
- Stack 是像「碗堆」，最後放上去的碗會最先拿出來

- Heap 是像「選最小值出來的機器」，每次都會幫你找出最小的（或最大的）

## 🧠 什麼時候用哪一個？
| 需求                | 適合資料結構 |
| ----------------- | ------ |
| 需要處理「最大 / 最小」值    | Heap   |
| 需要倒序處理資料          | Stack  |
| 實作 DFS、括號配對、撤銷操作  | Stack  |
| 實作 Top K、優先處理某些項目 | Heap   |

## 🏁 小結 | Summary
- Heap 適合處理 值的大小排序與優先性

- Stack 適合處理 歷史順序與後進先出的流程

- 兩者結構、用途與操作方式完全不同，但都在演算法中扮演重要角色

