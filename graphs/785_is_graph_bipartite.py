from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n  # 0: 未染色, 1: 紅色, -1: 藍色

        def dfs(node: int, color: int) -> bool:
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    if not dfs(neighbor, -color):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True

        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
        return True