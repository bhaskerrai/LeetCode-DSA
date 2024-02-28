'''
946. Validate Stack Sequences
'''

from typing import List


# def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
        
        # mySet = set()
        # stack = []

        # # for i in range(len(pushed)):
        # i = 1
        # while i < len(pushed):
        #     print(pushed[-i])
        #     print(popped[-i])
        #     print(pushed[-i] >= popped[-i])
        #     if mySet and popped[-i] in mySet:
        #         print("\nif chala")
        #         i += 1
        #     elif pushed[-i] >= popped[-i]:
        #         print("\nelif chala")
        #         mySet.add(pushed[-i])
        #         stack.append(pushed[-i])
        #         print(stack)
        #         i += 1
        #     else:
        #         print("\nelse chala")
        #         return False

        # return True



def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:        
    stack = []
    ans = []
    left = 0

    for right in range(len(pushed)):
        stack.append(pushed[right])

        while stack and popped[left] == stack[-1]:
            ans.append(stack.pop())
            left += 1

    # print(ans)
    # print(popped)
            
    return ans == popped

# OR for better space complexity
def validateStackSequences2(pushed: List[int], popped: List[int]) -> bool:        
    stack = []
    left = 0

    for right in range(len(pushed)):
        stack.append(pushed[right])

        while stack and popped[left] == stack[-1]:
            stack.pop()
            left += 1

    # print(stack)
    # print(popped)
            
    return True if not stack else False


print(validateStackSequences2([1,2,3,4,5], [4,5,3,2,1]))
print(validateStackSequences2([1,2,3,4,5], [4,3,5,1,2]))
# print(validateStackSequences2([0,2,1], [0,1,2]))
# print(validateStackSequences2([7,2,9,4,5], [4,5,9,2,7]))
# print(validateStackSequences2([2,1,0], [1,2,0]))