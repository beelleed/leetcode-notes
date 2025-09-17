from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

    # 若要 nodes 可以比較大小，加這 comparator
    def __lt__(self, other: 'ListNode') -> bool:
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 初始化 min-heap，只放非空的頭節點
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, node)

        # dummy 頭節點方便處理
        dummy = ListNode(0)
        current = dummy

        # 當堆還有節點時
        while min_heap:
            smallest_node = heapq.heappop(min_heap)   # 取出最小值節點
            current.next = smallest_node               # 接到結果串列
            current = current.next
            if smallest_node.next:
                heapq.heappush(min_heap, smallest_node.next)  # 推入下一節點

        return dummy.next