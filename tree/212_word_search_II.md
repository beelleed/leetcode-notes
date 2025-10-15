# 📘 LeetCode 212 — Word Search II / 字詞搜尋 II
🔗 [題目連結](https://leetcode.com/problems/word-search-ii/)

---

## 🧩 題目說明 | Problem Description
### 中文
給定一個字母方格 `board`（m x n）和一個字詞清單 `words`，找出所有能在 board 上「相鄰移動」組成的字詞（只能上下左右，不能重複使用同一格子）。
### English
Given an m x n board of letters and a list of words, return all words that can be formed by moving to adjacent cells (up/down/left/right). Each cell can only be used once per word.

### Examples
- Example 1:

    ![](../images/212_search1.jpg)

    - Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    - Output: ["eat","oath"]

- Example 2:

    ![](../images/212_search2.jpg)

    - Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    - Output: []

---

## 🔍 解題思路 | Solution Idea

### 🧠 核心方法：Trie + DFS (回溯)

1. **建 Trie 樹**：先將所有 `words` 建成一棵 Trie，利用共用字首節省重複判斷。
2. **對 board 的每個格子進行 DFS**：
   - 從每個格子開始探索，只走在 Trie 裡存在的字首方向。
   - 如果 Trie 節點有 `word` 字詞標記，代表這是一個有效的字詞，加入結果。
   - 為了避免同一格被多次使用，進入遞迴時將該格標記為訪問（如改為 `#`），完成後回溯還原。
   - 若某方向的字母不在 Trie 的子節點，立即剪枝，減少不必要探索。

這樣做可以顯著減少時間複雜度，相比於對每個單字重複 DFS 更有效率。

---

## 💻 程式碼 | Python Code

```python
from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}         # 動態存放子節點
        self.word: Optional[str] = None  # 若該節點對應完整字詞，則存入

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 1️⃣ 將所有 words 插入 Trie
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        rows, cols = len(board), len(board[0])
        res = []

        # 2️⃣ DFS 搜尋函式
        def dfs(r: int, c: int, node: TrieNode):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            ch = board[r][c]
            if ch == "#" or ch not in node.children:
                return

            next_node = node.children[ch]
            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None  # 防止重複加入

             
            board[r][c] = "#" # 標記 visited
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            board[r][c] = ch


        # 3️⃣ 從 board 每格出發做 DFS
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
```
### 1. Trie 節點類別 & 初始化
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word: Optional[str] = None
```
- 功能：定義 Trie 的節點結構。

- children：使用 Python 字典儲存子節點，key 是字母，value 是另一個 TrieNode。

- word：用來儲存完整的字詞（當這個節點標記為某個 words 中的字詞結尾時）。如果這個字段不為 None，代表從 root 到這裡構成了一個可被返回的字詞。

### 2. 建 Trie（插入所有 words）
```python
root = TrieNode()
for w in words:
    node = root
    for ch in w:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.word = w
```
- root = TrieNode()：創立一個空的根節點。

- 對每個字詞 w：

    - 從 root 開始，用 node = root。

    - 對 w 裡的每個字母 ch：

        - 若當前節點的 children 中沒有這個字母鍵，就新增一個 TrieNode。

        - 然後把 node 更新為子節點 node.children[ch]。

    - 最後，在結尾節點設 node.word = w，代表這條路徑對應一個完整字詞。

這樣就把 words 中所有字詞插入 Trie，建構出共用前綴的節點結構。
### 3. 宣告變數、維度與結果容器
```python
rows, cols = len(board), len(board[0])
res = []
```
- rows, cols：記錄 board 的行數與列數。

- res：用來放能在 board 上找到的字詞結果。
### 4. DFS 搜尋函數 dfs(r, c, node)
```python
def dfs(r:int, c:int, node: TrieNode):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return 
    ch = board[r][c]
    if ch == '#' or ch not in node.children:
        return 
```
- 邊界與合法性檢查

    - 檢查 (r, c) 是否越界。如果越界就直接返回（停止此路徑）。

    - ch = board[r][c] 抓當前格子字母。

    - 若 ch == "#"（已訪標記） 或這個字母不在 node.children 中 → 代表該方向不能繼續 → 返回。
```python
next_node = node.children[ch]
if next_node.word is not None:
    res.append(next_node.word)
    next_node.word = None
```
- 當前節點對應一個完整字詞

    - next_node = node.children[ch]：往該字母對應的子節點走。

    - 檢查 next_node.word 是否不為 None：若不為空，表示從 root → … → 這個節點的路徑構成了一個字詞。

    - 將這個字詞加入結果 res.append(...)。

    - 為避免重複加入，再把 next_node.word = None，標記為已被找到過。
```python
board[r][c] = '#'
dfs(r + 1, c, next_node)
dfs(r - 1, c, next_node)
dfs(r, c + 1, next_node)
dfs(r, c - 1, nexT_node)
board[r][c] = ch
```
- 標記與回溯

    - board[r][c] = "#"：把當前格子暫時標記為已訪，用 "#"（或其他符號）避免在同一字詞搜尋中重複使用這個格子。

    - 四個方向遞迴呼叫 dfs(...)：上、下、左、右。參數是新的座標 (r ± 1, c) 或 (r, c ± 1)，且傳入 next_node。

    - 探索完之後回溯：board[r][c] = ch 把該格恢復原本字母，讓後續路徑可以使用它。

### 5. 主循環：從 board 每一格啟動 DFS
```python
for r in range(rows):
    for c in range(cols):
        dfs(r, c, root)
```
- 對 board 上每一個位置 (r, c) 當作起點，呼叫 dfs(r, c, root) 開始尋字。

### 6. 回傳結果
```python
return res
```
- DFS 完成後，res 裡面就放了所有從 board 上能找到的字詞，直接回傳。

---

## 範例 | Example
```python
board = [
  ["a","b","c"],
  ["d","o","e"],
  ["f","g","h"]
]
words = ["abe", "dog", "ado"]
```
### 1. 建 Trie

- 插入 "abe"、"dog"、"ado"

- 最終 Trie 結構（字典表示）可能是：
    ```markdown
    root
    ├─ 'a' → nodeA
    │     ├─ 'b' → nodeAB
    │     │     └─ 'e' → nodeABE (word = "abe")
    │     └─ 'd' → nodeAD
    │           └─ 'o' → nodeADO (word = "ado")
    └─ 'd' → nodeD
        └─ 'o' → nodeDO
                └─ 'g' → nodeDOG (word = "dog")
    ```
- 每個 word 字串插入到對應的節點，並在該節點 word 欄位設為該字串。

### 2. 從 board 每個格子起點 DFS

- 遍歷 board 上每個座標 (i, j)：

    - **起點 (0, 0) = 'a'**

    - 呼叫 dfs(0, 0, root)

        - ch = 'a'，存在於 root.children → next_node = root.children['a']

        - next_node.word 是否不為 None？此時是 None → 沒有直接加入

        - 標記 board[0][0] = "#", 然後探索四個方向

            - 右 → (0,1) char = 'b'

                - 'b' 在 next_node.children 中 → 遞迴

                - 進到 nodeAB

                - next_node.word 還是 None

                - 接著探鄰近方向 → 右 → (0,2) = 'c'

                    - 'c' 不符 → 回去

                    - 下 → (1,1) = 'o'

                        - 'o' 不符 → 回去

                    - 左 / 上 都出界或走過 → 回到 nodeAB

                - 探其它方向 → 往 'e' 那邊要看是否在樹裡，有可能從 (1,2) = 'e'

                    - (1,2) 字母是 'e'，在 nodeAB.children 有 'e' → 進到 nodeABE

                    - nodeABE.word = "abe" 不為 None → 加入 res

                    - 然後設 nodeABE.word = None（避免重複）

                    - 回溯、還原

            - 下 → (1,0) = 'd'

                - 在 nodeA.children 有 'd' → nodeAD

                - 探 'o' →（1,1） = 'o' → nodeADO → word = "ado" → 加入

            - 左 / 上 是無效方向

        - 還原 board[0][0] = 'a'

    - 結果：從起點 (0,0) 找到 "abe" 和 "ado"

    - **起點 (0,1) = 'b'**

        - 呼叫 dfs(0,1, root)

            - ch = 'b'，但 root.children 沒有 'b' → 直接返回，不探索。

    - **起點 (0,2) = 'c'、(1,0) = 'd'、(1,1) = 'o'、(1,2) = 'e'、… 等，都類似地 DFS，但只有在某些能對應 Trie 的路徑才會有結果。**

        - 特別地起點 (1,0)='d'：

            - dfs(1,0, root) → ch = 'd' → 進到 nodeD

            - 探 'o' → (1,1), 再探 'g' → (2,2) 若是 'g' → 找到 "dog"

### 3. 最終結果

- res 可能包含 ["abe", "ado", "dog"]，但實際看 board 能拼哪些。

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
| 項目     | 複雜度                                               |
| ------ | ------------------------------------------------- |
| 時間複雜度  | `O(m * n * 4^L)`，m×n 是 board 大小，L 是單字最大長度（最多分支 4） |
| 建 Trie | `O(W * L)`，W 是字詞數，L 是平均字詞長度                       |
| 空間複雜度  | `O(W * L + m * n)`：Trie 結構 + 遞迴使用的 stack          |

---

## 🧠 我學到的事 | What I Learned

- Trie 是處理大量字詞匹配的利器，尤其當字詞有共通前綴時。

- 使用 DFS 回溯搭配 Trie 可以有效避免重複探索、節省時間。

- 標記 visited 時可以用原地修改（如設為 #）後還原，不必額外空間。

- 若找到字詞後可將 node.word = None 避免重複結果。