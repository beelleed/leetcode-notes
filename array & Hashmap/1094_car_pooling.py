from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001  # locations are within 0..1000

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        curr = 0
        for x in diff:
            curr += x
            if curr > capacity:
                return False

        return True
