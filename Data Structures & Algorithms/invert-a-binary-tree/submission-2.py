# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            #swap left and right
            t = node.left
            node.left = node.right
            node.right = t
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root