#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {

    unordered_map<string, vector<string>> hmap;

    for (auto &word : strs) {
      string sorted_word = word;
      sort(sorted_word.begin(), sorted_word.end());

      if (hmap.count(sorted_word)) {
        hmap[sorted_word].push_back(word);
      } else {
        hmap[sorted_word];
      }
    }
    vector<vector<string>> res;
    for (auto &[key, value] : hmap) {
      res.push_back(value);
    }

    return res;
  }
};
