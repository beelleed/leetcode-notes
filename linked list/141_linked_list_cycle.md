# 🔁 LeetCode 141 - 判斷連結串列是否有環 | Linked List Cycle

[Leetcode 141](https://leetcode.com/problems/linked-list-cycle/)
---

## 📘 題目說明 | Problem Description

### 中文：
給定一個單向連結串列的頭節點 `head`，請你判斷該串列中是否存在「環」：

- 如果某個節點的 `.next` 指向了前面出現過的節點，表示這個 linked list 有環。
- 若存在環，請回傳 `True`，否則回傳 `False`。

### English:
Given `head`, the head of a singly linked list, determine if the linked list has a cycle in it.

- A cycle occurs if a node's `.next` points to a previous node in the list.
- Return `True` if there is a cycle; otherwise, return `False`.

---

## 🧠 解題思路 | Solution Idea

### ✅ 使用「快慢指標」（Floyd's Cycle Detection）

### 中文：
使用「快慢指標法（Floyd's Tortoise and Hare 演算法）」是判斷 linked list 是否有環的標準做法。

1. 設兩個指標：`slow` 每次走一步，`fast` 每次走兩步。
2. 如果 linked list 有環，`fast` 終將追上 `slow`。
3. 如果無環，`fast` 會先到達結尾 `None`，程式會在迴圈中斷。

### English:
Use the **two pointers method** (Floyd's Cycle Detection algorithm):

1. Initialize two pointers: `slow` moves one step at a time, `fast` moves two steps.
2. If there's a cycle, `fast` will eventually meet `slow` inside the cycle.
3. If there's no cycle, `fast` will reach the end (`None`), and the loop stops.

---

## 🧾 程式碼 | Code

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # 每次走一步
            fast = fast.next.next    # 每次走兩步

            if slow == fast:         # 相遇表示有環
                return True

        return False                 # fast 到尾，無環
```

```python
while fast and fast.next:
```
- 只要 fast 和 fast.next 都存在，表示還能繼續往下走。

```python
slow = slow.next
fast = fast.next.next
```
- slow 每次走一步，fast 每次走兩步。

```python
if slow == fast:
    return True
```
- 如果兩個指標相遇，代表進入了環。

---

## ⏱️ 時間與空間複雜度 | Complexity Analysis
| 項目    | 複雜度  | 說明             |
| ----- | ---- | -------------- |
| 時間複雜度 | O(n) | 每個節點最多走訪兩次     |
| 空間複雜度 | O(1) | 只用兩個指標，無額外儲存空間 |

---

## 🧠 學到的重點 | What I Learned
- 如何用快慢指標判斷 linked list 是否有「環」

- while fast and fast.next 是常見的安全條件判斷寫法

- Floyd 演算法也可應用在「找環起點」等題目（如 LeetCode 142）

---

## 📚 延伸閱讀 | Related Topics
- LeetCode 142 - Linked List Cycle II（找環的起點）

- 快慢指標（two pointers）技巧

- Floyd 判圈演算法（Floyd's Cycle Detection）