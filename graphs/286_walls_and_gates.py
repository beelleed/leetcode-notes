from collections import deque

class Solution:
    def wallsAndGates(self, rooms):

        if not rooms:
            return

        rows = len(rooms)
        cols = len(rooms[0])

        queue = deque()

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))

        while queue:

            r,c = queue.popleft()

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    nr < 0
                    or nc < 0
                    or nr >= rows
                    or nc >= cols
                    or rooms[nr][nc] != 2147483647
                ):
                    continue

                rooms[nr][nc] = rooms[r][c] + 1

                queue.append((nr,nc))

---

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        def addRoom(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            queue.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
