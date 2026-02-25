#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    this->candidates = candidates;
    vector<vector<int>> res;
    dfs(0, 0, res, target);
    return res;
  }

private:
  vector<int> sub;
  vector<int> candidates;
  void dfs(int i, int sum, vector<vector<int>> res, int target) {
    if (sum == target) {
      res.push_back(sub);
      return;
    } else if (sum > target) {
      return;
    }
    sub.push_back(candidates[i]);
    dfs(i, sum + candidates[i], res, target);
    sub.pop_back();
    dfs(i + 1, sum, res, target);
  }
};
