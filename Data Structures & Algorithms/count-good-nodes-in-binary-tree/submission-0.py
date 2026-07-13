# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        total = 0
        stack.append((root, -101))
        while stack:
            node, m = stack.pop()
            if m <= node.val:
                m = node.val
                total+=1
            if node.left:
                stack.append((node.left, m))
            if node.right:
                stack.append((node.right, m))
        
        return total
        
            