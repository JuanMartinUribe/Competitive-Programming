# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def min_depth(node):
            if not node.left and not node.right:
                return 1
            else:
                cur_min = 10**20
                if node.left:
                    left_depth = min_depth(node.left)+1
                    cur_min = min(cur_min,left_depth) 
                if node.right:
                    right_depth = min_depth(node.right)+1
                    cur_min = min(cur_min,right_depth)
                return cur_min
        return min_depth(root)
        