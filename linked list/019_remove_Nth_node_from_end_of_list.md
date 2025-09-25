# 🔢 LeetCode 19 – Remove Nth Node From End of List
🔗 題目連結：[https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## 📄 題目說明 | Problem Description

### **中文**：

給你一個單向鏈結串列的頭節點 `head` 和整數 `n`，請移除從末尾數來第 `n` 個節點，並回傳修改後的鏈表的頭節點。  
### **English**: 

Given the head of a singly-linked list and an integer `n`, remove the n-th node from the end of the list and return its head.

### Examples
- Example 1:

![](../images/19_remove_ex1.jpg)

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

- Example 2:

    - Input: head = [1], n = 1
    - Output: []

- Example 3:

    - Input: head = [1,2], n = 1
    - Output: [1]

---

## 🧠 解題思路 | Solution Idea

1. **兩遍遍歷（Two‑Pass）**  
   - 第一次遍歷整個鏈表算出它的長度 `L`。  
   - 然後計算從前面來第 `L − n` 個節點（也就是被刪節點的前一個節點）。  
   - 再把該節點的 `next` 調整成 `next.next`，跳過要刪的節點。

2. **一次遍歷 + 雙指針（One‑Pass Two‑Pointer）** 
   - 使用兩指針 `fast` 和 `slow`，並加一個 dummy 節點指向 `head`，以處理邊界（例如要刪除第一個節點）的情況。  
   - 先讓 `fast` 向前走 `n` 步。  
   - 然後同時讓 `fast` 和 `slow` 一起往前走，直到 `fast` 到達尾端。此時 `slow` 停在要刪除節點的 **前一個節點**。  
   - 調整 `slow.next = slow.next.next` 跳過被刪除的節點。  
   - 回傳 `dummy.next`（新的 head）。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 建立 dummy 節點以處理要刪除 head 的邊界狀況
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # 讓 fast 先走 n+1 步
        for _ in range(n + 1):
            fast = fast.next

        # 同時移動 fast 和 slow，直到 fast 到最尾端
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next 就是要刪除的節點
        slow.next = slow.next.next

        # 回傳 dummy.next 作為新的 head
        return dummy.next
```
```python
dummy = ListNode(0)
dummy.next
```
- 在鏈表最前面加一個 dummy 節點。

- 這樣就算要刪掉頭節點，也能統一處理，不需要特別判斷。

鏈表示意：
    ```rust
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    ```
```python
fast = dummy
slow = dummy
```
- 兩個指針都從 dummy 開始。
```python
for _ in range(n + 1):
    fast = fast.next
```
- 為什麼要走 n+1 步？

    - 讓 fast 和 slow 之間保持一個「n+1 的間距」。

    - 之後當 fast 走到 None（鏈表尾後一格），slow 就會正好停在要刪的節點的前一個。

例子：[1,2,3,4,5], n=2
    ```rust
    fast 走 3 步後 (n+1=3):
    fast -> 3
    slow -> dummy
    ```
```python
while fast:
    fast = fast.next
    slow = slow.next
```
- 兩個指針一起往前走，直到 fast = None。

此時 slow 剛好在要刪的節點的前一個。

例子：
    ```ini
    fast = None
    slow = 3
    ```
```python
slow.next = slow.next.next
```
- slow.next 就是要刪的節點。

把它跳過即可。

例子：

    原本：3 -> 4 -> 5

    刪掉 4：3 -> 5
```python
return dummy.next
```
- 因為可能刪掉頭節點，所以最安全的做法是回傳 dummy.next（真正的鏈表頭）。

---

## 🧪 範例 | Example

為了幫你理解，這裡用一個具體例子：

- 鏈表： 1 → 2 → 3 → 4 → 5

- n = 2（要移除倒數第 2 個節點，也就是值為 4 的節點）

流程：

1. 建立 dummy(0) → 1 → 2 → 3 → 4 → 5
   
   fast = dummy, slow = dummy

2. for 讓 fast 移動 2 步：

    - 第一步：fast → 1

    - 第二步：fast → 2

3. 檢查 if not fast: fast 現在不是 None，所以繼續。

4. 進入 while fast.next: 迴圈，fast 和 slow 一起移動直到 fast.next 為 None：

    - fast at 2, slow at dummy → both 移動 → fast at 3, slow at 1

    - fast at 3, slow at 1 → both 移動 → fast at 4, slow at 2

    - fast at 4, slow at 2 → both 移動 → fast at 5, slow at 3

    - 現在 fast.next 是 None（fast 在最後一節點 5），停止

5. 此時 slow 在節點值為 3 的節點。
    - slow.next 是節點 4 → 這是要刪除的節點

    - slow.next = slow.next.next → 跳過節點 4，讓 3 指向 5

6. 回傳 dummy.next → 原來 head 仍是 1，因此整個修改後的鏈表是： 1 → 2 → 3 → 5

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類          | 複雜度                                                                |
| ----------- | ------------------------------------------------------------------ |
| 時間複雜度 Time  | **O(n)**，n 是鏈表節點數量。fast 指針先走 n 步 + then both 指針走直到尾端，總共最多遍歷一次整個鏈表。 |
| 空間複雜度 Space | **O(1)**，只用固定數量的指針變數和 dummy 節點，不額外用隨 `n` 成長的資料結構。                  |

---

## ✍️ 我學到了什麼 | What I Learned

- 使用 dummy 節點可以使移除第一個節點或整個 head 被刪除等邊界情況處理一致、簡潔。

- fast‑slow 雙指針技巧在 linked list 中是經典模式：先讓 fast 快跑（或保持 gap），再兩指針一起走，這樣可以在一次遍歷中解一些「從尾端數」這樣的問題。

- 一定要注意細節：若 fast 在快跑 n 步後變成 None，代表要刪除的是 head，要特殊處理。

- 面試中講這題時要清楚敘述「快指針先移動 n 步 → gap → 同步移動 → slow 在刪除點前」的流程。