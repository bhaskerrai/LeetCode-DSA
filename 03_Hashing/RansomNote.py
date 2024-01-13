'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
'''


from collections import defaultdict
import collections



# Approach 2: Two HashMaps

# def canConstruct2(ransomNote: str, magazine: str) -> bool:
#     ransomNote_map = defaultdict(int)
#     magazine_map = defaultdict(int)

#     for char in magazine:
#         magazine_map[char] += 1
    
#     for char in ransomNote:
#         ransomNote_map[char] += 1

#     for key in ransomNote_map:
#         if ransomNote_map[key] != magazine_map[key]:
#             return False
    
#     return True



# Approach 3: One HashMap

def canConstruct3(ransomNote: str, magazine: str) -> bool:

    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): 
        return False


    magazine_map = defaultdict(int)

    # for char in magazine:
    #     magazine_map[char] += 1

    # OR
    # In Python, we can use the Counter class. It does all the above work of creating a hashmap and keeping track of frequencies of each element.
    magazine_map = collections.Counter(magazine)
    
    for char in ransomNote:
        if magazine_map[char] <= 0:
            return False
        
        magazine_map[char] -= 1
    
    return True



print(canConstruct3("a", "b")) 
print(canConstruct3("aa", "ab"))
print(canConstruct3("aa", "aab"))
print(canConstruct3("cat", "boxcantop"))
