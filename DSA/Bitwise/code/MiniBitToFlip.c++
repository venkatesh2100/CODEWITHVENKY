using namespace std;
#include <iostream>
class Solution{
  public:
    int MiniBitsToFlip(int a,int b){
      int ans = a ^ b;
      int count  = 0;
      while(ans){
        if(ans & 1){
          ++count;
        }
        ans = ans >> 1;
      }
      return count;
    }
};

int main(){
  Solution sol;
  int res  = sol.MiniBitsToFlip(10,   7);
  cout << res;
  return 0;
}
