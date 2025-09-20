from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack 用於模擬遞迴中序遍歷
        stack = []
        current = root

        while True:
            # 一直往左走，把節點推進 stack
            while current:
                stack.append(current)
                current = current.left

            # stack 頂端的是當前最小的未訪問節點
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            # 訪問完節點之後轉到它的右子樹繼續
            current = current.right