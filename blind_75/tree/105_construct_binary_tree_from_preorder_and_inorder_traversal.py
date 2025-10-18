from typing import List, Optional

# 樹節點定義
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建一個字典，讓 inorder 值 → index 查找為 O(1)
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        # 遞迴函式，處理 preorder[start_pre : start_pre + size], inorder[start_in : start_in + size]
        def helper(pre_start: int, in_start: int, size: int) -> Optional[TreeNode]:
            if size == 0:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # inorder 中 root 的位置
            root_in_index = inorder_index_map[root_val]
            # 左子樹節點數量 = inorder 中根左邊的節點數
            left_size = root_in_index - in_start
            # 右子樹節點數量 = size - left_size - 1

            # 建立左子樹
            root.left = helper(
                pre_start + 1,
                in_start,
                left_size
            )
            # 建立右子樹
            root.right = helper(
                pre_start + 1 + left_size,
                root_in_index + 1,
                size - left_size - 1
            )

            return root

        return helper(0, 0, len(preorder))
