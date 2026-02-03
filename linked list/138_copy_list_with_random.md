# 📍 LeetCode 138 — Copy List with Random Pointer | 複製含 Random 指標的 Linked List
🔗 [題目連結](https://leetcode.com/problems/copy-list-with-random-pointer/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給定一個 linked list，每個節點除了 next 之外，還有一個 random 指標，random 可以指向串列中的任意節點，或是 None。

- 請回傳這個 linked list 的 深拷貝（deep copy）：

    - 新串列中的每個節點都必須是全新的節點

    - next 和 random 的關係要與原串列完全相同

    - 原串列不能被改動

### English

Given a linked list where each node has a next pointer and a random pointer that can point to any node or null, return a deep copy of the list.

### Examples
- Example 1:

    ![](../images/138_e1.png)

    - Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    - Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
- Example 2:

    ![](../images/138_e2.png)

    - Input: head = [[1,1],[2,1]]
    - Output: [[1,1],[2,1]]
- Example 3:

    ![](../images/138_e3.png)

    - Input: head = [[3,null],[3,0],[3,null]]
    - Output: [[3,null],[3,0],[3,null]]

---

## 🧠 解題思路 | Solution Idea

- 這是一題 Linked List 題，但因為多了 random，
所以必須搭配 HashMap 記錄節點對照關係。

- Linked List：負責「走訪節點」

- HashMap：負責「舊節點 → 新節點 的對照」

---

## 💻 程式碼實作 | Code (HashMap 方法)
```python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old_to_new = {}

        # 第一輪：複製節點本身
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 第二輪：補 next 和 random
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### Base case
```python
if not head:
    return None
```

- 空 linked list，直接回傳 None

#### 建立 HashMap
```python
old_to_new = {}
```

- key：原本的節點

- value：複製後的新節點

- 👉 用來記錄「舊 → 新」的對照關係

#### 第一輪：只複製節點（不接指標）
```python
cur = head
while cur:
    old_to_new[cur] = Node(cur.val)
    cur = cur.next
```

- 這一輪做的事：

    - 一個一個走 Linked List

    - 為每個舊節點建立一個新節點

    - 只複製 val

- 此時：

    - next 和 random 都還沒接

#### 第二輪：補 next 和 random
```python
cur = head
while cur:
    old_to_new[cur].next = old_to_new.get(cur.next)
    old_to_new[cur].random = old_to_new.get(cur.random)
    cur = cur.next
```

- 這一輪做的事：

    - 再次走 Linked List

    - 利用 HashMap：

        - 把舊節點的 next 對應到新節點

        - 把舊節點的 random 對應到新節點

- get() 的原因：

    - cur.next 或 cur.random 可能是 None

        - 在 138 題中，題目本來就允許：

            - next 在尾節點時是 None

            - random 可以指向任意節點或 None
        
        - ❌ 如果你直接寫（會出錯）
            ```python
            old_to_new[cur].next = old_to_new[cur.next]
            ```

            - 如果：cur.next is None

            - 那這一行會變成：old_to_new[None]
            
            - 👉 這會發生什麼？

                - None 不是一個 key

                - Python 會直接丟：KeyError

        - ✅ 用 get() 會怎樣？
            ```python
            old_to_new[cur].next = old_to_new.get(cur.next)
            ```

            - 如果：cur.next is None

            - 那就是：old_to_new.get(None)

            - 👉 結果是：None

            - 為什麼「回傳 None」是正確的？

                - 因為：原本 cur.next = None
                
                - 那複製後的節點：new.next = None

                - 這完全符合 deep copy 的要求

                - 同理：
                    ```python
                    cur.random = None
                    → new.random = None
                    ```

#### 回傳新串列頭
```python
return old_to_new[head]
```

- 回傳原本 head 對應的新節點

- 這就是完整複製後的 linked list

---

## 🧪 範例流程 | Example Walkthrough
### 原始 linked list
```text
A → B → C
```

random 關係：
```text
A.random → C
B.random → A
C.random → None
```
### 第一輪（建立對照表）

HashMap：
```text
A → A'
B → B'
C → C'
```

新節點目前狀態：
```text
A'   B'   C'
(next / random 都是 None)
```
### 第二輪（補指標）

- A'.next = B'

- A'.random = C'

- B'.next = C'

- B'.random = A'

- C'.next = None

- C'.random = None

### 最終結果
```text
A' → B' → C'
```

random 關係與原串列完全一致，但節點是全新的

---

## ✍️ 我學到的東西 | What I Learned

- LeetCode 138 本質上仍然是 Linked List 題
只是因為多了一個 random 指標，結構不再是單純線性。

- HashMap 是 在走 Linked List 的同時，用來輔助記住「舊節點 → 新節點」的對照關係。

- 這題不能只用傳統的 linked list 複製方式，因為 random 可能指向尚未被複製的節點，必須先建立 mapping，才能正確接指標。

- HashMap 解法的關鍵在於 分兩輪 traversal：

    - 第一輪：只複製節點本身（val），建立對照表

    - 第二輪：利用對照表補上 next 和 random

- 所以這題的本質是：Linked List traversal + HashMap mapping，而不是純 HashMap 題，也不是單純 Linked List 題。

- 當 linked list 題目出現：

    - random

    - 任意指向

    - cross pointer
- 👉 就要立刻想到「需要節點對照關係」

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n)

    - 走 Linked List 兩次

- 空間複雜度：O(n)

    - HashMap 儲存每個節點的對照

---

## 🧠 一句話總結

I traverse the linked list as usual and use a hash map to maintain a mapping from original nodes to copied nodes so that both next and random pointers can be assigned correctly.