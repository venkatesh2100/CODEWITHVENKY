import java.util.HashSet;
import java.util.Set;

class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        Set<Integer> set1=new HashSet<>();
//        Set<Integer> set2=new HashSet<>();
        for(int num:nums1){
            set1.add();
        }for(int num:nums2){
               if(set1.contains(num)) return num
        }
        return -1;
    }
}