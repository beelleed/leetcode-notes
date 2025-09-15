from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: List[int] = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            # 遍歷當前層，記錄最後一個節點的值（最右邊那個）
            for i in range(level_size):
                node = queue.popleft()
                # 當 i 是這層的最後一個 index，就把它加入 result
                if i == level_size - 1:
                    result.append(node.val)
                # 左、右孩子依序加入，供下一層使用
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
