/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
//
function middleNode(head: ListNode | null): ListNode | null {
  let len = 0;
  var current = head;

  while (current != null) {
    len++;
    current = current.next;
  }
  //? if Len is 5 THEN 5/2  (2+1)  or else 6/2 3+1

  var midpoint = Math.floor(len / 2);

  //?1 2 3 4 5 6  => 4 5 6
  let start = 0;
  while (start < midpoint) {
    current = current.next;
    start++;
  }

  return current;
}
