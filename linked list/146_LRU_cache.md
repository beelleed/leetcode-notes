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
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
```
### 🔧 Helper Functions
#### remove(node)：把 node 從 linked list 拿掉
```python
def remove(self, node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```

- 只處理「指標調整」

- O(1)

- 不碰 cache（dict）

#### add_to_head(node)：插到「最近使用」
```python
def add_to_head(self, node):
    node.prev = self.head
    node.next = self.head.next
    self.head.next.prev = node
    self.head.next = node
```

- 插入位置：
```text
head <-> node <-> 原本 head.next
```
#### move_to_head(node)：使用過 → 移到最前面
```python
def move_to_head(self, node):
    self._remove(node)
    self._add_to_head(node)
```

- get / put 更新時都會用

- 表示「最近被使用」

#### pop_tail()：移除最久沒用的 node
```python
def pop_tail(self):
    lru = self.tail.prev
    self._remove(lru)
    return lru
```

- tail.prev 永遠是 LRU

- 回傳該 node，方便從 dict 刪掉

### 🚀 主功能 | Main APIs
#### get(key)
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

#### put(key, value)
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
```python
new_node = Node(key, value)
self.cache[key] = new_node
self._add_to_head(new_node)
```

- 新 key：

    - 建立 node

    - 加到 head（最近使用）
```python
if len(self.cache) > self.capacity:
    lru = self._pop_tail()
    del self.cache[lru.key]
```

- 超過容量：

    - 從 linked list 移除 LRU

    - 從 dict 同步刪掉

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