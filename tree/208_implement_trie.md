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

## 🧠 解題思路 | Approach
- ✅ 自定義 TrieNode 類別

- ✅ 或使用 Python 的巢狀字典

### 方法一 : 巢狀字典
1. insert(word)：

    - 從 Trie 的根節點開始，對 word 的每個字元進行：

        - 若該字元不存在於當前字典中，則新增一個空字典。

        - 向下移動至下一層。

    - 最後在該單字的末尾位置，設 cur[True] = True 表示這裡是一個完整單字的結尾。

2. startsWith(prefix)：

    - 從 Trie 的根開始，遍歷 prefix 中每個字元：

        - 若該字元不在當前層字典中，直接返回 False。

        - 否則繼續向下走。

    - 若整個 prefix 都找到，返回 True。

### 方法二 : 資料結構選擇與設計

- 我們用一個 **TrieNode** 類別來代表每個節點。每個節點有：
  1. `children`：通常是一個長度為 26 的陣列或字典，代表 a–z 的子節點  
  2. `is_end_of_word`：一個布林標記，表示這個節點是否是某個完整字串的結尾  

- Trie 本體有一個 `root` 節點，代表空前綴的起點。

---

## 💡 方法一 : 程式碼範例

```python
class Trie:
    def __init__(self):
        self.root = {}
        self.END = True  # 特殊標記，代表某個節點為完整詞結尾

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.END] = True  # 加入結尾標記

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur:
                return False  # 沒有這個字母，單字不存在
            cur = cur[ch]
        return True in cur  # 只有有 True 標記，才算是完整單字

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```
```python
class Trie:
    def __init__(self):
        self.root = {}
```
- 建立 Trie 時初始化一個空字典 self.root，代表字首樹的根節點。

- 這個 self.root 將用來儲存所有單字的開頭。

```python
    def insert(self, word: str) -> None:
        cur = self.root
```
- 每次插入一個單字時，從根節點開始。

- cur 是目前走到的字典位置。

```python
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
```
- 遍歷單字中的每個字元 ch：

    - 如果目前層級 cur 中沒有這個字元，表示這個分支還沒建立 → 新增一個空字典。

    - 然後走到下一層，更新 cur 為 cur[ch]，繼續處理下個字元。

```python
        cur[True] = True
```
- 當整個單字都插入完，代表走到了最後一層。

- 在這一層加上 True: True 作為「完整單字結尾」的標記。
```python
def search(self, word):
    cur = self.root
```
- 初始化一個指針 cur，指向 Trie 的根節點（字典 self.root）。

- 從這個節點出發，逐層往下走。

```python
for ch in word:
    if ch not in cur:
        return False
    cur = cur[ch]
```

- 這段是在一個一個字母地檢查：

    - 以 "apple" 為例，第一輪會檢查 'a' 是否存在於 cur。

    - 若 ch 不在 cur 的 key 中，代表 Trie 裡根本沒有這個字，直接 return False。

    - 如果 ch 存在，則讓 cur = cur[ch]，進入下一層繼續檢查下一個字母。

- 這樣就把 word 從 Trie 的頂端一路「走」下去。

```python
return True in cur
```

- 這行很關鍵！

    - 到這裡表示「這個字每個字母都有在 Trie 裡」。

    - 但！不代表這是完整的單字。

    - 所以我們要檢查：這層是否有 True 這個 key → 是 insert() 時加上的結尾標記。

- 如果有 True，表示「這是完整的單字」，所以回傳 True。
- 如果沒有 True，代表這只是個前綴，像 app 只是 apple 的開頭 → 回傳 False。

```python
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
```
- 搜尋前綴字時，仍然從根節點開始。

```python
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
```
- 檢查 prefix 中的每個字元：

    - 如果該字元不存在於目前節點 → 回傳 False（找不到這個 prefix）

    - 如果存在 → 走進下一層，繼續檢查下一個字元

```python
        return True
```
- 若整個 prefix 都成功走完 → 回傳 True

---

## 📘 範例 | Examples
- 範例一：
```python
trie = Trie()
trie.insert("apple")
```
執行後的 self.root 結構會變成：
```python
{
  'a': {
    'p': {
      'p': {
        'l': {
          'e': {
            True: True
          }
        }
      }
    }
  }
}
```

- 每個字元是一層嵌套字典，最後的 True: True 是單字結尾標記。

- 範例二：
```python
trie.startsWith("app")  # ✅ True
```

- "a" 存在 → 繼續

- "p" 存在 → 繼續

- "p" 存在 → 結束

- 🔚 找到了整個 prefix，回傳 True

- 範例三：
```python
trie.startsWith("bat")  # ❌ False
```

- "b" 不存在於 root → 直接回傳 False

---

## 🧩 時間與空間複雜度 | Time & Space Complexity

| 操作           | 時間複雜度          | 空間複雜度        |
| ------------ | -------------- | ------------ |
| `insert`     | O(L) — L 為單字長度 | O(L) — 新節點空間 |
| `startsWith` | O(L)           | O(1)         |

---

## 📘 學到的東西 | What I Learned

- 巢狀字典可以簡潔地模擬 Trie 結構，不需額外 class。

- node = node[ch] 是在不斷深入 Trie 的每層。

- 使用特殊標記 self.END = True 來記錄完整詞結尾，這樣可以延伸實作 search()。

- 雖然這種寫法簡單，但在大型應用中建議還是用 TrieNode 來增加可維護性。

---

## 💡 方法二 : 程式碼範例 

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