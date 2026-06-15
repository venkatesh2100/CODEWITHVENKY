# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=1, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(0)
        prev.next = head 
        l = prev
        r = head  

        while r and r.next != None:
            r = r.next.next 
            l = l.next 
        l.next = l.next.next 

        return prev.next
