#　解法一：最大堆（Max Heap）
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))  # 模擬最大堆

        res = []
        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch * (-freq))  # 將字元重複出現次數
        return ''.join(res)


# 解法二：排序搭配 Counter
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return ''.join(ch * freq for ch, freq in sorted_items)


# 解法三：桶排序（Bucket Sort）
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]

        for ch, freq in count.items():
            bucket[freq].append(ch)

        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for ch in bucket[freq]:
                res.append(ch * freq)
        return ''.join(res)