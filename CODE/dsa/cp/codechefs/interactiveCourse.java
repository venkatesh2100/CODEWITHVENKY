package CP.CODECHEF;

import java.util.Scanner;

public class interactiveCourse {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t= sc.nextInt();
        int rate=sc.nextInt();
        while (t-->-1){
            int rating=sc.nextInt();
            if(rating<rate) System.out.println("Bad Boi");
            else if(rating>rate) System.out.println("Good Boi");
        }
    }
}
