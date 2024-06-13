import jdk.internal.classfile.components.ClassPrinter;

import java.util.LinkedList;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr=head;
        ListNode prev=null;
        ListNode nextNode=null;
        while (curr!=null){
           nextNode=curr.next;
           curr.next=prev;
           prev=curr;
           curr=nextNode;

        }
        return prev
    }
}