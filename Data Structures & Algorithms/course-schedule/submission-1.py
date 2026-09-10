class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0,1,
        #must take 0 before you take 1
        # 1,0 (0,1) (1,2) (2,0)

        # (0,2) (1,2) (2,3) (3,0) # any cycle is invalid


        # 0: 1
        # 1:0
        # construct the graph
        adj = {}
        for prereq,course in prerequisites:
            if prereq not in adj:
                adj[prereq] = []
            if course not in adj:
                adj[course] = []
            adj[prereq].append(course)
        
        visited_in_path = set() # ne ver visited,
        visited_before = set()

        def dfs(node):
            if node not in adj:
                return False
            if node in visited_in_path: # cycle
                return True
            if node in visited_before: #not a cycle because we've search that all
                return False
            
            visited_in_path.add(node)
            visited_before.add(node)
            for i in adj[node]:
                if dfs(i):
                    return True
            
            visited_in_path.remove(node)
            
            return False

        for i in range(0,numCourses):
            if i not in visited_before:
                if dfs(i):
                    return False
        
        return True


