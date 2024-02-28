from collections import defaultdict
from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    ans = 0
    left = 0
    score = 0
    counts = defaultdict(int)

    for right in range(len(nums)):
        curr = nums[right]
        score += curr
        counts[curr] = counts.get(curr, 0) + 1

        while counts[curr] > 1:
            counts[nums[left]] = counts.get(nums[left], 0) - 1
            score -= nums[left]
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1

        ans = max(ans, score)
    
    return ans

print(maximumUniqueSubarray([4,2,4,5,6]))
print(maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
print(maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))
