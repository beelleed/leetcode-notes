from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)
        L = len(beginWord)

        # 預處理：建立 pattern（中介樣式）對應表
        for w in wordList:
            for i in range(L):
                pattern = w[:i] + '*' + w[i + 1:]
                pattern_map[pattern].append(w)

        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, steps = queue.popleft()

            if current_word == endWord:
                return steps

            for i in range(L):
                pattern = current_word[:i] + '*' + current_word[i + 1:]
                for nei in pattern_map.get(pattern, []):
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))

        return 0
