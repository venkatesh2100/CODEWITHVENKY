#include "vector"
#include <iostream>
using namespace std;
#include <algorithm>
class Solution {
public:
  long long countFairPairs(vector<int> &nums, int lower, int upper) {
    // TODO Use Binary search algorithm
    int count = 1;
    sort(nums.begin(), nums.end());
    int n = nums.size();
    for (auto &val : nums) {
      cout << val;
    }
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (nums[mid] + nums[mid + 1] > upper) {
        right = mid;
      } else if (nums[mid] + nums[mid - 1] < lower) {
        left = mid + 1;
      } else {
        for (int i = left; i < right; i++) {
          for (int j = i + 1; j < right; j++) {
            count++;
          }
        }
      }
    }

    return count;
  }
};
