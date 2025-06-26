class DetectSquares:

    def __init__(self):
        self.counts = {}        

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.counts:
            self.counts[tuple(point)] += 1
        else:
            self.counts[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        # check if a valid diagonal point exists
        result = 0
        for element, count_diag in self.counts.items():
            # element = element[0]
            
            if point[0]==element[0] or abs(element[0]-point[0])!=abs(element[1]-point[1]):
                continue
            
            # if a valid diagonal exists, find the other two points and update the result
            point_3 = tuple([element[0], point[1]])
            count_3 = 0
            if point_3 in self.counts:
                count_3 = self.counts[point_3]

            point_4 = tuple([point[0], element[1]])
            count_4 = 0
            if point_4 in self.counts:
                count_4 = self.counts[point_4]

            result += count_diag*count_3*count_4

            
        return result
                      


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
