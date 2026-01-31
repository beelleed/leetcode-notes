# Greedy Algorithm
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())
        maxCount = sum(1 for v in count.values() if v == maxFreq)

        return max((maxFreq - 1) * (n + 1) + maxCount, len(tasks))
    
# Heap
from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # max heap: store (-freq, task)
        heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(heap)

        # cooldown queue: (ready_time, -freq, task)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            # 1) if the front task in cooldown is ready, move it back to heap
            if cooldown and cooldown[0][0] == time:
                ready_time, freq, task = cooldown.popleft()
                heapq.heappush(heap, (freq, task))

            # 2) execute one task if available
            if heap:
                freq, task = heapq.heappop(heap)  # freq is negative
                freq += 1  # one execution done: e.g., -3 -> -2

                # if still remaining, push it into cooldown
                if freq != 0:
                    cooldown.append((time + n + 1, freq, task))

        return time
