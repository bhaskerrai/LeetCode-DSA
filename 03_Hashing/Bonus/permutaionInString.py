# def checkInclusion(s1: str, s2: str) -> bool:
#     if len(s1) > len(s2):
#         return False
    
#     s1_count = [0] * 26
#     s2_count = [0] * 26

#     for i in range(len(s1)):
#         s1_count[ord(s1[i]) - ord("a")] += 1
#         s2_count[ord(s1[i]) - ord("a")] += 1

#     left = right = 0
#     # for right in range(1, len(s2)):
#     while right < len(s2):
#         if s1_count == s2_count:
#             return True
        
#         right += 1
#         if right != len(s2):
#             s2_count[ord(s2[right]) - ord("a")] += 1
        
#         s2_count[ord(s2[left]) - ord("a")] -= 1
#         left += 1
    

#     return False

# Using Arrays
def checkInclusion1(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    s1_count = [0] * 26
    s2_count = [0] * 26

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1
    
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    left = 0
    for right in range(len(s1), len(s2)):
        if s1_count == s2_count: return True

        index = ord(s2[right]) - ord("a")
        s2_count[index] += 1
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1


        index = ord(s2[left]) - ord("a")
        s2_count[index] -= 1
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1

        left += 1

        
    return matches == 26



# Using Hashmap
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    s1_count = {}

    for ch in s1:
        s1_count[ch] = s1_count.get(ch, 0) + 1
    
    
    for i in range(len(s2) - len(s1) + 1):
        s2_count = {}

        for j in range(len(s1)):
            s2_count[s2[i + j]] = s2_count.get(s2[i + j], 0) + 1
        
        if match(s1_count, s2_count):
            return True
    
    return False


        
def match(s1_count: dict, s2_count:dict) -> bool:
    for key in s1_count.keys():
        if s1_count[key] - s2_count.get(key, -1) != 0:
            # print("nahi:", False)
            return False
    # print("han:",True)
    return True


    

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("ab", "a"))

    
