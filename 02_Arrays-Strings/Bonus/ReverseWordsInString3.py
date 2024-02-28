# 557. Reverse Words in a String III

'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
'''

def reverseWords(s: str) -> str:
    s = s.split(" ")
    
    index = 0
    for word in s:
        wordList = list(word)
        left = 0
        right = len(word) - 1

        while left < right:
            wordList[left], wordList[right] = wordList[right], wordList[left]
            left += 1
            right -= 1

        s[index] = "".join(wordList)
        index += 1

    return " ".join(s)

# print(reverseWords("Let's take LeetCode contest"))


#Approach 2
def reverseWords2(s: str) -> str:
    s = s.split()
    print(s)

    for i in range(len(s)):
        s[i] = s[i][::-1]
    
    return " ".join(s)

print(reverseWords2("Let's take LeetCode contest"))
