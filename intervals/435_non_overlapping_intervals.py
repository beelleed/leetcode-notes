from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 按區間結束時間排序
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                # 衝突：刪除當前這個區間
                count += 1
            else:
                # 無衝突：保留當前區間，更新 prev_end
                prev_end = end
        
        return count