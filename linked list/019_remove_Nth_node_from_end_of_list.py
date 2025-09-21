from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 建立 dummy 節點以處理要刪除 head 的邊界狀況
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # fast 指針先走 n 步
        for _ in range(n):
            fast = fast.next

        # 若 fast 為 None，代表原本 head 長度等於 n，需要刪除 head
        if not fast:
            return head.next

        # 同時移動 fast 和 slow，直到 fast 到最尾端
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow.next 就是要刪除的節點
        slow.next = slow.next.next

        # 回傳 dummy.next 作為新的 head
        return dummy.next
