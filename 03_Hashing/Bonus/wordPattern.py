def wordPattern(pattern: str, s: str) -> bool:
    s = s.split(" ")
    print(s)

    if len(pattern) != len(s):
        return False

    map = {}
    values_mapped = set("")

    for i in range(len(pattern)):
        ch1 = pattern[i]
        ch2 = s[i]

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

print(wordPattern("abba", "dog cat cat dog"))