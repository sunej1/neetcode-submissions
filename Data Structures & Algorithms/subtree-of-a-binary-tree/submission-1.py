# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isEqual(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                return isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)
                
            return False

        if root:
            if isEqual(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
                

        