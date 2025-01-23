import java.util.Arrays;
 
//Example 1:
//
//Input: nums = [1,2,3,4]
//Output: [24,12,8,6]
//Example 2:
//
//Input: nums = [-1,1,0,-3,3]
//Output: [0,0,9,0,0]
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr=new int[nums.length];
        Arrays.fill(arr,0);
        int count0;
        int product=1;
        for(int num:nums){
            if(num==0){
                count++;
            }
            product*=num 
        }

        if(count==1){
            for(int i=0;i<nums.length;i++){
            arr[i]=nums[i]==0?product:0;
            }

        } else if (count==0) {
            for (int i=0;i<nums.length;i++){
                arr[i]=product/nums[i];
            }
        }
        return  arr;
    }
}
