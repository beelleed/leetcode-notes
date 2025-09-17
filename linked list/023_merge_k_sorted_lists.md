# 🔗 LeetCode 23 – Merge k Sorted Lists
🔗 題目連結：[https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## 📄 題目說明 | Problem Description

**中文**：給你 k 個已排序的鏈結串列（linked lists），每個串列中的節點值按升序排列。請把這 k 個串列合併成一個排序好的鏈結串列，並回傳其頭節點。

**English**: Given an array of k sorted linked lists, merge them into one sorted linked list and return its head.

### Examples
- Example 1:

    - Input: lists = [[1,4,5],[1,3,4],[2,6]]
    - Output: [1,1,2,3,4,4,5,6]
    - Explanation: The linked-lists are:

        [
        1->4->5,
        1->3->4,
        2->6
        ]

        merging them into one sorted linked list:

        1->1->2->3->4->4->5->6

- Example 2:

    - Input: lists = []
    - Output: []

- Example 3:

    - Input: lists = [[]]
    - Output: []

---

## 🧠 解題思路 | Solution Idea

有幾種做法，但最常見/效率好的包括：

1. **小根堆／優先佇列（Min-Heap / Priority Queue）方法**  
   - 把每個非空鏈表的頭節點推入小根堆  
   - 重複取出堆中的最小節點，將該節點接到結果串列尾部  
   - 如果該節點有下一個節點，就把下一個節點也推入堆  
   - 直到堆空  

2. **分治法（Divide and Conquer）**  
   - 將 k 個串列兩兩合併，一次合併兩個，重複此過程 → k 個串列合併為 k/2 個，再合併，直到只剩一個  
   - 合併兩個已排序鏈表的成本為 O(n)，透過分治能把總時間降到 O(n log k)

---

## 💻 程式碼實作（Min-Heap 方法）

```python
from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

    # 若要 nodes 可以比較大小，加這 comparator
    def __lt__(self, other: 'ListNode') -> bool:
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 初始化 min-heap，只放非空的頭節點
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, node)

        # dummy 頭節點方便處理
        dummy = ListNode(0)
        current = dummy

        # 當堆還有節點時
        while min_heap:
            smallest_node = heapq.heappop(min_heap)   # 取出最小值節點
            current.next = smallest_node               # 接到結果串列
            current = current.next
            if smallest_node.next:
                heapq.heappush(min_heap, smallest_node.next)  # 推入下一節點

        return dummy.next
```
### 🔍 初始化小根堆
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, node)
```
- 將每個非空鏈表的第一個節點推入 min_heap。

- 這裡 heapq 根據節點值自動排序。
### 🧱 準備 dummy 節點
```python
dummy = ListNode(0)
current = dummy
```
- 建立一個 dummy 頭節點作為結果串列的起點。

- current 指標用來逐步擴展結果鏈表。
### 🔁 處理所有節點
```python
while min_heap:
    smallest_node = heapq.heappop(min_heap)
    current.next = smallest_node
    current = current.next
    if smallest_node.next:
        heapq.heappush(min_heap, smallest_node.next)
```
- 每次從堆中取出最小節點 smallest_node，加到結果鏈結串列。

- 若該節點有下一個節點，就推入堆，保持 heap 的動態性。

- 重複直到堆空，所有節點都處理完。
### ✅ 回傳結果
```python
return dummy.next
```
- 回傳 dummy 的下一個節點，即為合併完成後的排序鏈結串列的頭節點。

---

## 🧪 範例流程

假設有三個已排序的鏈結串列：

- List A: 1 → 4 → 5

- List B: 1 → 3 → 4

- List C: 2 → 6

初始：
```ini
lists = [A (head=1), B (head=1), C (head=2)]
min_heap = [nodeA(1), nodeB(1), nodeC(2)]  # 值分別 1,1,2
```
建立 dummy → None

### 步驟 1：

    - heap pop → 拿到值最小的 node（假設是 A 的頭部節點 1 或 B 的頭部節點 1，任一者）

    - current.next 指向該節點

    - 接著把被取出節點的 next（若存在）推入 heap

    - 更新 current 移動

- 例如拿 A 的 1 → heap 後成 [B(1), C(2), A(4)] → 結果串列 dummy → 1

### 步驟 2：

    - pop heap → B(1) → 結果變 1 → 1

    - 把 B 的 next（3）推入 heap → heap = [C(2), A(4), B(3)]

### 步驟 3：

    - pop heap → C(2) → 結果 1 → 1 → 2

    - 把 C 的 next（6）推入 heap → heap = [B(3), A(4), C(6)]

- 接續直到所有節點都被處理完：

- 最終合併結果：
```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度 (Time Complexity)：O(N log k)，N 是所有節點總數，k 是串列數目。因為每個節點會被插入與取出 heap 一次，每次 heap 操作成本約 log k。

- 空間複雜度 (Space Complexity)：O(k)，因為 heap 中最多維持 k 個節點（或比 k 少，但為上界）。

---

## ✍️ 我學到了什麼 | What I Learned

- 小根堆是一種非常適合「k 個已排序資料合併」的模式

- 使用 dummy 節點能讓鏈表操作乾淨很多（不須特別處理第一節點）

- 定義 __lt__ 或比較器對 heap 操作很重要，語言不同做法會不同

- 分治法也能解這題，但 heap 方法通常實作簡潔且好維護