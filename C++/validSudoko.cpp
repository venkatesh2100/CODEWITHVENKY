#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
  bool isValidSudoku(vector<vector<char>> &board) {

    vector<vector<bool>> row_mat(9, vector<bool>(9, false));
    vector<vector<bool>> col_mat(9, vector<bool>(9, false));

    vector<vector<bool>> box_mat(9, vector<bool>(9, false));

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {

        if (board[i][j] != '.') {
          int val = board[i][j] - '1';
          int box_index = (i / 3) * 3 + (j / 3);

          if (row_mat[i][val] || col_mat[j][val] || box_mat[box_index][val]) {
            return false;
          }

          row_mat[i][val] = true;
          col_mat[j][val] = true;
          box_mat[box_index][val] = true;
        }
      }
    }

    return true;
  };
};
