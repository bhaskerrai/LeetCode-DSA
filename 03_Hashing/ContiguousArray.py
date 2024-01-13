'''
Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

from typing import List


def find_max_length(nums: List[int]) -> int:
    map = {}  # Use a dictionary for the map
    map[0] = -1  # Initialize with count 0 at index -1
    maxlen = 0
    count = 0

    for i in range(len(nums)):
        count += (1 if nums[i] == 1 else -1)  # Increment or decrement count
        if count in map:
            maxlen = max(maxlen, i - map[count])  # Update maxlen if a subarray with equal 0s and 1s is found
        else:
            map[count] = i  # Store the index of the current count

    return maxlen

# print(find_max_length([1,1]))
# print(find_max_length([0,1,0]))
# print(find_max_length([0,1,1,0,1,1,1,0]))


def fn(nums: List[int]) -> int:
    ans = 0
    count = 0
    map = {}
    map[0] = -1

    for i in range(len(nums)):
        count += (1 if nums[i] == 1 else -1)

        if count in map:
            ans = max(ans, i - map[count])
        else:
            map[count] = i

    return ans


print(fn([0,1]))
print(fn([0,1,0]))
print(fn([0,1,1,0,1,1,1,0]))