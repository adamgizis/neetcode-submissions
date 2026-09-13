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
        heapq.heappush(pq, (0,(k,0)))
        visited = set()
        total = 0
        while pq:
            distance, node = heapq.heappop(pq)
            print(distance, node)
            n,prev = node
            if n in visited:
                continue
            total = max(total, distance)
            visited.add(n)
            for neighbor,time in adj[n]:
                heapq.heappush(pq, (distance + time, (neighbor, time)))

        if len(visited) != t:
            return -1

        return total 


        # dijstrka's

        
        