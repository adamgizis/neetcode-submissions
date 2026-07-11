# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        it = root
        while it:
            if p.val > it.val and q.val > it.val:
                it = it.right
            elif p.val < it.val and q.val < it.val:
                it = it.left
            else:
                return it
        
        return it