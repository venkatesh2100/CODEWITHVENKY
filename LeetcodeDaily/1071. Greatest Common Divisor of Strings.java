//Example 1:
//
//Input: str1 = "ABCABC", str2 = "ABC"
//Output: "ABC"
//Example 2:
//
//Input: str1 = "ABABAB", str2 = "ABAB"
//Output: "AB"
//Example 3:
//
//Input: str1 = "LEET", str2 = "CODE"
//Output: ""
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(!(str1+str2).equals(str2+str1)){
            return "";
        }else {
            int n=gcd(str1.length(),str2.length());
            return str1.substring(0,n);
        }

    }
    public static int gcd(int a,int b){
        return b==0?a:gcd(b,a%b);
    }
}