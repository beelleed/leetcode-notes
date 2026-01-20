# 🗂️ LeetCode 146 — LRU Cache / 最近最少使用快取

🔗 [題目連結](https://leetcode.com/problems/lru-cache/) 

---

## 📄 題目說明 | Problem Description

### 中文：
- 請設計一個 LRU Cache（Least Recently Used Cache），支援以下操作，且每個操作時間複雜度必須是 O(1)：

    - get(key)

        - 若 key 存在，回傳 value，並將該 key 視為「最近使用」

        - 若不存在，回傳 -1

    - put(key, value)

        - 插入或更新 key

        - 若超過容量，移除「最久沒被使用」的 key

### English:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Both get and put must run in O(1) time.

---

## 🧠 解題思路 | Solution Idea

- 這題的核心需求是：

| 操作  | 需求                    |
| --- | --------------------- |
| get | O(1) 找資料 + 更新使用順序     |
| put | O(1) 插入 / 更新 + 移除最舊資料 |

👉 單用 dict 不夠（無法維持順序）

👉 單用 list 不夠（刪除中間元素不是 O(1)）

### ✅ 正確組合

HashMap + Doubly Linked List

---

## 🧩 資料結構設計 | Data Structure Design
### 1️⃣ HashMap（dict）
```python
self.cache = {}  # key -> Node
```

- 用途：

    - O(1) 找到某個 key 對應的 node

### 2️⃣ Doubly Linked List（雙向鏈結串列）
```text
head <-> node1 <-> node2 <-> ... <-> tail
```

- head.next：最近使用（Most Recently Used, MRU）

- tail.prev：最久沒用（Least Recently Used, LRU）

- 為什麼要雙向？

    - O(1) 移除任意節點（不用從頭找）

### 3️⃣ Dummy Head / Tail（假節點）
```python
self.head = Node(0, 0)
self.tail = Node(0, 0)
```

- 好處：

    - 不用處理空串列、單節點的 edge case

    - 插入與刪除邏輯一致

---

## 💻 程式碼 | Code (Python)
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)
    
    def pop_tail(self):
        lru = self.tail.prev
        self.remove(lru)
        return lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_to_head(new_node)
        
        if len(self.cache) > self.capacity:
            lru = self.pop_tail()
            del self.cache[lru.key]
```

  
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### 0️⃣ 先建立心智模型：兩個結構一起用
#### ✅ HashMap：self.cache

- key -> Node

- 目的：O(1) 找到某個 key 對應的節點（不用從 linked list 慢慢找）

#### ✅ Doubly Linked List：head <-> ... <-> tail

- 目的：O(1) 維持「最近使用順序」

- 規則（你這份程式碼的定義）：

    - head.next = 最近使用 (MRU)

    - tail.prev = 最久沒用 (LRU)

#### ✅ Dummy head / tail 的好處

- 你永遠不需要特判：
    - list 是空的

    - node 是第一個

    - node 是最後一個

- 因為 head/tail 永遠存在。
#### 1️⃣ Node 類別：為什麼要存 key？
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```
- key：用在 eviction（移除 LRU）時，能從 dict 刪掉：
    ```python
    del self.cache[lru.key]
    ```

    - 如果 Node 不存 key，你就不知道要從 dict 刪哪個 key。

- prev/next：雙向鏈結，讓你 O(1) 移除任意節點。
#### 2️⃣ 初始化：把 head/tail 先串起來
```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
```

**關鍵點**

- 所有新 Node 一開始就是
    ```text
    prev = None
    next = None
    ```

- 所以當你寫：
    ```python
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    ```

- 此時實際狀態是：
    ```text
    head.prev = None
    head.next = None

    tail.prev = None
    tail.next = None
    ```

```python
self.head.next = self.tail
self.tail.prev = self.head
```

-  self.head.next = self.tail

    - 只設定 head 的 next

    - 沒有動到 head.prev

    - 所以：
        ```text
        head.prev = None   ← 仍然是 None
        head.next = tail
        ```
-  self.tail.prev = self.head

    - 只設定 tail 的 prev

    - 沒有動到 tail.next

    - 所以：
        ```text
        tail.prev = head
        tail.next = None   ← 仍然是 None
        ```
### 🔧 Helper Functions
#### 3️⃣ remove(node)：把 node 從 linked list 拿掉
```python
def remove(self, node):
    prev_node = node.prev  # A
    next_node = node.next  # B
    prev_node.next = next_node  # A.next = B
    next_node.prev = prev_node  # B.prev = A
```
假設目前是：
```text
A <-> node <-> B
```

- node.prev = A
- node.next = B

remove 後要變成：
```text
A <-> B
```
✅ node 就被「跳過」了（node 自己的 prev/next 沒清掉也沒關係，因為我們不會再靠它走）

#### 4️⃣ add_to_head(node)：插到「最近使用」
```python
def add_to_head(self, node):
    node.prev = self.head          # node.prev 指向 head
    node.next = self.head.next     # node.next 指向原本的 first
    self.head.next.prev = node     # 原本 first.prev 改指向 node
    self.head.next = node          # head.next 改成 node
```
#### 先建立「插入前」的畫面（非常重要）

假設目前 linked list 是這樣（最典型的情況）：
```text
head <-> first <-> second <-> tail
```

對應指標關係是：
```text
head.next = first
first.prev = head
first.next = second
second.prev = first
second.next = tail
tail.prev = second
```

現在，我們要把 node 插到 head 和 first 中間，變成：
```text
head <-> node <-> first <-> second <-> tail
```
#### 🔹 第 1 行
```python
node.prev = self.head
```
意思是：

「先告訴 node：你的前一個是 head」

此時指標變成（只畫有改的）：
```text
node.prev → head
```
⚠️ 注意：

