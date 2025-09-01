class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head = None
    def append(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
            current = self.head
            while current:
                print(current.data,end='->')
                current= current.next 
            print("None")

l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.display()




