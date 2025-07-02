class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)       # 建立虛擬節點，合併結果從 dummy.next 開始
        tail = dummy              # 用 tail 指向目前合併串列的尾端

        while list1 and list2:    # 當兩個 list 都還有節點時
            if list1.val < list2.val:
                tail.next = list1    # 接上 list1 較小的節點
                list1 = list1.next   # list1 指標往前移
            else:
                tail.next = list2    # 接上 list2 較小的節點
                list2 = list2.next   # list2 指標往前移
            tail = tail.next         # 合併串列往前移

        # 把剩下的接上（其中一個會是 None）
        tail.next = list1 if list1 else list2

        return dummy.next         # 回傳真實的合併串列起點