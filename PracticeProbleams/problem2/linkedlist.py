#reverse the linked list 

def reverseLinkedList(head):
    #i need to reverse the linked list
    #i can do this by passing the nodes to the previous node
    prev = None 
    current = head
    while current is not None:
        next = current
        current.next = prev
        prev = current
        current = next
    
    return prev
