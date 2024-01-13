# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List



# Approach #1 Sorting   -> Time complexity : O(n.logn) bucuz of sort() and main loop 
# Space complexity : O(1) or O(n)

def missingNumber1(nums: List[int]) -> int:
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num

# print(missingNumber1([0, 1]))
# print(missingNumber1([3,0,1]))
# print(missingNumber1([9,6,4,2,3,5,7,0,1]))



# Approach #2 HashSet -> Time complexity : O(n + n) => O(n) bucuz of set(nums) and main loop 
# Space complexity : O(n) -> nums contains n−1 distinct elements, so it costs O(n) space to store a set containing all of them.

def missingNumber2(nums: List[int]) -> int:
    nums = set(nums)

    for i in range(len(nums)+1):
        if i not in nums:
            return i
    
# print(missingNumber2([0, 1]))
# print(missingNumber2([3,0,1]))
# print(missingNumber2([9,6,4,2,3,5,7,0,1]))
        

# Approach #3 Bit Manipulation
# samjh nhi aaya tha
        

# Approach #4 Gauss' Formula: Time complexity : O(n) and Space complexity : O(1)
def missingNumber4(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of numbers in the range [0, n]
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(missingNumber4([0, 1]))
print(missingNumber4([3,0,1]))
print(missingNumber4([9,6,4,2,3,5,7,0,1]))
