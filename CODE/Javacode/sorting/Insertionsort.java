package SORTING;

import java.util.Scanner;

public class Insertionsort {
  public void sorted(int[] arr){
    
	  for(int i=0;i<arr.length;i++){
		  System.out.println("hi");
	  }

    for(int i=0;i<arr.length;i++){
//Upto specific condition this loop will run and sort the array
      int min=i;
      while (min>0 && arr[min-1]>arr[min])

       int temp=arr[min];
       arr[min]=arr[min-1];
       arr[min-1]=temp; 
       min--;
      }
    }
    for(int num:arr){
      System.out.print(num+" ");
    }
  }
  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int size=sc.nextInt();
    int[] arr=new int[size];
    for(int i=0;i<size;i++){
      arr[i]=sc.nextInt();
    }
    sc.close();
    Insertionsort sort1=new Insertionsort();
    sort1.sorted(arr);
  }
  
}
