class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited[0] means not visited, visited[1] means that the node is in the
        # recursion stack, visited[2] means that the node is visited before and not
        # in the recursion stack


        # adj_list, adj_list[i] gives a list of courses that must be taken before i

        visited = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)
        
        def dfs_visit(course):
            # assumes that visited[course]!=1
            if visited[course]==2:
                return True

            visited[course] = 1
            for required in adj_list[course]:
                if visited[required]==1:
                    return False
                elif dfs_visit(required)==False:
                    return False
                # in both the above conditions, a cycle is formed, in both cases courses cannot be completed. Case 1 implies that "course" requires "required" but "required" transitively requires some course that requires "course"
                # case 2 is to check if "required" forms its cycle of its own
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if dfs_visit(course)==False:
                return False
        
        return True


            
                

