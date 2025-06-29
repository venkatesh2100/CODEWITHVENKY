




class ListNode{

  value:number;
  next:ListNode | null ;

  constructor(value:number){
    this.value=value;
    this.next=null;
  }
}


function findtheLengthofLinkedList(head:ListNode|null):number{
  let len=0;

  var current:ListNode| null=head;

  while(current!=null){
    len++;
    current=current.next;
  }
  return len;
}


const head=new ListNode(1);
head.next=new ListNode(2);
head.next.next=new ListNode(3);
head.next.next.next=new ListNode(4);

console.log(findtheLengthofLinkedList(head));