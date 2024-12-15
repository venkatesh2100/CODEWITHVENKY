# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        ##?checking Curr val and curr next val. If equal skip them
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next

        return head



        dummy=ListNode()
        curr=dummy
        if head==None:
            return head

        while curr:
            curr.next=head
            head=head.next
            # print(curr.val,curr.next.val)
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
            # print(curr)
        if curr.val==0:
            return curr
        return dummy.next
