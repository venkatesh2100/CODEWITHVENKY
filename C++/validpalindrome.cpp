#include <bits/stdc++.h>
#include <cctype>
#include <vector>
using namespace std;
class Solution {
public:
  bool isPalindrome(string s) {
    vector<char> res;
    for (char c : s) {
      if (isalnum(c)) {
        res.push_back(tolower(c));
      }
    }

    return palindromeCheck(res);
  }

  bool palindromeCheck(vector<char> word) {
    int l = 0;
    int r = word.size() - 1;

    while (l < r) {
      if (word[l] != word[r]) {
        return false;
      }
      l++;
      r--;
    }

    return true;
  }
};
