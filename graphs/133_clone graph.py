# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS solution for cloning a graph
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]

            clone = Node(current_node.val)
            visited[current_node] = clone

            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

# BFS solution for cloning a graph
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])

        return visited[node]
