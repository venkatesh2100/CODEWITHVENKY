#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    vector<vector<int>> res;
    sort(candidates.begin(), candidates.end());
    dfs(0, 0, target, res, candidates);
    return res;
  }

private:
  vector<int> sub;
  void dfs(int i, int sum, int target, vector<vector<int>> &res,
           vector<int> &c) {

    if (sum == target) {
      res.push_back(sub);
      return;
    }

    if (i >= c.size() || sum > target) {
      return;
    }

    sub.push_back(c[i]);
    dfs(i + 1, sum + c[i], target, res, c);
    sub.pop_back();
    while (i + 1 < c.size() && c[i] == c[i + 1]) {
      i++;
    }
    dfs(i + 1, sum, target, res, c);
  }
};
