#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {

    unordered_map<int, int> hmap;

    for (int i = 0; i < nums.size(); i++) {

      int rem = target - nums[i];
      if (hmap.find(rem) != hmap.end()) {
        return {hmap[rem], i};
      } else {
        hmap[nums[i]] = i;
      }
    }
    return {};
  }
};
