class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        heap = []

        # 建立 max-heap（用負號）
        for num in stones:
            heapq.heappush(heap, -num)

        # 只要還有兩顆以上就繼續 smash
        while len(heap) >= 2:
            first = -heapq.heappop(heap)   # 最重
            second = -heapq.heappop(heap)  # 第二重
            remain = first - second

            if remain != 0:
                heapq.heappush(heap, -remain)

        # 最後可能剩 0 或 1 顆
        return -heap[0] if heap else 0
