class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val

            # leaf 判斷（關鍵）
            if node.left is None and node.right is None:
                return current_sum == targetSum

            left = dfs(node.left, current_sum)
            right = dfs(node.right, current_sum)

            return left or right

        return dfs(root, 0)