from collections import Counter, defaultdict

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    word1_count = defaultdict(int)
    word2_count = defaultdict(int)


    for ch in word1:
        word1_count[ch] = word1_count.get(ch, 0) + 1
    
    for ch in word2:
        word2_count[ch] = word2_count.get(ch, 0) + 1

    # print(word1_count)
    # print(word2_count)

    if set(word1_count.keys()) != set(word2_count.keys()):
        return False
    
    word1_list = sorted(word1_count.values())
    word2_list = sorted(word2_count.values())

    if word1_list != word2_list:
        print("ye chal")
        return False

    return True


# print(closeStrings("abc", "bca"))
# print(closeStrings("a", "aa"))
# print(closeStrings("cabbba", "abbccc"))
# print(closeStrings("uxxa", "abbu"))
print(closeStrings("wxya", "wwxy"))