//package SORTING;

import java.util.Scanner;
public class Bubblesort {
    public  void sort(int[] arr,int n) {
        int temp = 0;
        boolean swapped;
        //Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent
        // elements if they are in the wrong order.
        // This algorithm is not suitable for large data sets as
        // its average and worst-case time complexity is quite high.
        for (int i = 0; i < arr.length-1;i++){
             swapped=false;
            for(int j=0;j<n-i-1;j++){
                if(arr[j]>arr[j+1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
                }
            if(swapped==false){
                break;
            }
        }
        for(int ch:arr){
            System.out.print(ch+ " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Array Size: ");
        int size=sc.nextInt();
        int []arr=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }
        sc.close();
        Bubblesort obj1=new Bubblesort();
        obj1.sort(arr,size);
    }
}
