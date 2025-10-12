
// TODO:1668. Maximum Repeating Substring
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  int maxRepeating(string sequence, string word) {

    int n = sequence.length();
    int m = word.length();

    int res = 0;

    vector<int> dp(n + 1, 0);

    for (int i = m; i < n + 1; i++) {
      if (sequence.compare(i - m, m, word) == 0) {
        dp[i] = dp[i - m] + 1;
        res = max(dp[i], res);
      }
    }

    return res;
  }
};
