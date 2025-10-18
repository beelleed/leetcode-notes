class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Step 1: 轉置（沿主對角線交換）
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: 反轉每一行（左右對調）
        for i in range(n):
            matrix[i].reverse()