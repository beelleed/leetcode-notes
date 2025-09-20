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
    