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

- 使用最小堆（Min Heap）來追蹤每個 linked list 中目前最小的節點。
- 初始時，把每條 linked list 的頭節點放入 min heap 中。
- 每次從 heap 取出最小值節點，接到結果 linked list 後面，並將該節點的下一個節點放入 heap。
- 重複直到所有節點處理完畢。

---

## 💻 程式碼實作（Min-Heap 方法）

```python
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ✅ 初始化 heap
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                # 💡 使用 (val, index, node) 避免 TypeError
                heapq.heappush(min_heap, (node.val, i, node))

        # ✅ 建立結果 linked list 的 dummy 起點
        dummy = ListNode()
        curr = dummy

        # ✅ 每次取出最小節點，加入結果串列
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            # ✅ 如果有下一個節點，就加入 heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
```
### 🔍 初始化小根堆
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

```
- min_heap 是一個最小堆，用來追蹤所有目前節點的最小值。

- enumerate(lists) 讓我們能追蹤是哪一個 linked list 的節點（避免同值比較失敗）。

- 每個放入 heap 的元素是三元組 (節點值, list編號, 節點物件)。

    - heapq 預設比較的是三元組的第一個元素（這裡是節點值）。

### 🧱 準備 dummy 節點
```python
dummy = ListNode()
curr = dummy
```
- 建立一個 dummy 節點當作結果 linked list 的開頭，方便最後直接回傳 dummy.next。

- curr 是指向目前結果串列的尾端節點，隨時更新。
### 🔁 處理所有節點
```python
while min_heap:
    val, i, node = heapq.heappop(min_heap)
    curr.next = node
    curr = curr.next
```
- 每次從堆中拿出值最小的節點 node。

- 把它接到 curr.next 上，並移動 curr 指針。
### ➕ 加入下一個節點
```python
if node.next:
    heapq.heappush(min_heap, (node.next.val, i, node.next))
```
- 如果這個節點 node 還有後續的節點（node.next 不為 None）：

    - 把它的下一個節點也加入堆中繼續比大小。
### ✅ 回傳結果
```python
return dummy.next
```
- dummy 是我們建立的虛擬節點，所以實際結果是從 dummy.next 開始的 linked list。

---

## 🧪 範例流程

假設有三個已排序的鏈結串列：

- List A: 1 → 4 → 5

- List B: 1 → 3 → 4

- List C: 2 → 6

| 步驟   | `min_heap`（包含哪些節點）                                                                               | 拿出的小節點 (val, i) | 結果 Linked List（從 dummy.next 開始） | 接入 heap 的下一節點（如果有）             |
| ---- | ------------------------------------------------------------------------------------------------ | --------------- | ------------------------------- | ------------------------------ |
| 初始化  | push A.head(1,0), B.head(1,1), C.head(2,2)  <br> 所以 `min_heap` = \[(1,0,A1), (1,1,B1), (2,2,C1)] | —               | `[]`                            | —                              |
| 步驟 1 | 同如上                                                                                              | pop (1,0,A1)    | `1`                             | A1.next 是 4 → 所以 push (4,0,A4) |
| 步驟 2 | heap 現在是 \[(1,1,B1), (2,2,C1), (4,0,A4)]                                                         | pop (1,1,B1)    | `1 → 1`                         | B1.next 是 3 → push (3,1,B3)    |
| 步驟 3 | heap = \[(2,2,C1), (4,0,A4), (3,1,B3)]                                                           | pop (2,2,C1)    | `1 → 1 → 2`                     | C1.next 是 6 → push (6,2,C6)    |
| 步驟 4 | heap = \[(3,1,B3), (4,0,A4), (6,2,C6)]                                                           | pop (3,1,B3)    | `1 → 1 → 2 → 3`                 | B3.next 是 4 → push (4,1,B4)    |
| 步驟 5 | heap = \[(4,0,A4), (6,2,C6), (4,1,B4)]                                                           | pop (4,0,A4)    | `1 → 1 → 2 → 3 → 4`             | A4.next 是 5 → push (5,0,A5)    |
| 步驟 6 | heap = \[(4,1,B4), (6,2,C6), (5,0,A5)]                                                           | pop (4,1,B4)    | `1 → 1 → 2 → 3 → 4 → 4`         | B4.next 是 None → 不推新的          |
| 步驟 7 | heap = \[(5,0,A5), (6,2,C6)]                                                                     | pop (5,0,A5)    | `1 → 1 → 2 → 3 → 4 → 4 → 5`     | A5.next 是 None → 不推新的          |
| 步驟 8 | heap = \[(6,2,C6)]                                                                               | pop (6,2,C6)    | `1 → 1 → 2 → 3 → 4 → 4 → 5 → 6` | C6.next 是 None → 不推新的          |
| 完成   | heap 空                                                                                           | —               | `1 → 1 → 2 → 3 → 4 → 4 → 5 → 6` | —                              |

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