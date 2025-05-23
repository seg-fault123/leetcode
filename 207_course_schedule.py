class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited[0] means not visited, visited[1] means that the node is in the
        # recursion stack, visited[2] means that the node is visited before and not
        # in the recursion stack
        visited = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]

        # adj_list, adj_list[i] gives a list of courses that must be taken before i
        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs_visit(course):
            # assumes that visited[course] is not 2

            if visited[course]==1:
                # means that this node is required to do some other course. But that other course is required for this course. Not possible to complete the courses 
                return False
            
            visited[course] = 1
            for required_course in adj_list[course]:
                if visited[required_course]==2:
                    continue

                if not dfs_visit(required_course):
                    return False
            
            visited[course]=2
            return True
        
        for course in range(numCourses):
            if not (visited[course]==2) and not dfs_visit(course):
                return False
        return True

            
                

