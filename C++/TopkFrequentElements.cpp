#include <bits/stdc++.h>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {

    unordered_map<int, int> hmap;

    for (int num : nums) {
      hmap[num]++;
    }

    priority_queue<pair<int, int>> pq;

    for (auto &[key, count] : hmap) {
      pq.push({key, count});
    }

    vector<int> res;
    while (k--) {
      int val = pq.top().first;
      pq.pop();
      res.push_back(val);
    }

    return res;
  }
};
