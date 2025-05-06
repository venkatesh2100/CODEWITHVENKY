#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  int minBitFlips(int start, int goal) {

    int res = start ^ goal;
    int c;
    while (res) {
      if (res & 1) {
        ++c;
      }
      res = res >> 1;
    }
    return c;
  }

public:
  int maxnum(vector<int> arr) {
    int maxi = 0;
    for (auto &num : arr) {
      maxi = max(num, maxi);
    }
    return maxi;
  };
};

int main() {
  Solution sol;
  vector<int> arr = {10, 20, 30};
  int res = sol.maxnum(arr);
  cout << res;
};
