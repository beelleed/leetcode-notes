# 🔄 LeetCode 143 — Reorder List / 重排序鏈表
🔗 [題目連結](https://leetcode.com/problems/reorder-list/)

---

## 題目說明 | Problem Statement
### 中文
給定一個單向鏈表的 `head`，其節點為： 
    
    L0 → L1 → L2 → … → Ln‑1 → Ln 

你需要 **原地重排（reorder）**，使鏈表變成如下形態：  

    L0 → Ln → L1 → Ln‑1 → L2 → Ln‑2 → …

你不能改變節點中的值，只能調整節點之間的連結（`next` 指向）。 :contentReference[oaicite:0]{index=0}

### English
You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### 範例 | Examples

- 輸入：`1 → 2 → 3 → 4`  
  輸出：`1 → 4 → 2 → 3`  
- 輸入：`1 → 2 → 3 → 4 → 5`  
  輸出：`1 → 5 → 2 → 4 → 3`  

---

## 解題思路 | Solution Idea

要把尾巴的節點交錯插入前半部中，因為是單向鏈表不能往回走，我們可以拆解這題為三步：

1. **找到中點**  
   使用快慢指針（fast / slow）技巧：fast 每次走兩步，slow 每次走一步。當 fast 到達尾端（或無法再走兩步）時，slow 就在中點位置。  
2. **反轉後半段鏈表**  
   從中點的下一節點開始，把後半截鏈表反轉，以方便從尾端向前操作。  
3. **交錯合併前後兩段**  
   用兩個指針交替取節點：從前半段取一個，接後半反轉後的節點，再回到前半段的下一個，依此類推。  

這三部合起來，就能達成 L0 → Ln → L1 → Ln‑1 … 的效果。 :contentReference[oaicite:1]{index=1}

---

## ✅ 程式碼（Python）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 找到中點
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 拆分 & 反轉後半段
        second = slow.next
        slow.next = None  # 切斷前半段與後半段的連結

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. 交錯合併前半段 head 和 反轉後半段 prev
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
```
### 🧩 處理特殊情況
```python
if not head or not head.next:
    return
```

- 如果鏈表為空或只有一個節點，無需處理，直接返回。

### 🧩 找出中點（使用快慢指針）
```python
slow = head
fast = head
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
```

- slow 每次走一步，fast 每次走兩步。

- 當 fast 無法再前進兩步時，slow 剛好在中間（或中間偏左一點）。

- 這樣可以把鏈表一分為二：前半段 head → ... → slow，後半段 slow.next → ... → end。

### 🧩 反轉後半段鏈表
```python
second = slow.next
slow.next = None  # 切斷前半段與後半段
```

- 把 slow 的下一個節點作為後半段的開頭，並且把它與前半段斷開。
```python
prev = None
curr = second
while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
```

- 這段是鏈表反轉的標準寫法：

    - curr.next = prev：把當前節點指向前一個節點（反向）

    - 逐步把 curr 移動到下一個節點，直到走完整個後半段

- 最後 prev 就是反轉後的新頭（也就是原本的 Ln）

### 🧩 交錯合併前後兩段
```python
first = head
second = prev
```

- first 指向前半段的開頭，second 指向反轉後的後半段開頭
```python
while second:
    tmp1 = first.next
    tmp2 = second.next

    first.next = second
    second.next = tmp1

    first = tmp1
    second = tmp2
```

- 每一輪操作把一個 second 節點插入 first 節點後面

- 使用 tmp1, tmp2 暫存 next 指針，避免斷鏈

- 不斷交錯插入，直到後半段用完（second 走完）

---

## 🧪 範例設定 | Example

假設鏈表是：

1 → 2 → 3 → 4 → 5

我們呼叫 reorderList(head)，最終想要得到：

1 → 5 → 2 → 4 → 3

### 1. 處理特殊情況
```python
if not head or not head.next:
    return
```

- 此例 head 不為空，且 head.next 存在，因此繼續。

### 2. 找中點
```python
slow = head        # slow 指向 1
fast = head        # fast 指向 1
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
```

- 第一次迴圈：slow → 2，fast → 3

- 第二次迴圈：slow → 3，fast → 5

- 此時 fast.next 為 None，停止迴圈
    ⇒ 中點 slow 停在節點 3

### 3. 拆分 & 反轉後半段
```python
second = slow.next      # second 指向 slow.next，即節點 4
slow.next = None        # 切斷：節點 3 的 next 設為 None，前半段斷開
```

- 此時鏈表分為：

    - 前半段： 1 → 2 → 3 → None

    - 後半段： 4 → 5

- 接著反轉後半段：
```python
prev = None
curr = second           # curr = 4
while curr:
    nxt = curr.next      # 保存 curr.next，第一次是 5
    curr.next = prev     # 將 curr.next 指向 prev（None）→ 4 → None
    prev = curr          # prev = 4
    curr = nxt           # curr = 5

    # 下一圈：
    nxt = curr.next      # nxt = None（5 的下一節點）
    curr.next = prev     # 5.next = 4 → 5 → 4 → None
    prev = curr          # prev = 5
    curr = nxt           # curr = None → 結束迴圈
```

- 最後 prev 指向節點 5，是反轉後半段的新頭。後半段變為： 5 → 4 → None

### 4. 交錯合併
```python
first = head    # first = 1
second = prev   # second = 5
while second:
    tmp1 = first.next    # tmp1 = 2
    tmp2 = second.next   # tmp2 = 4

    first.next = second  # 1 → 5
    second.next = tmp1   # 5 → 2

    first = tmp1         # first = 2
    second = tmp2        # second = 4

    # 下一輪
    tmp1 = first.next    # tmp1 = 3
    tmp2 = second.next   # tmp2 = None

    first.next = second  # 2 → 4
    second.next = tmp1   # 4 → 3

    first = tmp1         # first = 3
    second = tmp2        # second = None → 迴圈結束
```

- 中間步驟匯總：

    - 第一次插入： 1 → 5 → 2

    - 第二次插入： 1 → 5 → 2 → 4 → 3

- 最後得到鏈表： 1 → 5 → 2 → 4 → 3

- 因為 second 已經變為 None，迴圈停止。

---

## ⏱ 複雜度分析 | Complexity

| 項目    | 複雜度                                  |
| ----- | ------------------------------------ |
| 時間複雜度 | **O(n)**：三個主要步驟（找中點 + 反轉 + 合併）各做一次遍歷 |
| 空間複雜度 | **O(1)**：只用幾個指針變數，沒有額外資料結構           |

---

## 🧠 我學到的 / What I Learned

- 這題是一個典型把複雜操作拆成子步驟的例子：找中點 → 反轉 → 合併，這三招在鏈表題目中經常用到。

- 快慢指針是處理中點、拆段常用技巧。

- 善用就地反轉與合併技巧，可以在不使用額外空間下完成重構。

- 在合併時指針操作要非常小心：避免漏連、重複、或造成環。
