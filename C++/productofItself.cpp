#include <bits/stdc++.h>
#include <vector>
using namespace std;

// prefix sum
class Solution {
public:
  vector<int> productExceptSelf(vector<int> &nums) {

    vector<int> ps(nums.size(), 1);
    vector<int> ss(nums.size(), 1);

    for (int i = 1; i < nums.size(); i++) {
      ps[i] = ps[i - 1] * nums[i];
    }

    for (int i = nums.size() - 2; i > 0; i--) {
      ss[i] = ss[i + 1] * nums[i];
    }

    vector<int> res(nums.size(), 1);
    for (int i = 0; i < nums.size(); i++) {
      res[i] = ps[i] * ss[i];
    }

    return res;
  }
};
