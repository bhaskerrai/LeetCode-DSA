'''
Example 2: 2260. Minimum Consecutive Cards to Pick Up

Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.

note: The shortest subarray that contains a duplicate will have the first and last element be the duplicate
'''

from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]) -> int:
    counts = defaultdict(list)

    for i in range(len(cards)):
        counts[cards[i]].append(i)

    print(counts)

    ans = float("inf")

    for key in counts:
        arr = counts[key]

        # print()

        for i in range(len(arr) - 1):
            print("\nans before:", ans)
            print("arr[i+1] - arr[i] + 1:", arr[i+1] - arr[i] + 1)
            ans = min(ans, arr[i+1] - arr[i] + 1)
            print("ans after:", ans)
    
    return ans if ans < float("inf") else -1


# print(minimumCardPickup([3,4,2,3,4,7]))
# print(minimumCardPickup([1,0,5,3]))

'''
The time complexity is still O(n) even though we have a nested loop in the algorithm. 
This is because the inner loop in the nested loop can only iterate n times in total, 
since it's iterating over indices of elements from the array, where n is the length of the input array.

We can actually improve this algorithm slightly by observing that we don't need to store all the indices, 
but only the most recent one that we saw for each number. This improves the average space complexity. 
The current algorithm has O(n) space complexity always, but with the improvement, it is only O(n) in the worst case, when there are no duplicates.
'''


def minimumCardPickup2(cards: List[int]) -> int:
    
    map = defaultdict(int)
    ans = float("inf")

    for i in range(len(cards)):
        if cards[i] in map:
            ans = min(ans, i - map[cards[i]] + 1)

        map[cards[i]] = i
    
    return ans if ans < float("inf") else -1


print(minimumCardPickup2([3,4,2,3,4,7]))
print(minimumCardPickup2([1,0,5,3]))

# This algorithm also runs faster because we save on an iteration, although the time complexity of both algorithms is O(n), where n is the length of the input array.

