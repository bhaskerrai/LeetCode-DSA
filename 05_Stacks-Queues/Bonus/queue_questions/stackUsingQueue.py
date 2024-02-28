# 225. Implement Stack using Queues

from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while self.q1:
            item = self.q1.popleft()

            if self.q1:
                self.q2.append(item)

        res = item

        while self.q2:
            item = self.q2.popleft()
            self.q1.append(item)

        return res

    def top(self) -> int:
        while self.q1:
            item = self.q1.popleft()
            self.q2.append(item)

        res = item

        while self.q2:
            item = self.q1.popleft()
            self.q2.append(item)

        return res

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()