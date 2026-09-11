from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if len(prerequisites) > numCourses -1:
        #     return []
            
        adj = {}
        for prereq,course in prerequisites:
            if prereq not in adj:
                adj[prereq] = []
            if course not in adj:
                adj[course] = []
            adj[prereq].append(course)
        
        visited_in_path = set() # ne ver visited,
        visited_before = set()
        result = []
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
            result.append(node)
            visited_in_path.remove(node)
            
            return False

        for i in range(0,numCourses):
            if i not in visited_before:
                result.append(i)
                if dfs(i):
                    return []
        
        return result