#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // Calculate total sum
        int totalSum = accumulate(nums.begin(), nums.end(), 0);

        // If odd sum, can't partition equally
        if (totalSum % 2 != 0) return false;

        int n = nums.size();
        int target = totalSum / 2;

        vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

        // Base case: sum 0 is always possible
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }

        // Fill DP table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {
                if (nums[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[n][target];
    }
};

int main() {
    Solution sol;
    vector<int> nums = {5 , 4 , 3 , 5 , 1};
    bool res = sol.canPartition(nums);
    cout << (res ? "true" : "false") << endl;
}
