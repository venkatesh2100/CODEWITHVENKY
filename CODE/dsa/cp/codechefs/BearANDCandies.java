package CP.CODECHEF;

import java.sql.SQLOutput;
import java.util.Scanner;

public class BearANDCandies {
    public static void main(String[] args) {
        candies();
    }
    static void candies(){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while (t-->0){
            int i=0;
            int A=sc.nextInt(),B=sc.nextInt();
            while (true){
                if(i*i>A){
                    System.out.println("BOB");
                    break;
                } else if (i*(i+1)>B) {
                    System.out.println("Limak");
                    break;
                }
                i++;
            }
        }

    }
}
