# Definition for singly-linked list.
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwolists(self, list1: Optional[listNode], list2: Optional[listNode]) -> Optional[listNode]:


        dummy=listNode()

        curr=dummy

        while list1 and list2:
            # print(curr)
            if list1.val < list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next

        if list1:
            curr.next=list1
        if  list2:
            curr.next=list2
        print(dummy)
        return dummy.next
 
