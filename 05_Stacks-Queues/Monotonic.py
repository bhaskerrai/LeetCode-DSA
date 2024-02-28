'''
A monotonic stack or queue is one whose elements are always sorted. It can be sorted either ascending or descending, depending on the algorithm. Monotonic stacks and queues maintain their sorted property by removing elements that would violate the property before adding new elements. For example, let's say you had a monotonically increasing stack, currently stack = [1, 5, 8, 15, 23]. You want to push 14 onto the stack. To maintain the sorted property, we need to first pop the 15 and 23 before pushing the 14 - after the push operation, we have stack = [1, 5, 8, 14].

Here's some pseudocode for maintaining a monotonic increasing stack over an input array:

Given an integer array nums

stack = []
for num in nums:
    while stack.length > 0 AND stack.top >= num:
        stack.pop()
    // Between the above and below lines, do some logic depending on the problem
    stack.push(num)

As you can see, before we push a num onto the stack, we first check if the monotonic property would be violated, and pop elements until it won't be.
As we discussed earlier in the sliding window chapter, despite the nested loop, the time complexity is still O(n), where n is the length of the array, because the inner while loop can only iterate over each element once across all for loop iterations, making the for loop iterations amortized O(1).
Monotonic stacks and queues are useful in problems that, for each element, involves finding the "next" element based on some criteria, for example, the next greater element. They're also good when you have a dynamic window of elements and you want to maintain knowledge of the maximum or minimum element as the window changes. In more advanced problems, sometimes a monotonic stack or queue is only one part of the algorithm. Let's look at some examples.
'''


'''
Example 1: 739. Daily Temperatures

Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i thday to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.
'''

from collections import deque
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    ans = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            ans[j] = i - j

        stack.append(i)

    return ans

# print(dailyTemperatures([40, 35, 32, 32, 50]))


'''
Example 2: 239. Sliding Window Maximum

Given an integer array nums and an integer k, there is a sliding window of size k that moves from the very left to the very right. For each window, find the maximum element in the window.

For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return [3, 3, 5, 5, 6, 7]. The first window is [1, 3, -1, -3, 5, 3, 6, 7] and the last window is [1, 3, -1, -3, 5, 3, 6, 7]

Note: this problem is significantly more difficult than any problem we have looked at so far. Don't be discouraged if you are having trouble understanding the solution.
'''


# this method is passing some case, but failing some due to exceeding time limit, so it is a slow algorithm
def maxSlidingWindow0(nums: List[int], k: int) -> List[int]: 
    ans = []
    stack = deque()

    if len(nums) == 1:
        return nums

    for num in nums:
        print("\nnum:", num)
        print("Stack:", stack)

        if len(stack) == k:
            print("if chala")
            ans.append(max(stack))

        while stack and len(stack) > k:
            print("ye chala")
            stack.popleft()
            print(stack)
            ans.append(max(stack))
            print("ans:", ans)

        stack.append(num)
        print(stack)

    if len(stack) > k:
        stack.popleft()
        ans.append(max(stack))
    else:
        ans.append(max(stack))



    return ans



# this algo is fast as has a time complexity of O(n)
def maxSlidingWindow(nums: List[int], k: int) -> List[int]: 
    queue = deque() #this will save indexes not the values
    ans = []

    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        
        queue.append(i)

        if queue[0] + k == i:
            # print("kab chalega ye?")
            queue.popleft()

        if i >= k - 1:
            ans.append(nums[queue[0]])
        

    return ans


# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(maxSlidingWindow([1], 1))
# print(maxSlidingWindow([1,-1], 1))
# print(maxSlidingWindow([9, 11], 2))
# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))




'''
Example 3: 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
'''

def longestSubarray(nums: List[int], limit: int) -> int:
    increasing = deque()
    decreasing = deque()
    left = ans = 0

    for right in range(len(nums)):
        while increasing and nums[right] < increasing[-1]:
            increasing.pop()


        while decreasing and nums[right] > decreasing[-1]:
            decreasing.pop()

        increasing.append(nums[right])
        decreasing.append(nums[right])

        while decreasing[0] - increasing[0] > limit:
            if nums[left] == decreasing[0]:
                decreasing.popleft()
            
            if nums[left] == increasing[0]:
                increasing.popleft()

            left += 1

        ans = max(ans, right - left + 1)

    return ans



print(longestSubarray([1,5,6,7,8,10,6,5,6], 4))
# print(longestSubarray([10,1,2,4,7,2], 5))
# print(longestSubarray([4,2,2,2,4,4,2,2], 0))