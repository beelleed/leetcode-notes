import heapq

class MedianFinder:
    def __init__(self):
        # 大頂堆（存較小一半的數）
        self.max_heap = []  # Python 的 heapq 是 min-heap，存負值模擬 max-heap
        # 小頂堆（存較大一半的數）
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: 放入 max_heap（較小那半）
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Step 2: 平衡兩堆大小
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # 如果總數是偶數：取兩邊堆頂平均
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # 奇數：取 max_heap 頂端（因為它多一個）
        return float(-self.max_heap[0])
