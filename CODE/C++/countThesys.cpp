#include <iostream>
#include <numeric>
using namespace std;
#include <string>
class Solution {
public:
  int countSymmetricIntegers(int low, int high) {
    // Low and High
    int count = 0;
    while (low <= high) {
      string num = to_string(low);
      if (num.size() % 2 == 0) {
        int mid = num.size() / 2;
            int left = accumulate(num.begin(),num.begin()+mid,0,[](int sum,char c){
          return sum + (c - '0');
          });
        int right = accumulate(num.begin()+mid,num.end(),0,[](int sum,char c){
                return sum + (c-'0');
                });
        if(left==right){
            count++;
        }
      }
      low++;
    }
    return count;
  }
};
