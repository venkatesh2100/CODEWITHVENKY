package CP.CODENINJAS;
/*
* Problem statement
Given an array 'v' of 'n' numbers.

Your task is to find and return the highest and lowest frequency elements.
If there are multiple elements that have the highest frequency or lowest frequency,
*  pick the smallest element.
*Example:
Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
Output: 1 2
*
*
* */
public class HighLowFrequency {

    public static int[] getFrequencies(int[] v) {
        // Write Your Code Here
        boolean[] visited=new boolean[v.length];
        int[] ans=new int[2];
        int max=0;
        int min=v.length;
        int maxEle=0;
        int minEle=0;

        for(int i=0;i<v.length;i++){
            int count=1;
            for(int j=i+1;j<v.length;j++){
                if(v[i]==v[j]){
                    count++;
                }
                if(count>max){
                    max=count;
                    maxEle=v[i];
                }
                if (count < min) {
                    min=count;
                    minEle=v[i];
                }
            }
        }
        ans[0]=maxEle;
        ans[1]=minEle;
        return ans;
//        int count=0;//Traverse the elements to check wheather their are equal
//        int[] ans=new int[v.length];
//         for(int i=0;i<v.length-1;i++){
//             for(int j=i+1;j<v.length-1;j++){
//                 if(v[i]==v[j]){
//                     count++;
//                 }
//                 else{
//                     for(int k=0;k<ans.length;k++){
//                         ans[k]=count;
//                     }
//             }
//             }
//             count=0;
//         }
//         int[] max=new int[2];
//         max[0]=Math.max(ans);
//         max[1]=Math.max(ans);
//         return max;
    }

}
