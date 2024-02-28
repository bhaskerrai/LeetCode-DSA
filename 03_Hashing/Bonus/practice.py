from typing import List


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    winners = set()
    losers = set()
    one_time_losers = set()

    for w, l in matches:
        
        if w not in one_time_losers and w not in losers:
            winners.add(w)
            

        if l in winners:
            winners.remove(l) 
            one_time_losers.add(l)
        elif l in one_time_losers:
            one_time_losers.remove(l)
            losers.add(l)
        elif l in losers:
            continue
        else:
            one_time_losers.add(l)



    winners = sorted(list(winners))
    one_time_losers = sorted(list(one_time_losers))

    return [winners, one_time_losers]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))