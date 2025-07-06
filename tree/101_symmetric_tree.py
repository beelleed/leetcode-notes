# Recursive Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        return isMirror(root, root)
  
    
# Iterative Solution
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True
