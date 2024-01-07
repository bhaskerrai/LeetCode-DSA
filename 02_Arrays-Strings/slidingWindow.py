# Example 1: Given an array of positive integers nums and an integer k, 
# find the length of the longest subarray whose sum is less than or equal to k. 
# This is the problem we have been talking about above. We will now formally solve it.

from typing import List

def fn(nums, k):
    left = curr = ans = 0

    for right in range(len(nums)):
        curr += nums[right]

        while curr > k:
            curr -= nums[left]
            left += 1
            print(left)
        
        ans = max(ans, right - left + 1)
        print("answer", "at iteration", right, "is", ans)

    return ans

# print(fn([3, 1, 2, 7, 8, 1, 1, 1, 5], 8))




# Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
# What is the length of the longest substring achievable that contains only "1"?
# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

# Because the string can only contain "1" and "0", another way to look at this problem is "what is the longest substring that contains at most one "0"?". 
# This makes it easy for us to solve with a sliding window where our condition is window.count("0") <= 1. We can use an integer curr that keeps track of how many "0" we currently have in our window.

def fn2(s: str) -> int:
    left = curr = ans = 0

    for right in range(len(s)):
        if s[right] == "0":
            curr += 1

        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)

    return ans

# print(fn2("11001011"))




# Example 3: 713. Subarray Product Less Than K.
# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.
# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:

    if k <= 1:
        return 0
    
    left = ans = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]

        while curr >= k:
            curr //= nums[left]
            left += 1
        
        ans += right - left + 1
    
    return ans
        
        


# print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))



# Fixed window size
# Example 4: Given an integer array nums and an integer k, 
# find the sum of the subarray with the largest sum whose length is k.

def ind_best_subarray(nums, k):

    curr = 0

    for i in range(k):
        curr += nums[i]
    
    ans = curr

    for i in range(k, len(nums)):
        # curr += nums[i]
        # curr -= nums[i - k]
        curr += nums[i] - nums[i - k]

        ans = max(ans, curr)

    return ans

print(ind_best_subarray([3, -1, 4, 12, 8, 5, 6], 4))
