# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        # 如果 root 本身就是 p 或 q，直接回傳 root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p, q 分別在左右子樹 -> root 是 LCA
        if left is not None and right is not None:
            return root

        # 否則回傳存在的那一邊（可能是 p/q 或 LCA）
        return left if left is not None else right
