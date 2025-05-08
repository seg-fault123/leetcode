class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for element in range(asteroids):
            
            current = element
            while stack and current < 0 < stack[-1]:
                if abs(stack[-1]) > abs(current):
                    current = stack.pop()
                elif abs(stack[-1]) < abs(current):
                    stack.pop()
                else:
                    stack.pop()
                    if stack:
                        current = stack.pop()
                    else:
                        current = None
            if current is not None:
                stack.append(current)
        return stack

