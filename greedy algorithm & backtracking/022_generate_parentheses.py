from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left: int, right: int, current: str):
            # 剪枝：非法狀態
            if left > n or right > n or right > left:
                return
            # 基本條件：形成完整合法組合
            if left == n and right == n:
                result.append(current)
                return
            # 遞迴：加入 '('
            backtrack(left + 1, right, current + "(")
            # 遞迴：加入 ')'
            backtrack(left, right + 1, current + ")")

        backtrack(0, 0, "")
        return result