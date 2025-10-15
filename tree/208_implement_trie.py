# Method 1: Code Example
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[True] = True  # 標記完整單字

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur:
                return False  # 沒有這個字母，單字不存在
            cur = cur[ch]
        return True in cur  # 只有有 True 標記，才算是完整單字

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True


# Method 2: Code Example
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