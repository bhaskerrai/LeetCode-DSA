'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:
    left = ans = 0
    counts = defaultdict(int)
    
    for right in range(len(s)):
        curr = s[right]
        counts[curr] = counts.get(curr, 0) + 1

        # print(counts)

        while counts[curr] > 1:
            counts[s[left]] -= 1
            left += 1
        
        ans = max(ans, right - left + 1)

        # print(ans)

    return ans

# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))


'''
Approach 3: Sliding Window Optimized
Intuition
The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. 
Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. 
Then we can skip the characters immediately when we found a repeated character.
'''

def lengthOfLongestSubstring2(s: str) -> int:
    left = ans = 0
    map = defaultdict(int)

    for right in range(len(s)):
        if s[right] in map:
            left = max(map[s[right]], left)
        
        ans = max(ans, right - left + 1)

        map[s[right]] = right + 1

    return ans


print(lengthOfLongestSubstring2("abcabcbb"))
print(lengthOfLongestSubstring2("bbbbb"))
print(lengthOfLongestSubstring2("pwwkew"))
