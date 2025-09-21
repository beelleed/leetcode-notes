# 🔢 LeetCode 19 – Remove Nth Node From End of List

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

        # fast 指針先走 n 步
        for _ in range(n):
            fast = fast.next

        # 若 fast 為 None，代表原本 head 長度等於 n，需要刪除 head
        if not fast:
            return head.next

        # 同時移動 fast 和 slow，直到 fast 到最尾端
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow.next 就是要刪除的節點
        slow.next = slow.next.next

        # 回傳 dummy.next 作為新的 head
        return dummy.next
```

| 區段                                                    | 做什麼 / 功能                           | 為什麼這樣寫                                                                    |
| ----------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| `dummy = ListNode(0); dummy.next = head`              | 建一個虛擬節點 `dummy`，它的下個節點指向 `head`    | 為了處理要刪除第一個節點（即 head 本身被移除）的情況比較好處理，用 dummy 可以統一處理，不需 special case 太多。     |
| `fast = dummy; slow = dummy`                          | 設定兩個指針，一開始都從 dummy 出發              | fast 用來先往前跑，slow 則用來“追”fast，到特定距離後可以定位要刪的節點的前一個節點。                        |
| `for _ in range(n): fast = fast.next`                 | fast 先移動 n 步                       | 讓 fast 和 slow 之間有 n 節點的間距，這樣當 fast 到達尾端時，slow 正好在「要刪除節點的前一個節點」位置。         |
| `if not fast: return head.next`                       | 如果 fast 已經變成 `None`（到表尾後超過）        | 表示整個 list 的長度正好是 n 或更小，使得要刪除的是 head 節點本身。此時可以直接跳過 head 回傳 `head.next`。    |
| `while fast.next: fast = fast.next; slow = slow.next` | 同時往前移動 fast 和 slow，直到 fast 到最後一個節點 | 因為 fast 先走過 n 步，所以當 fast 到 list 的最後時，slow 正好在「被刪節點的前一節點」。                 |
| `slow.next = slow.next.next`                          | 刪除節點：跳過 slow 的下一個節點（即被刪掉的節點）       | 這樣就從鏈結串列中移除了第 n 個從尾端算起的節點。                                                |
| `return dummy.next`                                   | 回傳修改後的 head                        | dummy.next 是新的 head（可能原本的 head 沒被刪，也可能原 head 被刪，那 dummy.next 自動指向新的第一節點）。 |

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