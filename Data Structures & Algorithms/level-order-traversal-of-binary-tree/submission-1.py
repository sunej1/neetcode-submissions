from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        sol = []
        while queue:
            level = []
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped.left is not None:
                    queue.append(popped.left)
                if popped.right is not None:
                    queue.append(popped.right)
                level.append(popped.val)
            sol.append(level)
        return sol