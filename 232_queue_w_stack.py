class MyQueue:

    def __init__(self):
        self.main_stack = []


    def push(self, x: int) -> None:
        temp_stack = []
        while self.main_stack:
            temp_stack.append(self.main_stack.pop())
        temp_stack.append(x)
        while temp_stack:
            self.main_stack.append(temp_stack.pop())
        


    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return len(self.main_stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
