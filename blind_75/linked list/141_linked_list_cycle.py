class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # 慢指標每次走一步
            fast = fast.next.next    # 快指標每次走兩步

            if slow == fast:         # 若相遇則有環
                return True

        return False                 # 快指標到底，無環