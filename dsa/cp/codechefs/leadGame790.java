import java.util.Scanner;

public class leadGame790 {

  public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);
  int testcases=sc.nextInt();
  int lead=0,player1=0,player2=0;
  int win=0;
  while (testcases-- >0) {
    int a=sc.nextInt();
    int b=sc.nextInt();
    player1+=a;
    player22+=b;
    if(player1-player2>lead){
      win=1;
      lead=player1-player2;
    }if(player2-player1>lead){
      win=2;
      lead=player2-player1;
    }
  }
  System.out.println(win+" "+lead);
    
  }
  
}
