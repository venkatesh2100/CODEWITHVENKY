//Given a signed 32-bit integer x, return x with its digits reversed.
//If reversing x causes the value to go outside the signed 32-bit integer range
//[-231, 231 - 1], then return 0.
//
//Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
//Input: x = 123
//Output: 321
class Solution {
    public int reverse(int x) {
         int pop=0;
        int sum=0;
        while (x!=0){
            pop=x%10;
            x/=10;
            if(sum>Integer.MAX_VALUE/10||sum==Integer.MAX_VALUE&&pop>7)return 0;
            if(sum<Integer.MIN_VALUE/10||sum==Integer.MIN_VALUE&&pop<-8)return 0;
            sum=sum*10+pop;
        }
            return sum;
    }
    //     int rem=0;
    //     int sum=0;
    //     //  if(x>(Math.pow(2,31)-1)||x<Math.pow(-2,31)){
    //     //     return 0;
    //     // }
    //     // // if(x>1534236468||x<-2147483412){
    //     // //     return 0;
    //     // // }
    //     // while(x!=0){
    //     //     rem=x%10;
    //     //     sum=sum*10+rem;
    //     //     x=x/10;
    //     // }
    //     //  return sum;
    //     while (x != 0) {//1534236469
    //         if(sum>Integer.MAX_VALUE/10||sum==Integer.MAX_VALUE/10&&rem>7){
    //             return 0;
    //         }
    //         if(sum<Integer.MIN_VALUE/10||sum==Integer.MIN_VALUE/10&&rem<-8){
    //             return 0;
    //         }
    //          rem = x % 10;
    //         sum = sum * 10 + rem;
    //         x = x / 10;
    //     }
    //     return sum;
    // }
}
