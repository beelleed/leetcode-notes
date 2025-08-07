class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}         # 初始前綴和 0 在 -1 處先出現
        sum = 0              # running sum，以 +1 為 1，-1 為 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                sum += 1
            else:
                sum -= 1

            if sum in mp:  # 曾出現過 same sum
                max_len = max(max_len, i - mp[sum])
            else:
                mp[sum] = i  # 第一次出現 sum

        return max_len