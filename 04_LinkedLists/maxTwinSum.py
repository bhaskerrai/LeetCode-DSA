'''
2130. Maximum Twin Sum of a Linked List asks for the maximum pair sum. The pairs are the first and last node, second and second last node, third and third last node, etc.

The trivial solution would be to convert the linked list into an array, that way you can access the pairs easily by indexing. The more elegant O(1) space solution is as follows:

1. Find the middle of the linked list using the fast and slow pointer technique from the previous article.
2. Once at the middle of the linked list, perform a reversal. Basically, reverse only the second half of the list.
3. After reversing the second half, every node is spaced n / 2 apart from its pair node, where n is the number of nodes in the list which we can find from step 1.
4. With that in mind, create another fast pointer n / 2 ahead of slow. Now, just iterate n / 2 times from head to find every pair sum slow.val + fast.val.

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

A = ListNode(5)
B = ListNode(4)
C = ListNode(2)
D = ListNode(1)

A.next = B
B.next = C
C.next = D

# [1,100000]
# A = ListNode(1)
# B = ListNode(100000)
# A.next = B
head = A


def pairSum(head: Optional[ListNode]) -> int:
        maximumSum = 0
        slow = head
        fast = head

        #Get middle of the linked list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #Reverse second half of the linked list.
        prev = None
        current = slow

        while current:
            nextNode = current.next
            current.next = prev 
            prev = current
            current = nextNode

        # print(current)

        slow = head
        # fast = prev
        # print(prev.val)

        while prev:
            # print(prev.val)
            maximumSum = max(maximumSum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return maximumSum

print(pairSum(head))

        