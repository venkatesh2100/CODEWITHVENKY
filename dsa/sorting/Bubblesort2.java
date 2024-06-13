package SORTING;

import java.util.Scanner;

public class Bubblesort2 {
  public void sorted(int[] arr) {
    int size = arr.length;
//External loop sort single element in the respective position
    for (int i = 0; i < size - 1; i++) {
      int num = 0;
//checks every Adjcent numbers of Array
      for (int j = 0; j < size - i-1; j++) {
        if (arr[j] > arr[j + 1]) {
          int temp = arr[j + 1];
          arr[j + 1] = arr[j];
          arr[j] = temp;
          num = 1;
        }
      }
      if (num == 0) {
        break;
      }
    }

    for (int numbers : arr) {
      System.out.print(numbers + " ");
    }
  }


  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int size=sc.nextInt();
    int[] arr=new int[size];
    for(int i=0;i<size;i++){
      arr[i]=sc.nextInt();
    }
    sc.close();
    Bubblesort2 sort1=new Bubblesort2();
    sort1.sorted(arr);
  }

}
