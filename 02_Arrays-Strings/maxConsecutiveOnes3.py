from typing import List

def longestOnes(nums: List[int], k: int) -> int:

    left = ans = zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans
            
# print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
        
# alternative
def longestOnes2(nums: List[int], k: int) -> int:
    left = 0
    for right in range(len(nums)):
        print("\nBefore at right is", right, " and left is", left)

        # If we included a zero in the window we reduce the value of k.
        # Since k is the maximum zeros allowed in a window.
        k -= 1 - nums[right]
        # A negative k denotes we have consumed all allowed flips and window has
        # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
        if k < 0:
            # If the left element to be thrown out is zero we increase k.
            k += 1 - nums[left]
            left += 1
        
        print("left is", left)
        print("right - left + 1:",right - left + 1)
    return right - left + 1


# print(longestOnes2([1,1,1,0,0,0,1,1,0,1,0], 2))
print(longestOnes2([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
