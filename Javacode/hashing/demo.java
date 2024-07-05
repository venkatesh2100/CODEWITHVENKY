// package HASHING;

import java.util.Collection;
import java.util.HashMap;

public class demo {
    public static void main(String[] args) {
        System.out.println("Hashing Repository");
        System.out.println("Wow this is very cool");
    }

    public Collection<Integer> removeDuplicates(int[] nums) {
        // Remove Duplicate Elements
        HashMap<Integer, Integer> map = new HashMap();
        int temp = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            temp = nums[i + 1];
            if (nums[i] != temp) {
                map.put(nums[i], i);
            }
        } // Convert HashMap to arrlkdlfkd
        

        return map.values();
    }
}
