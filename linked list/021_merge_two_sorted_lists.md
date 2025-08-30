# 🔗 LeetCode 21 - 合併兩個已排序的連結串列 | Merge Two Sorted Lists

🔗 題目連結 | Problem Link: [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## 📘 題目說明 | Problem Description

### 中文：
給你兩個升序排序的單向連結串列 `list1` 和 `list2`，請你將它們合併成一個新的升序連結串列，並回傳新的頭節點。

### English:
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list and return the merged list’s head.

### Examples
- Example 1:

![](../images/21_merge_ex1.jpg)
    Input: list1 = [1,2,4], list2 = [1,3,4]

    Output: [1,1,2,3,4,4]

- Example 2:
    - Input: list1 = [], list2 = []
    - Output: []

- Example 3:
    - Input: list1 = [], list2 = [0]
    - Output: [0]

---

## 🧠 解法思路 | Solution Idea

### 中文：
1. 使用一個「虛擬節點 dummy」作為新串列的起點。
2. 使用 `tail` 指標幫我們不斷接上較小的節點。
3. 每次比較 `list1.val` 和 `list2.val`，接上小的那一個，並移動那個 list 的指標。
4. 最後只會有其中一個 list 還有剩，把它整個接上即可。

### English:
1. Create a **dummy node** to start the merged list.
2. Use a pointer `tail` to keep adding nodes to the merged list.
3. Compare values of `list1` and `list2`, attach the smaller one, and move its pointer.
4. Once either list is empty, attach the remaining part of the other list.

---

## 🧾 程式碼與註解 | Code with Explanation

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)       # 建立虛擬節點，合併結果從 dummy.next 開始
        tail = dummy              # 用 tail 指向目前合併串列的尾端

        while list1 and list2:    # 當兩個 list 都還有節點時
            if list1.val < list2.val:
                tail.next = list1    # 接上 list1 較小的節點
                list1 = list1.next   # list1 指標往前移
            else:
                tail.next = list2    # 接上 list2 較小的節點
                list2 = list2.next   # list2 指標往前移
            tail = tail.next         # 合併串列往前移

        # 把剩下的接上（其中一個會是 None）
        tail.next = list1 if list1 else list2

        return dummy.next         # 回傳真實的合併串列起點
```

```python
dummy = ListNode(0)
tail = dummy
```
- dummy（虛擬節點） 是一個假的起始節點，值可以是任意值（這裡用 0）。

- 它的好處是：可以簡化「處理頭節點是否為空」的邏輯。

- tail 是指標，代表目前合併串列的最後一個節點（尾巴），我們會一直往這邊加節點。

```python
while list1 and list2:
```
- 這個迴圈只要兩個 linked list 都還沒走完，就會持續執行。

- 每次從兩個 list 的目前節點中挑一個小的來接到 tail 後面。

```python
if list1.val < list2.val:
    tail.next = list1
    list1 = list1.next
```
- 如果 list1 的值比較小，我們就把 list1 的節點接到 tail.next（接在合併串列尾巴後面）。

- 然後把 list1 的指標移到「下一個節點」，表示這個節點已經處理完了。

```python
else:
    tail.next = list2
    list2 = list2.next
```
- 如果 list2 比較小（或一樣），就處理 list2 的節點。

```python
tail = tail.next
```
- 不管接的是哪個，現在 tail 都要往後移一格（更新尾巴的位置）。

```python
tail.next = list1 if list1 else list2
```
- 如果 list1 還有剩下的節點，就接上 list1；否則就接上 list2。

- 一旦 while 退出，代表至少有一條 list 已經空了。

- 另一條可能還有節點沒接完，直接整條接上就好（因為已經排序好）。
```python 
return dummy.next
```
- 注意！我們不是回傳 dummy，因為它是虛擬起點，真正的串列是從 dummy.next 開始。

---

## ⏱️ 時間與空間複雜度 | Complexity Analysis
| 項目 | 複雜度      | 說明                   |
| -- | -------- | -------------------- |
| 時間 | O(n + m) | 走訪 list1 和 list2 各一次 |
| 空間 | O(1)     | 沒有使用額外空間，原地連接        |

---

## 📌 學到的重點 | What I Learned
- 虛擬節點 dummy 是處理 linked list 問題的常用技巧。

- 用 while 比較兩個 sorted list 合併邏輯與 merge sort 很像。

- 操作 linked list 指標時，務必小心 .next 指向正確的物件。

---

## 📚 延伸閱讀 | Further Practice
- LeetCode 23 - Merge k Sorted Lists

- Merge Sort 的 Merge 步驟

- Linked List 基礎操作與 dummy head 技巧