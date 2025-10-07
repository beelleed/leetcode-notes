class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k: int) -> bool:
            total = 0
            for x in piles:
                total += (x + k - 1) // k
            return total <= h

        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
