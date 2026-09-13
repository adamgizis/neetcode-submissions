import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #shortest path
        pq = []
        #construct the directed graph
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for u,v,t in times:
            adj[u].append((v,t))
        t = n
        heapq.heappush(pq, (0,k))
        visited = set()
        total = 0
        while pq:
            distance, node = heapq.heappop(pq)
            if node in visited:
                continue
            total = max(total, distance)
            visited.add(node)
            for neighbor,time in adj[node]:
                heapq.heappush(pq, (distance + time, neighbor))

        if len(visited) != n:
            return -1

        return total 


        # dijstrka's

        
        