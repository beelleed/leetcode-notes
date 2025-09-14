# Method 1: Recursive
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

# Method 2: Iterative + Stack
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        current = root

        while current or stack:
            # 一直向左走，將節點推入 stack
            while current:
                stack.append(current)
                current = current.left
            # 左邊走到底，就從 stack 彈出節點訪問
            current = stack.pop()
            result.append(current.val)
            # 然後去右子樹
            current = current.right

        return result
