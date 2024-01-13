from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    group = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        group[key].append(s)

    return group.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
    
