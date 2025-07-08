# Method 1: In-order Traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None  # 保存中序遍歷中前一個節點的值

        def inorder(node):
            if not node:
                return True

            # 遞迴左子樹
            if not inorder(node.left):
                return False

            # 中序訪問當前節點，與前一個節點比較
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val  # 更新 prev

            # 遞迴右子樹
            return inorder(node.right)

        return inorder(root)
    
# Method 2: Recursive with Bounds
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)