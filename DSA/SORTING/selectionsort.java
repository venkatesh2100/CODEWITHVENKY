package SORTING;

import java.util.Scanner;

public class selectionsort {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Size of the Array");
        int size=sc.nextInt();
        int arr[]=new int[size];
        System.out.println("Enter the Array Elements");
        for(int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }
        sort(arr);

    }
    public  static void sort(int[] arr){
        for(int i=0;i<arr.length;i++){
            int min=i;
            for(int j=i+1;j< arr.length;j++){
                if(arr[min]>arr[j]){
                   min =j;
                           int temp=arr[i];
            arr[i]=arr[min];
            arr[min]=temp;
                }
            }

            //Now Swap-time

        }
        for(int num:arr){
            System.out.print(num+ " ");
        }
    }
}
