//Input: nums = [1,0,1,0,1], goal = 2
//Output: 4
//Explanation: The 4 subarrays are bolded and underlined below:
//[1,0,1,0,1]
//[1,0,1,0,1]
//[1,0,1,0,1]
//[1,0,1,0,1]
//Example 2:
//
//Input: nums = [0,0,0,0,0], goal = 0
//Output: 15
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int count=0;
        int current_sum=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i;j<nums.length;j++){
                current_sum+=nums[j];
                if(current_sum==goal) count++;
            }
            current_sum=0;
        }
        return count;

    }
}
