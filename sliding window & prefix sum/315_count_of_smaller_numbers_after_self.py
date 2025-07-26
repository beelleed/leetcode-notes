from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        index = list(range(len(nums)))

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            temp = []
            i, j = start, mid
            right_counter = 0

            while i < mid and j < end:
                if nums[index[j]] < nums[index[i]]:
                    temp.append(index[j])
                    right_counter += 1
                    j += 1
                else:
                    temp.append(index[i])
                    result[index[i]] += right_counter
                    i += 1

            while i < mid:
                temp.append(index[i])
                result[index[i]] += right_counter
                i += 1

            while j < end:
                temp.append(index[j])
                j += 1

            index[start:end] = temp

        merge_sort(0, len(nums))
        return result
