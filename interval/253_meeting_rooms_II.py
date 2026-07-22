import heapq


class Solution:
    def minMeetingRooms(
        self,
        intervals: List[Interval]
    ) -> int:
        if not intervals:
            return 0

        intervals.sort(
            key=lambda interval: interval.start
        )

        min_heap = []

        for interval in intervals:
            if (
                min_heap
                and min_heap[0] <= interval.start
            ):
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end
            )

        return len(min_heap)