package HASHING;
/*
Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
*/
public class MaxFrequency {
    public static void main(String[] args) {
        int[]  arr={10,5,10,15,10,5};
        int n=arr.length;
        FindMaxMin(arr,n);
    }
    public static void FindMaxMin(int[] arr,int n){
        //Create Boolean for Check visited or not
        boolean[] visited=new boolean[n];
        int maxEle=0;
        int minEle=0;
        int MaxFre=0;
        int MinFre=n;
        for (int i = 0; i <n ; i++) {
            int count=1;
            for (int j=i+1;j<n;j++){
                if(arr[i]==arr[j]){
                    count++;
                }
            }
            if(count>MaxFre){
                maxEle=arr[i];
                MaxFre=count;
            }
            if(count<MinFre){
                minEle=arr[i];
                MinFre=count;
            }
        }
        System.out.println(MaxFre+" "+MinFre);
    }
}
