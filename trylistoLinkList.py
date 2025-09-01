class ListNode:
    def __init__(self,data) :
        self.data = data
        self.next = None

def listLink(arr):
    dummy = ListNode(-1)
    tail  = dummy

    for val in arr:
        tail.next = ListNode(val)
        tail =  tail.next
    return dummy.next


arr = [1,2,3,4,5,6,7,8]
list_link = listLink(arr)

def dispaly(head):
    current  =  head
    while current:
        print(current.data,end="->")
        current =  current.next
    print("None")

dispaly(list_link)