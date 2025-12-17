from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2

            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    break

            if trips >= totalTrips:
                right = mid   # mid 可行，嘗試更小時間
            else:
                left = mid + 1  # mid 不夠，時間要變大

        return left
