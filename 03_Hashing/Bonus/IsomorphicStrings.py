def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map = {}
    values_mapped = set("")

    for i in range(len(s)):
        ch1 = s[i]
        ch2 = t[i]

        if ch1 in map:
            if map[ch1] != ch2:
                return False
        
        else:
            if ch2 in values_mapped:
                return False
            else:
                map[ch1] = ch2
                values_mapped.add(ch2)
    
    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
print(isIsomorphic("abcd", "dcba"))  # Output: True
print(isIsomorphic("abc", "abcd"))  # Output: False


