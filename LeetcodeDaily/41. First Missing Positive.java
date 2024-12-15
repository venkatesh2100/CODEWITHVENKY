//Input: nums = [7,8,9,11,12]
//Output: 1
//Explanation: The smallest positive integer 1 is missing.


class Solution {
    public int firstMissingPositive(int[] nums) {
        int size=nums.length;
        boolean [] state=new boolean[n+1];
        int i=0;
        while (nums[i]>0 && nums[i]<=n){
            state[i]=true;
            i++;
        }
        for(int i=1;i< nums.length;i++){
            if(!state[i]){
                return i;
            }
        }
        return n+1;
    }
    }