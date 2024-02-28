'''
Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits

Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.
'''

from collections import defaultdict
from typing import List


def maximumSum(nums: List[int]) -> int:

    map = defaultdict(list)

    def getDigitSum(num: int) -> int:
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        
        return digit_sum
    
    for num in nums:
        digit_sum = getDigitSum(num)
        map[digit_sum].append(num)

    ans = -1
    for key in map:
        curr = map[key]
        if len(curr) > 1:
            curr.sort(reverse=True)
            ans = max(ans, curr[0] + curr[1])
    
    return ans

# print(maximumSum([18,43,36,13,7]))
# print(maximumSum([10,12,19,14]))


'''
This algorithm is inefficient due to the sorting, which can potentially cost O(n⋅logn) if every number in the input has the same digit sum, 
where n is the length of the input array. Just like in the previous problem, we don't need to store all the numbers in the group. 
We can improve the time complexity and average space complexity by only saving the largest number seen so far for each digit sum.
'''

def maximumSum2(nums: List[int]) -> int:
   
    def getDigitSum(num: int) -> int:
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        
        return digit_sum
    

    map = defaultdict(int)
    ans = -1

    for num in nums:
        digit_sum = getDigitSum(num)
        
        if digit_sum in map:
            ans = max(ans, num + map[digit_sum])
        
        map[digit_sum] = max(map[digit_sum], num)
    
    return ans

# print(maximumSum2([18,43,36,13,7]))
# print(maximumSum2([10,12,19,14]))


'''
Just like in the last example, the first algorithm always uses O(n) space because we store all the elements in the hash map's values, 
but with the improvement, the average case will use much less space since each key only stores an integer. 
We also save on an extra iteration and a sort in each iteration, giving us a time complexity of O(n), where n is the length of the input array.
'''
       
        
a = 345
a = str(a)
s = 0
for num in a:
    s += int(num)
print(s)



