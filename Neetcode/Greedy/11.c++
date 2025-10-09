// TIP: More Optimal way For the same method
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maxArea(vector<int> &height) { int res = 0; }
  int res = 0;
  int l = 0;

  int r = height.size() - 1;

  while (l < r) {
    res = ((r - l) * min(height[r], height[l]));
    if (height[l] < height[r]) {
      l += 1;
    } else {
      r -= 1;
    }
  }
}

// TIP: Basic idea
//  #include <algorithm>
//  #include <bits/stdc++.h>
//  using namespace std;
//  class Solution {
//  public:
//    int maxArea(vector<int> &height) {
//
//      int res = 0;
//      int left = 0;
//      int length = height.size();
//
//      int right = length - 1;
//
//      while (left < right) {
//        if (height[left] == height[right]) {
//
//          res = max((right - left) * height[left], res);
//          right -= 1;
//          left += 1;
//        } else if (height[left] < height[right]) {
//          res = max((right - left) * height[left], res);
//          left += 1;
//        } else {
//          res = max((right - left) * height[right], res);
//          right -= 1;
//        }
//      }
//      return res;
//    }
//  };
