// package LINKEDLIST;

import java.util.LinkedList;

public class demo {
    public static void main(String[] args) {
        LinkedList<Integer> ll=new LinkedList<>();
        ll.add(10);
        ll.add(100);
        System.out.println(ll);
    }
    void insertBeggin(LinkedList<Integer> ll,int data){
        if(ll.isEmpty()){
            System.out.println("NUll");
        }else{
            for(int i=0;i<ll.size();i++){
                ll.add(data);
            }
        }
    }
}
