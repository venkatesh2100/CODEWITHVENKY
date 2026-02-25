#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  int n, m;
  string word;

  bool backtrack(vector<vector<char>> &board, int r, int c, int k) {
    if (k == word.size())
      return true;

    if (r < 0 || r >= n || c < 0 || c >= m || board[r][c] != word[k])
      return false;

    char temp = board[r][c];
    board[r][c] = '#'; // mark visited

    bool found = backtrack(board, r, c + 1, k + 1) ||
                 backtrack(board, r + 1, c, k + 1) ||
                 backtrack(board, r, c - 1, k + 1) ||
                 backtrack(board, r - 1, c, k + 1);

    board[r][c] = temp; // restore

    return found;
  }

  bool exist(vector<vector<char>> &board, string w) {
    word = w;
    n = board.size();
    m = board[0].size();

    for (int r = 0; r < n; r++) {
      for (int c = 0; c < m; c++) {
        if (backtrack(board, r, c, 0))
          return true;
      }
    }

    return false;
  }
};
