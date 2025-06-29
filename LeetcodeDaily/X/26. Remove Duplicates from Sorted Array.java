//Input: nums = [1,1,2]
//Output: 2, nums = [1,2,_]

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int removeDuplicates(int[] nums) {
        //Remove Duplicate Elements
        HashMap<Integer,Integer> map=new HashMap();
        int temp=0;
        for(int i=0;i<nums.length-1;i++){
            temp=nums[i+1];
            if(nums[i]!=temp){
                map.put(nums[i],i);
            }
        }//Convert HashMap to arr

        return map.values(Integer);
    }
}