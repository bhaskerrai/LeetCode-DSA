# https://www.youtube.com/watch?v=8A3N6HWnWtI

def customSortString(order: str, s: str) -> str:
    map = {}
    s1 = []
    s2 = []

    for ch in order:
        map[ch] = 0

    for ch in s:
        if ch not in map:
            s2.append(ch)
        else:
            map[ch] = map.get(ch, 0) + 1
    

    for ch in order:
        s1.append(ch * map[ch])

    return "".join(s1 + s2)

# print(customSortString("cba", "abcd"))
# print(customSortString("cbafg", "abcd"))
# print(customSortString("kqep", "pekeq"))
# print(customSortString("exv","xwvee"))
# print(customSortString("hucw", "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))



