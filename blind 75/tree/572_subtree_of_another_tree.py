from typing import Optional

# 定義二元樹節點（假設已有這樣的定義）
class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 如果主樹為空，則無法包含任何非空子樹
        if root is None:
            return False

        # 若從當前節點起的子樹與 subRoot 相同，則成功
        if self.isSameTree(root, subRoot):
            return True

        # 否則嘗試在 root 的左、右子樹繼續尋找
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 若兩個節點皆為空 → 相同
        if p is None and q is None:
            return True
        # 若其中一方為空，或節點值不相等 → 不同
        if p is None or q is None or p.val != q.val:
            return False
        # 否則遞迴比對左右子樹
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))