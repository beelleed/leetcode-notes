# linear
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear_optimized(houses: List[int]) -> int:
            prev1, prev2 = 0, 0
            for money in houses:
                temp = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = temp
            return prev1

        case1 = rob_linear_optimized(nums[:-1])
        case2 = rob_linear_optimized(nums[1:])
        return max(case1, case2)

# DP
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear_dp(houses: List[int]) -> int:
            n = len(houses)
            if n == 0: return 0
            if n == 1: return houses[0]
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]

        case1 = rob_linear_dp(nums[:-1])
        case2 = rob_linear_dp(nums[1:])
        return max(case1, case2)

