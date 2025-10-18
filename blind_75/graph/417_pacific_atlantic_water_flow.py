class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])                # Top row — Pacific
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row — Atlantic
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])                # Left column — Pacific
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column — Atlantic

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result
