# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

from typing import List
def sortedSquares(nums: List[int]) -> List[int]:

    n = len(nums) - 1

    result = [0] * len(nums) #making an array of same length as nums
    left = 0
    right = n

    for i in range(n, -1, -1):
        square = 0
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        
        result[i] = square * square

    return result




print(sortedSquares([-4,-1,0,3,10]))




# slower bcuz O(n^2)
# def old(nums: List[int]) -> List[int]:

    # Squaring
    # for i in range(len(nums)):
    #     nums[i] = nums[i] * nums[i]
    
    # j = 0
    # k = 1

    # sorted = False
    # while j < len(nums):
    #     sorted = False

    #     while k < len(nums):
    #         if nums[j] > nums[k]:
    #             sorted = True
    #             temp = nums[j]
    #             nums[j] = nums[k]
    #             nums[k] = temp
    #         k += 1

    #     j += 1

    #     if sorted == False:
    #         break


    # bubble sort
    # for i in range(len(nums)):
    #     for j in range(0, len(nums)-i-1):
    #         if nums[j] > nums[j+1]:
    #             nums[j], nums[j+1] = nums[j+1], nums[j]

    # return nums

