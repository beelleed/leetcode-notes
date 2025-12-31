from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        count = Counter(s)
        n = len(s)
        maxFreq = max(count.values())

        # Feasibility check
        if n - maxFreq < maxFreq - 1:
            return ""

        # Build max heap
        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))

        res = []
        prev_freq, prev_ch = 0, ""

        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch)

            # Push back previous char if still available
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))

            # Use one occurrence of current char
            freq += 1
            prev_freq, prev_ch = freq, ch

        # Safety check
        if prev_freq < 0:
            return ""

        return "".join(res)
