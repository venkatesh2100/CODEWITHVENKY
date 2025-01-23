package ARRAYS;

import java.util.*;
import java.util.function.Function;

public class demo1 {
  public static void main(String[] args) {
    

    System.out.println("I Love coding");
    ArrayList<Integer> al = new ArrayList<>();
    al.add(100);
    al.add(1000);
    al.add(10000);
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the Number you want:");
    System.out.println();
    int s = sc.nextInt();
    for (int i = 0; i < s; i++) {
      System.out.println(s);

    }
    int[] arr = new int[al.size()];
    System.arraycopy(al, 0, arr, 0, 3);
    for (int num : arr) {
      System.out.println(num);
    }
    sc.close();
  }

}
