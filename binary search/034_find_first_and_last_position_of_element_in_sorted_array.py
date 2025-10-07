from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst() -> int:
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_pos = mid
                    right = mid - 1  # 繼續向左搜尋
            return first_pos
        
        def findLast() -> int:
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last_pos = mid
                    left = mid + 1  # 繼續向右搜尋
            return last_pos

        first = findFirst()
        if first == -1:
            return [-1, -1]
        last = findLast()
        return [first, last]