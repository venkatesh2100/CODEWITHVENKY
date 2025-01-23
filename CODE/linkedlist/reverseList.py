class Node:
  def __init__(self,data) -> None:
    self.data=data
    self.prev=None
    self.next=None

def array2list(arr):
  if not arr:
    return None
  head=Node(0)
  mover=head
  for i in arr:
    val=Node(i)
    mover.next=val
    mover=mover.next
  return head.next

def printlist(head):
  mover=head
  while mover:
    print(f"",mover.data,end="-->")
    mover=mover.next
  print(None)



def reverselist(head):
  if not head or head.next==None:
    return head
  newhead=reverselist(head.next)

  front=head.next
  front.next=head
  head.next=None
  return newhead


list1=array2list([10,30,12,32,3,40])

printlist(list1 )
printlist(reverselist(list1))
