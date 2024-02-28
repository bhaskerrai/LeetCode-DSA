'''
Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
'''

from collections import deque

# the below approach is good but it failed at some last cases due to Time Limit Exceeded (88 / 99 testcases passed)
class StockSpanner1:

    def __init__(self):
        # self.val = []
        self.queue = deque()

        
    def next(self, price: int) -> int:
        # print("\nfor price:", price)
        # self.val.append(price)
        
        for num in self.val:
            while self.queue and price < self.queue[-1]:
                self.queue.popleft()
            
            self.queue.append(num)

    
        span = 1  # Initialize span to 1 (at least the current day)
        
        while self.queue and price >= self.queue[-1][0]:
            span += self.queue.pop()[1]

        self.queue.append((price, span))  # Store both price and span
        
        return span



class StockSpanner:

    def __init__(self):
        # self.val = []
        self.queue = deque()

        
    def next(self, price: int) -> int:
        print("\nfor price:", price)
        # self.val.append(price)
        
        span = 1  # Initialize span to 1 (at least the current day)
        
        while self.queue and price >= self.queue[-1][0]:
            span += self.queue.pop()[1]

        # print("(price, span):", (price, span))
        self.queue.append((price, span))  # Store both price and span
        print(self.queue)
        
        return span

# [[],[29],[91],[62],[76],[51]]


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
# param_1 = obj.next(price)
# print(obj.next(100))
# print(obj.next(80))
# print(obj.next(60))
# print(obj.next(70))
# print(obj.next(60))
# print(obj.next(75))
# print(obj.next(85))

# [[],[29],[91],[62],[76],[51]]
print(obj.next(29))
print(obj.next(91))
print(obj.next(62))
print(obj.next(76))
print(obj.next(51))
