# 🟦 LeetCode 703 — Kth Largest Element in a Stream | 第 K 大元素（資料流）

🔗 [題目連結](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

---

## 📘 題目說明 | Problem Description
### 中文

- 設計一個類別 KthLargest，用來動態維護「目前所有輸入數字中的 第 k 大元素」。

    - 初始化時會給：

        - 一個整數 k

        - 一個整數陣列 nums

    - 之後會不斷呼叫 add(val)：

        - 把 val 加進資料流

        - 回傳「目前第 k 大的數字」

- 📌 注意：

    - 不是第 k 個加入的

    - 是排序後的第 k 大

### English

- Design a class to find the k-th largest element in a stream.
Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

### Examples
- Example 1:

    - Input: 

        ["KthLargest", "add", "add", "add", "add", "add"]
        
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    - Output: [null, 4, 5, 5, 8, 8]

    - Explanation:

        - KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        - kthLargest.add(3); // return 4
        - kthLargest.add(5); // return 5
        - kthLargest.add(10); // return 5
        - kthLargest.add(9); // return 8
        - kthLargest.add(4); // return 8

- Example 2:

    - Input:

        ["KthLargest", "add", "add", "add", "add"]
        
        [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

    - Output: [null, 7, 7, 7, 8]

    - Explanation:

        - KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
        - kthLargest.add(2); // return 7
        - kthLargest.add(10); // return 7
        - kthLargest.add(9); // return 7
        - kthLargest.add(9); // return 8

---

## 🧠 關鍵觀察 | Key Insight
- ❓ 為什麼不能每次都排序？

    - add() 可能被呼叫很多次

    - 每次排序是 O(n log n) → 太慢

- ✅ 真正重要的事

    - 我們 不需要知道所有元素的完整排序結果
    - 只需要知道「前 k 大裡，最小的是誰」

---

## 🧠 核心解法 | Core Idea
- 使用「大小固定為 k 的 min-heap」

    - heap 中只存「目前最大的 k 個數」

    - heap 裡最小的那個（heap[0]）
        - 👉 就是第 k 大

- 為什麼是 min-heap？

    - heap 裡有 k 個數

    - 其中最小的那個前面有 k−1 個更大的

    - 所以它就是第 k 大

---

## 🧩 解題策略 | Solution Strategy
- 初始化 __init__

    1. 建立一個 min-heap

    2. 將 nums 一個一個放入 heap

    3. 若 heap size 超過 k，就 pop 最小的

        - 👉 結果：heap 裡只剩最大的 k 個數

- add(val)

    1. 把 val 加進 heap

    2. 若 heap size > k，pop 最小的

    3. 回傳 heap[0]

---

## 💻 Python 程式碼
```python
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k                  # 物件狀態：第 k 大
        self.min_heap = []          # 物件狀態：min-heap

        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
```
### 🧾 程式碼逐段解釋 | Code Walkthrough
為什麼要 self.k = k？
```python
self.k = k
```

- k 之後會在 add() 用到

- 代表「物件必須記住的狀態」

- 跨 method 使用 → 一定要存成 self

為什麼 heap size 要限制在 k？
```python
if len(self.min_heap) > self.k:
    heapq.heappop(self.min_heap)
```

- pop 掉的是「最小的」

- 等於丟掉「不可能成為第 k 大的元素」

- 保證 heap 裡永遠是「最大的 k 個數」

為什麼回傳 heap[0]？
```python
return self.min_heap[0]
```

- 因為 invariant（不變條件）是：

    - heap 裡 = 目前最大的 k 個數
    - heap[0] = 這 k 個數中最小的 = 第 k 大

### __init__：初始化（把 nums 處理成「只保留最大的 k 個」）
#### 建 heap 與存 k
```python
self.min_heap = []
self.k = k
```

- self.min_heap：要跨 __init__ 和 add() 使用，所以一定要用 self

- self.k：add() 也會用到 k，所以 k 不是區域變數，要存成物件狀態

#### 把 nums 一個個加進 heap
```python
for num in nums:
    heapq.heappush(self.min_heap, num)
```

- heappush 會把數字放進 min-heap，並維持 heap 的性質：

    - heap[0] 永遠是最小的

#### 如果 heap 超過 k 個，就 pop 掉最小的
```python
if len(self.min_heap) > self.k:
    heapq.heappop(self.min_heap)
```

- 這行是整題最關鍵的「維護規則」（invariant）：

    - heap 永遠只保留 k 個元素，且是目前「最大的 k 個」

- 因為每當多塞了一個進來：

    - 最小的那個一定是「不夠大」的（在最大 k 個之外）

    - 所以 pop 掉它

### add(val)：每來一個新數字就更新 heap，回傳第 k 大
#### 先把 val 丟進 heap
```python
heapq.heappush(self.min_heap, val)
```
#### 如果超過 k，就 pop 最小的
```python
if len(self.min_heap) > self.k:
    heapq.heappop(self.min_heap)
```

- 這保證 heap 仍然只保留最大的 k 個數。
#### 回傳 heap[0]
```python
return self.min_heap[0]
```

- 因為 heap 裡是「最大的 k 個數」，其中最小的就是第 k 大。

---

## 🧪 範例 | Example

- 使用題目常見例子：
```text
k = 3
nums = [4, 5, 8, 2]
```
### ✅ 初始化階段：跑 init
#### 初始：
```text
min_heap = []
k = 3
```
#### num = 4

push 4
```text
heap = [4]
len=1 <= 3 → 不 pop
```
#### num = 5

push 5
```text
heap = [4, 5]   # min-heap 的最小仍是 4
len=2 <= 3 → 不 pop
```
#### num = 8

push 8
```text
heap = [4, 5, 8]
len=3 == 3 → 不 pop
```
#### num = 2

push 2
```text
heap = [2, 4, 8, 5]
len=4 > 3 → pop 最小
pop 2
heap = [4, 5, 8]
```
#### 重要補充：其實 [2,4,5,8] 也合法，只是不一定會得到

[2,4,5,8] 畫成 tree：
```text
      2
     / \
    4   5
   /
  8
```
- 也滿足 heap 規則，所以也是合法 heap。
- 但 heapq 的 push/pop 過程會產生其中一種合法形狀，不會強迫變成排序。

### 🔹 Step 1：取出最小值（2）

- 這是回傳值，但 heap 內部還要整理。

### 🔹 Step 2：用「最後一個元素」補到 root

- 把 5 移到最前面：
```python
heap = [5, 4, 8]
```

（注意：2 已經被移除了）

### 🔹 Step 3：向下調整（sift down）

現在檢查 heap 性質：
```text
        5
       / \
      4   8
```

- 5 > 4 ❌（違反 min-heap）

- 所以交換 5 和 4

交換後：
```python
heap = [4, 5, 8]
```
### 🔹 Step 4：繼續檢查

- 5 沒有子節點

- heap 性質恢復

✅ 最終結果：
```python
heap = [4, 5, 8]
```
#### 為什麼不是 [4, 8, 5]？
```python
[4, 8, 5]
```
畫成樹：
```text
        4
       / \
      8   5
```

- 這是合法 heap，沒錯。

- 但 heapq 的內部實作選擇了另一條調整路徑，
最後得到的是：
```python
[4, 5, 8]
```
👉 heap 的最終樣子不唯一，只要滿足規則就行。

因為：
✅ 初始化結束後：
```text
heap = [4, 5, 8]
代表目前最大的 3 個數是 {4,5,8}
第 3 大 = heap[0] = 4
```

---

### ✅ add(val) trace
#### add(3)
push 3
```text
heap = [3, 4, 8, 5]
len=4 > 3 → pop 最小
pop 3
heap = [4, 5, 8]
return heap[0] = 4
```

- 🔎 目前所有數：[4,5,8,2,3]
- 排序：[8,5,4,3,2]
- 第 3 大 = 4 ✅

#### add(10)
push 10
```text
heap = [4, 5, 8, 10]
len=4 > 3 → pop 最小
pop 4
heap = [5, 10, 8]
return heap[0] = 5
```

- 🔎 目前所有數：[4,5,8,2,3,10]
- 排序：[10,8,5,4,3,2]
- 第 3 大 = 5 ✅

#### add(9)

push 9
```text
heap = [5, 9, 8, 10]
len=4 > 3 → pop 5
heap = [8, 9, 10]
return 8
```

---

## ⏱️ 時間與空間複雜度 | Complexity Analysis
- Time Complexity

    - add()：

        - push + pop → O(log k)

    - 初始化：O(n log k)

- Space Complexity

    - heap 大小固定為 k → O(k)

---

## ✍️ 我學到的重點 | What I Learned

- 第 k 大 ≠ 排序第 k 個

- 只要「前 k 大」即可

- min-heap + 固定大小 k 是關鍵套路

- self.xxx 代表「物件狀態」，不是隨便加的

---

## ✅ 一句話總結

We maintain a min-heap of size k containing the k largest elements seen so far.
The smallest element in the heap is always the k-th largest.