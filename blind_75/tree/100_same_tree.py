class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 若兩者都是 None，代表這部分一致
        if p is None and q is None:
            return True
        # 若其中一個是 None（另一個不是），或兩者的值不同
        if p is None or q is None or p.val != q.val:
            return False
        # 遞迴比較左子樹與右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
