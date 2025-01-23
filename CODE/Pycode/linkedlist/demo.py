


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head =None
    def insertAtBeginning(self, data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode



Linked=Linkedlist()
Linked.insertAtBeginning(10)
print(L)
