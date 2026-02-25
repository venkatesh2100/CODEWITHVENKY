#include <bits/stdc++.h>;
using namespace std;
class Solution {
public:
  vector<vector<int>> subsets(vector<int> &nums) {
    vector<vector<int>> res;
    dfs(0, nums, res);
    return res;
  }

private:
  vector<int> sub;
  void dfs(int i, vector<int> &nums, vector<vector<int>> &res) {

    if (i >= nums.size()) {
      res.push_back(sub);
      return;
    }

    sub.push_back(nums[i]);
    dfs(i + 1, nums, res);

    sub.pop_back();
    dfs(i + 1, nums, res);
  }
};
