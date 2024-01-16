'''
Reverse Linked List II

Solution
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
'''

# Watch: https://www.youtube.com/watch?v=RF_M9tX4Eag

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
F = ListNode(6)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

head = A

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and not head.next:
             return head
        
        dummy = ListNode(0, head)

        # reach node at position left
        left_prev = dummy
        curr = head

        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        
        # reverse from left to right
        prev = None
        for _ in range(right - left + 1): 
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode


        # update pointers
        left_prev.next.next = curr
        left_prev.next = prev


        return dummy.next

# print(reverseBetween(head, 2, 4))


# with recursion

def reverseBetween2(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    if not head:
        return None

    left, right = head, head
    stop = False

    def recurseAndReverse(right, m, n):
        nonlocal left, stop

        # base case. Don't proceed any further
        if n == 1:
            return

        # Keep moving the right pointer one step forward until (n == 1)
        right = right.next

        # Keep moving left pointer to the right until we reach the proper node
        # from where the reversal is to start.
        if m > 1:
            left = left.next

        # Recurse with m and n reduced.
        recurseAndReverse(right, m - 1, n - 1)

        # In case both the pointers cross each other or become equal, we
        # stop i.e. don't swap data any further. We are done reversing at this
        # point.

        # print("\nYehan se start hai")
        if left == right or right.next == left:
            # print("pheli if-statement chali")
            # print("left == right:", left == right)
            # print("right.next == left:", right.next == left)
            stop = True

        # print("left:", left.val)
        # print("right:", right.val)

        # Until the boolean stop is false, swap data between the two pointers     
        if not stop:
            # print("dosri if statement chali")
            left.val, right.val = right.val, left.val

            # Move left one step to the right.
            # The right pointer moves one step back via backtracking.

            # print(left.val)
            left = left.next           
            # print(left.val)
            # print(right.val)

    recurseAndReverse(right, m, n)
    return head

print(reverseBetween2(head, 2, 5))

print(head.next.val)


'''
Time complexity for both implementations is O(n), where n is the number of nodes in the linked list. This is because both approaches iterate through the sublist to be reversed.
The space complexity for the iterative approach is O(1) since it uses a constant amount of extra space, regardless of the size of the input linked list.
The space complexity for the recursive approach is O(n) due to the recursive call stack. In the worst case, the stack depth could be n, where n is the length of the sublist being reversed.
'''


