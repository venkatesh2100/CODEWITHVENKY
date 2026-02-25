#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  vector<vector<string>> res;
  vector<string> board;

  set<int> colset, dia1, dia2;

  void backtrack(int r, int n) {

    if (r == n) {
      res.push_back(board);
      return;
    }

    for (int c = 0; c < n; c++) {

      if (colset.count(c) || dia1.count(r + c) || dia2.count(r - c)) {
        continue;
      }

      board[r][c] = 'Q';
      colset.insert(c);
      dia1.insert(r + c);
      dia2.insert(r - c);

      backtrack(r + 1, n);

      board[r][c] = '.';
      colset.erase(c);
      dia1.erase(r + c);
      dia2.erase(r - c);
    }
  }

  vector<vector<string>> solveNQueens(int n) {
    board = vector<string>(n, string(n, '.'));
    backtrack(0, n);
    return res;
  }
};
