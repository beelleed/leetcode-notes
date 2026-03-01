from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x] = number of ways to make amount x
        dp = [0] * (amount + 1)

        # Base case: 1 way to make 0 (choose nothing)
        dp[0] = 1

        # Process coins one by one (this ensures combinations, not permutations)
        for coin in coins:
            # Update dp from coin..amount (unbounded usage of coin)
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]