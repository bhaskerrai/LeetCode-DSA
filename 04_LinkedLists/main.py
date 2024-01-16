class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three
head = one

# print(head.val)
# print(head.next.val)
# print(head.next.next.val)


'''

Linked List Advantages (compared to arrays):
1. Efficient Insertion/Removal (O(1)): Add or remove elements anywhere in the list in constant time, unlike arrays which require shifting elements (O(n)).
2. Dynamic Size: No fixed size like arrays, can grow and shrink on demand without resizing, avoiding cost of array resize operations.

Linked List Disadvantages (compared to arrays):
1. No Random Access (O(n)): Accessing specific elements by index requires iterating from the beginning, unlike arrays with O(1) indexing.
2. Memory Overhead: Each element needs extra space for pointers, potentially doubling memory usage for small data types.

'''

ptr = head
# print(ptr.val)
head = head.next
head = None


# Traversal
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans

# Moving to head.next is the equivalent of iterating to the next element in an array. Traversal can also be done recursively:
def get_sum2(head):
    if not head:
        return 0
    
    return head.val + get_sum2(head.next)

# print(get_sum2(ptr))


# Let's say you want to add the element at position i and let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# print(two.next.val)
four = ListNode(4)

add_node(two, four)
# print(two.next.val)
# print(four.next.val)



# Let's say you want to delete the element at position i and let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next


# print("before deleting: ",two.next.val)
# delete_node(two)
# print("after deleting: ",two.next.val)
# print(two.next.next)
    

# Doubly linked list
# A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node. This pointer is usually called prev, and it allows iteration in both directions.
    
class DoublyListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None 
        self.next = None   


one_dll = DoublyListNode(1)
two_dll = DoublyListNode(2)
three_dll = DoublyListNode(3)

one_dll.next = two_dll
two_dll.prev = one_dll
two_dll.next = three_dll
three_dll.prev = two_dll

startNode = one_dll
# print(startNode.next.next.prev.val)

four_dll = DoublyListNode(4)

# Let node be the node at position i
def add_to_dll(node, node_to_add):
    prevNode = node.prev
    node_to_add.prev = prevNode
    node_to_add.next = node
    prevNode.next = node_to_add
    node.prev = node_to_add


# print("Before:")
# print(two_dll.prev.val)
# print(two_dll.next.val)

add_to_dll(two_dll, four_dll)


# print("\nAfter:")
# print(two_dll.prev.val)
# print(startNode.next.val)
# print(four_dll.next.val)
    

# Let node be the node at position i
def delete_to_dll(node):
    prev_Node = node.prev
    next_node = node.next
    prev_Node.next = next_node
    next_node.prev = prev_Node

# print(four_dll.next.val)
# print(four_dll.prev.val)
# print(one_dll.next.val)
# delete_to_dll(four_dll)
# print(one_dll.next.next.val)