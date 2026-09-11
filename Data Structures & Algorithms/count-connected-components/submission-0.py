class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for j,k in edges:
            adj[j].append(k)
            adj[k].append(j)
        
        visited = set()
        num = 0
        for i in range(n):
            if i not in visited:
                stack = [i]
                visited.add(i)
                num +=1
                while stack != []:
                    node = stack.pop()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)

        return num
