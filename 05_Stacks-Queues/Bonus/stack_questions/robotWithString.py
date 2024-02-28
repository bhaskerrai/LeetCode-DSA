'''
2434. Using a Robot to Print the Lexicographically Smallest String
'''

def robotWithString(s: str) -> str:
    s = list(s)
    t = []
    p = []
    # print(t)
    
    for i in range(len(s)):
        # t.append(s[i])
    
        while t and s[i] > t[-1]:
            p.append(t.pop())

        t.append(s[i])

    print(t)

    while t:
        p.append(t.pop())

    return "".join(p)


# print(robotWithString("zza"))
# print(robotWithString("bac"))
print(robotWithString("bdda"))