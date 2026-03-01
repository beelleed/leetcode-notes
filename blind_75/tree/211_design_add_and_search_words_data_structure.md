# 🧩 LeetCode 211 — Design Add and Search Words Data Structure / 設計可加入與搜尋字詞的資料結構
🔗 [題目連結](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

---

## 📖 題目簡述 | Problem Summary

### **中文**  
設計一個資料結構 `WordDictionary`，支援以下兩個操作：

1. `addWord(word)`：將字串 `word` 加入資料結構中（由小寫英文字母組成）。  
2. `search(word)`：搜尋字串，其中該字串可能包含 `'.'` 通配符，`.` 可匹配任意一個字母。如果存在任一已加入的字詞能符合該模式，則回傳 `True`，否則回傳 `False`。

### **English**  
Design a data structure called `WordDictionary` that supports:

- `addWord(word)`: Adds a word (lowercase letters) into the data structure.  
- `search(word)`: Searches a given word or pattern, where `.` can match any single letter. Return `True` if there is any previously added word matching the pattern.

### Example
- Example:

    - Input

        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    - Output

        [null,null,null,null,false,true,true,true]

    - Explanation
        - WordDictionary wordDictionary = new WordDictionary();
        - wordDictionary.addWord("bad");
        - wordDictionary.addWord("dad");
        - wordDictionary.addWord("mad");
        - wordDictionary.search("pad"); // return False
        - wordDictionary.search("bad"); // return True
        - wordDictionary.search(".ad"); // return True
        - wordDictionary.search("b.."); // return True

---

## 🧠 解法思路 | Approach Overview

這題的核心在於：我們需要一個結構儲存所有加入的單字，並且在 `search()` 時能處理字母與通配符 `.`。常見做法是用 **Trie（字首樹）** 結合 DFS 來處理通配符的分支。

下面有兩種版本：

- **版本 A：不定義 `TrieNode`，用巢狀字典表示 Trie**  
- **版本 B：傳統定義 `TrieNode` 類別，搭配 children 陣列或字典實作 Trie**

兩者在功能上等價，你可以按喜好或面試要求選一種。

---

## 🧱 版本 A：巢狀字典版本
```python
class WordDictionary:
    def __init__(self):
        self.root = {}         # 根節點為空字典
        self.END = True        # 用 True 作為關鍵鍵標記完整詞結尾

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.END] = True

    def search(self, word: str) -> bool:
        def dfs(node: dict, i: int) -> bool:
            if i == len(word):
                return self.END in node
            ch = word[i]
            if ch == '.':
                # 遇到通配符：遍歷所有可能子節點
                for key, child in node.items():
                    if key is not self.END:
                        if dfs(child, i + 1):
                            return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(node[ch], i + 1)

        return dfs(self.root, 0)
```
```python
class WordDictionary:
    def __init__(self):
        self.root = {}         # 用字典當作根節點
        self.END = True        # 特殊鍵：True 作為結尾標記
```
- self.root：整棵字典樹的起點。

- self.END：插入單字後，在最後一層加上 True 當作結尾旗標。

### ➕ addWord(word)
```python
def addWord(self, word: str) -> None:
    node = self.root
    for ch in word:
        if ch not in node:
            node[ch] = {}         # 建立新分支
        node = node[ch]           # 移動到下一層
    node[self.END] = True         # 標記為單字結尾
```
- 建立一條由字母組成的分支鏈。

- 每一層是一個字典（類似 TrieNode），最後加上 END 標記表示完整單字。

### 🔍 search(word)
```python
def search(self, word: str) -> bool:
    def dfs(node: dict, i: int) -> bool:
        if i == len(word):
            return self.END in node  # 是否為完整單字

        ch = word[i]
```
- 遞迴 DFS：i 是目前在字串中比對的位置。

- 若走完整個 word，只要該節點有 END 就回傳 True。

### 📍處理通配符 .
```python
for key, child in node.items():
```

- node 是一個字典。

- .items() 回傳的是目前節點中所有的 key-value 組合。

    - key 是字元（a–z 或 True 作為結尾標記）

    - child 是下一層的字典（代表子 Trie）
```python
if key is not self.END:
```

- self.END 是我們設為 True 的結尾符號，用來標記一個完整字串的終點。

- 我們 不應該對 True 做遞迴，所以要跳過。
```python
if dfs(child, i + 1):
    return True
```

- 對每個子節點遞迴呼叫 dfs，如果任一條路徑成功（整個單字能對應上），就回傳 True。
```python
return False
```

- 如果 26 條路徑都試過了，沒有任何一條成功，那就表示這個通配符無法匹配，回傳 False。

### ▶ else: 普通字元的處理
```python
if ch not in node:
    return False
```

- 如果目前節點中沒有這個字元，那代表這個字無法構成。
```python
return dfs(node[ch], i + 1)
```

- 繼續往下一層遞迴。

```python
return dfs(self.root, 0)
```
- 從根節點開始遞迴搜尋整個字典。

---

## 🔍 範例 | Examples
```python
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

wd.search("bad")   # → True
wd.search(".ad")   # → True
wd.search("b..")   # → True
wd.search("pad")   # → False
```

下面我們逐個 search 調用，模擬 dfs 怎麼走。

### ➤ wd.addWord("bad")

- 插入 “bad” 的過程：

    - node = self.root，起始是空字典 {}

    - 字母 b：'b' not in node → node['b'] = {}，然後 node = node['b']

    - 字母 a：'a' not in node → node['a'] = {}，node = node['a']

    - 字母 d：'d' not in node → node['d'] = {}，node = node['d']

    - 最後：node[self.END] = True，也就是在這裡插入結尾標記

- 那麼 self.root 最後至少會長成（在部分支路）：
```python
{
  'b': {
    'a': {
      'd': {
        True: True
      }
    }
  }
}
```

- 類似地，插入 "dad" 和 "mad" 會在 root 裡建出其他分支。

### ➤ wd.search("bad")

- 呼叫 Search("bad")：

    - dfs(node = root, i = 0)：字元 'b'

        - 'b' 在 root 的 key 中嗎？是 → dfs(node = root['b'], i = 1)

- dfs(node, i = 1)：字元 'a'

    - 'a' 在這層的 key 嗎？是 → dfs(node = that['a'], i = 2)

- dfs(node, i = 2)：字元 'd'

    - 'd' 在這層的 key 嗎？是 → dfs(node = that['d'], i = 3)

- i = 3 == len("bad")，此時就跳到：
```python
return self.END in node
```

- 在這個節點確實有 True 那個鍵 → 回傳 True

### ➤ wd.search(".ad")

- 呼叫 Search(".ad")：

    - dfs(root, i = 0), word[0] = '.'

        - 因為是通配符，會遍歷 root.items() 的所有子鍵（例如 'b', 'd', 'm' 等）

        - 對每一個子節點 child 做 dfs(child, i + 1 = 1)

    - 假設我們走進 'b' 那條分支：

        - dfs(node = root['b'], i = 1), word[1] = 'a' → 必須有 'a' 鍵 → 有的話繼續

        - dfs(node = that['a'], i = 2), word[2] = 'd' → 檢查 'd'

        - dfs(node = that['d'], i = 3) → 檢查 END → 有 → 回傳 True

- 整條路徑找到符合 → search 回傳 True

### ➤ wd.search("b..")

- 呼叫 Search("b..")：

    - dfs(root, i = 0), word[0] = 'b' → 只走到 root['b']

    - dfs(node = root['b'], i = 1), word[1] = '.' → 遍歷這層所有字母鍵

        - 那層可能有 'a'、其他字母鍵，試 dfs(child, i=2)

- 如果試到 'a' 分支：

    - dfs(node at 'a', i = 2), word[2] = '.' → 又通配符

    - 遍歷該節點的子鍵（可能有 'd'）做 dfs(child, i=3)

    - i=3 時檢查 END → 如果該分支有 True → 回傳 True

- 這樣就成功匹配 "bad" 這條路。

### ➤ wd.search("pad")

- 呼叫 Search("pad")：

    - i=0: word[0] = 'p' → 檢查 root 是否有 'p' 鍵

    - 假設沒有 'p' 鍵 → 直接在 dfs 那邊走到：
        ```python
        if ch not in node:
            return False
        ```

- 回傳 False

---

## 🧱 版本 B： TrieNode 
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # a–z 子節點
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if child is not None:
                        if dfs(child, i + 1):
                            return True
                return False
            else:
                idx = ord(ch) - ord('a')
                child = node.children[idx]
                if child is None:
                    return False
                return dfs(child, i + 1)

        return dfs(self.root, 0)
```
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # a–z 子節點
        self.is_end = False
```
- children = [None] * 26：建立一個長度為 26 的陣列，每個位置對應字母 'a' 到 'z' 的子節點。

- is_end = False：布林值，用來標記這個節點是否為一個完整單字的結尾。

```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
```
- WordDictionary 的建構子：建立一個根節點 root，作為整棵 Trie 的起點。

### ➕ addWord(self, word: str)
```python
def addWord(self, word: str) -> None:
    node = self.root
    for ch in word:
        idx = ord(ch) - ord('a')
        if node.children[idx] is None:
            node.children[idx] = TrieNode()
        node = node.children[idx]
    node.is_end = True
```
- 步驟說明：

    1. node = self.root：從根節點開始。

    2. for ch in word:：對每個字母走訪、插入：

        - idx = ord(ch) - ord('a')：把字母 ch 轉成索引 0–25。

        - if node.children[idx] is None:：如果該子節點還沒建立，建立一個新的 TrieNode()。

        - node = node.children[idx]：移動到該子節點，繼續插入下一個字母。

    3. node.is_end = True：插入完成後，把最後一個節點標記為完整單字的結尾。

### 🔍 search(self, word: str) -> bool
```python
def search(self, word: str) -> bool:
    def dfs(node: TrieNode, i: int) -> bool:
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == '.':
            for child in node.children:
                if child is not None:
                    if dfs(child, i + 1):
                        return True
            return False
        else:
            idx = ord(ch) - ord('a')
            child = node.children[idx]
            if child is None:
                return False
            return dfs(child, i + 1)

    return dfs(self.root, 0)
```
- 這段包含遞迴函式 dfs(node, i)，用來比較從位置 i 開始的字串 word[i:] 是否能從 node 這個節點繼續匹配。以下逐段解釋：

### • 基本檢查 / 終止條件
```python
if i == len(word):
    return node.is_end
```
- 若已經比到字串結尾 (i == len(word))，就檢查當前節點 node 是否標記為一個完整單字的結尾 (is_end)。

- 若是結尾則返回 True，否則表示雖然字串走完但這條路不是一個完整單字 → 返回 False。

### • 處理通配符 .
```python
if ch == '.':
    for child in node.children:
        if child is not None:
            if dfs(child, i + 1):
                return True
    return False
```
- 當字元 ch 為 '.' 時，代表這一個位置可以匹配任意字母。

- 所以遍歷 node.children 陣列中的所有非空子節點：

    - 若有任何一條子節點路徑在後續 dfs(child, i+1) 返回 True，表示這條通配路徑可以匹配整個字串 → 整體返回 True。

- 如果所有子節點都試過但都不匹配 → 返回 False。

### • 處理普通字母
```python
else:
    idx = ord(ch) - ord('a')
    child = node.children[idx]
    if child is None:
        return False
    return dfs(child, i + 1)
```
- 若字元 ch 不是 '.'，就按正確字母路徑往下查：

    - 用 idx = ord(ch) - ord('a') 算出索引。

    - child = node.children[idx] 嘗試取得對應子節點。

    - 若該子節點 None → 無此路徑 → 返回 False。

    - 否則繼續 dfs(child, i+1) 比接下來的字元。

### • 呼叫入口
```python
return dfs(self.root, 0)
```
- 從根節點、字串的第 0 個字元開始做 DFS 比對整個字串 word。

---

## 範例 | Examples
```python
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
```
然後做搜尋：

1. wd.search("bad")

    - dfs(root, i=0)：ch = 'b' → idx = 1 → child = root.children[1] 不為 None

    - dfs(child_b, i=1)：ch = 'a' → child_b.children[0]

    - dfs(node_ba, i=2)：ch = 'd' → child_ba.children[3]

    - dfs(node_bad, i=3)：i == len(word) → 回傳 node_bad.is_end → True

2. wd.search(".ad")

    - dfs(root, i=0)：ch = '.' → 遍歷 root.children 所有非 None 子節點（這裡有 b, d, m）

        - 假設先試 b 分支：dfs(child_b, i=1)

    - dfs(child_b, i=1)：ch = 'a' → child_b.children[0]

    - dfs(node_ba, i=2)：ch = 'd' → child_ba.children[3]

    - dfs(node_bad, i=3)：檢查 .is_end → 如果是 True → 回傳 True

3. wd.search("b..")

    - dfs(root, i=0)：ch = 'b' → 走 root.children['b']

    - dfs(child_b, i=1)：ch = '.' → 遍歷 child_b.children → 試 a, …

    - 如果選 a： dfs(node_ba, i=2) → ch = '.' → 遍歷 node_ba.children → 試 d → dfs(node_bad, i=3) → 檢查 .is_end → 成功 → True

4. wd.search("b.d")

    - dfs(root, i=0)：ch = 'b' → 遞下去

    - dfs(child_b, i=1)：ch = '.' → 遍歷子節點

        - 試 a：dfs(node_ba, i=2) → ch = 'd' → 試 node_ba.children['d'] → 有節點 → dfs(node_bad, i=3) → 檢查 .is_end → 得到 True → 回傳 True

5. wd.search("pad")

    - dfs(root, i=0)：ch = 'p' → root.children['p'] 是 None → 直接返回 False

---

## ⏱ 複雜度比較 | Complexity
| 版本             | `addWord` 時間 | `search` 最壞時間（含通配符）         | 空間複雜度                    |
| -------------- | ------------ | --------------------------- | ------------------------ |
| 版本 A（dict）     | (O(L))       | 通配符多時最壞 ~(O(26^k * L)) | 插入總長度空間，dict 節點數量        |
| 版本 B（TrieNode） | (O(L))       | 同樣 ~(O(26^k * L))      | 節點數 × 26 pointers + 標記位元 |

---

## ✍ 我學到了什麼 / What I Learned

- 用巢狀字典可以快速、簡潔地模擬 Trie，不用額外類別結構。

- 定義 TrieNode 版本更具結構性、適合大專案或面試展示架構。

- 處理 '.' 通配符時要用 DFS 分支遍歷所有可能子路徑。

- 在遞迴中要注意 i == len(word) 是 base case 判斷完整詞的標記。