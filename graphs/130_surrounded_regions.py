# DFS
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != "O":
                return

            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1) 從邊界的 O 出發，把安全的 O 全標成 #
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        # 2) 翻轉：O -> X（被包圍），# -> O（安全）
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

# BFS
from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        queue = deque()

        # 1) 把所有邊界上的 'O' 加進 queue，並標記成 '#'
        for r in range(m):
            if board[r][0] == "O":
                board[r][0] = "#"
                queue.append((r, 0))
            if board[r][n - 1] == "O":
                board[r][n - 1] = "#"
                queue.append((r, n - 1))

        for c in range(n):
            if board[0][c] == "O":
                board[0][c] = "#"
                queue.append((0, c))
            if board[m - 1][c] == "O":
                board[m - 1][c] = "#"
                queue.append((m - 1, c))

        # 2) BFS：把所有與邊界連通的 O 標成 '#'
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))

        # 3) 翻轉結果
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
