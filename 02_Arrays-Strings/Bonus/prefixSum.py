'''
A prefix sum is a great tool whenever a problem involves sums of a subarray. It only costs O(n) to build but allows all future subarray queries to be 
O(1), so it can usually improve an algorithm's time complexity by a factor of O(n), where n is the length of the array. Let's look at some examples.
'''
from typing import List


nums = [5, 2, 1, 6, 3, 8] #prefix = [5, 7, 8, 14, 17, 25].

prefixSum = [nums[0]]

# print(prefixSum)

for i in range(1, len(nums)):
    prefixSum.append(prefixSum[len(prefixSum) - 1] + nums[i])

# print(prefixSum)


'''
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
'''
def answer_queries(nums, queries, limit):
    ans = []
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[len(prefix) - 1] + nums[i])

    for x,y in queries:
        curr = prefix[y] - prefix[x] + nums[x]            
        ans.append(curr < limit)

    return ans

# print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))



'''
Example 2: 2270. Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
'''
def waysToSplitArray(nums: List[int]) -> int:
    n = len(nums) 
    # prefix = [nums[0]]
    total = sum(nums)
    ans = first = 0

    # for i in range(1, n):
    #     prefix.append(prefix[len(prefix) - 1] + nums[i])

    for i in range(n - 1):
        # first = prefix[i]
        # second = prefix[-1] - prefix[i]

        first += nums[i]
        second = total - first

        if first >= second:
            ans += 1 

    return ans

print(waysToSplitArray([10,4,-8,7]))
print(waysToSplitArray([2,3,1,0]))