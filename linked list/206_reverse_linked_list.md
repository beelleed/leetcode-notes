# 🔁 LeetCode 206 - 反轉連結串列 | Reverse Linked List

---

## 📘 題目描述 | Problem Description

### 中文：
給定一個單向連結串列的頭節點 `head`，請你反轉該連結串列，並回傳反轉後的頭節點。

### English:
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

---

## 🧠 解法思路 | Solution Approach

### ✅ 雙指標原地反轉法（In-place two-pointer approach）

1. 使用 `prev`（前一節點）與 `curr`（目前節點）來進行指標反轉。
2. 每次迴圈中，把 `curr.next` 指向 `prev`，完成反轉。
3. 移動指標繼續進行下一步，直到整個串列反轉完成。
4. 回傳 `prev` 作為新串列的頭。

---

## 🧾 程式碼 | Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next     # 暫存下一節點
            curr.next = prev          # 反轉指向
            prev = curr               # 前移 prev
            curr = next_temp          # 前移 curr
        return prev
```

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```
- 定義一個方法 reverseList，參數是 head，表示原始 linked list 的起點（頭節點）。

- 回傳值會是反轉後的新頭節點。

```python
prev = None
```
- 初始化 prev 為 None，表示目前反轉後串列的最後一個節點（初始為空）。

- 將來反轉的每個節點都會逐步接到 prev 前面。

```python
curr = head
```
- 將 curr 指向原始的 head，準備開始遍歷整個 linked list。

```python
while curr:
```
- 開始一個 while 迴圈，只要還有節點（curr 不為 None）就持續處理。

- 每一圈會處理一個節點的反轉。

```python
next_temp = curr.next
```
- ⭐ 重點：先用變數 next_temp 暫存 curr.next

- 因為你等一下會改掉 curr.next，所以先記下「下一個節點的位置」

```python
curr.next = prev
```
- 核心：將目前節點 curr 的「下一個」指向前一個節點 prev，完成反轉的一步。

- 原本是：A → B，這一步會讓 B → A。

```python
prev = curr
```
- 移動 prev：現在 curr 節點已反轉完成，它就成了反轉串列的新尾端。

```python
curr = next_temp
```
- 移動 curr：繼續往下一個尚未處理的節點走（就是前面暫存的 next_temp）

```python
return prev
```
- 當所有節點都反轉完，curr 會變成 None，這時 prev 就是新的「反轉後串列的頭」。

### 📘 圖解（以 A → B → C → D 為例）
初始：
```python
prev = None
curr = A
```

步驟（每次 while）：
```mathematica
1. A → None   (prev = A)
2. B → A      (prev = B)
3. C → B      (prev = C)
4. D → C      (prev = D)
```

最後結果：
```css
D → C → B → A
```

### ✅ 小結
- 使用 prev、curr 與 next_temp 三個指標

- 每次迴圈把目前節點指回前一個（反轉）

- 原地操作，空間 O(1)，效率高，LeetCode 面試經典解法

---

## ⏱️ 時間與空間複雜度 | Time & Space Complexity
| 項目 | 複雜度  | 解釋                  |
| -- | ---- | ------------------- |
| 時間 | O(n) | 每個節點只走訪一次           |
| 空間 | O(1) | 使用常數額外記憶體（in-place） |

---

## 📌 學到的東西 | What I Learned
- 如何用雙指標 in-place 反轉 linked list

- 理解 pointer 操作與串接邏輯

- 實作中注意先儲存 curr.next 避免鏈結丟失

- 這種題型是 linked list 的經典考題，出現頻率高

---

## 📚 延伸練習 | Related Problems
- LeetCode 92 - Reverse Linked List II

- LeetCode 234 - Palindrome Linked List

- LeetCode 21 - Merge Two Sorted Lists