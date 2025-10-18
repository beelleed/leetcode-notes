# DFS + Preorder
from typing import Optional

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    NULL = "#"

    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                vals.append(Codec.NULL)
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        parts = data.split(",")
        self.index = 0
        def dfs() -> Optional[TreeNode]:
            val = parts[self.index]
            self.index += 1
            if val == Codec.NULL:
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
    
# BFS + Queue
from collections import deque
from typing import Optional

class CodecBFS:
    NULL = "#"

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node:
                vals.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                vals.append(CodecBFS.NULL)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        parts = data.split(",")
        root = TreeNode(int(parts[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < len(parts):
                left_val = parts[i]
                i += 1
                if left_val != CodecBFS.NULL:
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)
            if i < len(parts):
                right_val = parts[i]
                i += 1
                if right_val != CodecBFS.NULL:
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
        return root

    