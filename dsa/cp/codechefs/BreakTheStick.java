package CP.CODECHEF;

import java.util.Scanner;

public class BreakTheStick {
    public static void main(String[] args) {
       stick();
    }
static     void stick(){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while (t-->0){
            int N=sc.nextInt();
            int X=sc.nextInt();
            if(N%2==0){
                System.out.println("YES");
            }else if(X%2==0){
                System.out.println("NO");
            }else
                System.out.println("YES");
        }
    }

}
