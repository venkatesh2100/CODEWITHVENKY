import java.lang.classfile.components.ClassPrinter.ListNode;
import java.util.LinkedList;
import java.util.stream.Gatherer.Integrator;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * Input: list1 = [1,2,4], list2 = [1,3,4]
   Output: [1,1,2,3,4,4]
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
      LinkedList<Integer> ll=new LinkedList<>();
      for(int i=0;i<list1.size();i++){
        ll.add(i,list1.get(i))
      }
    }
}