# 2000. Reverse Prefix of Word

def reversePrefix(word: str, ch: str) -> str:
    wordList = list(word)

    index = 0
    found = False

    while index < len(word):
        if word[index] == ch:
            found = True
            break
        index += 1
    

    if not found:
        return word
    else:
        left = 0
        right = index

        while left < right:
            wordList[left], wordList[right] = wordList[right], wordList[left]
            left += 1
            right -= 1

        return "".join(wordList)


# print(reversePrefix("abcdefd", "d"))



# Approach 2: Using built-in methods of python
def reversePrefix2(word: str, ch: str) -> str:
    
    index = word.find(ch)
    if index == -1:
        return word
    
    segment = word[:index+1]
    reversed_segment = segment[::-1]

    res = reversed_segment + word[index+1:]

    return res
    
    

print(reversePrefix2("abcdefd", "d"))
print(reversePrefix2("xyxzxe", "z"))
print(reversePrefix2("abcd", "z"))
