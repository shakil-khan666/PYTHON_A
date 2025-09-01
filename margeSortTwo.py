from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail=dummy

        while list1 and list2:
            if list1.val <list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next=list1
        if list2:
            tail.next = list2

        return dummy.next 
   
def LinkToLinkedList(num):

    dummy = ListNode()
    tail = dummy
    for val in num:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next
       

def display(head):

    while head:
        print(head.val,end='->')
        head = head.next
    print('None')

l1 = LinkToLinkedList([1,2,3,4])
l2 = LinkToLinkedList([1,2,3,5,6])
s= Solution()
marged = s.mergeTwoLists(l1,l2)
display(marged)

            