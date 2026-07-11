# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def comparsion(n1, n2):
            q1 = deque([n1])
            q2 = deque([n2])
            while q1 or q2:
                n1 = q1.popleft()
                n2 = q2.popleft()
                if not n1 and not n2:
                    continue
                if (n1 and (not n2)) or (n2 and (not n1)):
                    return False
                
                if n1.val != n2.val:
                    return False
                q1.extend([n1.left, n1.right])
                q2.extend([n2.left, n2.right])

            return True

                
        queue = deque([root])
    

        while queue:
            node = queue.popleft()
            if comparsion(node, subRoot):
                return True
            if node.left:

                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        return False
