'''
325. Maximum Size Subarray Sum Equals k


Given an integer array nums and an integer k, return the maximum length of a 
subarray
 that sums to k. If there is not one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''


from collections import defaultdict
from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:

    map = defaultdict(int)
    map[0] = -1
    total = 0
    ans = 0
    # print(map)

    for i in range(len(nums)):
        total += nums[i]
        # print("\ntotal", total)
        if total - k in map:
            # print("chala")
            # print(total - k)
            # print("index",map[total - k])
            ans = max(ans, i - map[total - k])
            # print(i - map[total - k])
            # print(ans)

        if total not in map:
            map[total] = i

    # print(map)
    return ans



print(maxSubArrayLen([1,-1,5,-2,3], 3))
print(maxSubArrayLen([-2,-1,2,1], 1))

# Test case 2: All positive numbers, k = 3
print(maxSubArrayLen([1, 2, 3, 4], 3))  # Output: 4

# Test case 3: All negative numbers, k = -2
print(maxSubArrayLen([-1, -2, -3], -2))  # Output: 0

# Test case 4: Empty array, k = 0
print(maxSubArrayLen([], 0))  # Output: 0

# Test case 5: Array with one element, k = element
print(maxSubArrayLen([5], 5))  # Output: 1

# Test case 6: Array with elements summing to k, k = sum
print(maxSubArrayLen([1, 2, 1], 4))  # Output: 3

# Test case 7: Array with multiple subarrays summing to k
print(maxSubArrayLen([1, -1, 3, 2, -2, -1, 4], 3))  # Output: 5

# Test case 8: Array with zeros
print(maxSubArrayLen([0, 0, 0, 0], 0))  # Output: 4