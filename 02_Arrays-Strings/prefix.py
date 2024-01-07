# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, 
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, 
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

# prefix = [1, 7, 10, 12, 19, 21]

from typing import List

def answer_queries(nums: List[int], queries: List[int], limit: int) -> List[bool]:
    ans = []

    # for prefix sum
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        print(prefix[y], "-", prefix[x], "+", nums[x], "=", curr, "( curr < limit =", curr < limit, ")" )
        ans.append( curr < limit )
    
    return ans

print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))