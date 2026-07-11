# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 1
        dq = deque()
        while queue:
            node = queue.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            if (not queue) and dq:
                queue = dq
                dq = deque()
                depth +=1
        return depth
            