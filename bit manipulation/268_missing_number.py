# 數學總和法（Gauss' Formula）
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2  # 完整 0~n 的總和
        actual = sum(nums)          # 現有數字總和
        return expected - actual    # 缺失的那個就是差值
    
# XOR
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = 0
        # XOR 所有從 0 到 n 的整數
        for i in range(n + 1):
            missing ^= i
        # 再 XOR nums 中的每個數字
        for num in nums:
            missing ^= num
        return missing