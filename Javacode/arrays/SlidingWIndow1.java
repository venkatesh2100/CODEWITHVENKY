package ARRAYS;

public class SlidingWIndow1 {
    public static void main(String[] args) {
        int[] arr={ 1, 4, 2, 10, 2, 3, 1, 0, 20 };
        int k=3;
        System.out.println(slideWindow(arr,k));
        System.out.println(windowBruteForce(arr,k));
    }
    public  static  int windowBruteForce(int[] arr,int k){
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

    //Sliding Window Technique Optimised way of obtaining Largest of SubArray
    public  static  int slideWindow(int[] arr,int k){
        int max_sum=Integer.MIN_VALUE;
        int current_sum=0;
        for(int i=0;i<k;i++){
            current_sum+=arr[i];
        }
        max_sum=current_sum;
        for(int i=k;i<arr.length;i++){
            current_sum+=arr[i]-arr[i-k];
            max_sum=Math.max(current_sum,max_sum);
        }
        return max_sum;

    }
}
