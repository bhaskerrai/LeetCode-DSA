from typing import List


def pivotIndex1(nums: List[int]) -> int:

    if len(nums) == 1:
        return 0
    
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[len(prefix) - 1] + nums[i])


    for i in range(len(nums) - 1):
        if i - 1 < 0:
            left = 0
        else:
            left = prefix[i - 1]

        # print("\nleft:", left)

        # if i + 1 > len(nums):
        #     right = prefix[-1]
        # else:
        right = prefix[-1] - prefix[i + 1] + nums[i + 1]

        # print("right:", right)

        if left == right:
            return i


    if prefix[-2] == 0: return len(prefix) - 1
    
    return -1




# Alternatively a more clean and concise code:
def pivotIndex(nums: List[int]) -> int:
    total = leftSum = 0

    for num in nums:
        total += num

    # total = sum(nums)

    # print("sum:", total)

    for i in range(len(nums)):
        # print("\nleftSum:", leftSum)
        # print("nums[i]", nums[i])
        if leftSum == total - leftSum - nums[i]:
            return i

        leftSum += nums[i]

    return -1


print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
print(pivotIndex([-1,-1,0,1,1,0]))
print(pivotIndex([-1,-1,-1,1,1,1]))
print(pivotIndex([-1,-1,-1,-1,-1,0]))
print(pivotIndex([-1,-1,0,1,1,-1]))
print(pivotIndex([0]))