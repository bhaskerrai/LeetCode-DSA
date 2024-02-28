'''
Make The String Great

Solution
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
'''

def makeGood(s: str) -> str:

    stack = []

    for char in s:
        if stack and stack[-1] != char:
            if stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)

        else:
            stack.append(char)

    return "".join(stack)


# print(makeGood("leEeetcode"))
# print(makeGood("abBAcC"))
# print(makeGood("s"))


def makeGood2(s: str) -> str:

    stack = []

    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()

        else:
            stack.append(char)

    return "".join(stack)

print(makeGood2("leEeetcode"))
print(makeGood2("abBAcC"))
print(makeGood2("s"))


# above codes have Time complexity: O(n) and Space complexity: O(n)


# Approach 2: Two pointers, in-place modify


