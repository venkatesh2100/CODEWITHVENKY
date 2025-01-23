package CODE;

import java.util.Scanner;
import java.util.stream.Stream;

public class Bitvalue {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int  c= 0;
        System.out.println("Enter a bit value");
        int n=sc.nextInt();
        String value=Long.toString(n);
        char[] arr=value.toCharArray();
        for(int nums:arr){
            if(nums=='1'){
                c++;
            }
        }
//        String Bitvalue=sc.nextLine();
//        long d =Long.parseLong(Bitvalue,2);
        System.out.println(c);
    }
}
