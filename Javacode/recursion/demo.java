// package RECURSIONS;

import java.util.Scanner;

public class demo {
    public static void main(String[] args) {
        System.out.println("Enter the Number: ");
        Scanner sc =new Scanner(System.in);
        int n=sc.nextInt();
        System.out.print(recursion(n)+" ");


    }
    public  static int  recursion(int n){
        if(n==0||n==1){
            return 1;
        }else
            return recursion(n-1)+recursion(n-2);
    }
}
