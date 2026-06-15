# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1 2 3 --> 3 2 1 
        prev = ListNode(0)

        mover = head 
        temp = head
        while mover and mover.next:
            
            temp = mover.next 
            mover.next = prev 
            prev = mover 
            mover = temp 

        return prev
            
        
