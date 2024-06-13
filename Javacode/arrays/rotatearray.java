package ARRAYS;

import java.util.Arrays;

public class rotatearray {


    void rotate(int[] arr,int n,int k){
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[(i+3)%n]=arr[i];
        }
        System.out.println(Arrays.toString(a));
    }
    public static void main(String[] args) {
        int[] arr={1,2,3,4,5,6,7};
        rotatearray ob1=new rotatearray();
        ob1.rotate(arr,arr.length,3);
    }
}
