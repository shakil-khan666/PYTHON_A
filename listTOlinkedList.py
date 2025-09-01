
class ListNode:
    def __init__(self,data) :
        self.data = data
        self.next = None
    
def LinkList(arr):
    dummy = ListNode(-1)
    tail  = dummy
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next 
    return dummy.next 

arr = [1,2,3,4,5]
link_list =LinkList(arr) 

def Display(head):
    current = head

    while current:
        print(current.data,end='->')
        current = current.next
    print('None')

Display(link_list)

        