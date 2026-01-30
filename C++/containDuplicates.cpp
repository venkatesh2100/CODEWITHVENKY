#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {

    unordered_map<int, int> hmap;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == nums[i + 1]) {
        return false;
      }
      return true;
    }
    for (int num : nums) {
      hmap[num]++;
    }

    for (auto &[key, val] : hmap) {
      if (val > 1) {
        return true;
      }
    }
    return false;
  }
};
