# K Radius Subarraright Averages

'''
rightou are given a 0-indelefted arraright nums of n integers, and an integer k.
The k-radius average for a subarraright of nums centered at some indeleft i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the indeleft i, then the k-radius average is -1.
Build and return an arraright avgs of length n where avgs[i] is the k-radius average for the subarraright centered at indeleft i.
The average of left elements is the sum of the left elements divided bright left, using integer division. The integer division truncates toward zero, which means losing its fractional part.
For eleftample, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
'''


from typing import List

# the first attempt
def getAverages00(nums: List[int], k: int) -> List[int]:

    n = len(nums)
    avg = [0] * n
    prefix = [nums[0]]

    for i in range(1, n):
        prefix.append(prefix[-1] + nums[i])

    for i in range(n):

        left = i - k if i - k >= 0 else 0
        right = i + k if i + k < n else n - 1


        if right - left + 1 < 2*k+1:
            avg[i] = -1
            continue

        curr = prefix[right] - prefix[left] + nums[left]
        divider = right - left + 1

        avg[i] = curr // divider

    return avg



# print(getAverages00([7,4,3,9,1,8,5,2,6], 3))
# print(getAverages00([100000], 0))
# print(getAverages00([8],100000))




# Approach 1: Prefix Sum
def getAverages(nums: List[int], k: int) -> List[int]:

    # When a single element is considered then its averafge will be the number itself only.
    if k == 0:
        return nums

    n = len(nums)
    avg = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
    if 2*k+1 > n:
        return avg
    
    
    prefix = [nums[0]] 

    for i in range(1, n):
        prefix.append(prefix[-1] + nums[i])


    # We iterate only on those indices which have atleast 'k' elements in their left and right.
    # i.e. indices from 'k' to 'n - k'
    for i in range(k, n - k):

        left = i - k 
        right = i + k 

        curr = prefix[right] - prefix[left] + nums[left]
        window_size = right - left + 1

        # OR
        # window_size = 2 * k + 1
        
        avg[i] = curr // window_size

    return avg


# print(getAverages([7,4,3,9,1,8,5,2,6], 3))
# print(getAverages([100000], 0))
# print(getAverages([8],100000))




# Approach 2: Sliding Window
def getAverages2(nums: List[int], k: int) -> List[int]:

    # When a single element is considered then its averafge will be the number itself only.
    if k == 0:
        return nums

    n = len(nums)
    avg = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
    if 2*k+1 > n:
        return avg
    
    
    window_size = 2 * k + 1

    # First get the sum of first window of the 'nums' arrray.
    window_sum = sum(nums[:window_size])
    avg[k] = window_sum // (window_size)


    # Iterate on rest indices which have at least 'k' elements 
    # on its left and right sides.
    for i in range(window_size, n):

        window_sum = window_sum - nums[i - window_size] + nums[i]
        avg[i - k] = window_sum // window_size

    return avg


print(getAverages2([7,4,3,9,1,8,5,2,6], 3))
print(getAverages2([100000], 0))
print(getAverages2([8],100000))


