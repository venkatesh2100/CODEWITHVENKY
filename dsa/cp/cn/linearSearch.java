package CP.CODENINJAS;

public class linearSearch {
  public static int linearSearch(int n, int num, int[] arr) {
    // Write your code here.
    for (int i = 0; i < n; i++) {
      if (arr[i] == num) {
        return i;
      }
    }
    return -1;
  }

public static void main(String[] args) {
  int[] arr={1,2,3,4,5};
  int n=arr.length;
  System.out.println(linearSearch(n,4 , arr));
}
}
