'''
Find Players With Zero or One Losses

Solution
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
'''


from collections import defaultdict
from typing import List

'''

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    losers = defaultdict(int)
    loser = []
    winner = []

    for match in matches:
        losers[match[1]] += 1

    print(losers)

    for player in matches:
        # print("\nplayer[0] not in losers:", player[0] not in losers)
        if player[0] not in losers:
            # print("appending", player[0], "to winner...")
            winner.append(player[0])
        
            # print("winner:", winner)
        
        # print("\nlosers[player[1]] == 1:", losers[player[1]] == 1)
        if losers[player[1]] == 1:
            # print("appending", player[1], "to loser...")
            loser.append(player[1])
        
            # print("loser:", loser)

    loser.sort()
    winner.sort()

    return [winner, loser]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
'''


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        if (winner not in one_loss) and (winner not in more_losses):
            zero_loss.add(winner)

        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)

        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)

        elif loser in more_losses:
            continue

        else:
            one_loss.add(loser)


    return [sorted(list(zero_loss)), sorted(list(one_loss))]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))


    
