# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        
        def dfs(r: Optional[TreeNode]):
            if r.left:
                dfs(r.left)
            vals.append(r.val)
            if r.right:
                dfs(r.right)
        
        dfs(root)
        return vals[k-1]



        