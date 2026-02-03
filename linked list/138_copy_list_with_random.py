# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old_to_new = {}

        # 第一輪：複製節點本身
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 第二輪：補 next 和 random
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]
