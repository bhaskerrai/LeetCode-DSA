'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
'''

from collections import deque


class MovingAverage:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        # print(self.queue)


        if self.queue and len(self.queue) > self.size:
            # print("\nye chala")
            self.queue.popleft()
            # print(self.queue)



        ans = 0
        for i in self.queue:
            ans += i

        return ans / len(self.queue)


# OR, 
# this method one has better complexity    
class MovingAverage2:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)

        first = self.queue.popleft() if len(self.queue) > self.size else 0

        self.window_sum = self.window_sum + val - first

        return self.window_sum / len(self.queue)



# Time Complexity: O(1), as we explained in intuition.
# Space Complexity: O(n), where n is the size of the moving window.



# Your MovingAverage object will be instantiated and called as such:
# [[1],[4],[0]]
# obj = MovingAverage2(1)
# param_1 = obj.next(val)
# print(obj.next(4))
# print(obj.next(0))



# obj2 = MovingAverage2(3)
# print(obj2.next(1))
# print(obj2.next(10))
# print(obj2.next(3))
# print(obj2.next(5))



# Approach 3: Circular Queue with Array
# https://leetcode.com/problems/moving-average-from-data-stream/editorial/


class MovingAverage3:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val

        return self.window_sum / min(self.count, len(self.queue))


# obj2 = MovingAverage3(3)
# print(obj2.next(1))
# print(obj2.next(10))
# print(obj2.next(3))
# print(obj2.next(5))


c = 3
a = b = c
print(a, b)  # Output: 0 0

b = 5
print(a, b)  # Output: 5 5 (Both a and b now have the value 5)
