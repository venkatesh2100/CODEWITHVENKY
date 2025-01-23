import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class recentContenst793 {


  public static void main(String[] args) {
    // HashMap<String , Integer> map=new HashMap<>();
    Scanner sc=new Scanner(System.in);
    int testcases=sc.nextInt();
    int c1=0,c2=0;
    while (testcases-->0) {
      int number=sc.nextInt();
      while (number-->0) {
      String contest=sc.nextLine();
      if(contest.equals("START38")){
        c1++;
      }else{
        c2++;
      }
      }
      
    }
System.out.println(c1+" "+c2);
  }
  
}
