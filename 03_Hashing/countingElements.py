# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.


from typing import List

def countElements(arr: List[int]) -> int:
    ans = 0
    my_set = set(arr)

    for num in my_set:
        if num + 1 in my_set:
            ans += 1
    
    return ans    

print(countElements([1,2,3]))    
print(countElements([1,1,3,3,5,5,7,7]))    



