'''
Remove Duplicates from Sorted List

Solution
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
'''

from typing import Optional

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
head = one

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    
    def delete_node(prev_node):
        prev_node.next = prev_node.next.next


    while head:
        if head.val == head.next.val:
            delete_node(head)
        
        head = head.next

    return head
