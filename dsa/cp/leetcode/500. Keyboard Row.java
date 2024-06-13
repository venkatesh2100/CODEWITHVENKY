import java.util.HashMap;

//Example 1:
//
//Input: words = ["Hello","Alaska","Dad","Peace"]
//Output: ["Alaska","Dad"]
//Example 2:
//
//Input: words = ["omk"]
//Output: []
//Example 3:
//
//Input: words = ["adsdf","sfd"]
//Output: ["adsdf","sfd"]
//
 class Solution {
    public String[] findWords(String[] words) {
        String r1 = "qwertyuiopQWERTYUIOP";
        String r2 = "asdfghjklASDFGHJKL";
        String r3 = "zxcvbnmZXCVBNM";

        List<String> result = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            boolean inRow1 = true, inRow2 = true, inRow3 = true;

            for (int j = 0; j < words[i].length(); j++) {
                char c = words[i].charAt(j);

                if (!r1.contains(String.valueOf(c))) {
                    inRow1 = false;
                }

                if (!r2.contains(String.valueOf(c))) {
                    inRow2 = false;
                }

                if (!r3.contains(String.valueOf(c))) {
                    inRow3 = false;
                }
            }

            if (inRow1 || inRow2 || inRow3) {
                result.add(words[i]);
            }
        }
        String[] s = result.toArray(new String[0]);
        return s;
    }
}
