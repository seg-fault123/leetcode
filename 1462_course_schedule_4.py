class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connected = [[False]*numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            connected[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    connected[i][j] = connected[i][j] or  (connected[i][k] and connected[k][j])

        answer = []
        for u, v in queries:
            answer.append(connected[u][v])
        return answer 

