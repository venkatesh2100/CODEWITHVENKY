package CP.CODENINJAS;
25 17
1 0 1 1 1 1 1 0 1 0 1 1 1 0 0 1 0 0 1 0 0 0 1 1 0 

public class traffic {
//   public class Solution {
    public static int traffic(int n, int m, int []vehicle) {
        // Write your code here.
        int cnt;
        for(int num:vehicle){
          if(num==1){
            cnt++;
          }
        }
        for(int c:vehicle){
          if(c==0){
            m--;
            if(m>0){
              cnt++;
            }
          }
        }
        return cnt;

      }
// }
  
}
