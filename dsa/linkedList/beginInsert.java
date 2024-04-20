import java.util.LinkedList;
public class beginInsert {

  public class Node{
    int data;
    Node next;

    //constructor 
    public  Node (int data){
      this.data=data;
      this.next=null;
      
    }
  }
  //create a singly LL
  public Node heaNode=null;
  public Node tailNode=null;

  public void atStart(int data){
    Node newNode= new Node(data);
    
    if(heaNode==null){
      heaNode=newNode;
      tailNode=newNode;
    }else{
      Node temp=heaNode;
      heaNode=newNode;
      heaNode.next=temp;
    }
  }
  // public 
  public void display(){

    Node current=heaNode;

    if(heaNode==null){
      System.out.println("Linked ls is empty");
      return;
    }
    while (current!=null) {
      System.out.println(current.data+" ");
      current=current.next;      
    }
  }
  public static void main(String[] args) {
    LinkedList<Integer> ll=new LinkedList<>();
    beginInsert newNode=new beginInsert();
    newNode.atStart(10);
    newNode.atStart(1000);
    newNode.atStart(1000000000);
    newNode.display();
    Node current=newNode.heaNode;
    while(current!=null){
      ll.add(current.data);
      current=current.next;
    }
    ll.get(2); 
    ll.add(3);
    System.out.println(ll.size());
    for (int i = 0; i < ll.size(); i++) {
      System.out.print(ll.get(i)+" ");
    }
  
  }
}