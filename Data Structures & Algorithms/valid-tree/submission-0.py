
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        
        for i in range(n):
            adj[i] = []
        for j,k in edges:
            adj[j].append(k)
            adj[k].append(j)


        queue = deque()
        queue.append((0,-1))
        visited = set()
        visited.add(0)

        while queue:
            node,prev = queue.pop()
            
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                else:
                    print(node,prev)
                    return False
        
        
        return len(visited) == n



