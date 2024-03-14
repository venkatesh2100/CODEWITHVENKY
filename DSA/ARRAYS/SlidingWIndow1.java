package ARRAYS;

public class SlidingWIndow1 {
    public static void main(String[] args) {
        int[] arr={ 1, 4, 2, 10, 2, 3, 1, 0, 20 };
        int k=3;
        System.out.println(window(arr,k));
    }
    public  static  int window(int[] arr,int k){
        int maxSum=Integer.MIN_VALUE;
        int n=arr.length;
        for(int i=0;i<n-k+1;i++){
            int currentSum=0;
            for(int j=0;j<k;j++){
                currentSum+=arr[i+j];
            }
            maxSum=Math.max(currentSum,maxSum);
        }
        return maxSum;
    }
}
