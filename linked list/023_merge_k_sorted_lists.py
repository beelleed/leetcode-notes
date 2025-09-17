from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ✅ 初始化 heap
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                # 💡 使用 (val, index, node) 避免 TypeError
                heapq.heappush(min_heap, (node.val, i, node))

        # ✅ 建立結果 linked list 的 dummy 起點
        dummy = ListNode()
        curr = dummy

        # ✅ 每次取出最小節點，加入結果串列
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            # ✅ 如果有下一個節點，就加入 heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next