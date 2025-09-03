from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        # First pass: left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result