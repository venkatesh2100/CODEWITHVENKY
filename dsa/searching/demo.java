// package dsa.searching;

public class demo {
  public void binarysearch(int target, int[] arr) {
      int start = 0;
      int end = arr.length - 1;
    while (start <= end) {
      int mid =start + (end - start) / 2;

      if (target == arr[mid]) {
        System.out.println("Targer found:" + mid);
        return;
      } else if (target > arr[mid]) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
    System.out.println("target is not found in the list");
  }

  public static void main(String[] args) {
    int[] arr = { 10, 20, 30, 40, 50 };
    int target = 20;
    demo user = new demo();
    user.binarysearch(target, arr);
  }

}
