"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # breadth first search
        if not node:
            return 
        queue = deque() # go through bfs to get every node map original to clone, then iterate and add the edges  
        visited = {}
        queue.append(node)
        visited[node.val] = Node(node.val)
        while queue:
            node = queue.popleft()
            if node.val not in visited:
                visited[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, None)
                    queue.append(neighbor)
                n = visited[node.val]
                n.neighbors.append(visited[neighbor.val])
                #add the neighbor as a neighbor

        return visited.get(1, [])   
                
                