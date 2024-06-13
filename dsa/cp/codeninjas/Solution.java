/*
    Time complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of elements in the array.
*/

import java.util.ArrayList;

public class Solution {
  public static void reverseArray(ArrayList<Integer> arr, int m) {

    int n = arr.size();

    // Declare and initialize ArrayList BRR.
    ArrayList<Integer> brr = new ArrayList<Integer>();

    for (int i = 0; i < arr.size(); i++) {
      brr.add(0);
    }

    // Declare a varibale P.
    int p = 0;

    // First fill the BRR in the same order as the original array upto Mth postion.
    for (int i = 0; i <= m; i++) {
      brr.set(p++, arr.get(i));
    }

    // Now fill the BRR in the reverse order till (m+1)th postion.
    for (int j = n - 1; j > m; j--) {
      brr.set(p++, arr.get(j));
    }

    // Now copy back the array brr into array ARR.
    for (int i = 0; i < n; i++) {
      arr.set(i, brr.get(i));
    }
  }
}
