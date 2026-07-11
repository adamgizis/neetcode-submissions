# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q1.append(p)
        q2 = deque()
        q2.append(q)

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if not n1 and not n2:
                continue
            if (n1 and not n2) or n2 and not n1:
                return False
            if n1.val != n2.val:
                return False
            if n1:
                q1.extend([n1.left, n1.right])
            if n2:
                q2.extend([n2.left, n2.right])


        return True