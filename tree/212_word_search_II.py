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