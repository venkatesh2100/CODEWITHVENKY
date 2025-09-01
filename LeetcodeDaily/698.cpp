#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;
        int target = sum / k;

        sort(nums.rbegin(), nums.rend());
        vector<int> bucket(k, 0);
        return backtrack(nums, bucket, 0, target);
    }

private:
    bool backtrack(vector<int>& nums, vector<int>& bucket, int index, int target) {
        if (index == nums.size()) {
            for (int b : bucket)
                if (b != target) return false;
            return true;
        }
        for (int i = 0; i < bucket.size(); i++) {
            if (bucket[i] + nums[index] <= target) {
                bucket[i] += nums[index];
                if (backtrack(nums, bucket, index + 1, target))
                    return true;


                //print
                for(int val:bucket){
                  cout<< val  << " ";
                }
                
                bucket[i] -= nums[index];
            }
            if (bucket[i] == 0) break; // avoid symmetric states
        }
        return false;
    }
};
