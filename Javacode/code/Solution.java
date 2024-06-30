import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){//we tyr to use Regex in java for locate or search for the lines
			String pattern = in.nextLine();
          	//Write your code
     try{
			Pattern.compile(pattern);
			System.out.println("Is Valid");
		}catch(patternSyntaxException ex){
			System.out.println(ex);
			System.out.println("InValid");
		}
		testCases --;
		 }

		}
	}



