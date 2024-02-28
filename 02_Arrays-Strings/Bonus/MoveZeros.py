# 283. Move Zeroes
from typing import List


[0,1,0,3,12]

def moveZeroes(nums: List[int]) -> None:
    left = 0
    right = 1

    while right < len(nums):
        # print("\nleft:", left)
        # print("right:", right)

        if nums[left] == 0 and nums[right] == 0:
            right += 1
            continue
            
        elif nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]
        
        left += 1
        right += 1




nums = [0,1,0,3,12]
# nums = [1,0]
# nums = [2,1]
# nums = [1,0,1]
moveZeroes(nums)
print(nums)