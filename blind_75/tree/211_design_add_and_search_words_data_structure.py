# Method 1: Code Example
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

# Method 2: Code Example
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