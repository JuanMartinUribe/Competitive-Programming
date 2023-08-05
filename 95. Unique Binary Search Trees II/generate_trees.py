# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(arr):
            if not arr:
                return [None]
            ans = []
            for i,num in enumerate(arr):
                left_arr = arr[:i]
                right_arr = arr[i+1:]
                left = backtrack(left_arr)
                right = backtrack(right_arr)
                for l in left:
                    for r in right:
                        cur_node = TreeNode(num)
                        cur_node.left = l
                        cur_node.right = r
                        ans+=[cur_node]
            return ans
        return backtrack(sorted(num for num in range(1,n+1)))

