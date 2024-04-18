import java.util.Arrays;

//Note: An array A rotated by x positions results in an array B
// of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
//Example 1:
//Input: nums = [3,4,5,1,2]
//Output: true
//Explanation: [1,2,3,4,5] is the original sorted array.
//You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
//Example 2:
//Input: nums = [2,1,3,4]
//Output: false
//Explanation: There is no sorted array once rotated that can make nums.
//Example 3:
//Input: nums = [1,2,3]
//Output: true
//Explanation: [1,2,3] is the original sorted array.
//You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
class Solution {
    public boolean check(int[] nums) {
        public boolean check(int[] nums) {
    int c=0;
    for(int i=0;i<nums.length;i++){
        if(nums[i]>nums[(i+1)%nums.length]){
            c++;
        }
    }
    if(c>1){
        return false;
    }
    return true;

//        int[] ans=new int[nums.length];
//        System.arraycopy(nums,0,ans,0,nums.length);
//        int x=1;
//        for(int i=0;i<nums.length-1;i++){
//            if(nums[i]<nums[i+1]){
//                x++;
//            }
//        }
//        for(int i=0;i< nums.length;i++){
//            if(nums[i]!=ans[(i+x)% nums.length]){
//                return false;
//            }
//        }
//        return true;
    }
}