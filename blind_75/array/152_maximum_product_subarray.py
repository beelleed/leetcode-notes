from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化：以第一個元素為起點
        max_ending = nums[0]
        min_ending = nums[0]
        ans = nums[0]

        # 從第二個元素開始遍歷
        for i in range(1, len(nums)):
            x = nums[i]
            # 暫存上一輪的 max_ending（因為更新 min_ending 時會用到它）
            prev_max = max_ending
            prev_min = min_ending

            # 更新 max_ending、min_ending
            max_ending = max(x, prev_max * x, prev_min * x)
            min_ending = min(x, prev_max * x, prev_min * x)

            # 更新全域答案
            ans = max(ans, max_ending)

        return ans
