//Input: n = 8
//Output: 6
//Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
//Example 2:
class Solution {
    public int pivotInteger(int n) {
        for(int i=0;i<n;i++){
             if(i*(i+1)/2==(n+i)*(n-i+1)/2){
                 return i;
            }
        }return -1;
    }
}