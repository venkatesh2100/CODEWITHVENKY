package SORTING;

import java.util.Arrays;
import java.util.Scanner;

public class BinaryInsertionSort {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int size=sc.nextInt();
        int[] arr=new int[size];
        for (int i = 0; i < size; i++) {
            arr[i]=sc.nextInt();
        }
        BinaryInsertionSort obj1=new BinaryInsertionSort();
        obj1.BinaryISort(arr,size);
    }
    public void BinaryISort(int []arr,int s){
//Outer Loop Iterates everytime
        for (int i = 0; i <s ; i++) {
            int min=arr[i];
            //Min element will automatically search and assigned pos
            int j=Math.abs(Arrays.binarySearch(arr,0,i,min)+1);
            System.arraycopy(arr,j,arr,j+1,i-j);
//Min element changes
            arr[j]=min;
        }
        for(int nums:arr){
            System.out.print(nums+" ");
        }
    }
}
