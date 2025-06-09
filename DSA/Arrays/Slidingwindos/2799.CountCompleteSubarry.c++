#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
public:
  int countCompleteSubarrays(vector<int> &nums) {

    int n = nums.size();
    int left = 0;
    int count = 0;
    std::pmr::unordered_set<int> setarr(nums.begin(), nums.end());
    while (left < n) {
      std::pmr::unordered_set<int> new_setarr;
      for (int right = left; right < n; ++right) {
        new_setarr.insert(nums[right]);
        if (new_setarr == setarr) {
          ++count;
        }
      }
      ++left;
    }
    return count;
  }
};
// We call a subarray of an array complete if the following condition is
// satisfied:
//
// The number of distinct elements in the subarray is equal to the number of
// distinct elements in the whole array. Return the number of complete
// subarrays.
//
// A subarray is a contiguous non-empty part of an array.
//
//
//
// Example 1:
//
// Input: nums = [1,3,1,2,2]
// Output: 4
// Explanation: The complete subarrays are the following: [1,3,1,2],
// [1,3,1,2,2], [3,1,2] and [3,1,2,2]. Example 2:
//
