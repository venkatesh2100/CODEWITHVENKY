//Example 1:
//
//Input: s = "III"
//Output: 3
//Explanation: III = 3.
//Example 2:
//
//Input: s = "LVIII"
//Output: 58
//Explanation: L = 50, V= 5, III = 3.
//Example 3:
//
//Input: s = "MCMXCIV"
//Output: 1994
//Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map=new HashMap<>();
         map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        int ans=0;
        char[] arr=s.toCharArray();
        for(int i=0;i<arr.length;i++){
            if(i<arr.length-1&&map.get(arr[i])<map.get(arr[i+1])){
                ans-=map.get(arr[i]);
            }else {
                ans+=map.get(arr[i]);
            }
        }

        return ans;
    }
}