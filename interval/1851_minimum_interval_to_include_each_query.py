import heapq

class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:

        intervals.sort()

        sorted_queries = sorted((query,index) for index,query in enumerate(queries))

        answer = [-1] * len(queries)

        min_heap = []

        i = 0

        for query,index in sorted_queries:

            while (i < len(intervals) and intervals[i][0] <= query
            ):
                left,right = intervals[i]

                size = right-left+1

                heapq.heappush(min_heap, (size,right))

                i += 1

            while (min_heap and min_heap[0][1] < query):
                heapq.heappop(min_heap)

            if min_heap:

                answer[index] = min_heap[0][0]

        return answer

---

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1,r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]