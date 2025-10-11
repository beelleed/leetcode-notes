# 📊 LeetCode 295 — Find Median from Data Stream / 資料流中位數
🔗 [題目連結](https://leetcode.com/problems/unique-paths/)

---

## 📄 題目說明 | Problem Description

**中文**：設計一個資料結構 `MedianFinder`，支援兩種操作：

- `addNum(int num)`：將數字 `num` 新加入資料流  
- `findMedian()`：回傳目前資料流中的中位數（若元素數量為偶數，回傳兩中間值的平均）

要求：在動態資料流中維持中位數的查詢與插入效率。

**English**：Design a data structure `MedianFinder` with two operations:

- `addNum(int num)`: add the integer `num` into the data stream  
- `findMedian()`: return the median of all elements so far (if the number of elements is even, return the average of the two middle values)

The data structure should allow efficient insertion and median retrieval in a dynamic stream.

### Examples
- Example 1:

    - Input
        - ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]

        - [[], [1], [2], [], [3], []]
    
    - Output
        [null, null, null, 1.5, null, 2.0]

    - Explanation
        - MedianFinder medianFinder = new MedianFinder();
        - medianFinder.addNum(1);    // arr = [1]
        - medianFinder.addNum(2);    // arr = [1, 2]
        - medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        - medianFinder.addNum(3);    // arr[1, 2, 3]
        - medianFinder.findMedian(); // return 2.0
 

---

## 🧠 解法思路 | Solution Idea

維持中位數最常見與有效的方法是用 **兩個堆（heaps）**：

- 一個最大堆（max‑heap）：保存較小的一半元素  
- 一個最小堆（min‑heap）：保存較大的一半元素  

要保持以下不變量（invariant）：

1. `max_heap.size()` 要麼等於 `min_heap.size()`，要麼多 1 個（讓較小半部分可以多一個，在奇數個元素時給中位數）  
2. 所有 `max_heap` 的元素 ≤ 所有 `min_heap` 的元素  

插入新數字 `num` 的流程：

1. 若 `max_heap` 為空或 `num` ≤ max_heap 的頂點，就先推入 `max_heap`，否則推入 `min_heap`  
2. 平衡兩個堆的大小：如果一邊比另一邊多超過 1，就把頂端元素從那邊彈出到另一邊  
3. 查找中位數時，如果兩堆大小相同 → 中位數 = (頂端 max_heap + 頂端 min_heap) / 2；否則中位數就是那個比較大的堆的頂端  

這樣 `addNum` 是 O(\log n)，`findMedian` 是 O(1)。

---

## 💻 Python 程式碼

```python
import heapq

class MedianFinder:
    def __init__(self):
        # 在 Python 用 heapq 實現最小堆，對於最大堆我們會存負值
        self.max_heap = []  # 存較小一半，用負值模擬 max-heap
        self.min_heap = []  # 存較大一半，直接用 min-heap

    def addNum(self, num: int) -> None:
        # 若 max_heap 為空或 num 小於等於 max_heap 頂端，放入 max_heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 平衡兩堆：如果 max_heap 太少，從 min_heap 移一個過來
        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        # 如果 max_heap 比 min_heap 多超過一個，移一個到 min_heap
        elif len(self.max_heap) - len(self.min_heap) > 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return float(-self.max_heap[0])
```

### 📦 類別與初始化
```python
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 存較小的一半，用負值模擬最大堆
        self.min_heap = []  # 存較大的一半，Python 預設是最小堆
```
- max_heap：記錄「較小」的一半數字，為了模擬最大堆，我們將數值取負放進 min-heap。

- min_heap：記錄「較大」的一半數字，用 Python 預設的 min-heap 即可。

- max_heap 用來存 lower half（小的那一批），我們要能快速拿到這批中的「最大值」——因為那就是可能的中位數邊界。max_heap 的頂就是這批較小數字的最大者。

- min_heap 用來存 upper half（大的那一批），我們要快速拿到這批的最小值——因為那是另一個可能的中位數邊界。

