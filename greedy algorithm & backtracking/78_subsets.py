# Method 1: Backtracking
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res

# Method 2: Bit Manipulation
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(1 << n):  # 2^n
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
