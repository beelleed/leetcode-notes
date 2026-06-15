class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            kth = groupPrev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:

                temp = curr.next

                curr.next = prev

                prev = curr

                curr = temp

            temp = groupPrev.next

            groupPrev.next = kth

            groupPrev = temp
