class Node:
  def __init__(self,data) -> None:
    self.data=data
    self.prev=None
    self.next=None

def array2List(arr):
  if not arr:
    return None

  for i in arr:
    val=Node(i)



def reverseList(head):
  if not head and head.next:
    return head
