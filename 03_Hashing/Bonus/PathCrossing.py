def isPathCrossing1(path: str) -> bool:
    origin = [0, 0]
    curr = [0, 0]

    my_set = set([0, 0])

    opp = {"N": "S", "E": "W", "S": "N", "W":"E"}

    map = {
        'N' : (0, 1),
        'S' : (0, -1),
        'W' : (-1, 0),
        'E' : (1, 0)
    }


    for i in range(len(path)):
        x = path[i]

        curr[0] += map[x][0]
        curr[1] += map[x][1]

        if curr == origin:
            return True

        elif my_set and tuple(curr) in my_set:
            return True 

        elif i > 0 and opp[x] == path[i - 1]:
            return True
        
        my_set.add(tuple(curr))

        
    return False    
        

#Better one
def isPathCrossing(path: str) -> bool:
    my_set = set((0, 0))

    map = {
        'N' : (0, 1),
        'S' : (0, -1),
        'W' : (-1, 0),
        'E' : (1, 0)
    }


    x = 0
    y = 0

    for c in path:
        
        dx, dy = map[c]

        x += dx
        y += dy

        if (x, y) in my_set:
            return True

        my_set.add((x, y))

    return False    
        
print(isPathCrossing("NES"))