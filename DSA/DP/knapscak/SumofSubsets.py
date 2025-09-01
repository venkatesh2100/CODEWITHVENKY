'''416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int],sumi:int) -> bool:

      dp = [[False ] * (sumi+1) for _ in range(len(nums) + 1)]

      for i in range(len(nums)+1):
        dp[i][0] = True

      for i in range(1,len(nums)+1):
        for j in range(1,sumi+ 1):
          if nums[i-1] > j:
            dp[i][j] = dp[i-1][j]
          else:
            dp[i][j] = dp[i-1][j] or dp[i][j-nums[i-1]]
      print(dp)
      return dp[len(nums)][sumi]

ans = Solution()
res=ans.canPartition([1,2,3,12,8],11)
print(res)
'''
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums, int sumi) {
        int n = nums.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(sumi + 1, false));

        // Base case: sum 0 is always possible
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }

        // Fill DP table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sumi; j++) {
                if (nums[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j]; // Can't take this number
                } else {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }

        // Uncomment to print DP table
        /*
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= sumi; j++) {
                cout << (dp[i][j] ? "T " : "F ");
            }
            cout << endl;
        }
        */

        return dp[n][sumi];
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 12, 8};
    int sumi = 11;
    bool res = sol.canPartition(nums, sumi);
    cout << (res ? "true" : "false") << endl;
    return 0;
}
'''