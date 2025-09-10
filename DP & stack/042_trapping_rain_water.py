from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:              # 若長度小於等於 2，無法凹槽，回傳 0
            return 0

        left_max = [0] * n      # 初始化左邊最大值陣列
        right_max = [0] * n     # 初始化右邊最大值陣列
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        # 從左到右填充 left_max
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # 從右到左填充 right_max
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        # 計算每個位置能接多少水
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water