class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf')
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev is not None:
                self.min = min(self.min, node.val - self.prev)

            self.prev = node.val

            dfs(node.right)

        dfs(root)
        return self.min