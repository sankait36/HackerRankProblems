class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if head == None or head.next == None:
        return False
    elif head.next == head:
        return True
    else:
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False