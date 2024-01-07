from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:

    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr / k

    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]

        ans = max(ans, curr / k)
    
    return ans

print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))