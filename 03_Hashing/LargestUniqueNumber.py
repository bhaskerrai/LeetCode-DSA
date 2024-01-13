'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

Example 1:
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example
'''


from typing import List

def largestUniqueNumber(nums: List[int]) -> int:

    unique_numbers = set()
    duplicates = set()

    for num in nums:
        if num in duplicates:
            continue

        elif num in unique_numbers:
            unique_numbers.remove(num)
            duplicates.add(num)

        else:
            unique_numbers.add(num)

        
    # if len(unique_numbers) < 1: 
    #OR
    if not unique_numbers:
        return -1
    
    return max(unique_numbers)

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))
