#include <algorithm>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  bool isAnagram(string s, string t) {

    if (s.length() != t.length()) {
      return false;
    }

    vector<int> count(26, 0);

    for (int i = 0; i < s.length(); i++) {
      count[s[i] - 'a']++;
      count[t[i] - 'a']--;
    }

    for (int val : count) {
      if (val != 0) {
        return false;
      }
    }

    return true;

    // second way Sort technique
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());

    for (int i = 0; i < s.size(); i++) {
      if (s[i] != t[i]) {
        return false;
      }
    }

    return true;
  }
};
