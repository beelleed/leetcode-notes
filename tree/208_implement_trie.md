# 📚 LeetCode 208 — Implement Trie (Prefix Tree) / 前綴樹實作
🔗 [題目連結](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

## 📝 題目敘述 | Problem Description

**中文**  
設計一個 Trie（前綴樹）資料結構，支援以下三個操作：

1. `insert(word)`：將字串 `word` 插入 Trie 中。  
2. `search(word)`：判斷字串 `word` 是否已被插入（即為完整單字）。  
3. `startsWith(prefix)`：判斷是否有任何已插入字串以 `prefix` 為前綴。

假設所有輸入都是小寫英文字母 a–z。  

**English**  
Design a Trie (prefix tree) that supports these operations:

- `insert(word)`: Insert a string `word` into the trie.  
- `search(word)`: Return `true` if `word` is in the trie (inserted previously), else `false`.  
- `startsWith(prefix)`: Return `true` if there is any word in the trie that starts with `prefix`.  

All inputs are lowercase English letters (a‑z). :contentReference[oaicite:0]{index=0}

### Examples
- Example 1:

    - Input
        - ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        - [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    - Output
        - [null, null, true, false, true, null, true]

    - Explanation
        - Trie trie = new Trie();
        - trie.insert("apple");
        - trie.search("apple");   // return True
        - trie.search("app");     // return False
        - trie.startsWith("app"); // return True
        - trie.insert("app");
        - trie.search("app");     // return True
    
---

## 🧱 資料結構選擇與設計

- 我們用一個 **TrieNode** 類別來代表每個節點。每個節點有：
  1. `children`：通常是一個長度為 26 的陣列或字典，代表 a–z 的子節點  
  2. `is_end_of_word`：一個布林標記，表示這個節點是否是某個完整字串的結尾  

- Trie 本體有一個 `root` 節點，代表空前綴的起點。

---

## 💡 程式碼範例（Python 實作）

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch: str) -> int:
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = self._char_to_index(ch)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None

    def _search_prefix(self, prefix: str) -> TrieNode | None:
        node = self.root
        for ch in prefix:
            idx = self._char_to_index(ch)
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node
```
### 📦 TrieNode 節點定義
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
```
- children = [None] * 26：使用固定長度為 26 的 list 代表 a-z，每個字元一個位置。None 表示該字元子節點尚未建立。

- is_end = False：當插入的單字在該節點結束時，設為 True，代表這裡是「一個完整單字的結尾」。

### 🌳 Trie 類別的初始化
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```
- 建立 Trie 的主體，只需一個 root，表示整棵字典樹的起點（空字串的前綴）。

### 🔡 將字元轉成索引
```python
def _char_to_index(self, ch: str) -> int:
    return ord(ch) - ord('a')
```
- 將字元 'a'~'z' 轉為對應索引 0~25，方便操作 children 陣列。

### ✏️ 插入 insert(word)
```python
def insert(self, word: str) -> None:
    node = self.root
    for ch in word:
        idx = self._char_to_index(ch)
        if node.children[idx] is None:
            node.children[idx] = TrieNode()
        node = node.children[idx]
    node.is_end = True
```
1. node = self.root：從根節點開始插入字元。

2. 逐一讀取字元 ch：

    - 計算對應索引 idx

    - 若 children[idx] 為 None，表示該字元節點尚未建立 → 建立新 TrieNode。

3. 移動至下一層節點。

4. 插入結束後，將最後節點 is_end = True，表示此路徑對應一個完整單字。

### 🔍 搜尋完整字 search(word)
```python
def search(self, word: str) -> bool:
    node = self._search_prefix(word)
    return node is not None and node.is_end
```
- _search_prefix() 找到最後一個字元對應的節點。

- 若 node 存在且 node.is_end = True → 表示此字存在於 Trie 中。

### 🔍 搜尋前綴 startsWith(prefix)
```python
def startsWith(self, prefix: str) -> bool:
    node = self._search_prefix(prefix)
    return node is not None
```
- 只確認能走完 prefix 對應的節點路徑即可，不需要是完整單字。

### 🔁 搜尋輔助函數 _search_prefix()
```python
def _search_prefix(self, prefix: str) -> TrieNode | None:
    node = self.root
    for ch in prefix:
        idx = self._char_to_index(ch)
        if node.children[idx] is None:
            return None
        node = node.children[idx]
    return node
```
- 從 root 開始，逐個走 prefix 的字元。

- 若中途某個字元對應節點不存在，代表 prefix 不在 Trie 中 → 回傳 None。

- 若成功走完所有字元，回傳當前節點。

---

## 範例 | Example
```python
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True
```
### ✅ Step 1: trie.insert("apple")

建立字典樹如下：
```less
root
 └─ a
     └─ p
         └─ p
             └─ l
                 └─ e (is_end=True)
```

- 每個字元都變成節點，最後 'e' 節點標記 is_end=True 表示這是一個完整單字。

### ✅ Step 2: trie.search("apple")

- 逐一走過 a → p → p → l → e。

- 最後 'e' 是 is_end=True → 回傳 True

### ✅ Step 3: trie.search("app")

- 走過 a → p → p。

- 但最後的 'p' 節點 is_end=False → 不是完整單字 → 回傳 False

### ✅ Step 4: trie.startsWith("app")

- 一樣走過 a → p → p。

- 雖然 'p' 不是 is_end=True，但這是前綴 → 回傳 True

### ✅ Step 5: trie.insert("app")

- 'p' 節點原本就存在，只需設 is_end=True → 表示 "app" 也是一個單字

- 更新後的 Trie 結構：
```less
root
 └─ a
     └─ p
         └─ p (is_end=True)
             └─ l
                 └─ e (is_end=True)
```
### ✅ Step 6: trie.search("app")

- 現在 'p' 的節點是 is_end=True → 回傳 True

---

## ⏱ 複雜度分析 | Complexity
| 操作                   | 時間複雜度  | 原因                         |
| -------------------- | ------ | -------------------------- |
| `insert(word)`       | (O(m)) | 需走過字串長度 (m)，對每個字元做常數操作     |
| `search(word)`       | (O(m)) | 同樣走過字串長度進行查找               |
| `startsWith(prefix)` | (O(p)) | 走過 prefix 長度 (p)           |
| 空間複雜度                | (O(T)) | (T) = 所有插入字串的總長度（每個節點佔用空間） |

---

## ✍ 我學到了什麼 / What I Learned

- Trie（前綴樹）非常適合處理「字串集合 + 前綴搜尋」這類問題

- 用陣列或字典儲存子節點，可以讓每個字元查找為 O(1)

- search 與 startsWith 兩者邏輯非常相似，差別在於 is_end 標記

- 常見面試題：插入、搜尋完整字串、搜尋前綴，這三個操作的實作要清楚、正確