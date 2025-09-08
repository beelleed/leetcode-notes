class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        tail = prev.next
        for _ in range(right - left):
            temp = tail.next
            tail.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
