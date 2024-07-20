// package ARRAYS;

public class KadanessALGO {
    public static void main(String[] args) {
        int[] arr={ 2,-5,6,6,6};
        System.out.println(Integer.MIN_VALUE);
        System.out.println(algo(arr));
    }
    public static  int algo(int[] arr){
        int maxi=0;
        int sum=Integer.MIN_VALUE;
        for(int i=0;i<arr.length;i++){
            maxi+=arr[i];
            if(sum<maxi){
                sum=maxi;
            }else if(maxi<0){
                maxi=0;
            }
        }
        return sum;
    }
}
