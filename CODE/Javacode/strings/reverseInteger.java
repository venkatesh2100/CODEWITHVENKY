package STRINGS;

import java.net.Inet4Address;
import java.util.Arrays;

public class reverseInteger {
    public static void main(String[] args) {
        int x = 1534236469;
//        System.out.println(reverse(x));
//        System.out.println(Reverse2(x));
        System.out.println(finalReverse(x));
    }

    public static int reverse(int x) {
        int rem = 0;
       long  sum = 0;
//        if (x > (Math.pow(2, 31) - 1)) {
//            return 0;
//        }
//        if (x < Math.pow(-2, 31)) {
//            return 0;
//        }

        System.out.println(Integer.MAX_VALUE);


         while (x != 0) {//1534236469
            if(x>Integer.MAX_VALUE/10||sum==Integer.MAX_VALUE/10&&rem>7){
                return 0;
            }
            rem = x % 10;
            sum = sum * 10 + rem;
            x = x / 10;
        }
        return (int)sum;
    }
    public static int Reverse2(int x){
        String value=Integer.toString(x);
        char[] arr=value.toCharArray();
        int start=0;
        int end=arr.length-1;
        while(start<end){
            char temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
        }
        String v= Arrays.toString(arr);
        int sum= Integer.parseInt(v);
        return sum;
    }
    public static int finalReverse(int x){
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


}
