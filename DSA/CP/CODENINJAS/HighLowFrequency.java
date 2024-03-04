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
        int count=0;//Traverse the elements to check wheather their are equal
        int[] ans=new int[v.length];
         for(int i=0;i<v.length-1;i++){
             for(int j=i+1;j<v.length-1;j++){
                 if(v[i]==v[j]){
                     count++;
                 }
                 else{
                     for(int k=0;k<ans.length;k++){
                         ans[k]=count;
                     }
             }
             }
             count=0;
         }
         int[] max=new int[2];
         max[0]=Math.max(ans);
         max[1]=Math.max(ans);
         return max;
    }

}
