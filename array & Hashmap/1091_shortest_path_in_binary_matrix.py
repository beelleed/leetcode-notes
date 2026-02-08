from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 起點或終點被擋住，直接不可能
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 個方向
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque()
        queue.append((0, 0, 1))  # (row, col, path_length)

        # 標記已訪問（直接改 grid）
        grid[0][0] = 1

        while queue:
            r, c, dist = queue.popleft()

            # 到達終點
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1
