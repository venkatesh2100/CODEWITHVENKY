package SORTING;

import java.util.Scanner;

public class selectionsort {
    //Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the
    // smallest (or largest) element from the unsorted portion of the list and moving it to the sorted
    // portion of the list.
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Size of the Array");
        int size=sc.nextInt();
        int arr[]=new int[size];
        System.out.println("Enter the Array Elements");
        for(int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }
        selectionsort obj1=new selectionsort();
        obj1.sort(arr);

    }
    public  void sort(int[] arr){
        for(int i=0;i<arr.length;i++){
            int min=i;
            for(int j=i+1;j< arr.length;j++){
                if(arr[min]>arr[j]){
                 min =j;
                }
            }

            //Now Swap-time
            int temp=arr[i];
            arr[i]=arr[min];
            arr[min]=temp;

        }
        for(int num:arr){
            System.out.print(num+ " ");
        }
    }
}
