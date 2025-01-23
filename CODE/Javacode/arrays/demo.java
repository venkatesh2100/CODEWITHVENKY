package ARRAYS;

public class demo{
    public static void main(String[] args) {
        System.out.println("HEllO");
        System.out.println("WORLD");
        int[] arr=new int[5];
        System.out.println(arr.length);
        for(int i=0;i<arr.length;i++){
            arr[i]=i;
        }
        for(int num:arr){
            System.out.println(num+" ");
        }
        
    }
}

