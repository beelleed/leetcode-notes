## DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 交換左右子樹
        root.left, root.right = root.right, root.left
        
        # 遞迴處理左右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

## BFS
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # 交換左右子樹
            node.left, node.right = node.right, node.left
            
            # 將子節點加入隊列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root