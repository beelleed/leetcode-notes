from collections import defaultdict
from typing import List
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]

        # 找到第一個 timestamp > target 的位置
        idx = bisect.bisect_right(arr, (timestamp, chr(127))) - 1

        if idx >= 0:
            return arr[idx][1]
        return ""
