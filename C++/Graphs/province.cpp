#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {

public:
  int findCircleNum(vector<vector<int>> &isConnected) {
    vector<int> ls = (isConnected.size(), 0);
    int ans = 0;

    for (int i = 0; i < isConnected.size(); i++) {
      if (ls[i] == 0) {
        ans++;
        dfs(i, isConnected, ls);
      }
    }
    return ans;
  }

private:
  void dfs(int index, vector<vector<int>> &isConnected, vector<int> ls) {
    ls[index] = 1;
    for (int i = 0; i < isConnected.size(); i++) {
      if (isConnected[index][i] && ls[i] == 0) {
        ls[i] = 1;
        dfs(i, isConnected, ls);
      }
    }
  }
};
