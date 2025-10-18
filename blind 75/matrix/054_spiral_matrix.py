from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # 向右遍歷 top 行
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 向下遍歷 right 列
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 向左遍歷 bottom 行（需檢查 row 還沒交錯）
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 向上遍歷 left 列（需檢查 col 還沒交錯）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
