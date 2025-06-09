import java.util.Arrays;
import java.util.HashMap;

class Solution {
  public int firstCompleteIndex(int[] arr, int[][] mat) {
    int rows = mat.length;
    int cols = mat[0].length;

    HashMap<Integer, int[]> positionMap = new HashMap<>();

    int[] rowsCount = new int[rows];
    int[] colCount = new int[cols];
    Arrays.fill(rowsCount, cols);
    Arrays.fill(colCount, rows);

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        positionMap.put(mat[i][j], new int[] { i, j });
      }
    }

    for (int idx = 0; idx < arr.length; ++idx) {
      int[] pos = positionMap.get(arr[idx]);
      if (--rowsCount[pos[0]] == 0 || --colCount[pos[1]] == 0) {
        return idx;
      }
    }
  }
}
