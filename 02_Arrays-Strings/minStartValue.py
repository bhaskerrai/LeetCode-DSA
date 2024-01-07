from typing import List

# 1413. Minimum Value to Get Positive Step by Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# Approach 1: Brute Force
def minStartValue(nums: List[int]) -> int:
    # Start with startValue = 1. 
    start_value = 1

    while True:
        totalSum = start_value
        is_valid = True

        for num in nums:
            totalSum += num

            if totalSum < 1:
                is_valid = False
                break

        if is_valid:
            return start_value
        else:
            start_value += 1



# Approach 2: Binary Search
def minStartValue2(nums: List[int]) -> int:
    # Let n be the length of the array "nums", m be the absolute value 
    # of the lower boundary of the element. In this question we have m = 100.
    n = len(nums)
    m = 100

    left = 1
    right = m * n + 1

    while left < right:

        middle = (left + right) / 2
        total = middle
        isValid = True

        for num in nums:
            total += num

            if total < 1:
                isValid = False
                break

        if isValid:
            right = middle

        else:
            left = middle + 1


    # When the left and right boundaries coincide, we have found
    # the target value, that is, the minimum valid startValue.
    return left



# Approach 3: Prefix total
def minStartValue3(nums: List[int]) -> int:
    min_value = total =  0

    for num in nums:
        total += num    
        min_value = min(min_value, total)

    # We have to change the minimum step-by-step total to 1, 
    # by increasing the startValue from 0 to -min_val + 1, 
    # which is just the minimum startValue we want.

    return 1 - min_value

print(minStartValue3([-3,2,-3,4,2]))
print(minStartValue3([1,2]))
print(minStartValue3([1,-2,-3]))

