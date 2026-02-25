#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    cin >> w;
    int count = 0;

    while(w--){
      string s;
      cin >> s;

      if(s.find("++") != string::npos){
        count++;
      }else{
        count--;
      }
    }

    
    cout << count;

    return 0;
}