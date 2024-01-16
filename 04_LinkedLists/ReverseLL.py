
def reverseLL(head):
    prev = None
    current = head

    while current:
        nextNode = current.next
        current.next = prev 
        prev = current
        current = nextNode

    return prev


'''
Example: 24. Swap Nodes in Pairs

Given the head of a linked list, swap every pair of nodes. For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
'''
def swap(head):

    # Check edge case: linked list has 0 or 1 nodes, just return
    if not head and not head.next:
        return head
    
    prev = None
    dummy = head.next

    while head and head.next:

        if prev:
            prev.next = head.next

        prev = head

        nextNode = head.next.next
        head.next.next = head

        head.next = nextNode
        head = nextNode

    return dummy
