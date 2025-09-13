class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        while a != b:
            # 如果 a 到尾端了，就切換到 headB 開始；否則往下一個節點
            a = a.next if a else headB
            # 同理處理 b
            b = b.next if b else headA

        return a  # 或 b（a == b）