### ➕ 新增數字：addNum
```python
def addNum(self, num: int) -> None:
    if not self.max_heap or num <= -self.max_heap[0]:
        heapq.heappush(self.max_heap, -num)
    else:
        heapq.heappush(self.min_heap, num)
```
- 若目前 max_heap 是空的，或 num 比 max_heap 的最大值還小，則放進 max_heap（較小數）。

- 否則放進 min_heap（較大數）。

### ✨ 平衡兩堆大小
```python
if len(self.max_heap) < len(self.min_heap):
    val = heapq.heappop(self.min_heap)
    heapq.heappush(self.max_heap, -val)
elif len(self.max_heap) - len(self.min_heap) > 1:
    val = -heapq.heappop(self.max_heap)
    heapq.heappush(self.min_heap, val)
```
- 目標：max_heap 的長度應該永遠比 min_heap 多 不超過 1。

- 如果 min_heap 多，就把最小值移到 max_heap。

- 如果 max_heap 多超過 1，就把最大值移到 min_heap。

### 📐 取得中位數：findMedian
```python
def findMedian(self) -> float:
    if len(self.max_heap) == len(self.min_heap):
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
    else:
        return float(-self.max_heap[0])
```
- 若兩堆一樣長，代表總長度是偶數 → 中位數為中間兩數平均。

- 否則（奇數），中位數為 max_heap 的頂端（較小一半的最大值）。

### ❓ 為什麼 -self.max_heap[0] 是 max_heap 的「真正頂端值」？

- 我們把數字存入 max_heap 時用 -num（負值）

- 例如插入值 5 → 存入 -5

- Python 的 min-heap 會讓最小的數值浮到堆頂，對負值而言，最小負值就是最大的正值

- 所以堆頂是最小的負數，取反後就是原本最大的正數

- 因此 -self.max_heap[0] 才是這堆中真正的最大值

---

## 📘 範例 | Examples
依序插入 [5, 2, 3, 4]
```python
finder = MedianFinder()
finder.addNum(5)
finder.addNum(2)
finder.addNum(3)
finder.addNum(4)
finder.findMedian()
```
### 第一步：addNum(5)

- max_heap 是空的，加入 -5（模擬最大堆）

- max_heap = [-5]

- min_heap = []

➡️ 中位數是 5

### 第二步：addNum(2)

- 2 <= 5，所以也加入 max_heap（存成 -2）

- max_heap = [-5, -2]（實際是 [5, 2]）

➡️ 平衡：max_heap 太多 → 把最大值 -(-5)=5 移到 min_heap

- max_heap = [-2] → [2]

- min_heap = [5]

➡️ 中位數是 (-max_heap[0] + min_heap[0]) / 2 = (2 + 5)/2 = 3.5

### 第三步：addNum(3)

- 3 > 2 → 放入 min_heap

- min_heap = [3, 5]

➡️ 平衡：min_heap 太多 → 把 3 移回 max_heap

- max_heap = [-3, -2] → [3, 2]

- min_heap = [5]

➡️ 中位數是 -(-3) = 3

### 第四步：addNum(4)

- 4 > 3 → 放入 min_heap

- min_heap = [4, 5]

➡️ 不用平衡，兩邊長度相同

➡️ 中位數是 (3 + 4)/2 = 3.5

### 📌 最終結構：

- max_heap：[-3, -2]（實際值是 [3, 2]）

- min_heap：[4, 5]

- 中位數：(3 + 4) / 2 = 3.5

---

## ⏱ 時間與空間複雜度 | Complexity
| 操作             | 複雜度        | 解釋                                 |
| -------------- | ---------- | ---------------------------------- |
| addNum(num)  | O(log n) | 插入新數字到 heap，heap 的插入與移除都是 log n。 |
| findMedian() | O(1)    | 只讀取兩個 heap 的頂部元素 → 常數時間操作。         |

- heapq.heappush() 和 heapq.heappop() 都是 O(log n)，因為 heap 是一個平衡的二元樹結構。

- 所以，每次新增數字最多會做 2 次 push/pop，總體仍是 O(log n)。

---

## 🧠 學到的東西 | What I Learned

- 「維護兩個堆」是求即時中位數的經典做法。

- 使用最大堆需透過負值模擬，這是 Python 中常見技巧。

- 平衡邏輯需特別注意避免偏移，並確保正確取得中位數。