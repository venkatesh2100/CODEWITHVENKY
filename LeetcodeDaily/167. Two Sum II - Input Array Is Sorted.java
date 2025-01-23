//Example 1:
//
//Input: numbers = [2,7,11,15], target = 9
//Output: [1,2]
//Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
//Example 2:
//
//Input: numbers = [2,3,4], target = 6
//Output: [1,3]
//Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
//Example 3:
//
//Input: numbers = [-1,0], target = -1
//Output: [1,2]
//Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
class Solution {
    public int[] twoSum(int[] numbers, int target) {
            int start=0;
            int end=numbers.length-1;
            while (start<=end){
                if(numbers[start]+numbers[end]==target) {
                return new int[]{start+1,end+1};
                }
                else if(numbers[start]+numbers[end]>target){
                    end--;
                }else if(numbers[start]+numbers[end]<target){
                    start++;
                }
            }
            return new int[2];
        }
















//        for(int i=0;i<numbers.length;i++){
//            for(int j=i+1;j<numbers.length-1;j++){
//                if(target==numbers[i]+ numbers[j]){
//                    ans[0]=i+1;
//                    ans[1]=j+1;
//                }
//            }
//        }
//        return ans;

    }
}