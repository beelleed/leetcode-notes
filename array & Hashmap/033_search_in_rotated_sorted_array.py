class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 左半邊是有序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左半邊繼續找
                else:
                    left = mid + 1   # 在右半邊找
            # 右半邊是有序的
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右半邊找
                else:
                    right = mid - 1  # 在左半邊找

        return -1