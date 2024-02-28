class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        # print("\npush:")     
        # print(self.stack)
        # print(self.min_stack)
    

    def pop(self) -> None:
        if self.stack:
            poppedElement = self.stack.pop()
            if poppedElement == self.min_stack[-1]:
                self.min_stack.pop()

        # print("\npop:")     
        # print(self.stack)
        # print(self.min_stack)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1] 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(1)
# print(obj.stack)
# print(obj.min_stack)
# param_1 = obj.getMin()
# param_2 = obj.top()
# print(param_1)
# print(param_2)
# obj.pop()
# param_3 = obj.getMin()
# print(param_3)


# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.stack)
# print(obj.min_stack)
# param_1 = obj.getMin()
# obj.pop()
# param_2 = obj.top()
# print(param_1)
# print(param_2)
# param_3 = obj.getMin()
# print(param_3)



# ["MinStack","push","push","push","getMin","pop","getMin"]
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
# print(obj.stack)
# print(obj.min_stack)
param_1 = obj.getMin()
obj.pop()
param_2 = obj.top()
print(param_1)
print(param_2)
param_3 = obj.getMin()
print(param_3)


