//
//Input: strs = ["flower","flow","flight"]
//Output: "fl"
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String value=strs[0];
        StringBuilder ans=new StringBuilder();
        for(int i=0;i<value.length();i++){
            for(String s:strs){
                if(i==value.length()||value.charAt(i)!=s.charAt(i)){
                    return ans.toString();
                }
                ans.append(value.charAt(i));
            }
        }
        return  ans.toString();

    }
}