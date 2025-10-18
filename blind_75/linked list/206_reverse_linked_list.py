# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next     # 暫存下一節點
            curr.next = prev          # 反轉指向
            prev = curr               # 前移 prev
            curr = next_temp          # 前移 curr
        return prev