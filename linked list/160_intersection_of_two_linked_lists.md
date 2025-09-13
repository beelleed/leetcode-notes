# 🆔 LeetCode 160 – Intersection of Two Linked Lists | 兩條鏈表的交叉點

🔗 題目連結：[https://leetcode.com/problems/intersection-of-two-linked-lists/](https://leetcode.com/problems/intersection-of-two-linked-lists/)

---

## 📄 題目說明 | Problem Description

### 中文：
給你兩條單向鏈表的頭節點 headA 和 headB，找出兩條鏈表的交點節點（即從該節點之後它們共用同一組節點）。如果沒有交點，回傳 None。

### English:
Given the heads of two singly linked lists headA and headB, return the node at which the two lists intersect. If the two linked lists do not intersect, return null.

For example, the following two linked lists begin to intersect at node c1:

![](../images/160_statement1.png)

- The test cases are generated such that there are no cycles anywhere in the entire linked structure.

- Note that the linked lists must retain their original structure after the function returns.

- Custom Judge:

    - The inputs to the judge are given as follows (your program is not given these inputs):

        - intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
        - listA - The first linked list.
        - listB - The second linked list.
        - skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
        - skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
- The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

### Examples
- Example 1:

![](../images/160_example_1_1.png)

    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3

    Output: Intersected at '8'
    
    Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
    
    Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

- Example 2:

![](../images/160_example_2.png)

    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1

    Output: Intersected at '2'

    Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

![](../images/160_example_3.png)

    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2

    Output: No intersection
    
    Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    
    Explanation: The two lists do not intersect, so return null.

---

## 🧠 解題思路 | Solution Idea
### 中文
- 使用 雙指針技巧（Two‑Pointer Technique）：分別讓兩個指針從兩鏈表頭開始走。

- 當指針走到鏈表末端時，切換到另一條鏈表的頭繼續走。這樣兩指針總共走過的節點數會相同（假設有交點）或同時到 “末端（None）”。

- 當 pointerA == pointerB 的時候要麼指向交點節點，要麼兩個都 None（代表無交點）。

### English
- Use the Two-Pointer Technique: start two pointers from the heads of the two linked lists respectively.

- When a pointer reaches the end of its list, it switches to the head of the other list and continues traversing. This ensures that both pointers traverse an equal total number of nodes (assuming there is an intersection), or they both reach None at the same time (if there is no intersection).

- When pointerA == pointerB, they are either pointing to the intersection node, or both are None (indicating no intersection).

---

## 💻 程式碼
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        while a != b:
            # 如果 a 到尾端了，就切換到 headB 開始；否則往下一個節點
            a = a.next if a else headB
            # 同理處理 b
            b = b.next if b else headA

        return a  # 或 b（a == b）
```
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
```
- 初始化兩個指針，a 指向鏈表 A 的頭，b 指向鏈表 B 的頭。

- 我們的目標是找出「從哪個節點開始，兩鏈表共享同樣的節點（也就是指向同一個記憶體位址）」。

```python
while a != b
```
- 如果 a 和 b 指向不同的節點，就繼續往下走。

- 注意：這裡比較的是節點物件本身（是否為同一個節點物件），而不是值相等。
```python
a = a.next if a else headB
```
- 如果 a 還有下一個節點 → a = a.next

- 如果 a 走到尾端 (None) → 跳去 headB 開始重走 B 鏈表

- 意義：補齊 A 鏈表比 B 短的部分
```python
b = b.next if b else headA
```
- 同理：b 走完就跳去 A

- 這樣 a + b 總共都會走 m + n 步，即便兩鏈表長度不同，最終會同步到相遇點（或都走到 None）
```python
        return a  # 或 b（a == b）
```
- 最後會有兩種情況：

    - 如果有交點 → a == b 為交點節點

    - 如果沒交點 → 最後兩個指針都會走到 None，a == b == None

### 🧠 核心觀念：讓長的補短的

這個方法等效於：

1. 指針 a 走完整個 A 鏈表後接著走 B

2. 指針 b 走完整個 B 鏈表後接著走 A

3. 若有交點，它們會在相交處同步；若沒有，則都走到 None 結束

---

## 🧪 範例流程 | Step‑by‑Step Walkthrough

假設節點如下（用節點標籤示意）：
```makefile
A:      4 → 1 → 
                ↘
                  8 → 4 → 5 → None
                ↗
B:    5 → 6 → 1 →
```
標記：

- headA 開始於節點值 4

- headB 開始於節點值 5

### 🔍 每次迭代的情況
| 步驟 | pointer a 在哪 | pointer b 在哪 | a == b 嗎？ |
| -- | ------------ | ------------ | --------- |
| 起始 | A 的 `4`      | B 的 `5`      | 否         |
| 1  | `4 → 1`      | `5 → 6`      | 否         |
| 2  | `1 → 8` (交點) | `6 → 1`      | 否         |
| 3  | `8`          | `1 → 8`      | 是（都到交點）   |


---

## ⏱ 複雜度分析 | Complexity Analysis
| 類型    | 複雜度                                       |
| ----- | ----------------------------------------- |
| 時間複雜度 | O(m + n) — m, n 分別是兩條鏈表的長度 |
| 空間複雜度 | O(1) — 只使用兩個指針，不用額外資料結構     |

---

## 🛠 我學到了什麼 | What I Learned
- 雙指針「走完自己的 + 再走對方的」技巧，可以自動平衡不同長度的鏈表，讓指針最終會同步到交點或同步到 None。

- 不需要事先計算鏈表長度，也不用 hash 或 set 儲存節點，只用 O(1) 空間就可以做到。

- 比較節點是否相同必須是比較節點物件的參考（地址），而不只是值。


