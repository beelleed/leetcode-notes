from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1  # 初始化，表示前綴和為 0 的情況

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            sum_freq[prefix_sum] += 1

        return count
