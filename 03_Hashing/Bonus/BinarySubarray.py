from collections import defaultdict
from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    ans = left = 0
    counts = defaultdict(int)

    for right in range(len(nums)):
        currNum = nums[right]
        curr = nums[left:right+1]
        total = sum(curr)

        counts[currNum] = counts.get(currNum, 0) + 1

        if total == goal:
            if len(counts) == 1 and goal < 2:
                ans += counts[currNum]
                print("\n1. ans:", ans)
            else:
                ans += 1
                print("\n2. ans:", ans)

        
        elif total > goal:
            while left < right:
                left += 1
                curr = nums[left:right+1]
                total = sum(curr) 

                if total == goal: 
                    print("Ye chala")
                    ans += 1
                    print("ans bna:", ans)
    
    return ans

# print(numSubarraysWithSum([1,1,1,1,1], 2))
# print(numSubarraysWithSum([0,0,0,0,0], 2))
# print(numSubarraysWithSum([1,1,1,1,1], 1))
# print(numSubarraysWithSum([1,1,1,1,1], 0))
# print(numSubarraysWithSum([0,0,0,0,0], 0))
# print(numSubarraysWithSum([1,0,1,0,1], 2))
print(numSubarraysWithSum([0,1,1,1,1], 3))