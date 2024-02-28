from typing import List

# Approach 1: Two HashMaps
def destCity( paths: List[List[str]]) -> str:
    map1 = {}
    map2 = {}

    for x,y in paths:
        map1[x] = 1
        map2[y] = 1

    for y in map2:
        if y not in map1:
            return y


print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["jMgaf WaWA","iinynVdmBz"],[" QCrEFBcAw","wRPRHznLWS"],["iinynVdmBz","OoLjlLFzjz"],["OoLjlLFzjz"," QCrEFBcAw"],["IhxjNbDeXk","jMgaf WaWA"],["jmuAYy vgz","IhxjNbDeXk"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))


# Approach 2: Single HashMap
def destCity2( paths: List[List[str]]) -> str:
    map = {}

    for x in paths:
        map[x[0]] = 1

    for x in paths:
        if x[1] not in map:
            return x[1]
        

# print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
# print(destCity([["jMgaf WaWA","iinynVdmBz"],[" QCrEFBcAw","wRPRHznLWS"],["iinynVdmBz","OoLjlLFzjz"],["OoLjlLFzjz"," QCrEFBcAw"],["IhxjNbDeXk","jMgaf WaWA"],["jmuAYy vgz","IhxjNbDeXk"]]))
# print(destCity([["B","C"],["D","B"],["C","A"]]))
        

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        my_set = set("")

        for x in path:
            if x in my_set:
                return True
            my_set.add(x)

        return False