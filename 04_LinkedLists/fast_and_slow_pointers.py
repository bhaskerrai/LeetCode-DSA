'''
Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.
'''

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

# The most elegant solution comes from using the fast and slow pointer technique. 
# If we have one pointer moving twice as fast as the other, then by the time it reaches the end, the slow pointer will be halfway through since it is moving at half the speed.

def get_middle(head) -> int:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

# print(get_middle(head))


'''
Example 2: 141. Linked List Cycle

Given the head of a linked list, determine if the linked list has a cycle.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
'''

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False
    

# This approach gives us a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. 
# Note that this problem can also be solved using hashing, although it would require O(n) space.

def hasCycle(head: ListNode) -> bool:

    seen = set()

    while head:
        if head in seen:
            return True
        
        seen.add(head)
        head = head.next

    return False

# the previous solution is better as it uses less space.



'''
Example 3: Given the head of a linked list and an integer k, return the k-th node from the end.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.
'''

def find_node(head, k):
    slow = head
    fast = head

    for _ in range(k):
        fast = head.next

    while fast and fast.next:
        slow = slow.head
        fast = fast.head

    return slow
