# Method 1: Simple Loop
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += (n & 1)
            n >>= 1
        return count

# Method 2: Brian Kernighan's Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
