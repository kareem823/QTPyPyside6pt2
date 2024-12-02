'''
1. Determine if a Linked List Contains a Cycle

Question:
Given a singly linked list, determine whether it contains a cycle.
 A cycle occurs when a node's next pointer points back to a previous node, forming a loop.

Solution:
To detect a cycle in a linked list, I can employ Floyd's Tortoise and 
Hare algorithm. This algorithm uses two pointers that traverse the list 
at different speeds. If there's a cycle, the two pointers will eventually meet;
 if not, one of the pointers will reach the end of the list.
'''
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    #initialize the pointers, both starting at the head of the list
    tortoise = head
    hare = head

    #traverse the list with the tortoise and the hare
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next

        #if the 2 pointers meet, there's a cycle
        #meaning, if the next pointer of the tortoise is the same as the hare
        #then there's a cycle
        if tortoise == hare:
            return True
        
    return False


def main():
    # Create a linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    #use the next pointer to create a cycle
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    print(has_cycle(node1))

main()

