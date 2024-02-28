# 649. Dota2 Senate

# Approach: Two Queues
from collections import deque

def predictPartyVictory(senate: str) -> str:
        n = len(senate)
        radiant_q = deque()
        dire_q = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while radiant_q and dire_q:
            r_turn = radiant_q.popleft()
            d_turn = dire_q.popleft()

            if d_turn < r_turn:
                dire_q.append(dire_q + n)
            else:
                radiant_q.append(r_turn + n)
            
        return "Radient" if radiant_q else "Dire"


# Approach: Single Queue
# When you have learned greedy algorithm, use it to solve this problem.
