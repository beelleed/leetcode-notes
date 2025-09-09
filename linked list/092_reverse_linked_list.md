# 🔁 92. Reverse Linked List II｜反轉連結串列 II
🔗 題目連結：[https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)

## 📘 題目說明 | Problem Description
### 中文
給定一個單向鏈結串列的 `head` 節點，以及兩個整數 `left` 和 `right`，請你反轉從第 `left` 個節點到第 `right` 個節點這一段的節點（1-indexed），並返回整個串列的頭節點。

### English
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

**範例：**
- Example 1:

![](../images/92_rev2ex2.jpg)

    Input: `head = [1,2,3,4,5], left = 2, right = 4`  
    Output: `[1,4,3,2,5]`

- Example 2:

    - Input: head = [5], left = 1, right = 1
    - Output: [5]

---

## 🧠 解題思路 | Solution Idea

1. 🔧 使用 **dummy 節點** 處理邊界條件（如 left = 1）
2. 🔁 先將指標移至第 `left-1` 個節點，記作 `prev`
3. 🔄 開始反轉 `left` 到 `right` 節點
4. 🔗 最後重新接回原串列並回傳 `dummy.next`

---

## 🧩 程式碼 | Code (Python)

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 移動 prev 到 left 前一個節點
        for _ in range(left - 1):
            prev = prev.next

        tail = prev.next  # 起始節點
        for _ in range(right - left):
            temp = tail.next
            tail.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
```
### 1⃣ 邊界條件判斷
```python
if not head or left == right:
    return head
```
若鏈表為空、或不需要反轉（left == right），直接回傳原鏈表。
### 2⃣ 使用 dummy 節點降低邏輯複雜度
```python
dummy = ListNode(0)
dummy.next = head
prev = dummy
```
透過 dummy 建立前置節點，可協助處理 left=1 的情況，避免 special case。
### 3⃣ 定位 prev 至待反轉區段前
```python
for _ in range(left - 1):
    prev = prev.next
```
完成後，prev.next 是反轉區段的首節點（也稱 tail）。
### 4⃣ 局部反轉操作（使用頭插法）
```python
tail = prev.next
for _ in range(right - left):
    temp = tail.next
    tail.next = temp.next
    temp.next = prev.next
    prev.next = temp
```
反轉流程模擬（以 left=2, right=4 的 1→2→3→4→5 為例）：

- 初始：prev → 2 → 3 → 4 →...

- 第一次迴圈後：prev → 3 → 2 → 4 →...

- 第二次迴圈後：prev → 4 → 3 → 2 →...

這樣就完成指定區間的反轉！
### 5⃣ 回傳正確的 head
```python
return dummy.next
```
dummy.next 是反轉後的新 head，確保即使 head 被反轉區包含也能正確回傳。
### 小結
| 步驟              | 說明                         |
| --------------- | -------------------------- |
| `dummy` 設定      | 處理 head 變動的特殊情況            |
| 定位 `prev`       | 找到待反轉區段前的位置                |
| 局部反轉邏輯          | 使用插入法反轉節點（O(1) 空間，O(n) 時間） |
| 回傳 `dummy.next` | 確保新的 head 能正確回傳            |

---

## 範例演算流程

- 輸入範例
    鏈表：1 → 2 → 3 → 4 → 5
    left = 2, right = 4

1. 邊界判斷
    - 如果鏈表為空或 left == right，直接回傳 head。

2. 加入 dummy 節點
    - 建立 dummy 並讓 dummy.next = head，然後令 prev = dummy。

3. 將 prev 移至反轉區段前
    - 迴圈跑 left - 1 = 1 次後，prev 指向節點 1（反轉準備階段）。

4. 原始鏈表：
    ```markdown
    dummy → 1 → 2 → 3 → 4 → 5
            ↑    ↑
          prev  tail
    ```
    - 設定：

        - prev：在第 1 個節點（值為 1）

        - tail：prev.next，也就是第 2 個節點（值為 2）

5. 🔁 第一次執行迴圈
    ```python
    prev = 1
    tail = 2（固定不動）

    temp = tail.next  # 所以 temp = 3
    ```
    圖像變成這樣（尚未改變）：
    ```text
    1 → 2 → 3 → 4 → 5
      ↑    ↑
    tail  temp
    ```
    - ✂️ 第一步：tail.next = temp.next
        這行是讓 2 不再指向 3，而是指向 4：
        ```python
        tail.next = temp.next  # 也就是 tail（=2）.next = 4
        ```
        圖變成：
        ```text
        1 → 2 → 4 → 5
              ↑
             tail

        3（暫時斷開）
        ```
        - 這時候：

            - temp.next 仍然是 4

            - 但因為 2 → 3 被改成 2 → 4，所以 3 是斷開的節點
    - 🪄 第二步：temp.next = prev.next
        - 現在 prev = 1，prev.next = 2，所以：temp.next = 2
        - 此行是讓 temp = 3 指向 prev.next，而 prev.next = 2
        ```python
        temp.next = prev.next  # 3 → 2
        ```
        - 這時候 temp.next 會從原本的 4，變成了 2！
        
        圖變成：
        ```text
        3 → 2 → 4 → 5
              ↑
             tail
        ```
    - 🔗 第三步：prev.next = temp

        讓 1 指向 3：
        ```python
        prev.next = temp  # 1 → 3
        ```
        最終結果變成：
        ```text
        1 → 3 → 2 → 4 → 5
                  ↑
                 tail
        ```
    - 📌 小結四行是做什麼的：
        ```python
        temp = tail.next         # 找到要移動的節點（3）
        tail.next = temp.next    # 把 tail（2）後面指向 4，斷開 3
        temp.next = prev.next    # 讓 3 指向 2
        prev.next = temp         # 把 1 指向 3
        ```
6. 🔁 第二次執行迴圈
    ```python
    temp = tail.next         # temp = 4
    tail.next = temp.next    # tail.next = 5（2 指向 5）
    temp.next = prev.next    # 4.next = 3
    prev.next = temp         # 1 指向 4
    ```
    結果鏈表變成：
    ```nginx
    dummy → 1 → 4 → 3 → 2 → 5
    ```
### 🧠 重點整理

- tail 永遠是「被移動區段的尾端」（一開始是 left 節點）

- temp 是 tail.next，也就是準備要搬到前面的節點

- 每一次都把 temp 插到 prev.next 前面，形成反轉效果

- tail 自始至終不動，但它後面的節點一直被插到前面去

### 總結
| 步驟       | 說明            |
| -------- | ------------- |
| dummy 節點 | 處理反轉包含頭節點的情況  |
| 定位 prev  | 指向要反轉區段前的節點   |
| tail 設定  | 標記區段開頭，最終成為尾端 |
| 頭插法反轉    | 一步一步把內部節點插入起點 |
| 回收鏈結     | 恢復整條鏈表連接完整性   |

---

## ⏱ 複雜度分析 | Complexity
| 類型 | 複雜度  |
| -- | ---- |
| 時間 | O(n) |
| 空間 | O(1) |

---

## 📚 我學到了什麼 | What I Learned

- 使用 dummy node 可有效處理 head 被改動的情況

- 使用局部反轉（類似頭插法）技巧在單次遍歷內反轉任意區間

- 精準控制節點指標（prev, tail, temp）是關鍵