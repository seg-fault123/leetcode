class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visited = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)
        
        def dfs_visit(course):
            if visited[course]==2:
                return True
            
            visited[course] = 1
            for required in adj_list[course]:
                if visited[required]==1 or not dfs_visit(required):
                    return False
            
            visited[course] = 2
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs_visit(course):
                return []
        
        return result
