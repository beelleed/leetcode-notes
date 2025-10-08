from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. 左邊完全在 newInterval 前面的區間，無重疊
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. 合併所有與 newInterval 重疊的區間
        #    當 intervals[i][0] <= newInterval[1] 時，有重疊
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 把合併後的 newInterval 加入
        result.append(newInterval)

        # 3. 加入右側所有不重疊區間
        while i < n:
            result.append(intervals[i])
            i += 1

        return result