# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p,q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p) or (q.val!=p.val) or (q.left and not p.left) or (p.left and not q.left) or (q.right and not p.right) or (p.right and not q.right):
                return False
            left,right = None,None
            if p.left and q.left and p.val==q.val:
                left = dfs(p.left,q.left)
            if p.right and q.right and p.val==q.val:
                right = dfs(p.right,q.right)

            return left!=False and right!=False
        return dfs(p,q)
            