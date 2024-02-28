# 1456. Maximum Number of Vowels in a Substring of Given Length
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    ans = len(nums)
    left = 0
    sum = 0
    flag = False
    
    for right in range(len(nums)):
        sum += nums[right]
        print("\nsum:", sum)

        while sum >= target:
            print("-------while chala--------:")
            flag = True
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1
            print("sum hogaya:", sum)
            print("ans hogaya:", ans)
        

    return ans if flag else 0

print(minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))
# print(minSubArrayLen(7, [2,3,1,2,4,3]))
# print(minSubArrayLen(4, [1,4,4]))
# print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen(11, [1,2,3,4,5]))


