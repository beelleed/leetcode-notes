from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 存放 **索引**，對應 nums 的值會單調遞減
        res = []
        for i, num in enumerate(nums):
            # 移除 deque 前端中已經離開 window 的索引
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 移除 deque 後端所有對應值比 nums[i] 小的索引
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 把當前索引加入 deque
            dq.append(i)

            # 只有當 i >= k - 1，window 完整時才記錄最大值
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res