package ARRAYS;

import java.util.HashMap;

public class BinarySubArray {
    public static void main(String[] args) {
        int[] arr = {1, 0, 1, 0, 1};
        int goal = 2;
//        System.out.println(hash(arr,goal));
        int x=Sliding(arr,goal);
        int y=Sliding(arr,goal-1);
        System.out.println(x-y);
    }

    public static int Sliding(int[] arr, int k) {
        int start = 0, end = 0, sum = 0, count = 0;
        //Iterate the Loop
        while (end < arr.length) {
            sum += arr[end];
            while (sum > k && start < arr.length) {
                sum -= arr[start];
                start++;
            }
            if (sum <= k) {
                count +=+end - start + 1;
            }
            end++;
        }
        return count;
    }

    public static int hash(int[] arr, int goal) {
        int sum = 0, ans = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(sum, 1);
        for (int num : arr) {
            sum += num;
            if (map.containsKey(sum - goal)) {
                ans += map.get(sum - goal);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        return ans;
    }
}

