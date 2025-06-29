"use strict";
class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
function findtheLengthofLinkedList(head) {
    let len = 0;
    var current = head;
    while (current != null) {
        len++;
        current = current.next;
    }
    return len;
}
const head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
console.log(findtheLengthofLinkedList(head));
