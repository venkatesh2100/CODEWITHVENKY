# Definition for singly-linked list.
# class listNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[listNode]) -> Optional[listNode]:
        mover = head

        while mover and mover.next:

            val = self.findGCD(mover.val,mover.next.val)
            newNode= listNode(val)

            newNode.next = mover.next
            mover.next = newNode
            mover = mover.next.next
        return head



    def findGCD(self,val1, val2):
        if val2==0:
            return val1
        return self.findGCD(val2,val1%val2 )
