# Complete the function below.

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

def mergeInBetween(list1, list2, a, b):
    temp_iterator_before_a = list1

    for x in range(0, a-2):
        temp_iterator_before_a = temp_iterator_before_a.next

    temp_iterator_after_b = list1

    for x in range(0, b):
        temp_iterator_after_b = temp_iterator_after_b.next
    

    temp_iterator_tail_l2 = list2

    while temp_iterator_tail_l2.next != None:
        temp_iterator_tail_l2 = temp_iterator_tail_l2.next
    
    if a == 1 and b == 1:
        list1 = list2
        return list1

    elif a == 1:
        temp_iterator_tail_l2.next = temp_iterator_after_b
        list1 = list2
        return list1
    else:
        temp_iterator_tail_l2.next = temp_iterator_after_b
        temp_iterator_before_a.next = list2
        return list1


    