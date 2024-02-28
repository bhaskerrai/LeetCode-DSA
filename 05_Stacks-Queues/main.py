'''
Example 1: 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.
For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.
'''

from collections import deque


def isValid(s: str) -> bool:

    map = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for c in s:
        if c in map:
            stack.append(c)
        
        else:
            if not stack:
                return False

            previousOpening = stack.pop()
            if map[previousOpening] != c:
                return False
            
    return not stack

# print(isValid("(){}[]a"))
# print(isValid("({})"))
# print(isValid("({)}"))
# print(isValid("()"))



'''
Example 2: 1047. Remove All Adjacent Duplicates In String

You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer
'''

def removeDuplicates(s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

# print(removeDuplicates("abbaca"))





'''
Example 3: 844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".
'''

def backspaceCompare(s: str, t: str) -> bool:
    stack1 = []
    stack2 = []

    for c in s:
        if c == "#":
            if stack1:
                stack1.pop()
            else:
                continue
        else:
            stack1.append(c)

    # print(stack1)

    for c in t:
        print(c)
        if c == "#":
            if stack2:
                stack2.pop()
            else:
                continue
        else:
            stack2.append(c)

    # print(stack2)

    return "".join(stack1) == "".join(stack2)


# print(backspaceCompare("ab#c", "ad#c"))
# print(backspaceCompare("a#c", "b"))



def backspaceCompare2(s: str, t: str) -> bool:

    def build(str):
        stack = []

        for c in str:
            if c != "#":
                stack.append(c)
            
            elif stack:
                stack.pop()

        return "".join(stack)


    return build(s) == build(t)


# print(backspaceCompare2("ab#c", "ad#c"))
# print(backspaceCompare2("a#c", "b"))





'''
Example: 933. Number of Recent Calls

Implement the RecentCounter class. It should support ping(int t), which records a call at time t, and then returns an integer representing the number of calls that have happened in the range [t - 3000, t]. Calls to ping will have increasing t.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

'''

class RecentCounter:
    def __init__(self) -> None:
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)

        return len(self.queue)
    

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
# param_1 = obj.ping(1)
# param_1 = obj.ping(100)
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))