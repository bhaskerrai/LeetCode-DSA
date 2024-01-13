'''
Example 4: 2352. Equal Row and Column Pairs

Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column, and R and C are equal if we consider them as 1D arrays.

How can we calculate the number of equal pairs? Let's say there are three rows that look like [1, 2, 3], and there are two columns that look the same. For each of the three rows, there are two columns to pair with, so that means there are 3 * 2 = 6 pairs. 
We can use a hash map to count how many times each row occurs. We can use a second hash map to do the same thing with the columns. Then, we can iterate over the rows hash map, and for each row, check if the same array appeared as a column. 
If it did, then the product of the number of appearances is added to our answer.

The problem is, arrays can't be put in a hash map as a key because they are mutable. We need to convert the rows and columns into a hashable form such as a string or tuple. The best choice will depend on the language you're using.
'''

from collections import defaultdict
from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    
    def conver_to_key(arr: List[int]) -> tuple:
        return tuple(arr)
    
    row_dict = defaultdict(int)
    col_dict = defaultdict(int)
    
    for row in grid:
        row_dict[conver_to_key(row)] += 1


    for col in range(len(grid[0])):
        curr_col = []
        for row in range(len(grid)):
            curr_col.append(grid[row][col])
        
        col_dict[conver_to_key(curr_col)] += 1

    ans = 0

    for arr in row_dict:            
        ans += row_dict[arr] * col_dict[arr] 

    return ans

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


'''
If the grid has a size of n⋅n, this algorithm has a time complexity of (n^2) - there are n^2 elements and 
each element is iterated over twice initially (once for the row it occupies and once for the column it occupies). 
Populating and then iterating over the hash maps will be dominated by this. The space complexity is O(n^2) - if all rows and columns are unique, then each of the two hash maps will both grow to a size of n, with each key having a length of n.
'''