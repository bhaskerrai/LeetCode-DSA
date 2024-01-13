'''
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

 
Example 1:
Input: text = "nlaebolko"
Output: 1
'''


# note: read this article if you find any trouble understanding the solution
from collections import defaultdict

# Approach 1: Counting Characters

def maxNumberOfBalloons(text):
    bCount = 0
    aCount = 0
    lCount = 0
    oCount = 0
    nCount = 0
    
    for i in range(len(text)):
        if text[i] == 'b':
            bCount += 1
        elif text[i] == 'a':
            aCount += 1
        elif text[i] == 'l':
            lCount += 1
        elif text[i] == 'o':
            oCount += 1
        elif text[i] == 'n':
            nCount += 1
    
    lCount = lCount // 2
    oCount = oCount // 2
    
    return min(bCount, min(aCount, min(lCount, min(oCount, nCount))))

# print(maxNumberOfBalloons("nlaebolko"))
# print(maxNumberOfBalloons("loonbalxballpoon"))
# print(maxNumberOfBalloons("leetcode"))

# using hashmap instead of arrays
def maxNumberOfBalloons2(text: str) -> int:
    counts = defaultdict(int)
    ballonChars = set("ballon")

    for char in text:
        if char in ballonChars:
            counts[char] = counts.get(char, 0) + 1


    # as letter 'l' and 'o' must appear twice in order to make an instance of 'ballon' so we do handle these two letters:
    # for char 'l'
    counts['l'] //= 2
    # for char 'o'
    counts['o'] //= 2

    return min(counts['b'], min(counts['a'], min(counts['l'], min(counts['o'], counts['n']))))

print(maxNumberOfBalloons2("nlaebolko"))
print(maxNumberOfBalloons2("loonbalxballpoon"))
print(maxNumberOfBalloons2("leetcode"))