- 這一行 沒有改任何原本串列的指標

- 現在只是 node 自己「記得」誰在前面

- 串列目前還是：
```text
head <-> first <-> second <-> tail
```
#### 🔹 第 2 行
```python
node.next = self.head.next
```

因為：
```python
self.head.next == first
```

所以這行等於：
```python
node.next = first
```

現在 node 變成：
```text
head <- node -> first
```

- 但注意 ⚠️

**first 還不知道 node 的存在**

此時的關係是：
```text
node.prev = head
node.next = first

head.next = first
first.prev = head   # 還沒改！
```
#### 🔹 第 3 行（這一行是關鍵轉折點）
```python
self.head.next.prev = node
```

- 拆開來看：

    - self.head.next 是 first

    - 所以這行其實是：
        ```python
        first.prev = node
        ```

現在，first 終於「知道」node 在它前面了。

此時指標狀態：
```text
head -> first
first.prev = node
node.next = first
node.prev = head
```

目前「邏輯上」其實已經像這樣了：
```text
head <- node -> first
```

但還差最後一步。

#### 🔹 第 4 行（正式接上 head）
```python
self.head.next = node
```

- 也就是：
```python
head.next = node
```

現在整條鏈正式變成：
```text
head <-> node <-> first <-> second <-> tail
```

而且每個 prev / next 都是對的。

**為什麼順序一定要這樣寫？**
❓ 如果你先寫這行會怎樣？
```python
self.head.next = node
```

那 first 就會「暫時消失」：
```text
head -> node
first.prev 還指向 head（錯）
```

- 接下來你再想補 first.prev，就會：

    - 找不到原本的 first

    - 或造成指標斷裂

👉 Linked list 操作最怕「中途斷鏈」

用一句話記這四行

>>先接 node 自己的 prev / next，再修原本節點的指標，最後才動 head 的 next。

把四行濃縮成「每行的角色」
| 行數 | 做的事                 | 白話              |
| -- | ------------------- | --------------- |
| 1  | `node.prev = head`  | 告訴 node：你前面是誰   |
| 2  | `node.next = first` | 告訴 node：你後面是誰   |
| 3  | `first.prev = node` | 告訴 first：你前面換人了 |
| 4  | `head.next = node`  | 告訴 head：你後面換人了  |


#### 5️⃣ move_to_head(node)：使用過 → 移到最前面
```python
def move_to_head(self, node):
    self.remove(node)
    self.add_to_head(node)
```
- 先把 node 從原位置拔掉

- 再插到 head 後面

- 代表「我剛用過它」
#### 6️⃣ pop_tail()：移除最久沒用的 node
```python
def pop_tail(self):
    lru = self.tail.prev
    self.remove(lru)
    return lru
```
- 因為你定義：

    - tail.prev 永遠是 最久沒用

    - 所以直接拿 tail.prev 就是 LRU

- 注意：如果只有 head<->tail（空的），那 tail.prev 是 head，但實際不會發生，因為只有超容量時才 pop。
### 🚀 主功能 | Main APIs
#### 7️⃣ get(key)
```python
def get(self, key: int) -> int:
    if key not in self.cache:
        return -1

    node = self.cache[key]
    self._move_to_head(node)
    return node.value
```
邏輯說明

- 不存在 → -1

- 存在：

    - 代表「剛被使用」

    - 移到 head

    - 回傳 value

#### 8️⃣ put(key, value)
#### 情況 A：key 已存在（更新）
```python
def put(self, key: int, value: int) -> None:
    if key in self.cache:
        node = self.cache[key]
        node.value = value
        self._move_to_head(node)
        return
```

- 已存在：

    - 更新 value

    - 移到最前（最近使用）
#### 情況 B：key 不存在（插入新 node）
```python
new_node = Node(key, value)
self.cache[key] = new_node
self._add_to_head(new_node)
```

- 新 key：

    - 建立 node

    - 加到 head（最近使用）
#### 插入後可能超容量 → eviction
```python
if len(self.cache) > self.capacity:
    lru = self._pop_tail()
    del self.cache[lru.key]
```

- 超過容量：

    - 從 linked list 移除 LRU（O(1)）

    - 從 dict 同步刪掉（O(1)）

---

## 🧪 範例流程 | Example Walkthrough（照程式碼跑）

假設：
```text
capacity = 2
```
#### put(1,1)
```text
head <-> (1) <-> tail
cache = {1}
```
#### put(2,2)
```text
head <-> (2) <-> (1) <-> tail
cache = {1,2}
```
#### get(1)

- key 存在

- move_to_head(1)
```text
head <-> (1) <-> (2) <-> tail
```

回傳 1

#### put(3,3)（超過容量）

- 插入 3
```text
head <-> (3) <-> (1) <-> (2) <-> tail
```

- pop_tail → 移除 (2)
```text
head <-> (3) <-> (1) <-> tail
cache = {1,3}
```
#### get(2)

- 不存在 → -1

---

## ⏱ 複雜度分析 | Complexity Analysis
| 操作  | 時間   |
| --- | ---- |
| get | O(1) |
| put | O(1) |

- HashMap：O(1) lookup

- Doubly Linked List：O(1) insert / delete

- 空間複雜度：O(capacity)

---

## ✍️ 我學到的東西 | What I Learned

- LRU Cache 是「資料結構設計題」，不是演算法題

- dict + doubly linked list 是黃金組合

- Dummy head / tail 可以讓程式碼大幅簡化

- 所有操作都只做「指標操作」，才能保證 O(1)

---

## 🧠 面試一句話總結

I use a hash map for O(1) access and a doubly linked list to maintain the usage order.

The head represents the most recently used item, and the tail represents the least recently used one.