class Node:
  def __init__(self,data) -> None:
    self.data=data
    self.next=None


def array2LinkedList(arr):
  if not arr:
    return None
  head=Node(0)
  mover=head
  for i in arr:
    val=Node(i)
    mover.next=val
    mover=mover.next
  return head.next
##** Traverse the LinkedList and if it equal just Print it out
def searchLinkedList(head,val):
  mover=head
  while mover:
    if mover.data==val:
      return mover
    mover=mover.next
  return mover

def printLinkedList(head):
  mover=head
  count=0
  while mover:
    print(mover.data,end='->')
    count+=1
    mover=mover.next
  print(None,count)
  # print(count)
link=(array2LinkedList([10,30,12,32,3,40]))
printLinkedList(link)
print("End")
print(link,30)


array2LinkedList([])