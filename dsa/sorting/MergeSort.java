package SORTING;

import java.util.Scanner;

public class MergeSort {
    void merge(int[] arr,int first,int mid,int last){
        //Size of the arrays
        int size1=mid-first+1;
        int size2=last-mid;
        //Declare the Array
        int[] left=new int[size1];
        int[] right=new int[size2];
        //Copy the Data to Array:
        for (int i = 0; i < size1; i++) {
            left[i]=arr[first+i];
        }
        for (int j = 0; j <size2 ; j++) {
            right[j]=arr[mid+j+1];
        }
        //Merge the Elements
        int k=first,i=0,j=0;
        while (i<size1 && j<size2){
            if(left[i]<=right[j]){
                arr[k]=left[i];
                i++;
            }else {
                arr[k]=right[j];
                j++;
            }
            k++;
        }
        //for remaining elements
        while (i<size1){
            arr[k]=left[i];
            i++;
            k++;
        }
        while (j<size2){
            arr[k]=right[j];
            j++;
            k++;
        }
    }
    void sort(int[] arr,int first,int last){
        if(first<last){
            int mid=first+(last-first)/2; //Mid values
            sort(arr,first,mid);    //Sorting the arrays
            sort(arr,mid+1,last);

            merge(arr,first,mid,last);

        }
    }
    //Printing the Array
    void print(int[] arr,int Size){
        for(int num:arr){
            System.out.print(num+" ");
        }
    }


    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int size=sc.nextInt();
        int[] arr=new int[size];
        for (int i = 0; i < size; i++) {
            arr[i]=sc.nextInt();
        }
        MergeSort obj1=new MergeSort();
        obj1.sort(arr,0,size-1);
        obj1.print(arr,size);

    }
}
