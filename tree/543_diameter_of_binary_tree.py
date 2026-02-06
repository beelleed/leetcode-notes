class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            # 更新直徑（邊數）
            self.ans = max(self.ans, left + right)

            # 回傳高度
            return 1 + max(left, right)

        depth(root)
        return self.ans
