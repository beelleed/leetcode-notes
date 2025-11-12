# linear
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_range(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end + 1):
                new = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, new
            return prev1
        return max(rob_range(0, n - 2), rob_range(1, n - 1))
# DP
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start: int, end: int) -> int:
            m = end - start + 1
            dp = [0] * (m + 1)
            dp[1] = nums[start]
            for i in range(2, m + 1):
                # nums[start + i - 1] 是第 i 間房子的實際值（因為 nums 是 0-based）
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i - 1])
            return dp[m]

        return max(rob_range(0, n - 2), rob_range(1, n - 1))

