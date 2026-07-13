# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        #last left, last right, node
        stack.append((-1001, 1001, root))
        while stack:
            last_left, last_right, node = stack.pop()
            if not (node.val > last_left and node.val < last_right):
                print(node.val)
                return False
            if node.left:
                stack.append((last_left, node.val, node.left))
            if node.right:
                stack.append((node.val,last_right, node.right))


        return True
            