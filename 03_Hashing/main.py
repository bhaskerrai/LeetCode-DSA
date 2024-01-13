# Example 1: 1. Two Sum
# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

from collections import defaultdict, Counter
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    dict = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in dict:
            return [i, dict[complement]]
        
        dict[num] = i

    return [-1, -1]


# print(twoSum([5, 2, 7, 10, 3, 9], 8))


# If the question wanted us to return a boolean indicating if a pair exists or to return the numbers themselves, then we could just use a set. However, since it wants the indices of the numbers, we need to use a hash map to "remember" what indices the numbers are at.

def twoSum2(nums: List[int], target: int) -> bool:

    my_set = set()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in my_set:
            return True
        
        my_set.add(num)

    return False


# print(twoSum2([5, 2, 7, 10, 3, 9], 8))

def twoSum3(nums: List[int], target: int) -> set:

    my_set = set()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in my_set:
            return {num, complement}
        
        my_set.add(num)

    return {-1, -1}


# print(twoSum3([5, 2, 7, 10, 3, 9], 9))


# Example 2: 2351. First Letter to Appear Twice
# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

def repeatedCharacter(s: str) -> str:
    my_set = set()

    for character in s:

        if character in my_set:
            return character
        
        my_set.add(character)

    return ""


# print(repeatedCharacter("cde"))



# Example 3: Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
def find_numbers(nums: List) -> List:
    my_set = set(nums)

    ans = []

    for num in nums:
        if (num + 1 not in my_set) and (num - 1 not in my_set):
            ans.append(num)

    return ans


# print(find_numbers([1,2,4,5,6,4,8]))



# Counting
'''
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
'''

def find_longest_substring(s, k):
    left = ans = 0
    count = defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans

        

# print(find_longest_substring("eceba", 2))

'''
Example 2: 2248. Intersection of Multiple Arrays
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.
For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''

def intersection(nums: List[List[int]]) -> List[int]:
    counts = defaultdict(int)

    for arr in nums:
        for i in arr:
            counts[i] += 1

    ans = []
    for key in counts:
        if counts[key] == len(nums):
            ans.append(key)
    
    return sorted(ans)
        
# print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,2]]))


'''
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences
Given a string s, determine if all characters have the same frequency.
For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''
def areOccurrencesEqual(s: str) -> bool:
    counts = defaultdict(int)

    for i in s:
        counts[i] += 1
    
    
    # prevCount = counts[s[0]]
    # for key in counts:
    #     if counts[key] != prevCount:
    #         return False
        
    # return True

    # OR
    return len(set(counts.values())) == 1


def areOccurrencesEqual2(s: str) -> bool:
    return len(set(Counter(s).values())) == 1

# print(areOccurrencesEqual2("abacbc"))
# print(areOccurrencesEqual2("aaabb"))



def countSubarraysWithSumK(nums, k):
    counts = {0: 1}  # Initialize counts[0] because an empty prefix has a sum of 0
    
    curr = 0
    total_subarrays = 0
    
    for num in nums:
        curr += num  # Update current prefix sum
        print("\ncurr:",curr)
        print(curr - k)
        print(curr - k in counts)
        print("counts befor:",counts)
        print("total_subarrays before:", total_subarrays)

        
        # Check if (curr - k) has been seen before
        if curr - k in counts:
            # print(counts)
            
            total_subarrays += counts[curr - k]
            print("total_subarrays after:", total_subarrays)

        
        # Update counts map
        counts[curr] = counts.get(curr, 0) + 1
        print(counts)
    
    return total_subarrays

# print(countSubarraysWithSumK([1, 2, 1, 3, 4], 3))




'''
Example 5: 1248. Count Number of Nice Subarrays
Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.
For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1] and [1, 2, 1, 1].
'''
def numberOfSubarrays(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    
    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1

    # print("oK")

    return ans

print(numberOfSubarrays([1, 2, 1, 1, 1], 3))
