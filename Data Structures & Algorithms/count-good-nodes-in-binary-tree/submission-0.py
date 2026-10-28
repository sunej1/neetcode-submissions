# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(sub: TreeNode, m: int) -> int:
            if sub is None:
                return 0
            count = 0
            if sub.val >= m:
                count += 1
            count += dfs(sub.left, max(m, sub.val))
            count += dfs(sub.right, max(m, sub.val))
            return count
            
        return dfs(root, root.val)
        