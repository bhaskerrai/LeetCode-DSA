from collections import defaultdict

def frequencySort(s: str) -> str:
    ans = []
    counts = defaultdict(int)

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    values = sorted(counts.values())

    # for ch in counts.keys():
    #     # max_freq = max(counts.values())
    #     max_freq = max(values)
    #     print("\nvalues:", values)
    #     print(max_freq)

    #     print(ch)
    #     if counts[ch] == max_freq:
    #         # for _ in range(max_freq):
    #         ans.append(ch * max_freq)
    #         # del counts[ch]
    #         values.pop()
    #         print(values)
    #         print(ans)

    while len(values) > 0:
        max_freq = max(values)

        for ch in counts:
            if counts[ch] == max_freq:
                ans.append(ch * max_freq)
                values.pop()
                # print(values)
                # print(ans)



    
    return "".join(ans)


print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))