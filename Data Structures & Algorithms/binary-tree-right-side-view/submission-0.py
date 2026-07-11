# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = deque()
        lr  = []
        result = [root.val]
        while queue:
            node = queue.popleft()
            if node.left:
                lr.append(node.left.val)
                level.append(node.left)
            if node.right:
                lr.append(node.right.val)
                level.append(node.right)
            if not queue and level:
                result.append(lr[-1])
                queue = level
                level = deque()
                lr = []

        return result
